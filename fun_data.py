import os
import re
import sqlite3
import csv

#import chardet
import pandas as pd

from PySide6.QtWidgets import QMessageBox ,QApplication


''''-----------右键菜单-----------------'''
def 复制选中(self):  # 复制选中的内容
    selection = self.ui.table_echo.selectionModel()
    if not selection.hasSelection():
        return

    # 获取选中行的数据
    rows = selection.selectedIndexes()[0].data()
    # 写入剪贴板
    QApplication.clipboard().setText(rows.strip())

def 表格保存(self):  # 将表格保存
    model = self.ui.table_echo.model()
    if not model:
        return
    文件名 = f"{self.file_path}/{self.vol指令}.csv"
    with open(文件名, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # 写入数据
        for row in range(model.rowCount()):
            row_data = [model.index(row, col).data() for col in range(model.columnCount())]
            writer.writerow(row_data)


    """
    def 导出(self):  # 指定数据导出
        新命令 = self.指令

    def 表格选中(行头):
        try:
            selection = self.ui.print_echo.selectionModel()  # 获取当前表格的选中内容
            if not selection.hasSelection():  # 如果没有选中内容，直接返回
                return
            model = self.ui.print_echo.model()  # 获取当前表格控件
            selected_row = selection.selectedIndexes()[0].row()
            for i in range(model.columnCount()):  # 获取指定行头的坐标
                index = model.index(0, i)
                if index.data().lower() == 行头:
                    first_column_data = model.index(selected_row, i).data()
                    return first_column_data
        except Exception:
            pass

    if not self.指令:  # 获取当前命令
        error_data = [["错误类型", "无数据，请检查命令是否正确"]]
        数据输出(self, error_data)
        return
    if any(command in self.指令 for command in 可导出列表):
        行头列表 = ["pid", "name", "base", "offset"]
        try:
            for i in 行头列表:
                数据 = 表格选中(i)
                if 数据:
                    if 数据 != "-":
                        if i == "offset":
                            新命令 += f' --filter "{数据}"'
                        else:
                            新命令 += f' --{i} "{数据}"'
        except Exception:
            pass

    新命令 = f"{新命令} --dump "
    命令执行(self, 新命令)

    """


''''-----------数据分析-----------------'''

单人层级 = []
列数据 = []

def 数据库连接(self):
    with sqlite3.connect(f"{self.file_path}/数据分析.db") as conn:  # 打开或创建数据库连接
        conn.execute("PRAGMA synchronous = OFF")  # 关闭同步模式,提高写入速度
        conn.execute("PRAGMA journal_mode = WAL")  # 使用WAL模式，提高并发性能 # 创建游标
        cursor = conn.cursor()
        return conn, cursor
def 数据库创建(self,sample_data):
    conn, cursor = 数据库连接(self)
    try:
        # 检查表是否存在
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='fenxi'")
        if not cursor.fetchone():
            # 表不存在，创建表
            num_columns = len(sample_data[0])
            columns = [f"col_{i+1}" for i in range(num_columns)]
            create_sql = f"CREATE TABLE fenxi ({', '.join([f'{col} TEXT' for col in columns])})"
            cursor.execute(create_sql)
            conn.commit()
    except Exception as e:
        self.text_输出(f"数据库操作失败: {str(e)}")
        return
    finally:
        conn.close()


def 处理文件(self, file_lsit):
    for file in file_lsit:
        # 先读取文件获取列数
        sample_data = []
        chunk_size = 10000
        try:
            if file.lower().endswith('.txt'):
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        chunk = []
                        for line in f:
                            if line.strip():
                                sample_data.append([line.strip()])
                                # 检查数据库是否存在
                                if not os.path.exists(f"{self.file_path}/数据分析.db"):
                                    数据库创建(self, sample_data)
                                chunk.append([line.strip()])
                                if len(chunk) >= chunk_size:  #  10000行写入一次数据库
                                    批量入库(self, chunk)
                                    chunk = []
                                    self.text输出(f"正在处理文件: {os.path.basename(file)}")
                        if chunk:
                            批量入库(self, chunk)
                except Exception as e:
                    self.text_输出(f"txt失败: {str(e)}")

            elif file.lower().endswith('.csv'):
                try:
                    sample_data = pd.read_csv(file, nrows=1).values.tolist()
                    if not os.path.exists(f"{self.file_path}/数据分析.db"):
                        数据库创建(self, sample_data)
                    n = 1
                    for chunk in pd.read_csv(file, chunksize=chunk_size):
                        data = chunk.values.tolist()
                        # data = list(set(tuple(row) for row in data))
                        self.start_thread(批量入库,self, data)
                        self.text_输出(f"正在处理文件第{n}0000行")
                        n += 1
                except Exception as e:
                    self.text_输出(f"csv失败: {str(e)}")

            elif file.lower().endswith(('.xlsx', '.xls')):
                try:
                    sample_data = pd.read_excel(file, nrows=1).values.tolist()
                    if not os.path.exists(f"{self.file_path}/数据分析.db"):
                        数据库创建(self, sample_data)
                    df = pd.read_excel(file)
                    for i in range(0, len(df), chunk_size):
                        chunk = df.iloc[i:i+chunk_size]
                        data = chunk.values.tolist()
                        # data = list(set(tuple(row) for row in data))
                        批量入库(self, data)
                        self.text_输出(f"正在处理文件第{chunk_size}行")
                except Exception as e:
                    self.text_输出(f"excel失败: {str(e)}")

        except Exception as e:
            self.text_输出(f"文件读取失败: {str(e)}")
            return


def 数据入库(self):  # 文件数据入库
    # UI初始化
    self.ui.select_one.setEnabled(True)
    self.ui.show_guanxi.setEnabled(True)
    self.ui.list_clear.setEnabled(True)

    if not self.file_name:
        QMessageBox.warning(self, "警告", "请先选择文件或文件夹！")
        return
    self.is_running = True
    # 获取需要处理的文件列表
    if os.path.isdir(self.file_name):
        file_list = [os.path.join(self.file_path, f) for f in os.listdir(self.file_path) 
                    if os.path.isfile(os.path.join(self.file_path, f)) and 
                    f.lower().endswith(('.txt', '.csv', '.xlsx','.xls'))]
    else:
        if self.file_name.lower().endswith(('.txt', '.csv', '.xlsx','.xls')):
            file_list = [self.file_name]
        else:
            QMessageBox.warning(self, "警告", "只支持txt/csv/xlsx/xls文件 格式！")
            return
            
    self.text_输出("开始导入数据...")
    
    # 多线程处理文件
    处理文件(self, file_list)
    # 等待任务完成再显示数据
    数据显示(self)  # 显示数据

def 批量入库(self, data):
    if not data:
        return
    with self.db_lock:  # 需要在类初始化时定义self.db_lock = threading.Lock()
        conn, cursor = 数据库连接(self)
        try:
            # 获取表结构信息
            cursor.execute("PRAGMA table_info(fenxi)")
            columns = [col[1] for col in cursor.fetchall()]  # 获取所有列名
            num_columns = len(columns)
            
            # 数据去重
            seen = set()
            unique_data = []
            for row in data:
                row_tuple = tuple(row)
                if row_tuple not in seen:
                    seen.add(row_tuple)
                    unique_data.append(row)

            # 动态生成插入语句
            if unique_data:
                placeholders = ",".join(["?"] * num_columns)
                sql = f"INSERT INTO fenxi VALUES ({placeholders})"
                cursor.executemany(sql, unique_data)
                conn.commit()

        except Exception as e:
            self.text_输出(f"数据库写入失败: {str(e)}")
        finally:
            conn.close()


def 数据显示(self):
    """显示数据"""
    conn, cursor = 数据库连接(self)
    try:
        # 获取数据库表的列名（表头）
        cursor.execute("PRAGMA table_info(fenxi)")
        columns = [col[1] for col in cursor.fetchall()]  # 例如：['col_1', 'col_2', 'col_3']

        cursor.execute("SELECT * FROM fenxi LIMIT 100")
        data = cursor.fetchall()
        
        display_data = [columns] + data  # 关键修改：添加表头行
        # 如果有数据，设置表头
        if data and hasattr(self, 'ui') and hasattr(self.ui, 'table_echo'):
            from PySide6.QtGui import QStandardItemModel
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(columns)  # 使用真实列名作为表头
            self.ui.table_echo.setModel(model)
            
        self.table_输出(display_data)  # 传递包含表头和数据的完整列表
        
    except Exception as e:
        self.text_输出(f"数据库查询失败: {str(e)}")
    finally:
        conn.close()

def 数据库查询(self):
    """执行 SQL 查询并将结果显示在表格中"""
    query = self.ui.db_str.text().strip()
    if not query:
        return
    # 防注入
    query = re.sub(r"['\"“”‘’]", "'", query)
    results = 执行查询(self, query)
    try:
        self.table_输出(results)
    except Exception as e:
        self.text_输出(f"查询执行失败: {str(e)}")

def 执行查询(self, query):
    conn, cursor = 数据库连接(self)
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.execute("PRAGMA table_info(fenxi)")
        columns = [col[1] for col in cursor.fetchall()]
        display_data = [columns] + data
        return display_data
    except Exception as e:
        self.text_输出(f"查询执行失败: {str(e)}")
    finally:
        conn.close()


def 删除数据库(self):
    """删除数据库文件"""
    db_path = f"{self.file_path}/数据分析.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        self.text_输出("数据库文件已删除")
    else:
        self.text_输出("数据库文件不存在")


### @todo ! fnMap (待办) 查询语法再增加一点

def 查询语法(self):
    """将语法说明按行text_输出到表格中"""
    # 定义语法说明
    syntax_lines = [
        ["SQL语法说明", ""],
        ["SELECT * FROM table", "查询表中所有数据"],
        ["SELECT col1,col2 FROM table", "查询指定列"],
        ["WHERE condition", "条件查询"],
        ["ORDER BY col", "按列排序"],
        ["LIMIT n", "限制返回行数"]
    ]
    self.table_输出(syntax_lines)  # 将每一行作为单独的一行数据添加到表格中


def 查询上线(self):

    单人层级 = []
    唯一ID = self.ui.data_input.text().strip()
    查询信息 = ""
    #层级 = 1
    try:
        conn, cursor = 数据库连接(self)
        cursor.execute("SELECT * FROM fenxi WHERE A=?", (唯一ID,))
        data = cursor.fetchone()
        if data:
            查询信息 = f"ID: {data[0]}, 名称: {data[1]}"
            单人层级.append(查询信息)
        conn.close()
    except Exception as e:
        self.text_输出(f"查询失败: {str(e)}")


def 生成树状图(self):
  # 清空表格
    """生成可折叠的层级树状图"""
    try:
        conn, cursor = 数据库连接(self)
        cursor.execute("SELECT * FROM fenxi")
        data = cursor.fetchall()
        conn.close()

        # 生成HTML树状图代码
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>层级关系图</title>
    <style>
        .tree ul {{
            padding-left: 20px;
            list-style-type: none;
        }}
        .tree li {{
            margin: 5px 0;
        }}
        .tree li:before {{
            content: "+ ";
            color: blue;
            cursor: pointer;
        }}
        .tree li.collapsed:before {{
            content: "- ";
        }}
        .tree li.collapsed > ul {{
            display: none;
        }}
    </style>
</head>
<body>
    <h2>人员层级统计（总人数：{len(data)}，最大层级：{max([int(row[2]) for row in data] if data else 0)}）</h2>
    <div id="tree">
        <ul>
            {''.join([f'<li>{row[1]} (ID: {row[0]}, 层级: {row[2]})</li>' for row in data])}
        </ul>
    </div>
    <script>
        document.querySelectorAll('.tree li').forEach(li => {{
            li.addEventListener('click', function(e) {{
                e.stopPropagation();
                this.classList.toggle('collapsed');
            }});
        }});
    </script>
</body>
</html>"""
        self.text_输出(html)
    except Exception as e:
        self.text_输出(f"生成树状图失败: {str(e)}")