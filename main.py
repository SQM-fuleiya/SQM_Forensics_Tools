# -*- coding: utf-8 -*-
# !/usr/bin/python3
# SQM的misc工具
# 2025年5月1日 V1.1.1

import os

from PySide6.QtCore import Qt ,QProcess,Signal , QThread
from PySide6.QtGui import QAction, QDragEnterEvent, QDropEvent, QIcon ,QStandardItemModel, QStandardItem 
from PySide6.QtWidgets import QApplication, QMenu, QWidget
import threading  # 新增：导入线程模块

import fun_file
import fun_net
import fun_vol
import fun_others
import fun_data

from zhuye_ui import Ui_zhu_windows


class 多线程(QThread):  # 多线程类
    执行结果信号 = Signal(str) 
    结束信号 = Signal() 
    进度信号 = Signal(str)  
    def __init__(self, func, *args, **kwargs):  # 初始化函数，func为要执行的函数，*args和**kwargs为函数的参数
        super().__init__()  # 调用父类的初始化函数
 
        self.func = func  # 保存要执行的函数
        self.args = args  # 保存函数的参数
        self.kwargs = kwargs  # 保存函数的参数

    def run(self):
        try:
            result = self.func(*self.args, **self.kwargs)  # 执行传入的函数
            self.执行结果信号.emit(result)  # 发送结果信号
        except Exception as e:
            self.执行结果信号.emit(f"{self.func.__name__} 出错: {str(e)}")


