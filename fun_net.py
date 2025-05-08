import base64
import binascii
import re
from urllib import parse
import chardet
import pyshark
from FlowAnalyzer import FlowAnalyzer
from PIL import Image
from tools import Behinder
from tools import 蚁剑
import json


def 读取流量数据(self, 过滤器=None):
    if not self.file_name:
        self.输出("请先选择流量包")
        return
    try:
        if 过滤器:
            流量数据 = pyshark.FileCapture(self.file_name, display_filter=过滤器)
        else:
            流量数据 = pyshark.FileCapture(self.file_name)
        return 流量数据
    except Exception as e:
        self.输出(f"读取流量数据出错: {str(e)}")
        return None


def 字符串搜索(self):
    self.ui.print_echo.clear()  # 清空输出框
    字符串 = self.ui.re_input_2.text()
    if 字符串 != "可输入正则，默认为flag":
        正则 = [
            字符串,
            字符串 + "{.*}",
            base64.b64encode(字符串.encode()).decode()[0:4] + "[a-zA-Z0-9=]+",
            "[0-9a-fA-F]+" + binascii.hexlify(字符串.encode()).decode()[1:] + "[0-9a-fA-F]+",
            "&#[0-9].+;",
        ]
    else:
        正则 = ["flag-.*", "flag{.*}", "Zmxh", "&#[0-9].+;", "[0-9a-fA-F]+66c6167[0-9a-fA-F]+"]
    self.输出(f"正则表达式已设置为 : {'、'.join(正则)}")
    try:
        流量数据 = 读取流量数据(self)
        if 流量数据 is None:
            self.输出("未读取到流量数据,请检查")
            return
        可打印字符 = set()
        for 流量帧 in 流量数据:
            帧内容 = str(流量帧)
            for pattern in 正则:
                matches = re.findall(pattern, 帧内容, re.IGNORECASE)
                可打印字符.update(matches)
                if hasattr(流量帧, "DATA") and hasattr(流量帧.DATA, "data"):
                    decoded = binascii.unhexlify(流量帧.DATA.data).decode("utf-8", "ignore")
                    matches = re.findall(pattern, decoded, re.IGNORECASE)
                    可打印字符.update(matches)
        if 可打印字符:
            self.输出("流量中存在以下可打印字符:")
            for i in 可打印字符:
                self.输出(i)
        else:
            self.输出("未找到可打印的字符")
    except Exception as e:
        self.输出(f"处理流量数据出错: {str(e)}")
    self.输出("搜索字符串完成")


def 提取日志(self):
    self.ui.print_echo.clear()  # 清空输出框
    流量数据 = 读取流量数据(self, 过滤器="http")  # 读取流量包
    if 流量数据 is None:
        self.输出("未读取到流量数据,请检查")
        return

    self.输出("开始提取日志")

    流量包 = []
    for 流量帧 in 流量数据:
        try:
            if 流量帧.http:  # 确保http属性存在
                流量包.append(f"源IP:{流量帧.ip.src},目标IP:{流量帧.ip.dst},URL:{流量帧.http.request_full_uri}")
                # 流量包.append(f"{流量帧.http.request_full_uri}")
            else:
                流量包.append(流量帧)
        except Exception:
            pass
    with open(f"{self.file_path}/流量数据包.txt", "w+", encoding="utf-8") as f:
        for 数据帧 in 流量包:
            f.write(parse.unquote(数据帧) + "\n")
    self.输出(f"流量日志已保存至:{self.file_path}/流量数据包.txt")


def TTL分析(self):
    self.ui.print_echo.clear()  # 清空输出框
    try:
        流量数据 = 读取流量数据(self, 过滤器="icmp")  # 读取流量包
    except Exception:
        self.输出("流量数据提取错误")
    ttl = []
    for 流量帧 in 流量数据:
        ttl.append(int(流量帧.ip.ttl))
    self.输出(str(ttl))
    with open(self.file_path + "/ttl流量.txt", "w") as f:
        f.write(str(ttl))
    self.输出("执行完毕")


def len长度分析(self):  # len隐藏分析
    self.ui.print_echo.clear()  # 清空输出框
    流量数据 = 读取流量数据(self, 过滤器="icmp && icmp.type==8")  # 读取流量包
    con1 = ""
    con2 = ""
    for i in range(0, len(流量数据)):
        if 流量数据[i].icmp.data_len == "32":
            con1 += "0"
            con2 += "1"
        elif 流量数据[i].icmp.data_len == "64":
            con1 += "1"
            con2 += "0"
    self.输出(con1)
    self.输出(con2)
    self.输出("执行完毕")


def telnet分析(self):
    capture = 读取流量数据(self, 过滤器="telnet.data")
    空列表 = []
    for packet in capture:
        try:
            if packet.tcp.dstport == "23":  # 响应包
                请求内容 = bytes.fromhex("".join(packet.tcp.payload.split(":"))).decode("gbk")
                if "\r\n|\x08" not in 请求内容:
                    空列表.append(请求内容)
            else:  # 请求包
                响应内容 = bytes.fromhex("".join(packet.tcp.payload.split(":"))).decode("gbk")
                响应内容 = re.sub(r"\[[0-9]*;[0-9]*H|[\x00]|\r\n|\[K", "", 响应内容)
                响应内容 = re.sub(r"[\x1b]+", "\n", 响应内容)
                if len(响应内容) <= 3:
                    pass
                else:
                    self.输出("".join(空列表))
                    空列表 = []
                    self.输出(响应内容)
        except Exception:
            pass


def 文件提取(self, 流量):
    self.ui.print_echo.clear()  # 清空输出框
    if "504B0304" in 流量.hex():
        self.输出("发现压缩包,正在提取:")
        文件 = re.findall(r"504B0304.+", 流量.hex(), re.I)
        try:
            with open(self.file_path + "\提取的流量.zip", "wb+") as f:
                f.write(binascii.unhexlify(文件[0]))
            self.输出("压缩包提取完成,请查看" + self.file_path + '\提取的流量.zip"')
        except Exception:
            self.输出("压缩包提取失败")


