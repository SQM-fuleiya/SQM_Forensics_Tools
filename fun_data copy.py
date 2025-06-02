import os
import re
import sqlite3
import csv

#import chardet
import pandas as pd

from PySide6.QtWidgets import QMessageBox ,QApplication,QInputDialog 


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

def 表格清理(self):  # 清空表格
    self.ui.table_echo.clearContents()
''''-----------数据分析-----------------'''
def 按钮开关判断(self):
    db_path = f"{self.file_path}数据分析.db"
    if os.path.exists(db_path):
        self.ui.revise_column_name.setEnabled(True)
        self.ui.db_select_but.setEnabled(True)

        self.ui.select_one_up.setEnabled(True)
        self.ui.select_one_down.setEnabled(True)
        self.ui.show_guanxi.setEnabled(True)

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
        if not cursor.fetchone(): # 表不存在，创建表
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
                    with open(file, "r", encoding='utf-8') as f:
                        lines = f.readlines()
                        self.text_输出(f"正在处理文件: {os.path.basename(file)}")
                        for line in lines:
                            line = line.replace(" ",'').split('\\n')
                            for i in line :
                                if len(i) > 2:
                                    i = i.split('|')
                                    print(i)
                                    sample_data.append(i)
                                    if len(sample_data) >= chunk_size:
                                        if not os.path.exists(f"{self.file_path}/数据分析.db"):
                                            数据库创建(self, sample_data)
                                        批量入库(self, sample_data)
                                        sample_data = []               
                except Exception as e:
                    self.text_输出(f"txt失败: {str(e)}")

            elif file.lower().endswith('.csv'):
                try:
                    # 尝试多种编码格式
                    encodings = ['utf-8', 'gbk']
                    for encoding in encodings:
                        try:
                            sample_data = pd.read_csv(file, nrows=1, encoding=encoding).values.tolist()
                            if not os.path.exists(f"{self.file_path}/数据分析.db"):
                                数据库创建(self, sample_data)
                            n = 1
                            for chunk in pd.read_csv(file, chunksize=chunk_size, encoding=encoding):
                                data = chunk.values.tolist()
                                self.start_thread(批量入库,self, data)
                                self.text_输出(f"正在处理文件第{n}0000行")
                                n += 1
                            break  # 如果成功就跳出循环
                        except UnicodeDecodeError:
                            continue
                    else:
                        self.text_输出(f"无法解码文件 {file}，尝试了多种编码格式")
                        continue
                except Exception as e:
                    self.text_输出(f"csv失败: {str(e)}")

            elif file.lower().endswith(('.xlsx', '.xls')):
                try:
                    sample_data = pd.read_excel(file, nrows=1, engine='openpyxl').values.tolist()
                    if not os.path.exists(f"{self.file_path}/数据分析.db"):
                        数据库创建(self, sample_data)
                    n = 1
                    for chunk in pd.read_excel(file, chunksize=chunk_size, engine='openpyxl'):
                        data = chunk.values.tolist()
                        批量入库(self, data)
                        self.text_输出(f"正在处理文件第{n*chunk_size}行")
                        n += 1
                except Exception as e:
                    self.text_输出(f"excel失败: {str(e)}")
                    self.text_输出("也许不是excel文件，请尝试打开并另存为csv格式")


        except Exception as e:
            self.text_输出(f"文件读取失败: {str(e)}")
            return

def 数据入库(self):  # 文件数据入库

    # UI初始化
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
    for thread in self.threads:
        thread.wait()
    self.text_输出("数据导入完成！")
    self.is_running = False
    数据显示(self)  # 显示数据
    按钮开关判断(self)

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
                # 确保每行数据列数与表结构匹配
                if len(row) != num_columns:
                    row = row[:num_columns]  # 截断多余列
                    if len(row) < num_columns:  # 不足则填充空值
                        row += [""] * (num_columns - len(row))
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
            # 打印出错的SQL语句和数据用于调试
            self.text_输出(f"SQL语句: {sql}")
            self.text_输出(f"数据样例: {unique_data[0] if unique_data else '无数据'}")
        finally:
            conn.close()

