# SQM 取证分析工具集

基于Python + PySide6开发的本地取证分析工具，提供文件分析、网络流量分析、内存取证等多种功能。

## 主要功能模块

### 文件分析
- 图片分析：LSB隐写检测、PNG高宽爆破、JPG块分析
- 压缩包分析：伪加密检测、CRC爆破
- 多媒体处理：GIF帧分离与合并
- 数据转换：RGB转图片、坐标转图片

### 网络分析
- 流量包解析：HTTP请求/响应分析
- 注入检测：SQL注入、XSS等攻击检测
- 协议分析：支持常见网络协议解析

### 内存取证
- 集成Volatility 2/3框架
- 进程分析、注册表解析、恶意软件检测
- 支持Windows/Linux内存镜像分析

### 其他工具
- 编码转换：摩斯密码、云隐密码等
- 数据可视化：关系图谱生成
- 数据库操作：SQLite数据查询与分析

## 运行环境

- Python 3.11+
- 依赖库：
  ```bash
  pip install -r requirements.txt

## 项目结构
.
├── main.py              # 主程序入口
├── main_ui.py           # Qt界面定义
├── fun_file.py          # 文件分析模块
├── fun_net.py           # 网络分析模块  
├── fun_vol.py           # 内存取证模块
├── fun_others.py        # 其他工具模块
├── fun_data.py          # 数据处理模块
├── tools/               # 集成工具(Volatility等)
├── mod/                 # 扩展模块
└── output/              # 输出目录

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