def 蓝牙流量分析(self):
    self.ui.print_echo.clear()  # 清空输出框
    try:
        流量数据 = 读取流量数据(self, 过滤器="btcommon.eir_ad.entry.type == 0x09")
        self.输出("开始分析蓝牙流量")

        信息记录 = {}  # 存储设备信息的字典
        mac_dict = {}  # 以MAC地址为主键的字典

        for 流量帧 in 流量数据:
            try:
                # 从 frame 层提取接蓝牙接口信息
                if hasattr(流量帧.frame_info, "interface_name"):
                    接口信息 = 流量帧.frame_info.interface_name
                    信息记录["捕获接口"] = 接口信息
                    接口描述 = 流量帧.frame_info.interface_description
                    信息记录["接口描述"] = 接口描述

                if hasattr(流量帧.btle, "btcommon_eir_ad_entry_manufacturer_data"):
                    manufacturer_data = 流量帧.btle.btcommon_eir_ad_entry_manufacturer_data
                    company_id = manufacturer_data.split(":")[0]  # 获取公司ID
                    self.输出(f"制造商数据: {manufacturer_data}")
                    self.输出(f"公司ID: {company_id} (可查询蓝牙SIG获取制造商信息)")

                    # 将制造商信息存入记录
                    信息记录["制造商数据"] = manufacturer_data
                    信息记录["公司ID"] = company_id

                if hasattr(流量帧.btle, "btcommon_eir_ad_entry_device_name"):
                    device_name = 流量帧.btle.btcommon_eir_ad_entry_device_name
                    mac_address = 流量帧.btle.advertising_address.lower()  # 统一转为小写
                    timestamp = str(流量帧.sniff_time)

                    # 检查设备名是否包含非法字符
                    if device_name and not any(c in device_name for c in ["�", "\\x", "$", "~", "&", ":"]):
                        # 以MAC地址为主键
                        if mac_address not in mac_dict:
                            mac_dict[mac_address] = {"设备名变更": [device_name, timestamp], "最后设备名": device_name}
                        else:
                            # 如果设备名不同才记录变更
                            if device_name != mac_dict[mac_address]["最后设备名"]:
                                mac_dict[mac_address]["设备名变更"].extend([device_name, timestamp])
                                mac_dict[mac_address]["最后设备名"] = device_name

            except Exception as e:
                self.输出(f"解析错误: {str(e)}")
            finally:
                continue

        # 输出所有设备信息
        self.输出(f"\n捕获接口: {信息记录['捕获接口']}")
        self.输出(f"接口描述: {信息记录['接口描述']}")
        self.输出("\n设备信息汇总:")
        for mac, info in sorted(mac_dict.items(), key=lambda x: x[0]):
            initial_name = info["设备名变更"][0]
            timestamp = info["设备名变更"][1]
            self.输出(f"\nMAC地址: {mac} \n设备名: {initial_name}  首次发现时间: {timestamp}")

            # 如果有变更记录则输出
            if len(info["设备名变更"]) > 2:
                last_name = initial_name  # 记录上一个设备名
                for i in range(2, len(info["设备名变更"]), 2):
                    device_name = info["设备名变更"][i]
                    timestamp = info["设备名变更"][i + 1]
                    # 只有当设备名与上一个不同时才输出
                    if device_name != last_name:
                        self.输出(f"变更设备名: {device_name}  修改时间: {timestamp}")
                        last_name = device_name  # 更新上一个设备名

        # 输出分析结果
        if 信息记录:
            self.输出(f"\n记录已保存在:{self.file_path}/蓝牙流量分析结果.json")
            with open(f"{self.file_path}/蓝牙流量分析结果.json", "w+", encoding="utf-8") as f:
                f.write(json.dumps(信息记录, indent=2, ensure_ascii=False))
        else:
            self.输出("未找到蓝牙流量信息")

    except Exception as e:
        self.输出(f"蓝牙流量分析错误: {str(e)}")
    finally:
        self.输出("蓝牙流量分析完成")