def 数据显示(self):
    """显示数据"""
    conn, cursor = 数据库连接(self)
    try:
        # 获取数据库表的列名（表头）
        cursor.execute("SELECT name FROM PRAGMA_TABLE_INFO('fenxi')") # 判断表是否存在
        if not cursor.fetchone():
            self.text_输出("数据库中没有fenxi表")
            return
        cursor.execute("PRAGMA table_info(fenxi)") # 获取表结构信息
        columns = [col[1] for col in cursor.fetchall()] # 获取所有列名

        cursor.execute("SELECT * FROM fenxi LIMIT 100") # 查询前100行数据
        data = cursor.fetchall()
        data.insert(0, columns) # 将列名插入到数据的第一行
        self.table_输出(data)
        
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

def 修改列名(self):
    """修改数据库表的列名"""
    conn, cursor = 数据库连接(self)
    try:
        # 获取数据库表的列名（表头）
        cursor.execute("PRAGMA table_info(fenxi)")
        columns_info = cursor.fetchall()  # 获取所有列信息
        if not columns_info:
            self.text_输出("数据库中没有fenxi表")
            return
            
        # 提取列名列表
        columns = [col[1] for col in columns_info]  # 列名在元组的第二个位置
        
        # 获取用户输入的新列名列表
        from PySide6.QtWidgets import QInputDialog
        new_column_names, ok = QInputDialog.getText(
            self, 
            "修改列名", 
            f"当前列名: {', '.join(columns)}\n请输入新列名(用逗号分隔):"
        )
        
        if not ok or not new_column_names:
            return
            
        # 分割用户输入为列名列表
        new_columns = [name.strip() for name in new_column_names.split(',')]
        
        # 检查列数量是否匹配
        if len(new_columns) != len(columns):
            self.text_输出(f"错误: 需要{len(columns)}个列名，但提供了{len(new_columns)}个")
            return
            
        # 构建并执行修改列名的SQL语句
        for old_name, new_name in zip(columns, new_columns):
            if old_name != new_name:  # 只修改名称不同的列
                sql = f"ALTER TABLE fenxi RENAME COLUMN {old_name} TO {new_name}"
                cursor.execute(sql)
                
        conn.commit()
        self.text_输出(f"列名已修改为: {', '.join(new_columns)}")
        
    except Exception as e:
        self.text_输出(f"修改列名失败: {str(e)}")
    finally:
        conn.close()
    数据显示(self)

def 查询语法(self):
    """将语法说明按行text_输出到表格中"""
    # 定义语法说明
    syntax_lines = [
        ["SQL语法说明", "方法","说明"],
        ["一般查询","",""],
        ["查询表中所有数据","SELECT * FROM fenxi",""],
        ["查询指定列     ","SELECT <col1>,<col2> FROM fenxi",""],
        ["","",""],
        ['select 后面可以加的条件'],
        ['对列进行条件查询',"SELECT 条件(*) FROM fenxi"],
        ["聚合函数       ","SUM(), AVG(), COUNT(), MAX(), MIN()","SUM()总和, AVG()平均值, COUNT()计数, MAX()最大值, MIN()最小值"],
        ["去重查询       ","DISTINCT()","DISTINCT表示去重"],
        ["绝对值查询     ","ABS()","ABS 函数返回数值参数的绝对值,通常用在有正负的数值计算时"],
        ["字符串大小转换 ","UPPER(), LOWER(),LENGTH()",'UPPER()将字符串转换为大写, LOWER()将字符串转换为小写,LENGTH()返回字符串的长度'],
        ["","",""],
        ['查询后过滤     ', "",""],
        ["条件查询       ","WHERE <条件>",'如果满足给定的条件，即为真（true）时，则从表中返回特定的值'],
        ["按列排序       ","ORDER BY <col>"],
        ["限制返回行数   ","LIMIT <num>"],
        ["模糊查询       ","LIKE 'Ki%'","%表示任意字符"],
        ["正则表达式查询 ","REGEXP 'Ki.*'","REGEXP表示正则表达式"],
        ["分组查询       ","GROUP BY <col>","GROUP BY表示对结果进行分组"],
        ["通配符查询     ","GLOB 'XXXX?'","GLOB表示通配符查询,*：匹配多个字符,?：匹配单个字符,[abc]：匹配a、b、c中的任意一个字符,[!abc]：匹配除了a、b、c中的任意一个字符"],
        ["","",""],
        ['高级查询', "",""],
        ["AND/OR查询     ","WHERE <条件1> AND <条件2> OR <条件3>",'多个条件之间使用AND或OR连接'],
        ["子查询         ","IN (SELECT col2 FROM fenxi WHERE col3 = 'value')",'子查询可以嵌套，也可以使用IN或NOT IN进行条件查询'],
    ]
    self.table_输出(syntax_lines)  # 将每一行作为单独的一行数据添加到表格中

