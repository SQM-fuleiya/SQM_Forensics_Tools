import os
import re
import sqlite3

import chardet
import pandas as pd
from PySide6.QtGui import QStandardItem
from PySide6.QtWidgets import QMessageBox

file_name = []
file_path = ""
单人层级 = []
列数据 = []


def append_to_table(self, row_data):  # 将数据添加到表格中
    items = [QStandardItem(str(item)) for item in row_data]
    self.model.appendRow(items)
    # self.list_echo.resizeColumnsToContents()  # 自动调整列宽
    self.list_echo.setWordWrap(True)  # 启用文本换行


def clear_table(self):  # 清空表格
    self.model.clear()
    self.model.setHorizontalHeaderLabels([])


def 数据入库(self):  # 文件数据入库
    clear_table(self)  # 清空表格
    # 启用按键
    self.ui.db_select_but.setEnabled(True)
    self.ui.db_clear.setEnabled(True)
    self.ui.select_one.setEnabled(True)
    self.ui.show_guanxi.setEnabled(True)

    if not file_name:  # 检查文件是否存在
        QMessageBox.warning(self, "警告", "请先选择文件！")
        return
    self.is_running = True  # 初始化标志位
    append_to_table(self, ["开始导入数据..."])

    for file_idx, file_path in enumerate(file_name, 1):  # 确认存在文件
        if not self.is_running:
            break

        # 判断文件编码
        with open(file_path, "rb") as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result["encoding"]

        try:  # 判断文件类型
            if file_path.endswith(".txt"):
                batch_size = 1000  # 建立缓存池
                batch_data = []
                with open(file_path, "r", encoding=encoding) as f:
                    f.seek(0)

                    for line_idx, line in enumerate(f, 1):
                        if not self.is_running:
                            break

                        data = line.strip().split("----")  # 分割数据，分隔符为 ----
                        batch_data.append(data)

                        if len(batch_data) >= batch_size:
                            批量入库(self, batch_data)
                            batch_data = []

                # 处理剩余的数据
                if batch_data and self.is_running:
                    批量入库(self, batch_data)

            elif file_path.endswith((".xlsx", ".xls")):
                try:
                    excel_file = pd.ExcelFile(file_path)
                    sheet_names = excel_file.sheet_names
                    for sheet_name in sheet_names:
                        df = excel_file.parse(sheet_name)
                        批量入库(self, df.values.tolist())
                except Exception as e:
                    raise Exception(f"读取Excel文件失败：{str(e)}")

            elif file_path.endswith(".csv"):
                try:
                    df = pd.read_csv(file_path, encoding=encoding, quotechar='"', quoting=0)

                    if len(df.values.tolist()[0]) != 1:  # 判断是否只有一行数据
                        批量入库(self, df.values.tolist())
                    else:  # 如果只有一行,则将数据分割成多行
                        data = []
                        with open(file_path, "r", encoding=encoding) as f:
                            for line in f:
                                row = line.replace('"', "").replace("\n", "").split(",")
                                data.append(row)
                        批量入库(self, data)

                except Exception as e:
                    raise Exception(f"读取CSV文件失败：{str(e)}")
        except Exception as e:  # 处理异常
            append_to_table(self, [f"处理文件{file_path}时出错：{str(e)}"])
            continue

    append_to_table(self, ["导入完成！" if self.is_running else "导入已取消"])


def cancel_process(self):
    self.is_running = False
    append_to_table(self, ["正在停止处理..."])


def 数据库连接(self):
    with sqlite3.connect(f"{file_path}/数据分析.db") as conn:  # 打开或创建数据库连接
        conn.execute("PRAGMA synchronous = OFF")  # 关闭同步模式,提高写入速度
        conn.execute("PRAGMA journal_mode = WAL")  # 使用WAL模式，提高并发性能 # 创建游标
        cursor = conn.cursor()
        return conn, cursor


def 数据库清理(self):
    conn, cursor = 数据库连接(self)
    try:
        cursor.execute("DROP TABLE IF EXISTS fenxi")
        conn.commit()
        append_to_table(self, ["数据库已清理"])
    except Exception as e:
        append_to_table(self, f"Error deleting table: {e}")
    conn.close()  # 关闭数据库连接