class USB流量分析:  # 基本完成
    def 流量提取(self):
        self.输出("正在提取USB流量")
        try:
            # 尝试usbhid.data读取
            流量数据 = pyshark.FileCapture(self.file_name, display_filter="usbhid.data")
            if not any(hasattr(pkt, "DATA") for pkt in 流量数据):
                # 如果没有usbhid.data，尝试usb.capdata读取
                流量数据 = pyshark.FileCapture(self.file_name, display_filter="usb.capdata")
        except Exception as e:
            self.输出(f"读取流量包错误: {e}")
            return
        流量数据包 = []

        for 流量帧 in 流量数据:
            if hasattr(流量帧, "DATA") and hasattr(流量帧.DATA, "usbhid_data"):
                流量数据包.append("".join(流量帧.DATA.usbhid_data.split(":")))
            elif hasattr(流量帧, "DATA") and hasattr(流量帧.DATA, "usb.capdata"):
                流量数据包.append("".join(流量帧.DATA.usb_capdata.replace(":", "")))

        with open(f"{self.file_path}/USB流量数据包.txt", "w+", encoding="utf-8") as f:
            for 数据 in 流量数据包:
                f.write(数据 + "\n")
        self.输出(f"流量数据包已保存至:{self.file_path}流量数据包.txt")

        return 流量数据包

    def 鼠标流量分析(self):
        self.ui.print_echo.clear()  # 清空输出框
        if self.file_name:  # 判断文件名的后缀 为pcap 还是txt
            if self.file_name.lower().endswith((".pcap", ".pcapng", ".cap")):  # 如果是pcap文件，直接读取
                流量数据包 = USB流量分析.流量提取(self)
            elif self.file_name.lower().endswith(".txt"):
                with open(self.file_name, "r", encoding="utf-8") as f:  # 如果是txt文件，读取文件内容
                    流量数据包 = f.readlines()
            else:
                self.输出("请选择正确的文件格式")
                return
        self.输出("开始分析鼠标流量")

        左键轨迹 = []
        右键轨迹 = []
        pos_x, pos_y = 0, 0
        try:
            for 鼠标流量 in 流量数据包:
                鼠标流量 = 鼠标流量.strip()

                if not 鼠标流量 or len(鼠标流量) in (8, 16, 32):  # 确保数据有效
                    # 解析鼠标数据
                    btn_flag = int(鼠标流量[:2], 16)
                    x = int(鼠标流量[2:4], 16)
                    y = int(鼠标流量[4:6], 16)

                    # 处理有符号位移
                    x = x - 256 if x > 127 else x
                    y = y - 256 if y > 127 else y

                    pos_x += x
                    pos_y += y

                    # 根据按键类型记录轨迹
                    if btn_flag == 1:  # 左键
                        左键轨迹.append((pos_x, pos_y))
                    elif btn_flag == 2:  # 右键
                        右键轨迹.append((pos_x, pos_y))
                    # elif btn_flag == 0:  # 无按键移动
                    #    pass  # 可根据需要记录无按键移动轨迹
        except Exception as e:
            self.输出(f"解析鼠标数据错误: {e}")
        self.输出("轨迹分析完成")

        # 绘制左键轨迹
        if 左键轨迹:
            USB流量分析.绘图(self, 左键轨迹, "左键轨迹.png")

        # 绘制右键轨迹
        if 右键轨迹:
            USB流量分析.绘图(self, 右键轨迹, "右键轨迹.png")
        self.输出("轨迹图已保存,鼠标流量分析完成")

    def 绘图(self, points, filename):
        self.输出("开始绘图")
        try:
            if not points:
                self.输出("没有有效的坐标点")
                return
            # 找出轨迹点的最小和最大 x、y 坐标
            min_x = min([point[0] for point in points])
            max_x = max([point[0] for point in points])
            min_y = min([point[1] for point in points])
            max_y = max([point[1] for point in points])
            # 计算画布大小，添加一些边距
            margin = 50
            width = max_x - min_x + 2 * margin
            height = max_y - min_y + 2 * margin
            # 创建画布
            img = Image.new("RGB", (width, height), (255, 255, 255))
            from PIL import ImageDraw

            draw = ImageDraw.Draw(img)
            # 定义像素点大小
            pixel_size = 3
            # 绘制所有轨迹点
            for x, y in points:
                # 调整坐标以适应画布
                adjusted_x = x - min_x + margin
                adjusted_y = y - min_y + margin
                # 绘制矩形代替单个像素点
                draw.rectangle([(adjusted_x, adjusted_y), (adjusted_x + pixel_size, adjusted_y + pixel_size)], fill=(0, 0, 0))
            # 保存并显示图像
            self.输出(f"正在打开{filename}")
            img.show()
            img.save(f"{self.file_path}/{filename}")
            self.输出(f"已保存轨迹图: {self.file_path}/{filename}")

        except Exception as e:
            self.输出(f"绘制轨迹图错误: {e}")

    def 键盘流量分析(self):
        self.ui.print_echo.clear()  # 清空输出框
        if self.file_name:  # 判断文件名的后缀 为pcap 还是txt
            if self.file_name.lower().endswith((".pcap", ".pcapng", ".cap")):  # 如果是pcap文件，直接读取
                流量数据包 = USB流量分析.流量提取(self)
            elif self.file_name.lower().endswith(".txt"):
                with open(self.file_name, "r", encoding="utf-8") as f:  # 如果是txt文件，读取文件内容
                    流量数据包 = f.readlines()
            else:
                self.输出("不支持的文件格式")
                return

        按键记录 = {}

        for 键盘数据 in 流量数据包:
            键盘数据 = 键盘数据.strip()  # 去除可能存在的空格和换行符
            if not 键盘数据:  # 跳过空数据
                continue
            数据长度 = len(键盘数据)

            修饰键 = int(键盘数据[2:4], 16)
            if 修饰键 not in [0x00, 0x01, 0x02, 0x03]:  # 忽略无效的修饰键
                continue
            键值A = int(键盘数据[4:6], 16)
            键值B = int(键盘数据[6:8], 16)
            if 键值A == 0x00 and 键值B == 0x00:  # 忽略空键值
                continue
            if 数据长度 not in 按键记录:
                按键记录[数据长度] = {"A": [], "B": []}
            按键记录[数据长度]["A"].append(USB流量分析.键盘解析(修饰键, 键值A))
            按键记录[数据长度]["B"].append(USB流量分析.键盘解析(修饰键, 键值B))
        # 输出结果
        for 长度, 记录 in sorted(按键记录.items()):
            self.输出(f"\n长度为{长度}的按键顺序为:")
            self.输出(f"A记录: {''.join(记录['A'])}")
            self.输出(f"B记录: {''.join(记录['B'])}")
        self.输出("\n键盘流量分析完成")

    def 键盘解析(修饰键, 键值):
        键盘映射 = {
            0x04: "a",
            0x05: "b",
            0x06: "c",
            0x07: "d",
            0x08: "e",
            0x09: "f",
            0x0A: "g",
            0x0B: "h",
            0x0C: "i",
            0x0D: "j",
            0x0E: "k",
            0x0F: "l",
            0x10: "m",
            0x11: "n",
            0x12: "o",
            0x13: "p",
            0x14: "q",
            0x15: "r",
            0x16: "s",
            0x17: "t",
            0x18: "u",
            0x19: "v",
            0x1A: "w",
            0x1B: "x",
            0x1C: "y",
            0x1D: "z",
            0x1E: "1",
            0x1F: "2",
            0x20: "3",
            0x21: "4",
            0x22: "5",
            0x23: "6",
            0x24: "7",
            0x25: "8",
            0x26: "9",
            0x27: "0",
            0x28: "\n",
            0x29: "[ESC]",
            0x2A: "[DEL]",
            0x2B: "\t",
            0x2C: " ",
            0x2D: "-",
            0x2E: "=",
            0x2F: "[",
            0x30: "]",
            0x31: "\\",
            0x32: "#",
            0x33: ";",
            0x34: "`",
            0x36: ",",
            0x37: ".",
            0x38: "/",
            0x39: "[CAPS LOCK]",
            0x3A: "[F1]",
            0x3B: "[F2]",
            0x3C: "[F3]",
            0x3D: "[F4]",
            0x3E: "[F5]",
            0x3F: "[F6]",
            0x40: "[F7]",
            0x41: "[F8]",
            0x42: "[F9]",
            0x43: "[F10]",
            0x44: "[F11]",
            0x45: "[F12]",
            0x4C: "[Del]",
            0x4F: "[Right]",
            0x50: "[Left]",
            0x51: "[Down]",
            0x52: "[Up]",
            0x54: "/",
            0x55: "*",
            0x56: "-",
            0x57: "+",
            0x58: "\n",
            0x5C: "[WIN]",
            0x60: "[WIN]",
        }
        shift_map = {
            0x1E: "!",
            0x1F: "@",
            0x20: "#",
            0x21: "$",
            0x22: "%",
            0x23: "^",
            0x24: "&",
            0x25: "*",
            0x26: "(",
            0x27: ")",
            0x2D: "_",
            0x2E: "+",
            0x2F: "{",
            0x30: "}",
            0x31: "|",
            0x32: "~",
            0x33: ":",
            0x34: '"',
            0x35: "~",
            0x36: "<",
            0x37: ">",
            0x38: "?",
        }
        功能键 = [0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x4F, 0x50, 0x51, 0x52, 0x5C, 0x60]
        键盘记录 = ""
        try:
            if 修饰键 & 0x02:  # Shift键按下
                if 键值 in shift_map:
                    键盘记录 = shift_map[键值]
                else:
                    键盘记录 = 键盘映射[键值]

            else:  # 普通按键
                if 键值 in 键盘映射:
                    键盘记录 = 键盘映射[键值]
                    if 键值 != 0xFF and 键值 not in 功能键:
                        键盘记录 = 键盘映射[键值]
        except Exception:
            pass
        return 键盘记录


