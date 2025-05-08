import json
import os
import subprocess

from PySide6.QtWidgets import QInputDialog

from main import tabecho

"--------------------------全局设置------------------------------"
config_file = "config.json"
vol3_path = ""
vol2_path = ""


# 全局设置
表格数据 = ""
命令字典 = {
    "cmd历史记录": "windows.cmdline",
    "dll动态库列表": "windows.dlllist",
    "进程树": "windows.pstree",
    "进程扫描": "windows.psscan",
    "获取IDS": "windows.getsids",
    "句柄信息": "windows.handles",
    "隐藏进程识别": "windows.psxview",
    "环境变量信息": "windows.envars",
    "恶意yara检测": "yarascan.YaraScan --yara-file fm.yara",
    "TrueCrypt检测": "windows.truecrypt.Passphrase",
    "恶意malfind检测": "windows.malfind",
    "恶意Skeleton检测": "windows.skeleton_key_check",
    "sessions会话记录": "windows.sessions",
    "获取服务ids": "windows.getservicesids",
    "MFT扫描": "windows.mftscan.MFTScan",
    "服务运行状态": "windows.svcscan",
    "驱动树查看": "windows.devicetree",
    "隐藏驱动扫描": "windows.driverscan",
    "回调检测": "windows.callbacks",
    "PE文件信息": "windows.verinfo",
    "内存映射": "windows.memmap",
    "线程信息": "windows.threads",
    "线程扫描": "windows.thrdscan",
    "缓冲池": "windows.bigpools",
    "转储缓存文件": "windows.dumpfiles",
    "进程权限信息": "windows.privileges",
    "内核模块": "windows.modules",
    "进程内存范围": "windows.vadinfo",
    "重定向检测": "windows.symlinkscan",
    "ssdt系统调用表": "windows.ssdt",
    "注册表配置信息": "windows.registry.hivelist",
    "cer证书扫描": "windows.registry.certificates",
    "注册表项和信息": "windows.registry.userassist",
    "获取注册表key": "windows.registry.printkey",
    "扫描注册表": "windows.registry.getcellroutine",
    "测试": "memprocfs",
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
physical列表 = ["windows.pstree", "windows.psscan", "windows.psxview"]
文件名搜索列表 = ["windows.registry.hivelist", "windows.dumpfiles"]


def 加载配置(self):  # 加载vol配置文件
    global vol3_path, vol2_path
    try:
        if os.path.exists(config_file):
            with open(config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
                vol3_path = config["vol3_path"]
                vol2_path = config["vol2_path"]
                return json.load(f)
        return {}
    except Exception as e:
        self.输出(f"加载配置文件出错: {e} ,请设置vol的路径")
        return {}  # 当读取失败时也返回空字典


def 设置vol(self):  # 设置vol路径
    global vol3_path, vol2_path
    config = {}

    vol3_file, ok = QInputDialog.getText(self, "设置Vol3路径,需要指定vol.py", "默认路径为:", text=vol3_path)
    if ok and vol3_file:  # 如果用户输入了内容:
        config["vol3_path"] = vol3_file
    vol2_file, ok = QInputDialog.getText(self, "设置Vol2路径,需要指定vol.py", "默认路径为:", text=vol2_path)
    if ok and vol2_file:
        config["vol2_path"] = vol2_file

    # 检查路径是否存在
    if not os.path.isfile(vol3_path) or not os.path.isfile(vol2_path):
        self.输出("Vol3或Vol2路径下的vol.py文件不存在，请重新输入,指定路径为到vol.py \n 如果只使用一种vol，可以将vol2和vol3设置到同一目录")
        return

    # 保存配置
    try:
        with open(config_file, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        self.输出("配置已保存")
    except Exception as e:
        self.输出(f"保存配置出错: {str(e)}")


def vol手动执行(self):
    命令 = self.ui.vol_input.text()
    if 命令:
        # 命令代码 = f"python {self.vol3_path} -o {self.file_path} -f {self.file_name} {命令}"
        命令执行(self, 命令)
    else:
        self.输出("请输入要执行的命令")


"--------------------------vol3---------------------------------"


def 命令生成(self, 命令):  # 生成需要执行的命令
    if self.file_name:
        命令 = self.指令
        if self.ui.help.isChecked():
            命令 += " -h"
            self.命令执行(self, 命令)
            return
        if self.ui.win_pid.text():
            命令 += f" --pid {self.ui.win_pid.text()}"
            self.ui.win_pid.clear()
        if self.ui.win_offset.text():
            命令 += f" --offset {self.ui.win_offset.text()}"
            self.ui.win_offset.clear()
        if self.ui.win_physical.isChecked():
            命令 += " --physical"
        if self.ui.win_filter.text():
            命令 += f" --filter {self.ui.win_filter.text()}"
            self.ui.win_filter.clear()
        if self.ui.win_registry_key_recurse.isChecked():
            命令 += " --recurse"
        if self.ui.win_dump.isChecked():
            命令 += " --dump "
        命令执行(self, 命令)
    else:
        self.输出("未选择需要解析的内存文件")


def 命令执行(self, 命令):  # 开始执行命令
    if self.file_name:
        self.指令 = 命令
        命令 = f"python {vol3_path} -o {self.file_path} -f {self.file_name} {命令}"
        try:
            输出 = subprocess.check_output(命令, shell=True)
            字符串 = 输出.decode("utf-8", errors="ignore")
            分段 = 字符串.splitlines()
            if not 分段:
                self.执行结果信号.emit("无数据，请检查命令是否正确")
                return
            数据行 = [line.split("\t") for line in 分段[1:] if line.strip()]
            table_echo = tabecho(self.file_path, self.指令)
            table_echo.表格输出(数据行)
            table_echo.show()  # 显示表格窗口

        except Exception as e:
            self.执行结果信号.emit(f"故障命令:{命令},失败代码, {str(e)}")
            return

    else:
        self.执行结果信号.emit("错误类型, 未选择需要解析的内存文件")


def vol3_win列表(self):  # 列表选择事件处理函数
    # 指令接受
    self.指令 = 命令字典[self.ui.fun_list.currentItem().text()]
    # 控件启用规则
    控件规则 = {
        "win_pid": pid开放列表,
        "win_offset": offset开放列表,
        "win_dump": 可导出列表,
        "win_physical": physical列表,
        "win_filter": 文件名搜索列表,
    }

    # 根据规则启用或禁用控件
    for 控件名, 规则列表 in 控件规则.items():
        getattr(self.ui, 控件名).setEnabled(self.指令 in 规则列表)

    # 特殊处理注册表相关控件
    if self.指令 == "windows.registry.printkey":
        self.ui.registry_key.setEnabled(True)
        self.ui.win_registry_key_recurse.setEnabled(True)
    else:
        self.ui.registry_key.setEnabled(False)
        self.ui.win_registry_key_recurse.setEnabled(False)