def 批量入库(self, data):
    conn, cursor = 数据库连接(self)
    if not data:  # 检查数据是否为空
        return
    # 检查数据类型，防止出现浮点数和非整数的情况
    data = [[str(int(item)) if isinstance(item, float) and item.is_integer() else str(item) for item in row] for row in data]
    # 获取数据的列数
    columns = [chr(65 + i) for i in range(len(data[0]))]  # 生成列名，列名以A, B, C...的顺序命名
    placeholders = ",".join(["?"] * len(columns))  # 生成占位符，数量与列数相同
    sql = f"INSERT INTO fenxi ({','.join(columns)}) VALUES ({placeholders})"  # 生成插入语句
    try:
        # 检查表是否存在
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='fenxi'")
        # 确保 cursor 是 Cursor 对象
        if not cursor.fetchone():
            create_sql = f"CREATE TABLE fenxi ({','.join([f'{col} TEXT' for col in columns])})"
            cursor.execute(create_sql)

        cursor.executemany(sql, data)  # 执行插入语句
        conn.commit()  # 提交事务

        # 将数据输出到表格
        append_to_table(self, columns)  # 添加表头
        for row in data:
            append_to_table(self, row)  # 添加数据
    except Exception as e:
        raise Exception(f"数据库写入失败：{str(e)}")
    conn.close()


def db_select(self):
    """执行 SQL 查询并将结果显示在表格中"""
    clear_table(self)
    query = self.ui.db_str.text().strip()
    if not query:
        self.QMessageBox.warning(self, "警告", "请输入查询语句！")
        return
    # 防注入
    query = re.sub(r"['\"“”‘’]", "'", query)
    results = database_query(self, query)
    try:
        # 清空表格并显示查询结果
        self.model.clear()
        if results != []:
            for row in results:
                append_to_table(self, row)  # 添加数据
        else:
            append_to_table(self, ["没有查询到任何数据"])
    except Exception as e:
        append_to_table(self, [f"查询失败：{str(e)}"])
    self.list_echo.resizeColumnsToContents()  # 自动调整列宽


def delete_database(self):
    """删除数据库文件"""
    db_path = f"{file_path}/数据分析.db"
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            append_to_table(self, ["数据库已删除"])
        except Exception as e:
            append_to_table(self, [f"删除数据库失败：{str(e)}"])
    else:
        append_to_table(self, ["数据库文件不存在"])


def select_yufa(self):
    """将语法说明按行输出到表格中"""
    clear_table(self)  # 清空表格

    # 定义语法说明
    syntax_lines = [
        "基本查询   : select * from fenxi",
        "单列查询   : select 列名 from fenxi",
        "条件查询   : 基本查询语句 where 列名 = value     # where 后面跟查询条件",
        "多条件查询 : 基本查询语句 where 列名 = value and 列名 = value  # and 代表与 or 代表或",
        "排序查询   : select * from fenxi order by 列名 desc  # desc 代表降序 asc 代表升序",
        "联合查询   : 基本查询语句 union 基本查询语句      # union 代表联合查询",
        "限制查询   : 基本查询语句 limit 10               # 限制查询结果的数量",
        "统计查询   : select count(*) from fenxi         # count(*) 代表统计所有行数",
        "去重查询   : select distinct 列名 from fenxi    # distinct 代表去重",
        "合计查询   : select sum(列名) from fenxi        # sum(列名) 代表求和",
        "绝对值统计 : select sum(ABS(列名)) from fenxi   # ABS 用于数字绝对值",
        "嵌套查询   : 基本查询语句 where 列名 in (select 列名 from fenxi)",
        "模糊查询   : 基本查询语句 where 列名 like '%value%'",
        "% 代表任意字符 * 代表任意长度 %value% 代表包含 value 的字符串 %value 代表以 value 结尾的字符串 value% 代表以 value 开头的字符串 like 分大小写 LIKE 不分大小写",
        "聚合查询 : select 列名 from fenxi group by 列名 # group by 用于对数据进行分组",
    ]

    # 设置表头
    self.model.setHorizontalHeaderLabels(["SQL 语法说明"])
    self.list_echo.resizeColumnsToContents()  # 自动调整列宽

    # 逐行添加到表格中
    for line in syntax_lines:
        append_to_table(self, [line])  # 将每一行作为单独的一行数据添加到表格中


def 查询上线(self):
    clear_table(self)
    单人层级 = []
    唯一ID = self.ui.data_input.text().strip()
    查询信息 = ""
    层级 = 1
    try:
        x = 0
        while x != 1:
            查询语句 = f"SELECT * FROM fenxi WHERE B = '{唯一ID}'"
            result = database_query(self, 查询语句)
            if not result:
                单人层级.append([查询信息[0][2], 层级])
                层级 += 1
                x += 1

            else:
                查询信息 = result
                唯一ID = result[0][3]
                单人层级.append([result[0][0], 层级])
                层级 += 1

        # 显示结果
        clear_table(self)
        append_to_table(self, ["姓名", "层级"])  # 添加表头

        for i in range(len(单人层级)):
            单人层级[i][1] = len(单人层级) - i

        for 数据 in 单人层级:
            append_to_table(self, 数据)

    except Exception as e:
        append_to_table(self, [f"查询失败：{str(e)}"])
    self.list_echo.resizeColumnsToContents()  # 自动调整列宽