class 注入分析:
    def 注入分析(self):
        self.ui.print_echo.clear()
        self.输出("开始分析流量包")

        注入语句列表 = 注入分析.流量读取(self)
        注入分析.流量分析(self, 注入语句列表)

    def 流量读取(self):
        try:
            jsonpath = FlowAnalyzer.get_json_data(self.file_name, display_filter="http.request or http.response")
        except Exception:
            self.输出("流量数据读取错误，请检查文件输入")
        注入语句列表 = []
        for count, http in enumerate(FlowAnalyzer(jsonpath).generate_http_dict_pairs(), start=1):
            if http.request.full_uri:
                网址 = http.request.full_uri
                if re.findall(r"([0-9]+).?1\W\W=([0-9]+)", 网址, re.I):  # 判断是否为布尔注入
                    注入语句列表.append(网址)
                if re.findall(r"([0-9 .,]+)..>([0-9]+)", 网址, re.I):  # 判断是否为盲注
                    注入语句列表.append(网址)
        self.输出("注入语句解析完成")

        return 注入语句列表

    def 流量分析(self, 注入语句列表):
        表名_字典 = {}
        列名_字典 = {}
        flag_字典 = {}
        数据库 = []
        x = 1
        y = 1
        for 注入语句 in 注入语句列表:
            self.输出(注入语句)
            if "user" in 注入语句:
                用户名 = re.findall(r"user\s+([0-9a-z_]+)", 注入语句, re.I)[-1]
                self.输出(用户名)
            if "database" in 注入语句:
                数据库名 = re.findall(r"database\s+([0-9a-z_]+)", 注入语句, re.I)[-1]
                self.输出(数据库名)
            if re.findall(r"select\s+(.+)\s+from", 注入语句, re.I):
                表名_字典[re.findall(r"select\s+(.+)\s+from", 注入语句, re.I)[0]] = re.findall(r"select\s+(.+)\s+from", 注入语句, re.I)[0]
                列名_字典[re.findall(r"from\s+([0-9a-z_.]+)", 注入语句, re.I)[0]] = re.findall(r"from\s+([0-9a-z_.]+)", 注入语句, re.I)[0]
                try:  # 布尔注入
                    字符 = re.findall(r"([0-9]+..[0-9]+)\W\W=([0-9]+)", 注入语句)[-1]
                    if len(list(表名_字典)) != x:
                        聚合 = [
                            list(表名_字典.values())[-1],
                            list(列名_字典.values())[-1],
                            "".join(list(flag_字典.values())),
                        ]
                        数据库.append(聚合)
                        flag_字典 = {}
                        x += 1
                    if len(list(列名_字典)) != y:
                        聚合 = [
                            list(表名_字典.values())[-1],
                            list(列名_字典.values())[-1],
                            "".join(list(flag_字典.values())),
                        ]
                        数据库.append(聚合)
                        flag_字典 = {}
                        y += 1
                    flag_字典[字符[0]] = chr(int(字符[1]))
                except Exception:  # 盲注
                    try:
                        字符 = re.findall(r"([0-9 .,]+)..>([0-9]+)", 注入语句)[-1]
                        if len(list(表名_字典)) != x:
                            聚合 = [
                                list(表名_字典.values())[-1],
                                list(列名_字典.values())[-1],
                                "".join(list(flag_字典.values())),
                            ]
                            数据库.append(聚合)
                            flag_字典 = {}
                            x += 1
                        if len(list(列名_字典)) != y:
                            聚合 = [
                                list(表名_字典.values())[-1],
                                list(列名_字典.values())[-1],
                                "".join(list(flag_字典.values())),
                            ]
                            数据库.append(聚合)
                            flag_字典 = {}
                            y += 1
                        flag_字典[字符[0]] = chr(int(字符[-1]))
                    except Exception:
                        pass
        try:
            self.输出("流量分析结果:\n")
            数据库.append([list(表名_字典.values())[-1], list(列名_字典.values())[-1], "".join(list(flag_字典.values()))])
            for i in 数据库:
                self.输出(f"\n表名:{i[0]}\n列名:{i[1]}\n字段:{i[2]}")
        except Exception as e:
            self.输出(f"数据打印错误:{e}")
        self.输出("流量分析结束")
        self.输出("如果可能存在字符串错误，请在搜索字符串中输入注入成功的参数，例如 200 OK 或 其他可能判断正确的参数")


