import sqlite3
import pandas as pd
import os

def 数据库连接(database_path):
    with sqlite3.connect(f"{database_path}\数据分析.db") as conn:  # 打开或创建数据库连接
        conn.execute("PRAGMA synchronous = OFF")  # 关闭同步模式,提高写入速度
        conn.execute("PRAGMA journal_mode = WAL")  # 使用WAL模式，提高并发性能 # 创建游标
        cursor = conn.cursor()
        return conn, cursor


def 层级分析(database_path):
    #列名列表 = 层级分析获取列名(self)
    #if not 列名列表 or len(列名列表) < 2:
    #    return
    # id_col = 列名列表[0]  # 唯一ID列
    # parent_col = 列名列表[1]  # 上线ID列

    id_col = 'col_2'
    parent_col = 'col_4'

    # 查询顶层节点（处理两种情况：1. 没有上线的节点 2. 在parent_col但不在id_col中的节点）
    try:
        conn, cursor = 数据库连接(database_path)
        cursor.execute(f"""
                SELECT DISTINCT {parent_col} FROM fenxi 
                WHERE {parent_col} NOT IN (SELECT {id_col} FROM fenxi) 
                AND {parent_col} IS NOT NULL  LIMIT 1""")
        顶层节点 = cursor.fetchone()
        conn.close()
    except Exception as e:
        print(f"查询顶层节点失败: {str(e)}")
        return
     
            
    if 顶层节点:
        顶层ID = 顶层节点[0]
        层级数据 = 递归查询下线( 顶层ID, id_col, parent_col)
    else:
        print("错误：无法确定顶层节点")
        return


    # 将结果保存为JSON文件
    import json
    output_path = 'C:\\Users\\wadd\\Desktop\\测试\\层级关系练习\\层级关系.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(层级数据, f, ensure_ascii=False, indent=4)
        
    print(f"层级关系数据已保存到: {output_path}")
    os.startfile(output_path)  # 自动打开文件
    # 显示树状图(output_path)
        

def 递归查询下线(当前ID, id_col, parent_col, 上级列表=None, 已处理IDs=None):
    """递归查询下线关系（添加上级列表保护）"""
    if 已处理IDs is None:
        已处理IDs = set()
    if 上级列表 is None:
        上级列表 = []
    
    # 防止循环引用和重复处理
    if 当前ID in 已处理IDs or 当前ID in 上级列表:
        print(f"发现循环/重复ID: {当前ID}，跳过处理")
        return None
    
    上级列表.append(当前ID)
    已处理IDs.add(当前ID)

    try:
        conn, cursor = 数据库连接(database_path)
        # 查询当前节点信息
        cursor.execute(f"SELECT * FROM fenxi WHERE {parent_col} = ?", (当前ID,))
        current_data = cursor.fetchone()
        if not current_data:
            conn.close()
            return None

        # 查询所有下线（不再限制上级列表）
        cursor.execute(f"SELECT {id_col} FROM fenxi WHERE {parent_col} = ?", (当前ID,))
        下线列表 = [row[0] for row in cursor.fetchall()]
        conn.close()

        print(f"开始处理节点 {当前ID}，找到 {len(下线列表)} 个直接下线")

        节点 = {
            'ID': str(当前ID),
            '姓名': str(current_data[0]),
            '直属下线数': len(下线列表),
            '下线总人数': 0,  # 初始化为0，后续累加
            '下级': []
        }

        # 处理每个下线
        processed_count = 0
        for index, 下线ID in enumerate(下线列表, 1):
            print(f"正在处理第 {index}/{len(下线列表)} 个下线: {下线ID}")
            下级节点 = 递归查询下线(下线ID, id_col, parent_col, 上级列表.copy(), 已处理IDs)
            
            if 下级节点 is None:
                print(f"下线 {下线ID} 处理返回空，跳过")
                continue
                
            if not isinstance(下级节点, dict) or '下线总人数' not in 下级节点:
                print(f"下线 {下线ID} 返回无效数据格式，跳过")
                continue
                
            节点['下级'].append(下级节点)
            节点['下线总人数'] += 下级节点['下线总人数']
            processed_count += 1
            print(f"完成处理下线 {下线ID}，累计总下线: {节点['下线总人数']}")

        # 添加直接下线人数
        节点['下线总人数'] += processed_count
        print(f"节点 {当前ID} 处理完成: 有效下线 {processed_count}/{len(下线列表)}，总下线 {节点['下线总人数']}")

        return 节点

    except Exception as e:
        print(f"查询失败: {str(e)}")
        return None
    finally:
        conn.close()
        # 回溯时移除当前ID，保持上级列表状态
        上级列表.pop()


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
    

if __name__ == '__main__':
    database_path = 'C:\\Users\\wadd\\Desktop\\测试\\层级关系练习'
    层级分析(database_path)