def database_query(self, query):
    conn, cursor = 数据库连接(self)
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"数据库查询出错: {e}")
        return []
    finally:
        conn.close()


def 生成树状图(self):
    clear_table(self)  # 清空表格
    """生成可折叠的层级树状图"""
    try:
        # 获取所有人员关系数据
        relations = database_query(self, "SELECT * FROM fenxi")
        if not relations:
            append_to_table(self, ["数据库中没有人员数据"])
            return

        # 统计相关数据
        总人数 = len(relations)
        直推人数 = {}
        全部下线数 = {}

        for row in relations:  # 统计直推人数
            上线id = row[3]  # 假设D列是上线ID
            if 上线id not in 直推人数:
                直推人数[上线id] = 0
            直推人数[上线id] += 1

        # 递归统计全部下线数
        def 统计下线(node_id):  # 统计某个节点下的所有下线人数（包括子下线）
            if node_id not in 全部下线数:
                全部下线数[node_id] = 0
                for row in relations:
                    if str(row[3]) == str(node_id):  # D列是上线ID
                        current_id = row[1]  # B列是当前人员ID
                        全部下线数[node_id] += 1 + 统计下线(current_id)
            return 全部下线数[node_id]

        tree = {}  # 存储树结构
        id_node_map = {}  # 存储ID到节点映射表

        # 强制创建根节点（即使ID=1不在B列）
        根节点_id = "1"
        根节点_label = f"总部-{根节点_id}(0-总人数:{统计下线(根节点_id)})"
        tree[根节点_label] = []
        root_nodes = [根节点_label]

        # 构建节点映射表
        for row in relations:
            姓名, 电话, _, 上线id = row[0], row[1], row[2], row[3]
            node_label = f"{姓名}-{电话}(直推人数：{直推人数.get(电话, 0)}-总下线{统计下线(电话)})"
            id_node_map[电话] = node_label

        # 建立父子关系
        for row in relations:
            姓名, 电话, _, 上线id = row[0], row[1], row[2], row[3]
            node_label = id_node_map[电话]

            # 处理父节点
            parent_id = str(上线id)
            if parent_id == "1":  # 直接属于根节点
                tree[根节点_label].append(node_label)
            else:
                parent_label = id_node_map.get(parent_id, 根节点_label)
                tree.setdefault(parent_label, []).append(node_label)

        # 生成HTML树结构
        def generate_tree_html(nodes, tree_data):
            """递归生成HTML树结构"""
            html = "<ul>"
            for node in nodes:
                has_children = node in tree_data and len(tree_data[node]) > 0
                caret_class = "expanded" if has_children else "no-child"
                html += f'<li><span class="node {caret_class}">{node}</span>'
                if has_children:
                    html += generate_tree_html(tree_data[node], tree_data)
                html += "</li>"
            html += "</ul>"
            return html

        # 统计层级人数
        level_count = {}

        def calculate_levels(parent_node, current_level):
            nonlocal level_count
            level_count[current_level] = level_count.get(current_level, 0) + 1
            for child in tree.get(parent_node, []):
                calculate_levels(child, current_level + 1)

        # 初始化层级统计
        level_count = {}
        # 从根节点开始统计
        calculate_levels(根节点_label, 1)  # 根节点为第1层

        # 生成HTML内容
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>层级关系图</title>
    <style>
        .node {{ cursor: pointer; padding-left: 15px; }}
        .expanded::before {{ content: "▼ "; color: #666; }}
        .collapsed::before {{ content: "▶ "; color: #666; }}
        .no-child::before {{ content: "● "; color: #999; }}
        ul {{ padding-left: 20px; list-style: none; }}
        ul ul {{ display: none; }}  /* 默认隐藏子节点 */
        ul .expanded + ul {{ display: block; }} /* 展开时显示 */
    </style>
</head>
<body>
    <h2>人员层级统计（总人数：{总人数}，最大层级：{max(level_count.keys(), default=0)}）</h2>
    <div id="tree">
        {generate_tree_html(root_nodes, tree)}
    </div>
    <script>
        document.querySelectorAll('.node').forEach(node => {{
            if(node.classList.contains('expanded')) {{
                node.nextElementSibling.style.display = 'block';
            }}
            node.addEventListener('click', function(e) {{
                e.stopPropagation();
                const ul = this.nextElementSibling;
                if (ul) {{
                    const isHidden = ul.style.display === 'none';
                    ul.style.display = isHidden ? 'block' : 'none';
                    this.classList.toggle('collapsed', !isHidden);
                    this.classList.toggle('expanded', isHidden);
                }}
            }});
        }});
    </script>
</body>
</html>
  """
        # 保存文件
        with open(f"{file_path}/层级关系图.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        append_to_table(self, [f"树状图已生成：{file_path}/层级关系图.html"])

    except Exception as e:
        append_to_table(self, [f"生成树状图失败：{str(e)}"])