def shell数据读取(self):
    key = self.ui.input_key.text()
    pass_ = self.ui.input_pass.text()
    shell_manner = self.ui.shell_manner.currentText()
    return key, pass_, shell_manner


def 获取shell表(self):
    self.ui.shell_type.clear()
    if self.ui.shell_tab.currentText() == "菜刀":
        self.ui.shell_type.addItems(["PHP"])
    elif self.ui.shell_tab.currentText() == "蚁剑":
        self.ui.shell_type.addItems(["PHP", "JAVA", "ASP"])
    elif self.ui.shell_tab.currentText() == "哥斯拉":
        self.ui.shell_type.addItems(["PHP", "ASP", "CSHAP", "JAVA"])
    elif self.ui.shell_tab.currentText() == "冰蝎3":
        self.ui.shell_type.addItems(["PHP", "JAVA", "ASP", "ASPX"])
    elif self.ui.shell_tab.currentText() == "冰蝎4":
        self.ui.shell_type.addItems(["PHP", "JAVA", "ASP"])


def 获取shell类型(self):
    shell工具 = self.ui.shell_tab.currentText()
    self.ui.shell_manner.clear()
    if shell工具 == "菜刀":
        self.ui.shell_manner.clear()
        if self.ui.shell_type.currentText() == "PHP":
            self.ui.shell_manner.addItems(["PHP"])
    elif shell工具 == "蚁剑":  # 蚁剑没做
        if self.ui.shell_type.currentText() == "PHP":
            self.ui.shell_manner.addItems(["PHP"])
        elif self.ui.shell_type.currentText() == "JAVA":
            self.ui.shell_manner.addItems(["JAVA"])
        elif self.ui.shell_type.currentText() == "ASP":
            self.ui.shell_manner.addItems(["ASP"])
    elif shell工具 == "哥斯拉":
        if self.ui.shell_type.currentText() == "PHP":
            self.ui.shell_manner.addItems(["PHP_XOR_BASE64", "PHP_XOR_RAW", "PHP_EVAL_XOR_BASE64"])
        elif self.ui.shell_type.currentText() == "JAVA":
            self.ui.shell_manner.addItems(["JAVA_AES_BASE64", "JAVA_AES_RAW"])
        elif self.ui.shell_type.currentText() == "ASP":
            self.ui.shell_manner.addItems(["ASP_BASE64", "ASP_EVAL_BASE64", "ASP_RAW", "ASP_XOR_BASE64", "ASP_XOR_RAW"])
        elif self.ui.shell_type.currentText() == "CSHAP":
            self.ui.shell_manner.addItems(["CSHAP_AES_BASE64", "CSHAP_EVAL_AES_BASE64", "CSHAP_ASMX_AES_BASE64", "CSHAP_AES_RAW"])
        self.ui.find_key.setEnabled(True)  # 启用按钮
    elif shell工具 == "冰蝎3":
        if self.ui.shell_type.currentText() == "PHP":
            self.ui.shell_manner.addItems(["PHP"])
        elif self.ui.shell_type.currentText() == "JAVA":
            self.ui.shell_manner.addItems(["JAVA"])
        elif self.ui.shell_type.currentText() == "ASP":
            self.ui.shell_manner.addItems(["ASP"])
        elif self.ui.shell_type.currentText() == "ASPX":
            self.ui.shell_manner.addItems(["CSHARP"])
        self.ui.find_key.setEnabled(True)  # 启用按钮
    elif shell工具 == "冰蝎4":
        if self.ui.shell_type.currentText() == "PHP":
            self.ui.shell_manner.addItems(["PHP"])
    self.ui.input_key.setEnabled(True)  # 启用输入框
    self.ui.input_pass.setEnabled(True)  # 启用输入框
    self.ui.input_srt.setEnabled(True)  # 启用输入框
    self.ui.sd_but.setEnabled(True)  # 启用按钮
    self.ui.auto_but.setEnabled(True)  # 启用按钮
    self.ui.req_box.setEnabled(True)  # 启用按钮
    self.ui.res_box.setEnabled(True)  # 启用按钮


def 搜索KEY(self):
    self.ui.print_echo.clear()
    if self.ui.shell_tab.currentText() == "哥斯拉":
        哥斯拉流量分析.搜索key(self)
    elif self.ui.shell_tab.currentText() == "冰蝎3":
        冰蝎3流量分析.搜索key(self)
    elif self.ui.shell_tab.currentText() == "冰蝎4":
        冰蝎4流量分析.搜索key(self)


def 单条shell解析(self):
    self.ui.print_echo.clear()
    if self.ui.shell_tab.currentText() == "菜刀":  # 完成
        字符串 = self.ui.input_srt.toPlainText()
        菜刀流量分析.单条解密(self, 字符串)
    elif self.ui.shell_tab.currentText() == "蚁剑":  # 完成
        self.ui.input_srt.toPlainText()
        蚁剑流量分析.单条解密(self, 字符串)
    elif self.ui.shell_tab.currentText() == "哥斯拉":  # 完成
        字符串 = self.ui.input_srt.toPlainText()
        哥斯拉流量分析.单条解密(self, 字符串)
    elif self.ui.shell_tab.currentText() == "冰蝎3":  # 完成
        字符串 = self.ui.input_srt.toPlainText()
        冰蝎3流量分析.单条解密(self, 字符串)
    elif self.ui.shell_tab.currentText() == "冰蝎4":  # deepseek写的
        字符串 = self.ui.input_srt.toPlainText()
        冰蝎4流量分析.单条解密(self, 字符串)


