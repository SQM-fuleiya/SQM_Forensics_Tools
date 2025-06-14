# SQM 取证分析工具集

基于Python + PySide6开发的本地取证分析工具，提供文件分析、网络流量分析、内存取证等多种功能。

## 主要功能模块

### 文件分析
- 文本分析：字符统计、关键字搜索、字符串提取、文件类型识别等
- 编码转换: html编码 url编码 全base64编码 栅栏凯撒编码等
- 图片处理: LSB隐写检测、PNG高宽爆破、JPG块分析等
- 压缩包分析：伪加密检测、CRC爆破等

### 网络分析
- 常用ctf流量解析
- SQL注入解析
- webshell分析：菜刀 蚁剑 哥斯拉 冰蝎3 冰蝎4 流量解析

### 内存取证
- 集成Volatility 2/3框架
- 进程分析、注册表解析、恶意软件检测
- 支持Windows/Linux内存镜像分析

### 数据分析
- txt excel csv 等文件转换为SQLite数据库 
- SQLite数据库自定义查询与分析
- 上线下分析及层级关系图谱生成

### 逆向分析
- ios分析：Plist文件解析
- android：frida hook 
- python: 反编译
- 人工智能软件: facefusion配置文件分析
- 常用软件配置分析: 还没做
- 各种小脚本合集

## 运行环境

- Python 3.11+
- 依赖库：
  ```bash
  pip install -r requirements.txt

## 项目结构

- main.py              # 主程序入口
- main_ui.py           # Qt界面定义
- fun_file.py          # 文件分析模块
- fun_net.py           # 网络分析模块  
- fun_vol.py           # 内存取证模块
- fun_others.py        # 其他工具模块
- fun_data.py          # 数据处理模块
- tools/               # 集成工具(Volatility等)
- mod/                 # 扩展模块
- output/              # 输出目录


## 使用说明
### 源码使用
1. 克隆项目到本地：
   ```bash
   git clone https://github.com/yourusername/SQM_Forensics_Tools.git
   cd SQM_Forensics_Tools
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行主程序：
   ```bash
   python main.py
   ```
### 编译使用
1. 下载发行版运行 exe文件即可。

## 功能特点
- 可视化操作界面，支持文件拖拽
- 模块化设计，易于功能扩展
- 集成多种取证分析工具
- 自动化报告生成
- 支持自定义插件开发

## 许可证

MIT License
Copyright (c) 2025 SQM