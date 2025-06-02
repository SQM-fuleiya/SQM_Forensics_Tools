import json
import os

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QInputDialog


"--------------------------全局设置------------------------------"
config_file = "config.json"
vol3_path = "./tools/vol3/vol.py"
vol2_path = "./tools/vol2/vol.py"


# 全局设置
表格数据 = ""
v3_win_fun_list = {
    '已执行的程序信息':'windows.amcache',
    '获取系统缓存的密码哈希':'windows.cachedump',
    "查看cmd启动命令": "windows.cmdline",
    '扫描cmd历史记录':'windows.cmdscan',
    '提取cmd会话记录':'windows.consoles',
    '分析Windows崩溃转储':'windows.crashinfo',
    "列出驱动程序和关联设备树": "windows.devicetree",
    "列出进程加载的DLL模块": "windows.dlllist",
    '检测隐藏的驱动模块':'windows.drivermodule',
    "隐藏驱动扫描": "windows.driverscan",
    "环境变量信息": "windows.envars",
    "获取服务ids": "windows.getservicesids",
    "显示进程所属的 SID": "windows.getsids",
    "列出进程打开的句柄": "windows.handles",
    '从内存中转储各种凭据':'windows.lsadump',
    "检测进程中潜在的内存注入代码": "windows.malfind",
    '扫描主引导记录MBR':'windows.mbrscan',
    "扫描MFT文件对象": "windows.mftscan.MFTScan",
    '扫描网络连接对象':'windows.netscan',
    '列出内存中的进程':'windows.pslist',
    "扫描内存中的进程": "windows.psscan",
    "以树状结构显示进程父子关系": "windows.pstree",
    "检测注册表配置单元": "windows.registry.getcellroutine",
    "注册表配置信息": "windows.registry.hivelist",
    '扫描内存中的注册表配置单元':'windows.registry.hivescan',
    "列出注册表键值": "windows.registry.printkey",
    "提取记录用户执行程序的历史": "windows.registry.userassist",
    '计划任务信息':'windows.scheduled_tasks',
    "sessions会话记录": "windows.sessions",
    '获取历史执行记录':'windows.shimcachemem',
    "恶意Skeleton检测": "windows.skeleton_key_check",
    '隐藏服务检测':'windows.svcdiff',
    "扫描内存中的Windows服务": "windows.svcscan",
    "检测系统中存在的符号链接": "windows.symlinkscan",
    "查找TrueCrypt缓存的密码": "windows.truecrypt.Passphrase",
    "列出进程的虚拟地址描述符": "windows.vadinfo",
    "提取 PE 文件的版本信息": "windows.verinfo",
    "使用 YARA 规则扫描内核内存": "yarascan.YaraScan --yara-file fm.yara",
}
v3_linux_fun_list = {
    "cmd历史记录": "linux.cmdline",
    "进程树": "linux.pstree", 
}
v3_mac_fun_list = {
    "cmd历史记录": "mac.cmdline",
    "进程树": "mac.pstree",
}
可导出列表 = [
    "windows.dlllist",
    "windows.psscan",
    "windows.malfind",
    "windows.modules",
    "windows.vadinfo",
    "windows.registry.hivelist",
    "windows.registry.certificates",
]
pid开放列表 = [
    "windows.cmdline",
    "windows.dlllist",
    "windows.pstree",
    "windows.psscan",
    "windows.getsids",
    "windows.handles",
    "windows.envars",
    "windows.malfind",
    "windows.sessions",
    "windows.threads",
    "windows.privileges",
    "windows.vadinfo",
    "windows.dumpfiles",
]
offset开放列表 = [
    "windows.dlllist",
    "windows.handles",
    "windows.registry.userassist",
    "windows.registry.printkey",
]
字符串搜索列表 = ['windows.strings']
physical列表 = ["windows.pstree", "windows.psscan", "windows.psxview"]
文件名搜索列表 = ["windows.registry.hivelist", "windows.dumpfiles"]



def 设置vol(self):  # 设置vol路径
    global vol3_path, vol2_path
    config = {}

    vol3_file, ok = QInputDialog.getText(self, "设置Vol3路径,需要指定vol.py", "默认路径为:", text=vol3_path)
    if ok and vol3_file:  # 如果用户输入了内容:
        vol3_path = vol3_file
    vol2_file, ok = QInputDialog.getText(self, "设置Vol2路径,需要指定vol.py", "默认路径为:", text=vol2_path)
    if ok and vol2_file:
        vol2_path = vol2_file

    # 检查路径是否存在
    if not os.path.isfile(vol3_path) or not os.path.isfile(vol2_path):
        self.text_输出("Vol3或Vol2路径下的vol.py文件不存在，请重新输入,指定路径为到vol.py \n 如果只使用一种vol，可以将vol2和vol3设置到同一目录")
        return

    # 保存配置
    try:
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        self.text_输出("配置已保存")
    except Exception as e:
        self.text_输出(f"保存配置出错: {str(e)}")


def vol手动执行(self):
    self.ui.text_echo.clear()  # 清空table_输出框
    命令 = self.ui.vol_input.text()
    
    if not self.file_name:
        self.错误信号.emit("未选择内存文件")
        return
    if 命令:
        self.text_输出(f"正在执行命令:{命令}")
        output = os.popen(命令).read()
        分段 = output.splitlines()
        if not 分段:
            self.text_输出("无数据，请检查命令")
            return
        数据行 = [line.split("\t") for line in 分段[1:] if line.strip()]
        self.text_输出("命令执行成功,正在table_输出表格，请稍后")
        self.table_输出(self,数据行)
        
    else:
        self.text_输出("请输入要执行的命令")


"--------------------------vol3---------------------------------"