def 自动shell解析(self):
    self.ui.print_echo.clear()
    if self.ui.shell_tab.currentText() == "菜刀":  # 完成
        菜刀流量分析.批量解密(self)
    elif self.ui.shell_tab.currentText() == "蚁剑":  # 完成
        蚁剑流量分析.批量解密(self)
    elif self.ui.shell_tab.currentText() == "哥斯拉":  # 完成
        哥斯拉流量分析.批量解密(self)
    elif self.ui.shell_tab.currentText() == "冰蝎3":  # 完成
        冰蝎3流量分析.批量解密(self)
    elif self.ui.shell_tab.currentText() == "冰蝎4":  # deepseek写的
        冰蝎4流量分析.批量解密(self)


def 写文件(self, decoded_data):
    try:
        # 使用utf-8编码写入文件
        with open(f"{self.file_path}/shell自动分析.txt", "a", encoding="utf-8") as f:
            f.write(decoded_data + "\n")  # 添加换行符分隔记录
    except Exception as e:
        self.输出(f"写入文件失败: {str(e)}")


class 哥斯拉流量分析:  # 基本完成，搜索key待优化
    def 搜索key(self):
        self.ui.print_echo.clear()
        流量包 = 读取流量数据(self, 过滤器="http.response.code == 200")
        if 流量包 is None:
            self.输出("无法读取流量数据")
            return
        发现的keys = set()  # 3. 使用集合避免重复key
        for 流量帧 in 流量包:
            try:
                if ":" in 流量帧.http.file_data:  # 判断是不是16进制格式
                    需要解码的数据 = "".join(流量帧.http.file_data.split(":"))  # 去除冒号
                    需要解码的数据 = binascii.unhexlify(需要解码的数据).decode("utf-8", errors="ignore")  # hex 解码

                    try:
                        keys = re.findall(r'xc="([0-9a-f]{16})"', 需要解码的数据)  #  xc="3c6e0b8a9c15224a"
                        for key in keys:
                            if key not in 发现的keys:
                                发现的keys.add(key)
                                self.输出(f"发现有效key: {key}")
                    except (binascii.Error, UnicodeDecodeError) as e:
                        self.输出(f"数据处理错误: {str(e)}")
                        continue
            except Exception as e:
                self.输出(f"处理流量帧时出错: {str(e)}")
                continue
        if not 发现的keys:
            self.输出("未发现有效key")
        self.输出("搜索key完毕")

    def 单条解密(self, 字符串):
        key, pass_, shell_manner = shell数据读取(self)
        if pass_ == "":
            pass_ = "pass"
        if key == "":
            key = "3c6e0b8a9c15224a"
        命令 = f'{shell_manner}(pass_="{pass_}",key="{key}")'
        decrypter = eval(命令)  # 实例化PHP类
        特殊列表 = ["PHP_XOR_RAW", "JAVA_AES_RAW", "ASP_XOR_RAW", "CSHAP_AES_RAW"]
        i = 1
        if self.ui.req_box.isChecked():
            try:
                if any(element in shell_manner for element in 特殊列表):
                    data = decrypter.decrypt_req_payload(bytes(bytearray.fromhex(字符串.hex())))
                else:
                    data = decrypter.decrypt_req_payload(字符串.encode())
                self.输出(f"第{i}条请求结果为:\n{data.decode()}")
                i += 1
                return data.decode()
            except Exception:
                self.输出(f"{shell_manner}解密失败\n")
        elif self.ui.res_box.isChecked():
            try:
                if any(element in shell_manner for element in 特殊列表):
                    data = decrypter.decrypt_res_payload(bytes(bytearray.fromhex(字符串.hex())))
                else:
                    data = decrypter.decrypt_res_payload(字符串.encode())
                self.输出(f"第{i}条响应结果为:\n{data.decode()}")
                i += 1
                return data.decode()
            except Exception:
                self.输出(f"{shell_manner}解密失败\n")

    def 批量解密(self):
        self.ui.print_echo.clear()
        # jsonpath = FlowAnalyzer.get_json_data(self.file_name,display_filter='tcp and http.request or http.response.code == 200')
        jsonpath = FlowAnalyzer.get_json_data(self, 过滤器="http.request.method == POST or http.response.code == 200")
        for count, http in enumerate(FlowAnalyzer(jsonpath).generate_http_dict_pairs(), start=1):
            request, response = http.request, http.response
            try:
                if self.ui.rep_or_rsp.currentText() == "请求":
                    file_data = request.file_data
                elif self.ui.rep_or_rsp.currentText() == "响应":
                    file_data = response.file_data

                decoded_data = 哥斯拉流量分析.单条解密(self, file_data)
                写文件(self, decoded_data)
            except Exception:
                pass