'---------------文件转换-------------'
def txt转csv(self):
    if os.path.isdir(self.file_name):
        file_list = [os.path.join(self.file_path, f) for f in os.listdir(self.file_path) 
                    if os.path.isfile(os.path.join(self.file_path, f)) and 
                    f.lower().endswith('.txt')]
    else:
        if self.file_name.lower().endswith('.txt'):
            file_list = [self.file_name]
        else:
            QMessageBox.warning(self, "警告", "只支持txt文件 格式！")
            return
    try:
        for file in file_list:
            self.text_输出(f"正在处理文件: {file}")
            data = []
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.replace(" ",'').split('\\n')
                    for i in line :
                        if len(i) > 2:
                            i = i.split('|')
                            data.append(i)
    except Exception as e:
        self.text_输出(f"读取文件 {file} 失败: {str(e)}")
         
    try:
        output_path = os.path.join(self.file_path, '合并的数据.csv')
        with open(output_path, "w", encoding="utf-8",newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
    except Exception as e:
        self.text_输出(f"写入CSV文件失败: {str(e)}")
    self.text_输出(f"文件转换完成，保存路径: {output_path}")


'''-------------层级分析-------------'''

def 层级分析获取列名(self):
    conn, cursor = 数据库连接(self)
    cursor.execute("PRAGMA table_info(fenxi)")
    columns = [col[1] for col in cursor.fetchall()]
    if len(columns) < 3:
        QMessageBox.warning(self, "警告", "数据库表列数不足3列")
        return
    # 让用户选择指定的列名
    items = []
    重要列名 = ['','唯一ID','上下线ID']
    for i in range(1, 3):
        col, ok = QInputDialog.getItem(
            self, 
            "选择列", 
            f"请从下拉列表中选择{重要列名[i]}的列名:", 
            columns, 
            0, 
            False
        )
        if not ok or not col:
            return
        items.append(col)
    return items

def 查询上下线(self):
    # 获取用户输入的查询ID和列名
    初始ID, ok1 = QInputDialog.getText(self, "输入要查询的ID", "请输入要查询的ID:")
    if not ok1 or not 初始ID:
        return 
    try:
        列名列表 = 层级分析获取列名(self)
    except Exception as e:
        self.text_输出(f"获取列名失败: {str(e)}")
        return
    结果列表 = []
    try:
        conn, cursor = 数据库连接(self)
        while True:
            cursor.execute(f"SELECT * FROM fenxi WHERE {列名列表[0]} = {初始ID}")
            data = cursor.fetchone()
            if not data:
                break
            # 添加到结果列表
            结果列表.append(list(data))
            cursor.execute(f"SELECT {列名列表[1]} FROM fenxi WHERE {列名列表[0]} = {初始ID}")
            初始ID = cursor.fetchone()[0]
            if not 初始ID:
                break
        conn.close()

        if 结果列表: 
            结果列表.insert(0, ['查询结果:'])
            self.table_输出(结果列表)
        else:
            self.text_输出("没有找到相关数据")
    except Exception as e:
        self.text_输出(f"查询执行失败: {str(e)}")

def 树状图(self):
    """重构后的层级分析函数，支持新的数据结构"""
    try:
        # 获取所有人员数据
        conn, cursor = 数据库连接(self)
        cursor.execute("SELECT * FROM fenxi")
        all_data = cursor.fetchall()
        
        if not all_data:
            self.text_输出("数据库中没有人员数据")
            return
            
        # 构建两个映射字典：ID->数据和上线ID->下线ID列表
        id_to_data = {}
        parent_to_children = {}
        
        for row in all_data:
            user_id, user_name, parent_id, _ = row[:4]
            id_to_data[user_id] = {'name': user_name, 'parent_id': parent_id}
            
            if parent_id not in parent_to_children:
                parent_to_children[parent_id] = []
            parent_to_children[parent_id].append(user_id)
        
        # 找出所有顶层节点（没有上线或上线不在系统中的节点）
        top_nodes = []
        for user_id, data in id_to_data.items():
            parent_id = data['parent_id']
            if not parent_id or parent_id not in id_to_data:
                top_nodes.append(user_id)
        
        # 如果没有顶层节点，选择第一个节点作为顶层
        if not top_nodes and all_data:
            top_nodes = [all_data[0][0]]
            
        if not top_nodes:
            self.text_输出("错误：无法确定顶层节点")
            return
            
        # 递归构建层级结构
        def build_hierarchy(node_id, processed_ids=None):
            if processed_ids is None:
                processed_ids = set()
                
            if node_id in processed_ids:
                self.text_输出(f"发现循环引用: {node_id}，跳过处理")
                return None
                
            processed_ids.add(node_id)
            
            # 获取节点信息
            node_data = id_to_data.get(node_id, {})
            if not node_data:
                return None
                
            # 获取所有下线
            children_ids = parent_to_children.get(node_id, [])
            
            # 构建节点结构
            node = {
                'ID': node_id,
                '姓名': node_data['name'],
                '直属下线数': len(children_ids),
                '下线总人数': 0,
                '下级': []
            }
            
            # 递归处理每个下线
            for child_id in children_ids:
                child_node = build_hierarchy(child_id, processed_ids.copy())
                if child_node:
                    node['下级'].append(child_node)
                    node['下线总人数'] += child_node['下线总人数'] + 1
            
            self.text_输出(f"处理完成: {node['姓名']}(ID:{node_id}), 直属下线: {node['直属下线数']}, 总下线: {node['下线总人数']}")
            return node
            
        # 从所有顶层节点开始构建层级
        hierarchy = []
        for top_id in top_nodes:
            top_node = build_hierarchy(top_id)
            if top_node:
                hierarchy.append(top_node)
        
        # 合并多个顶层节点的结构（如果有多个顶层）
        if len(hierarchy) > 1:
            merged_hierarchy = {
                'ID': 'TOP',
                '姓名': '顶层节点汇总',
                '直属下线数': len(hierarchy),
                '下线总人数': sum(node['下线总人数'] for node in hierarchy),
                '下级': hierarchy
            }
            hierarchy = merged_hierarchy
        elif hierarchy:
            hierarchy = hierarchy[0]
            
        # 保存结果
        import json
        output_path = os.path.join(self.file_path, '层级关系.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(hierarchy, f, ensure_ascii=False, indent=4)
            
        self.text_输出(f"层级关系数据已保存到: {output_path}")
        os.startfile(output_path)
        显示树状图(output_path)
        
    except Exception as e:
        self.text_输出(f"生成树状图失败: {str(e)}")
    finally:
        conn.close()

def 递归查询下线(self, node_id, id_to_data, parent_to_children, processed_ids=None):
    """辅助递归函数，用于构建层级结构"""
    if processed_ids is None:
        processed_ids = set()
        
    if node_id in processed_ids:
        self.text_输出(f"发现循环引用: {node_id}，跳过处理")
        return None
        
    processed_ids.add(node_id)
    
    # 获取节点信息
    node_data = id_to_data.get(node_id, {})
    if not node_data:
        return None
        
    # 获取所有下线
    children_ids = parent_to_children.get(node_id, [])
    
    # 构建节点结构
    node = {
        'ID': node_id,
        '姓名': node_data['name'],
        '直属下线数': len(children_ids),
        '下线总人数': 0,
        '下级': []
    }
    
    # 递归处理每个下线
    for child_id in children_ids:
        child_node = self.递归查询下线(child_id, id_to_data, parent_to_children, processed_ids.copy())
        if child_node:
            node['下级'].append(child_node)
            node['下线总人数'] += child_node['下线总人数'] + 1
    
    return node


def 显示树状图(json文件路径, 输出html路径=None):
    """生成网页版树状图"""
    import json
    from pathlib import Path
    
    if 输出html路径 is None:
        输出html路径 = Path(json文件路径).with_suffix('.html')
    
    with open(json文件路径, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 生成HTML内容
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>组织结构图 - {data['姓名']}</title>
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                margin: 20px;
                line-height: 1.6;
            }}
            .tree {{ margin-left: 20px; }}
            .node {{ cursor: pointer; }}
            .node:hover {{ color: #0066cc; }}
            .hidden {{ display: none; }}
            .toggle {{ 
                color: #666;
                margin-right: 5px;
                cursor: pointer;
            }}
            .summary {{ 
                color: #666;
                font-size: 0.9em;
                margin-left: 10px;
            }}
        </style>
    </head>
    <body>
        <h2>组织结构图 - {data['姓名']} (总人数: {data['下线总人数']})</h2>
        <div id="tree"></div>
        
        <script>
            const data = {json.dumps(data)};
            const treeContainer = document.getElementById('tree');
            
            function 构建树(节点, 父元素, 层级 = 0) {{
                const nodeDiv = document.createElement('div');
                nodeDiv.className = 'node';
                
                const toggleSpan = document.createElement('span');
                toggleSpan.className = 'toggle';
                toggleSpan.textContent = 节点.下级.length > 0 ? '[-]' : '';
                toggleSpan.onclick = function() {{
                    const childrenDiv = this.parentNode.nextElementSibling;
                    if (childrenDiv.classList.contains('hidden')) {{
                        childrenDiv.classList.remove('hidden');
                        this.textContent = '[-]';
                    }} else {{
                        childrenDiv.classList.add('hidden');
                        this.textContent = '[+]';
                    }}
                }};
                
                const nameSpan = document.createElement('span');
                nameSpan.textContent = `${{节点.姓名}} (ID:${{节点.ID}})`;
                
                const summarySpan = document.createElement('span');
                summarySpan.className = 'summary';
                summarySpan.textContent = `[直属下线:${{节点.直属下线数}} 总下线:${{节点.下线总人数}}]`;
                
                nodeDiv.appendChild(toggleSpan);
                nodeDiv.appendChild(nameSpan);
                nodeDiv.appendChild(summarySpan);
                父元素.appendChild(nodeDiv);
                
                if (节点.下级.length > 0) {{
                    const childrenDiv = document.createElement('div');
                    childrenDiv.className = 'tree';
                    if (层级 > 0) {{
                        childrenDiv.classList.add('hidden');
                        toggleSpan.textContent = '[+]';
                    }}
                    
                    节点.下级.forEach(child => 构建树(child, childrenDiv, 层级 + 1));
                    父元素.appendChild(childrenDiv);
                }}
            }}
            
            构建树(data, treeContainer);
        </script>
    </body>
    </html>
        """
    
    with open(输出html路径, 'w', encoding='utf-8') as f:
        f.write(html)
    


if __name__ == "__main__":
    显示树状图('C:\\Users\\wadd\\Desktop\\测试\\层级关系练习\\层级关系.json')