def vol3命令生成(self, 命令):  # 生成需要执行的命令
    
    if self.file_name:
        self.指令 = 命令
        if self.ui.help.isChecked():
            命令 += " -h"
            vol3命令执行(self, 命令)
            return
            
        # 只有在命令支持时才添加pid参数
        if self.ui.v3w_pid.text() and self.指令 in pid开放列表:
            命令 += f" --pid {self.ui.v3w_pid.text()}"
            self.ui.v3w_pid.clear()
            
        # 只有在命令支持时才添加physaddr参数
        if self.ui.v3w_physaddr.text() and self.指令 in offset开放列表:
            命令 += f" --physaddr {self.ui.v3w_physaddr.text()}"
            self.ui.v3w_physaddr.clear()
            
        # 只有在命令支持时才添加name-filter参数
        if self.ui.v3w_filter.text() and self.指令 in 文件名搜索列表:
            命令 += f" --name-filter {self.ui.v3w_filter.text()}"
            self.ui.v3w_filter.clear()
            
        # 总是可以添加字符串过滤
        if self.ui.v3w_str.text() and self.指令 in 文件名搜索列表:
            命令 += f" | findstr /i '{self.ui.v3w_str.text()}'"   # "\.docx \.pdf \.zip"
            self.ui.v3w_str.clear()
            
        # 只有在命令支持时才添加dump参数
        if self.ui.v3w_dump.isChecked() and self.指令 in 可导出列表:
            命令 += f" --output-dir {self.file_path}"
        
        # 注册表相关参数
        if self.指令 in ["windows.registry.hivelist", "windows.registry.hivescan"]:
            if self.ui.v3w_registry_hive.text():
                命令 += f" --registry {self.ui.v3w_registry_hive.text()}"
                self.ui.v3w_registry_hive.clear()
            if self.ui.v3w_registry_key.text():
                命令 += f" --key {self.ui.v3w_registry_key.text()}"
                self.ui.v3w_registry_key.clear()
            if self.ui.v3w_recurse.isChecked():
                命令 += " --recurse"

        vol3命令执行(self, 命令)

    else:
        self.text_输出("未选择需要解析的内存文件")


def vol3命令执行(self, 命令):  # 开始执行命令
    self.ui.text_echo.clear()  # 清空table_输出框
    if not self.file_name:
        self.错误信号.emit("未选择内存文件")
        return

    command_args = [vol3_path, "-o", self.file_path, "-f", self.file_name] + 命令.split()
    self.text_输出(f"正在执行命令: {' '.join(command_args)}")

    def _handle_finish(exit_code, exit_status):  # 进程结束处理
        if exit_code == 0:
            full_output = self.process.readAllStandardOutput().data().decode("utf-8", errors="ignore")
            分段 = full_output.splitlines()
            if not 分段:
                self.text_输出("无数据，请检查命令")
                return
            数据行 = [line.split("\t") for line in 分段[1:] if line.strip()]
            self.text_输出("命令执行成功,正在table_输出表格，请稍后")
            self.table_输出(数据行)

        else:
            error_output = self.process.readAllStandardError().data().decode("utf-8", errors="ignore")
            self.text_输出(f"命令执行失败 (Code {exit_code}): {error_output}")

    try:
        self.process = QProcess()  # 保存为实例变量
        self.process.setProgram("python")
        self.process.setArguments(command_args)

        self.process.readyReadStandardError.connect(lambda: self.text_输出(self.process.readAllStandardError().data().decode("utf-8")))
        self.process.finished.connect(_handle_finish)
        self.process.start()
    except Exception as e:
        self.错误信号.emit(f"启动失败: {str(e)}")

def 开启文件操作(self):
    # 根据复选框状态切换控件启用状态
    state = self.ui.v3w_file_but.isChecked()
    self.ui.v3w_pid.setEnabled(state)
    self.ui.v3w_physaddr.setEnabled(state)
    # self.ui.v3w_physical.setEnabled(state)
    self.ui.v3w_filter.setEnabled(state)
    self.ui.v3w_str.setEnabled(state)
    self.ui.v3w_dump.setEnabled(state)


def vol3_参数选项列表(self):  # 列表选择事件处理函数
    # 检查是否有指令
    if not self.指令:
        self.text_输出("请先选择功能")
        return
    # 控件启用规则
    控件规则 = {
        "win_pid": pid开放列表,
        "win_offset": offset开放列表,
        "win_dump": 可导出列表,
        "win_physical": physical列表,
        "win_filter": 文件名搜索列表}

    # 根据规则启用或禁用控件
    for 控件名, 规则列表 in 控件规则.items():
        getattr(self.ui, 控件名).setEnabled(self.指令 in 规则列表)

    # 特殊处理注册表相关控件
    if self.指令 == "windows.registry.hivelist" or self.指令 == "windows.registry.hivescan":
        self.ui.v3w_registry_hive.setEnabled(True)
        self.ui.v3w_registry_key.setEnabled(True)
        self.ui.v3w_recurse.setEnabled(True)
        self.ui.v3w_printkey.setEnabled(True)


def vol3功能列表(self,按钮号):  # 功能列表
    if 按钮号 == 1:
        self.指令 = v3_win_fun_list[self.ui.v3w_fun_list.currentItem().text()]
    elif 按钮号 == 2:
        self.指令 = v3_linux_fun_list[self.ui.v3l_fun_list.currentItem().text()]
    elif 按钮号 == 3:
        self.指令 = v3_mac_fun_list[self.ui.v3m_fun_list.currentItem().text()]
    else:
        self.text_输出("请选择功能列表")
        return
    命令 = self.指令
    vol3_参数选项列表(self)
    vol3命令生成(self, 命令)