class 冰蝎3流量分析:  # 基本完成，搜索key待优化
    def 搜索key(self):
        self.ui.print_echo.clear()
        数据包 = 读取流量数据(self, 过滤器="http.content_length")
        if 数据包 is None:
            self.输出("无法读取流量数据")
            return
        发现的keys = set()  # 3. 使用集合避免重复key
        for 数据帧 in 数据包:
            try:
                if ":" in 数据帧.file_data:  # 5. 优化hex数据处理逻辑
                    try:
                        hex_data = 数据帧.file_data.replace(":", "")
                        decoded_data = binascii.unhexlify(hex_data).decode("utf-8", errors="ignore")
                        # 冰蝎3的key通常是16位hex字符串
                        keys = re.findall(r"(?<![0-9a-fA-F])([0-9a-fA-F]{16})(?![0-9a-fA-F])", decoded_data)
                        for key in keys:
                            if key.lower() not in 发现的keys:  # 统一转为小写比较
                                发现的keys.add(key.lower())
                                self.输出(f"发现有效key: {key}")

                    except (binascii.Error, UnicodeDecodeError) as e:
                        self.输出(f"数据处理错误: {str(e)}")
                        continue
            except Exception as e:
                self.输出(f"处理流量帧时出错: {str(e)}")
                continue
        # 7. 优化结果输出
        if not 发现的keys:
            self.输出("未发现有效key")
        self.输出("key搜索完成")

    def 单条解密(self, 字符串):
        key, pass_, shell_manner = shell数据读取(self)
        if not key:  # 更简洁的判断空值方式
            key = "e45e329feb5d925b"  # 这里是默认密码 rebeyond key值为密码的md5值前16位
        try:
            # 使用字典映射代替多重if-else
            decrypters = {"PHP": Behinder.PHP, "ASP": Behinder.ASP, "ASPX": Behinder.CSHARP, "JAVA": Behinder.JAVA}

            if shell_manner not in decrypters:
                self.输出(f"不支持的shell类型: {shell_manner}")
                return

            decrypter = decrypters[shell_manner](key)

            # 统一处理请求/响应逻辑
            if self.ui.req_box.isChecked():
                data = decrypter.decrypt_req_payload(字符串.encode())
                prefix = "请求"
            elif self.ui.res_box.isChecked():
                data = decrypter.decrypt_res_payload(字符串.encode())
                prefix = "响应"
            else:
                self.输出("请选择请求或响应类型")
                return

            # 统一解码处理
            try:
                encoding = chardet.detect(data)["encoding"]
                decoded_data = data.decode(encoding)
                self.输出(f"{prefix}内容为:\n{decoded_data}")
                return decoded_data
            except Exception as e:
                self.输出(f"解码失败: {str(e)}")

        except Exception as e:
            self.输出(f"解密失败: {str(e)}")

    def 批量解密(self):
        self.ui.print_echo.clear()
        jsonpath = FlowAnalyzer.get_json_data(self, 过滤器="http.request or http.response")
        for count, http in enumerate(FlowAnalyzer(jsonpath).generate_http_dict_pairs(), start=1):
            if http.request:
                file_data = http.request.file_data.decode()
                try:
                    if "<" in file_data:
                        pass
                    elif "\n" in file_data:
                        pass
                    else:
                        self.输出(f"[+] 正在处理第{count}个HTTP流!")
                        decoded_data = 冰蝎3流量分析.单条解密(self, file_data)
                        写文件(self, decoded_data)

                except Exception:
                    pass
            if http.response:
                file_data = http.response.file_data.decode()
                try:
                    if "<" in file_data:
                        pass
                    elif "\n" in file_data:
                        pass
                    else:
                        self.输出(f"[+] 正在处理第{count}个HTTP流!")
                        decoded_data = 冰蝎3流量分析.单条解密(self, file_data)
                        写文件(self, decoded_data)

                except Exception:
                    pass
        self.输出("自动解密完成")


class 菜刀流量分析:  # 完成40%
    def 单条解密(self, 字符串):
        if not isinstance(字符串, str):  # 确保输入是字符串
            try:
                字符串 = str(字符串)
            except Exception:
                self.输出("输入数据格式错误")
                return

        try:
            # 1. 处理array_map类型的菜刀流量
            if 'array_map("ass"."ert",array' in 字符串:
                self.输出("发现菜刀流量(array_map类型):")
                字符串 = parse.unquote(字符串)

                # 使用更精确的正则匹配base64编码的命令
                主语句 = re.findall(r'array_map\("ass"."ert",array\("([A-Za-z0-9+/=]+)"\)\)', 字符串)
                if 主语句:
                    try:
                        主语句解码 = base64.b64decode(主语句[0]).decode("utf-8", errors="ignore")
                        self.输出(f"解析出的命令:\n{主语句解码}")
                        return 主语句解码
                    except Exception as e:
                        self.输出(f"base64解码失败: {str(e)}")

            # 2. 处理base64_decode类型的菜刀流量
            elif "base64_decode" in 字符串:
                self.输出("发现菜刀流量(base64_decode类型):")
                字符串 = parse.unquote(字符串)

                # 改进正则表达式，更准确匹配base64编码
                主语句 = re.findall(r'base64_decode\((["\']?)([a-zA-Z0-9+/=]+)\1\)', 字符串)
                if 主语句:
                    for _, encoded in 主语句:
                        try:
                            decoded = base64.b64decode(encoded).decode("utf-8", errors="ignore")
                            self.输出(f"解析出的命令:\n{decoded}")
                            return decoded
                        except Exception as e:
                            self.输出(f"base64解码失败: {str(e)}")

            # 3. 处理返回结果类型的菜刀流量
            elif "X@Y" in 字符串 and "->|" in 字符串:
                self.输出("发现菜刀返回结果:")
                返回值 = [line.strip() for line in 字符串.split("\n") if line.strip()]
                for i in 返回值:
                    self.输出(i)
                    return i

            else:
                self.输出("未识别出有效的菜刀流量特征")

        except Exception as e:
            self.输出(f"菜刀流量解析错误: {str(e)}")

    def 批量解密(self):
        try:
            jsonpath = FlowAnalyzer.get_json_data(self, 过滤器="http.request or http.response")
            if not jsonpath:
                self.输出("未获取到有效的流量数据")
                return

            for count, http in enumerate(FlowAnalyzer(jsonpath).generate_http_dict_pairs(), start=1):
                request, response = http.request, http.response
                self.输出(f"正在处理第{count}个HTTP流...")

                # 处理请求数据
                if request and hasattr(request, "file_data"):
                    try:
                        req_data = request.file_data.decode("utf-8", errors="ignore")
                        if req_data.strip():
                            decoded = 菜刀流量分析.单条解密(self, req_data)
                            if decoded:
                                写文件(self, decoded)
                    except Exception as e:
                        self.输出(f"请求数据处理失败: {str(e)}")

                # 处理响应数据
                if response and hasattr(response, "file_data"):
                    try:
                        res_data = response.file_data.decode("utf-8", errors="ignore")
                        if res_data.strip():
                            decoded = 菜刀流量分析.单条解密(self, res_data)
                            if decoded:
                                写文件(self, decoded)
                                文件提取(self, response.file_data)
                    except Exception as e:
                        self.输出(f"响应数据处理失败: {str(e)}")

        except Exception as e:
            self.输出(f"批量解密过程中发生错误: {str(e)}")
        finally:
            self.输出("批量解密完成")