class MainWindow(QWidget):
    输出信号 = Signal(str)  # 输出信号

    def __init__(self):
        super().__init__()  # 初始化父类
        self.ui = Ui_zhu_windows()  # 实例化UI类
        self.ui.setupUi(self)  # 设置UI
        self.setAcceptDrops(True)  # 设置 input_text 窗口可以接受拖拽放入文件
        self.ui.function_list.currentChanged.connect(self.tab标签事件)  # 设置tab标签切换事件
        """-----全局变量------"""
        self.file_name = ""  # 保存文件名称
        self.file_path = ""  # 保存文件路径
        self.指令 = ""  # 保存指令
        self.threads = []  # 用于存储所有线程对象的列表
        self.db_lock = threading.Lock()  # 数据库锁

        """-----设置信号------"""
        self.输出信号.connect(self.text_输出)  # 连接线程的进度信号到输出函数
        """-----按钮设置------"""
        self.file_but()  # 设置文件页面按钮功能
        self.net_but()  # 设置流量分析按钮功能
        self.vol3_but()  # 设置内存分析按钮功能
        self.msic_but()  # 杂项分析按钮功能
        self.data_but()  # 设置数据分析按钮功能
        """-----右键菜单设置------"""
        self.ui.text_echo.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        menu = QMenu(self)
        action1 = QAction("base64解码", self, triggered=lambda: fun_file.右键base64解码(self))
        action2 = QAction("URL解码", self, triggered=lambda: fun_file.右键url解码(self))
        action3 = QAction("hex解码", self, triggered=lambda: fun_file.hex解码(self))
        action4 = QAction("html解码", self, triggered=lambda: fun_file.html解码(self))
        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)
        menu.addAction(action4)
        self.ui.text_echo.addActions([action1, action2, action3, action4])

        self.ui.table_echo.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        tabmenu = QMenu(self)
        action11 = QAction("复制内容", self, triggered=lambda: fun_data.复制选中(self))
        action12 = QAction("保存为csv", self, triggered=lambda: fun_data.表格保存(self))
        # action13 = QAction("导出", self, triggered=lambda: self.导出(self))
        tabmenu.addAction(action11)
        tabmenu.addAction(action12)
        # tabmenu.addAction(action13)
        self.ui.table_echo.addActions([action11, action12])

    # 
    #  FnMap(待办)
    def start_thread(self, func, *args, **kwargs):  # 启动线程函数，func为要执行的函数，*args和**kwargs为函数的参数
        thread = 多线程(func, *args, **kwargs)  # 创建线程对象
        thread.setObjectName(func.__name__)  # 添加这行
        thread.执行结果信号.connect(self.text_输出)  # 连接线程的执行结果信号到输出函数
        thread.finished.connect(lambda: self.threads.remove(thread))  # 线程结束后从列表中移除
        thread.start()  # 启动线程
        self.threads.append(thread)  # 将线程对象添加到列表中

    def closeEvent(self, event):  # 关闭线程
        # 检查 QProcess 进程是否在运行，如果是则终止
        if hasattr(self, 'process'):
            try:
                if self.process.state() == QProcess.Running:
                    self.process.terminate()
                    if not self.process.waitForFinished(3000):  # 等待 3 秒
                        self.process.kill()
                        self.process.waitForFinished()  # 确保进程已结束
                # 销毁进程对象
                self.process.deleteLater()
                delattr(self, 'process')
            except Exception as e:
                print(f"关闭窗口时清理进程出错: {str(e)}")

        for thread in self.threads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        event.accept()

    def tab标签事件(self, index):
        def text_echo(self):
            self.ui.text_echo.setMaximumSize(16777215, 16777215)
            self.ui.table_echo.setMaximumSize(16777215, 0)
        def table_echo(self):
            self.ui.text_echo.setMaximumSize(16777215, 70)
            self.ui.table_echo.setMaximumSize(16777215, 16777215)

        # tab_text = self.ui.function_list.tabText(index)
        # self.text_输出(f"你点击了标签页: {tab_text}，索引为: {index}")
        if index == 0:  # 文件分析
            text_echo(self)
        if index == 1:  # 网络流量分析
            text_echo(self)
        if index == 2:  # 内存分析
            table_echo(self)
        if index == 3:  # 数据分析
            table_echo(self)
        if index == 4:  # 逆向分析
            text_echo(self)


    def text_输出(self, 字符串):
        if 字符串:
            self.ui.text_echo.append(字符串)
            QApplication.processEvents()

    def table_输出(self, data):
        if data:
            if not data or len(data) < 1:
                return
            model = QStandardItemModel()  # 创建模型并填充数据
            model.setHorizontalHeaderLabels(data[0])  # 设置表头
            for row_idx, row_data in enumerate(data[1:]):  # 填充数据
                for col_idx, cell_data in enumerate(row_data):
                    model.setItem(row_idx, col_idx, QStandardItem(str(cell_data)))

        self.ui.table_echo.setModel(model)  # 表格输出    
        self.ui.table_echo.resizeColumnsToContents()

    # 拖拽文件到窗口，并加载文件路径到输入框
    def dragEnterEvent(self, a0: QDragEnterEvent) -> None:  # 鼠标托放事件，并执行一些操作
        if a0.mimeData().hasUrls():  # 判断有没有接受到文件路径,有的话保存文件路径，没有的话忽略
            a0.accept()  # 接受文件内容 ，a0 里面保存有文件的路径
        else:
            a0.ignore()  # 忽略文件内容

    def dropEvent(self, a0: QDropEvent) -> None:  # 鼠标释放事件，并执行一些操作
        self.ui.input_text.clear()
        if a0.mimeData().hasUrls():  # 判断有没有接受到文件路径,有的话保存文件路径，没有的话忽略
            for 路径 in a0.mimeData().urls():  # 遍历文件路径
                local_path = 路径.toLocalFile()  # 获取文件路径
                if os.path.isdir(local_path):  # 判断是否为文件夹
                    self.file_path = local_path
                    self.ui.text_echo.append(f"已加载文件夹: {self.file_path}")

                else:  # 是文件
                    self.file_name = 路径.toLocalFile()
                    self.file_path = os.path.split(路径.toLocalFile())[0] + "/"
                    self.ui.input_file.setText(f"{self.file_name}")
                    self.ui.text_echo.append(f"已加载文件: {self.file_name}")

                    fun_file.文件处理(self)  # 识别文件头，并加载二进制文件数据
                    fun_data.按钮开关判断(self)

    def file_but(self):  # 文件页面按钮功能设置
        self.ui.shibie_but.clicked.connect(lambda: fun_file.识别文件(self))
        self.ui.clear_but.clicked.connect(lambda: self.ui.text_echo.clear())

        # 文件分析和编码
        self.ui.flag_search_but.clicked.connect(lambda: fun_file.字符串搜索(self))
        self.ui.shibie_but.clicked.connect(lambda: fun_file.二进制打开(self))
        self.ui.fenli_but.clicked.connect(lambda: fun_file.binwalk分离(self))
        self.ui.for_but.clicked.connect(lambda: fun_file.format文件分离(self))

        self.ui.zipin_but.clicked.connect(lambda: fun_file.字频分析(self))
        self.ui.cipin_but.clicked.connect(lambda: fun_file.词频分析(self))
        self.ui.print_str_but.clicked.connect(lambda: fun_file.可打印字符(self))
        self.ui.zero_str_but.clicked.connect(lambda: fun_file.零宽字符隐写(self))
        self.ui.str_down_but.clicked.connect(lambda: fun_file.字符串翻转(self))

        # 各种编码
        self.ui.hex_str_but.clicked.connect(lambda: fun_file.hex解码(self))
        self.ui.base_but.clicked.connect(lambda: fun_file.base解码(self))
        self.ui.zhalan_but.clicked.connect(lambda: fun_file.栅栏密码(self))
        self.ui.kaisa_but.clicked.connect(lambda: fun_file.爆破凯撒密码(self))
        self.ui.fuck_but.clicked.connect(lambda: fun_file.fuck解码(self, ""))
        self.ui.ook_but.clicked.connect(lambda: fun_file.ook解码(self))
        self.ui.hexin_but.clicked.connect(lambda: fun_file.核心价值观解码(self))
        self.ui.hex_str.clicked.connect(lambda: fun_file.hex_str_带偏移(self))
        self.ui.html_but.clicked.connect(lambda: fun_file.html解码(self))
        self.ui.url_but.clicked.connect(lambda: fun_file.url解码(self, ""))

        # 图像处理
        self.ui.png_high_but.clicked.connect(lambda: fun_file.png高宽爆破(self))
        self.ui.exif_but.clicked.connect(lambda: fun_file.图片元数据(self))
        self.ui.rgb2img_but.clicked.connect(lambda: fun_file.RGB转图片(self))
        self.ui.bin_image_but.clicked.connect(lambda: fun_file.bin_image(self))  # 二进制字符串转图片
        self.ui.jpg_high_but.clicked.connect(lambda: fun_file.jpg高宽爆破(self))
        self.ui.gif_fenli_but.clicked.connect(lambda: fun_file.GIF帧分离(self))
        self.ui.gif_hebing.clicked.connect(lambda: fun_file.GIF合并(self))
        self.ui.tu_re.clicked.connect(lambda: fun_file.图片逆序(self))
        self.ui.heibai_but.clicked.connect(lambda: fun_file.黑白图(self))
        self.ui.hide_str_but.clicked.connect(lambda: fun_file.hide_str(self))  # hide解码出字符串
        self.ui.jpg_block_but.clicked.connect(lambda: fun_file.JPG块分析(self))
        self.ui.png_idat_but.clicked.connect(lambda: fun_file.PNG_IDAT分析(self))
        # self.ui.mangshuiyin_but.clicked.connect(lambda:  file_fun.盲水印,self))
        # self.ui.f5_steg_but.clicked.connect(file_fun.F5隐写)
        # self.ui.Stegpy_but.clicked.connect(file_fun.Stegpy)

        # 压缩包
        self.ui.single_crc_but.clicked.connect(lambda: fun_file.单压缩包内CRC爆破(self))
        self.ui.more_crc_but.clicked.connect(lambda: fun_file.多文件压缩包CRC爆破(self))
        self.ui.zip_wei_but.clicked.connect(lambda: fun_file.伪加密(self))

        # TODO 日志文件分析

    def net_but(self):  # 流量分析按钮功能设置
        self.ui.flag_search_but_2.clicked.connect(lambda: fun_net.字符串搜索(self))
        self.ui.tiqu_but.clicked.connect(lambda: fun_net.提取日志(self))
        self.ui.ttl_but.clicked.connect(lambda: fun_net.TTL分析(self))
        self.ui.len_but.clicked.connect(lambda: fun_net.len长度分析(self))
        self.ui.telnet_but.clicked.connect(lambda: fun_net.telnet分析(self))

        self.ui.mouse_but.clicked.connect(lambda: fun_net.USB流量分析.鼠标流量分析(self))
        self.ui.keyboard_but.clicked.connect(lambda: fun_net.USB流量分析.键盘流量分析(self))
        self.ui.Bluetooth_but.clicked.connect(lambda: fun_net.蓝牙流量分析(self))

        self.ui.sql_but.clicked.connect(lambda: fun_net.注入分析.注入分析(self))

        self.ui.shell_tab.activated.connect(lambda: fun_net.获取shell表(self))
        self.ui.shell_type.activated.connect(lambda: fun_net.获取shell类型(self))
        self.ui.find_key.clicked.connect(lambda: fun_net.搜索KEY(self))
        self.ui.sd_but.clicked.connect(lambda: fun_net.单条shell解析(self))
        self.ui.auto_but.clicked.connect(lambda: fun_net.自动shell解析(self))

    def vol3_but(self):
        self.ui.set_vol.clicked.connect(lambda: fun_vol.设置vol(self))
        self.ui.vol3_but.clicked.connect(lambda: os.startfile(f"{os.getcwd()}/tools/vol3使用说明.txt"))
        self.ui.vol2_but.clicked.connect(lambda: os.startfile(f"{os.getcwd()}/tools/vol2使用说明.txt"))
        self.ui.vol3_start_but.clicked.connect(lambda: fun_vol.vol手动执行(self))

        '''----------vol3按钮设置----------'''
        self.ui.v3w_info.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.info"))
        self.ui.v3w_hashdump.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.hashdump"))
        self.ui.v3w_netstat.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.netstat"))
        self.ui.v3w_cmdscan.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.cmdscan"))

        self.ui.v3w_amcache.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.amcache"))
        self.ui.v3w_shimcache.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.shimcachemem"))
        self.ui.v3w_scheduled_tasks.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.scheduled_tasks"))
        self.ui.v3w_psxview.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.psxview"))

        self.ui.v3w_timeliner.clicked.connect(lambda: fun_vol.vol3命令生成(self, "timeliner"))
        self.ui.v3w_certificates.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.registry.certificates"))

        self.ui.v3w_file_but.clicked.connect(lambda: fun_vol.开启文件操作(self))
        self.ui.v3w_filescan.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.filescan"))
        self.ui.v3w_dumpfiles.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.strings"))
        self.ui.v3w_strings.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.strings"))

        self.ui.v3w_printkey.clicked.connect(lambda: fun_vol.vol3命令生成(self, "windows.printkey"))


    def data_but(self):  # 数据分析按钮功能设置

        self.ui.start_db_but.clicked.connect(lambda: fun_data.数据入库(self))
        self.ui.db_clear.clicked.connect(lambda: fun_data.删除数据库(self))
        self.ui.list_clear.clicked.connect(lambda: fun_data.表格清理(self))
        self.ui.read_db.clicked.connect(lambda: fun_data.数据显示(self))
        self.ui.revise_column_name.clicked.connect(lambda: fun_data.修改列名(self))

        self.ui.select_yufa.clicked.connect(lambda: fun_data.查询语法(self))
        self.ui.db_select_but.clicked.connect(lambda: fun_data.数据库查询(self))

        self.ui.txt_csv.clicked.connect(lambda: fun_data.txt转csv(self))

        self.ui.select_one_up.clicked.connect(lambda: fun_data.查询上下线(self))
        self.ui.show_guanxi.clicked.connect(lambda: fun_data.树状图(self))


    def msic_but(self):  # 流量分析按钮功能设置
        # IOS分析
        self.ui.plist_but.clicked.connect(lambda: fun_others.plist解析(self))

        # android分析
        self.ui.hook_but.clicked.connect(lambda: fun_others.hook执行(self))

        # python逆向
        self.ui.pyc_but.clicked.connect(lambda: fun_others.pyc_反编译(self))

        # 人工智能软件
        self.ui.facefusion_but.clicked.connect(lambda: fun_others.facefusion解析(self))

        # 其他工具
        self.ui.mod_but.clicked.connect(lambda: os.startfile(os.path.relpath("./mod")))

        self.ui.time_zhuan.clicked.connect(lambda: fun_others.时间戳转换(self))
        self.ui.ceshi111_but.clicked.connect(lambda: self.ui.text_echo.append("测试按钮"))

        # self.ui.ceshi111_but.clicked.connect(lambda: others.测试输出1(self))
        # self.ui.ceshi111_but.clicked.connect(lambda: others.测试输出2(self))
        # self.ui.BT_en_but.clicked.connect(lambda:  others.bt_密码生成,self))
        # self.ui.rsa_public.clicked.connect(lambda:  others.RSA公钥分解,self))



if __name__ == "__main__":
    app = QApplication()
    app.setWindowIcon(QIcon("logo.ico"))
    windows = MainWindow()
    windows.show()
    app.exec()