class 蚁剑流量分析:  # 未完成
    def 单条分析(self):
        try:
            key, pass_, shell_manner = shell数据读取(self)
            字符串 = self.ui.input_srt.toPlainText()
            if shell_manner == "PHP":
                解码字符串 = parse.unquote(字符串)
                self.输出(f"请求命令:\n{解码字符串}")
                return 解码字符串

            elif shell_manner == "PHP_RSA":
                if self.ui.req_box.isChecked():
                    请求字符串 = self.ui.input_echo.toPlainText()
                    if 请求字符串 == "":
                        self.输出("请先输入请求")
                        return
                    if not key:
                        self.输出("请输入key")
                        return
                    请求命令 = 蚁剑.PHP.PHP_RSA_req(请求字符串, key)
                    self.输出(f"请求命令: \n{请求命令}")
                    return 请求命令
        except Exception as e:
            self.输出(f"单条分析出错: {str(e)}")

    def 批量分析(self):
        try:
            shell_maner = self.ui.shell_maner.currentText()
            jsonpath = FlowAnalyzer.get_json_data(self, 过滤器="http.request.method == POST or http.response.code == 200")
            if not jsonpath:
                self.输出("未获取到有效的流量数据")
                return
            for count, http in enumerate(FlowAnalyzer(jsonpath).generate_http_dict_pairs(), start=1):
                request, response = http.request, http.response
                self.输出(f"正在处理第{count}个HTTP流...")

                try:
                    if shell_maner == "PHP":
                        if request and hasattr(request, "file_data"):
                            decoded = 蚁剑流量分析.单条解密(self, request.file_data.decode("utf-8", errors="ignore"))
                            if decoded:
                                写文件(self, decoded)
                    elif shell_maner == "PHP_RSA":
                        if request and hasattr(request, "file_data"):
                            req_data = request.file_data.decode("utf-8", errors="ignore")
                            if req_data:
                                key = shell数据读取(self)[0]
                                if not key:
                                    self.输出("缺少RSA密钥")
                                    continue

                                请求命令 = 蚁剑.PHP.PHP_RSA_req(req_data, key)
                                self.输出(f"请求命令: \n{请求命令}")

                            if response and hasattr(response, "file_data"):
                                res_data = response.file_data.decode("utf-8", errors="ignore")
                                if res_data:
                                    key = self.ui.key_link.text().encode()
                                    if not key:
                                        self.输出("缺少解密密钥")
                                        continue

                                    响应内容 = 蚁剑.PHP.PHP_RSA_res(请求命令, res_data, key)
                                    self.输出(f"响应内容: \n{响应内容}")
                                    写文件(self, 响应内容)
                except Exception as e:
                    self.输出(f"处理第{count}个HTTP流出错: {str(e)}")
        except Exception as e:
            self.输出(f"批量分析出错: {str(e)}")
        finally:
            self.输出("批量分析完成")


class 冰蝎4流量分析:
    def 搜索key(self):
        self.ui.print_echo.clear()
        流量包 = 读取流量数据(self, 过滤器="http.content_length")
        if 流量包 is None:
            self.输出("无法读取流量数据")
            return
        发现的keys = set()
        for 数据帧 in 流量包:
            try:
                if hasattr(数据帧, "file_data"):
                    # file_data = 数据帧.file_data
                    # 冰蝎4的key通常在响应头或cookie中
                    if hasattr(数据帧.http, "response_for_uri"):
                        uri = 数据帧.http.response_for_uri
                        if ";" in uri:
                            possible_key = uri.split(";")[-1].strip()
                            if len(possible_key) == 16 and all(c in "0123456789abcdef" for c in possible_key):
                                发现的keys.add(possible_key)
                                self.输出(f"发现可能key: {possible_key}")
            except Exception as e:
                self.输出(f"处理流量帧时出错: {str(e)}")

        if not 发现的keys:
            self.输出("未发现有效key")

        self.输出("key搜索完成")

    def 单条解密(self, 字符串):
        key, pass_, shell_manner = shell数据读取(self)
        if not key:
            key = "e45e329feb5d925b"  # 冰蝎4默认key

        try:
            # 冰蝎4使用AES-128-CBC加密
            from Crypto.Cipher import AES
            from Crypto.Util.Padding import unpad
            import hashlib

            # 生成16字节的key
            key = hashlib.md5(key.encode()).hexdigest()[:16].encode()
            iv = b"\x00" * 16  # 冰蝎4使用全零IV

            cipher = AES.new(key, AES.MODE_CBC, iv)
            try:
                # 尝试base64解码
                encrypted = base64.b64decode(字符串)
                decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
                result = decrypted.decode("utf-8", errors="ignore")
                self.输出(f"解密结果:\n{result}")
                return result
            except Exception:
                # 尝试直接解密hex数据
                encrypted = binascii.unhexlify(字符串)
                decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
                result = decrypted.decode("utf-8", errors="ignore")
                self.输出(f"解密结果:\n{result}")
                return result

        except Exception as e:
            self.输出(f"解密失败: {str(e)}")
            return None

    def 批量解密(self):
        self.ui.print_echo.clear()
        jsonpath = FlowAnalyzer.get_json_data(self, 过滤器="http.request or http.response")
        if not jsonpath:
            self.输出("未获取到有效的流量数据")
            return

        for count, http in enumerate(FlowAnalyzer(jsonpath).generate_http_dict_pairs(), start=1):
            try:
                if http.request:
                    file_data = http.request.file_data.decode("utf-8", errors="ignore")
                    if file_data.strip():
                        self.输出(f"[+] 正在处理第{count}个请求流")
                        decoded = self.单条解密(file_data)
                        if decoded:
                            写文件(self, decoded)

                if http.response:
                    file_data = http.response.file_data.decode("utf-8", errors="ignore")
                    if file_data.strip():
                        self.输出(f"[+] 正在处理第{count}个响应流")
                        decoded = self.单条解密(file_data)
                        if decoded:
                            写文件(self, decoded)
            except Exception as e:
                self.输出(f"处理第{count}个HTTP流出错: {str(e)}")

        self.输出("批量解密完成")
