import base64
import binascii
import itertools
import math
import os
import re
import string
import struct
import subprocess
import zipfile
import zlib
from urllib import parse

import base36
import base58
import base62
import base91
import base128
import py3base92
import pybase100
import pyexiv2
from PIL import Image, ImageSequence

文件头 = {
    "FFD8FFE0": "JPG",
    "89504E47": "PNG",
    "47494638": "GIF",
    "38425053": "PSD(Adobe Photoshop)",
    "00000100": "ICO",
    "504B0304": "ZIP",
    "52617221": "RAR",
    "49492A00": "TIFF",
    "7B5C7274": "rtf",
    "3C3F786D": "XML",
    "68746D6C": "HTML",
    "44656C69": "eml",
    "7FFE340A": "doc",
    "D0CF11E0": "xls.or.doc",
    "25504446": "PDF",
    "50407373": "TXT",
    "2142444E": "Outlook (pst)",
    "57415645": "WAV",
    "41564920": "AVI",
    "4D546864": "MIDI",
    "3026B275": "ASF(Windows Media)",
    "4D5A9000": "exe",
}
file_data = ""  # 识别到的文件内容
file_type = ""  # 识别到的文件类型
正则参数 = [
    "flag.*",
    "flag{.*}",
    "Zmxh",
    "[\u4e00-\u9fa5]+",
    "&#[0-9].+;",
    "[0-9a-fA-F]+66c6167[0-9a-fA-F]+",
]

"""----------------------------------文件操作-------------------------------"""


def 文件处理(self):
    文件扩展名 = os.path.splitext(self.file_name)[1]  # 获取文件扩展名
    if 文件扩展名 in [".png"]:  # png 文件处理
        识别文件(self)
        png高宽爆破(self)
        binwalk分离(self)


def 文件读取(self):
    if self.file_name == "":  # 读取输入框内容
        if self.ui.input_text.toPlainText() != "":
            file_data = self.ui.input_text.toPlainText()
            return file_data.encode("utf-8")
        else:
            self.输出("文件和输入都为空,你打算解个p吃?")
    elif self.file_name != "":  # 读取文件内容
        try:
            with open(self.file_name, "rb") as f:
                file_data = f.read()  # 读取文件数据 布尔类型
            return file_data
        except Exception as e:
            self.输出(f"未能读取文件,请检查输入目录{e}")
    else:
        self.输出("请输入内容，或拖拽文件到窗口")


def 识别文件(self):
    file_data = 文件读取(self)
    data_hard = binascii.hexlify(file_data)[0:8].decode()  # 转换为十六进制数据 并剪切前8位
    self.输出("文件头为：" + data_hard)

    if data_hard.upper() in 文件头.keys():
        file_type = 文件头[data_hard.upper()]
        self.输出("自动识别的文件类型为：" + str(file_type))
        return file_data, file_type
    else:
        self.输出("未识别的文件类型")
    try:
        decoded_data = file_data.decode("utf-8", errors="ignore")  # 更安全的解码方式
        if re.search(r"=$", decoded_data, re.I):
            self.输出("文件中包含 '=' 字符,可能是base64编码")

        zero_width_chars = re.findall(r"[\u200b\u200C\u200d\u200e\u202a\u202c\u202d\u2022\u2023\ufeff]", decoded_data)

        if zero_width_chars:
            unique_chars = list(dict.fromkeys(zero_width_chars))  # 去重
            self.输出(f"文件中包含 '{unique_chars}' 等字符,可能是零宽隐写")
            self.输出("请注意,解码时可能需要不勾选200b")
    except UnicodeDecodeError:
        self.输出("文件内容无法解码为文本")
    except Exception as e:
        self.输出(f"分析文件时发生错误: {str(e)}")


"""----------------------------------右键功能-------------------------------"""


def 右键base64解码(self):
    字符串 = self.ui.print_echo.textCursor().selectedText()
    if 字符串:
        try:
            self.输出(base64.b64decode(字符串).decode())
        except Exception:
            self.输出("base64解码错误,请检查编码格式")
    else:
        self.输出("没有选中任何内容。")


def 右键url解码(self):
    字符串 = self.ui.print_echo.textCursor().selectedText()
    if 字符串:
        try:
            self.输出(parse.unquote(字符串))
        except Exception:
            self.输出("url解码错误,请检查编码格式")
    else:
        self.输出("没有选中任何内容。")


def hex解码(self):
    file_data = self.ui.print_echo.textCursor().selectedText()
    if file_data.split(":"):
        file_data = "".join(file_data.split(":"))
    if file_data:
        try:
            if len(file_data) % 2 == 0:
                解码后字符串 = binascii.unhexlify(file_data).decode()
            else:
                解码后字符串 = binascii.unhexlify(file_data[:-1]).decode()
            self.输出(解码后字符串)
        except Exception:
            self.输出("hex解码错误,请检查编码格式")
    else:
        self.输出("没有选中任何内容。")


"""----------------------------------文件分析-------------------------------"""


def 字符串搜索(self):
    self.ui.print_echo.clear()
    输入正则 = self.ui.re_ipnut.text().split(",")
    if 输入正则 != ["可输入正则，默认为flag"]:
        正则参数.clear()
        for i in 输入正则:
            escaped_i = re.escape(i)
            正则参数.append(f"{escaped_i}.*")
            正则参数.append(f"{escaped_i}{{.*}}")
            正则参数.append(f"{base64.b64encode(escaped_i.encode())[:4].decode()}[a-zA-Z0-9=]+")
            正则参数.append(f"[0-9a-fA-F]+{binascii.hexlify(escaped_i.encode()).decode()}[0-9a-fA-F]+")
        for i in range(len(正则参数)):
            self.输出("已更换正则表达式为：" + 正则参数[i])

    try:
        file_data = 文件读取(self)
        for i in 正则参数:  # 列表中内容循环存进 i
            s = re.findall(i, file_data.decode(), re.I)
            for match in s:
                self.输出(f"匹配到: {match}")
        self.输出("正则匹配结束")
    except Exception as e:
        self.输出(f"正则搜索错误{str(e)}")

        return


def 二进制打开(self):
    self.ui.print_echo.clear()
    file_data = 文件读取(self)
    if file_data:
        self.输出(f"{file_data}")
    else:
        self.输出("请输入内容，或拖拽文件到窗口")


def binwalk分离(self):
    self.ui.print_echo.clear()
    self.输出("正在运行binwalk分离")
    try:
        try:
            输出 = subprocess.check_output(f"python -m binwalk -e {self.file_name} -C {self.file_path}")
            for i in 输出.decode().splitlines():
                self.输出(i)
            self.输出(f"binwalk分离运行完毕，请到{self.file_path}目录下查看分离结果")
        except ModuleNotFoundError as e:
            self.输出(f"binwalk错误: {e}")
    except Exception:
        self.输出("没装binwalk吧,或者没配置环境?")


def format文件分离(self):
    self.ui.print_echo.clear()
    self.输出("正在运行foremost分离")
    try:
        output_dir = os.path.join(self.file_path, "foremost分离结果")
        subprocess.check_output(f"./tools/foremost.exe -v -o {output_dir} -i {self.file_name} ")
    except Exception as e:
        self.输出(f"foremost错误: {e}")
    with open(self.file_path + "foremost分离结果/audit.txt", "r") as f:
        for i in f.readlines():
            i = i.strip()
            if i != "":
                self.输出(i.split("\n")[0])

    self.输出(f"分离成功，请到{self.file_path + 'foremost分离结果'}目录下查看分离结果")


def 字符串翻转(self):
    self.ui.print_echo.clear()
    file_data = 文件读取(self).decode()
    self.输出(file_data[::-1])


def 字频分析(self):
    self.ui.print_echo.clear()
    self.输出("正在运行字频分析")
    try:
        file_data = 文件读取(self)
        字频 = {}
        lines = file_data.decode().replace("\n", "").replace("\r", "")
        x = 0
        for line in lines:
            if 字频.get(line) is None:
                字频.update({line: 1})
            else:
                字频[line] += 1
            x += 1
        字频排序 = sorted(字频.items(), key=lambda d: d[1], reverse=True)
    except Exception:
        self.输出("字频分析错误")
    for i in 字频排序:
        self.输出("字频排序为:" + str(i))


def 词频分析(self):
    self.输出("正在运行词频分析")
    try:
        file_data = 文件读取(self).decode("utf-8", errors="ignore")
        # 使用正则表达式提取英文单词（过滤纯数字）
        words = re.findall(r"\b[a-zA-Z]{2,}\b", file_data.lower())
        词频 = {}

        for word in words:
            词频[word] = 词频.get(word, 0) + 1

        词频排序 = sorted(词频.items(), key=lambda d: d[1], reverse=True)

        # 只显示前50个高频词
        for i, (word, count) in enumerate(词频排序[:50]):
            self.输出(f"TOP{i + 1}: {word.ljust(15)} 出现次数: {count}")

    except Exception as e:
        self.输出(f"词频分析错误: {str(e)}")


def 可打印字符(self):
    file_data = 文件读取(self)
    try:
        chars = r"A-Za-z0-9/\-:.,_$%'()[\]<>!@#$%^&*{}|~`+=;\\/ \""  # 可打印字符集
        shortestReturnChar = 4
        regExp = "[%s]{%d,}" % (chars, shortestReturnChar)
        pattern = re.compile(regExp)
        字符 = []
        data = pattern.findall(file_data.decode("utf-8", "ignore"))
        for i in data:
            字符.append(i)
        if not 字符:
            self.输出("无可打印字符")
        else:
            self.输出("".join(字符))
    except Exception:
        self.输出("出现错误")


def 零宽字符隐写(self):
    self.输出("正在调用网页进行零宽字符隐写解密")
    os.startfile(os.path.relpath("./tools/unicode.html"))


"""----------------------------------编码解码-------------------------------"""


def hex_str_带偏移(self):
    try:
        file_data = self.ui.input_text.toPlainText()
        if file_data == "":
            file_data = 文件读取(self).decode("utf-8")
    except Exception:
        self.输出("文件读取失败")
    偏移值 = 10
    for x in range(偏移值):
        temp_result = ""
        i = 0
        while i < len(file_data):
            try:
                a = chr(int(file_data[i : i + 2], 16) + x)
                temp_result += a
                i += 2
            except ValueError:
                self.输出(f"偏移值{x}在发生错误。")
        if temp_result:
            self.输出(f"偏移值为正{x}的结果为：" + temp_result)
    for x in range(偏移值):
        temp_result = ""
        i = 0
        while i < len(file_data):
            try:
                a = chr(int(file_data[i : i + 2], 16) - x)
                temp_result += a
                i += 2
            except ValueError:
                self.输出(f"偏移值{x}在发生错误。")
        if temp_result:
            self.输出(f"偏移值为负{x}的结果为：" + temp_result)


def base解码(self):
    try:
        file_data = self.ui.input_text.toPlainText()
        if not file_data:
            file_data = 文件读取(self).decode("utf-8")
        if any(char in file_data for char in ["%20", "%23", "%27", "%3D"]):
            file_data = url解码(self, file_data)
    except Exception as e:
        self.输出(f"文件读取失败: {str(e)}")
        return

    命令 = [
        ["base16", lambda: base64.b16decode(file_data).decode()],
        ["base32", lambda: base64.b32decode(file_data).decode()],
        ["base36", lambda: base36.dumps(int(file_data))],
        ["base58", lambda: base58.b58decode(file_data).decode()],
        ["base62", lambda: base62.decodebytes(file_data).decode()],
        ["base64", lambda: base64.b64decode(file_data).decode()],
        ["base85", lambda: base64.a85decode(file_data).decode()],
        ["base91", lambda: base91.decode(file_data).decode()],
        ["base92", lambda: py3base92.b92decode(file_data).decode()],
        ["base100", lambda: pybase100.decode(file_data).decode()],
        [
            "base128",
            lambda: b"".join(base128.base128(chars=None, chunksize=7).decode(file_data).decode()),
        ],
    ]
    i = 1
    while True:
        for n in range(len(命令)):
            x, y = 命令[n]
            try:
                if y() != "":
                    data = y()
                    self.输出(f"第{i}次为{x}解码:{data}")
            except Exception:
                pass
        max_attempts = 10  # 最大尝试次数防止无限循环
        data = file_data  # 初始化data变量

        for i in range(1, max_attempts + 1):
            decoded = False
            for name, decoder in 命令:
                try:
                    result = decoder()
                    if result and result != data:  # 有新解码结果
                        self.输出(f"第{i}次为{name}解码:{result}")
                        data = result
                        decoded = True
                        break  # 找到一个可解码的就跳出循环
                except Exception:
                    continue

            if not decoded or data == file_data:
                self.输出("解码完成")
                break

            file_data = data


def 栅栏密码(self):
    try:
        file_data = self.ui.input_text.toPlainText()
        if file_data == "":
            file_data = 文件读取(self).decode("utf-8")
    except Exception:
        self.输出("文件读取失败")
    try:
        # 通过因数法解码栅栏密码
        factors = [fac for fac in range(2, len(file_data) + 1) if len(file_data) % fac == 0]  # 找到所有因数
        for fac in factors:
            flag = "".join(file_data[i::fac] for i in range(fac))  # 输出栅栏密码
            self.输出(f"{fac}栏：{flag}")

        # 通过w字形法解码栅栏密码
        for n in range(2, len(file_data)):  # 遍历所有可能的栏数
            array = [["."] * len(file_data) for i in range(n)]  # 生成初始矩阵
            row = 0
            upflag = False  # 判断是否向上移动
            for col in range(len(file_data)):  # 在矩阵上按w型画出string
                array[row][col] = file_data[col]
                if row == n - 1:
                    upflag = True
                if row == 0:
                    upflag = False
                if upflag:
                    row -= 1
                else:
                    row += 1
            sub = 0
            for row in range(n):  # 将w型字符按行的顺序依次替换为string
                for col in range(len(file_data)):
                    if array[row][col] != ".":
                        array[row][col] = file_data[sub]
                        sub += 1
            msg = []
            for col in range(len(file_data)):  # 以 列的顺序依次连接各字符
                for row in range(n):
                    if array[row][col] != ".":
                        msg.append(array[row][col])
            self.输出(f"Z字形{n}栏：{''.join(msg)}")
    except ValueError as e:
        self.输出(str(e))
    except Exception:
        self.输出("解码错误,请确认字符串是否正确")


def 爆破凯撒密码(self):
    try:
        file_data = self.ui.input_text.toPlainText()
        if file_data == "":
            file_data = 文件读取(self).decode("utf-8")
    except Exception:
        self.输出("文件读取失败")
    try:
        # 凯撒密码 同key解密
        message = file_data.upper()  # 去掉二进制标注并为转大写
        LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for key in range(len(LETTERS)):  # 最多就25个key，一个一个来
            translated = ""
            for symble in message:  # 对于每一个key 都要输出一组明文
                if symble in LETTERS:
                    num = LETTERS.find(symble)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symble
            self.输出(f"第{key}的结果为: {translated}")  # 输出结果  共计26个结果
        # 凯撒密码 异key解密

    except Exception:
        self.输出("解码错误,请确认字符串是否正确")


def 核心价值观解码(self):
    try:
        file_data = self.ui.input_text.toPlainText()
        if file_data == "":
            file_data = 文件读取(self).decode("utf-8")
    except Exception:
        self.输出("文件读取失败")
    try:
        VALUE = "富强民主文明和谐自由平等公正法治爱国敬业诚信友善"
        assert len(file_data) % 2 == 0  # 确认字符串长度
        ans = []  # 将字符串转换为数字
        for i in range(0, len(file_data), 2):
            ans.append(VALUE.index(file_data[i : i + 2]) >> 1)
        i = 0
        bns = ""
        while i < len(ans):
            if ans[i] < 10:
                bns += str(ans[i])
                i += 1
            elif ans[i] == 10:
                bns += hex(ans[i + 1] + 10)[2:]
                i += 2
            elif ans[i] == 11:
                bns += hex(ans[i + 1] + 6)[2:]
                i += 2
            else:
                self.输出("数据错误:" + ans)
        tmp = ""
        for i in range(len(bns)):
            if not i % 2:
                tmp += "%"
            tmp += bns[i]
        result = parse.unquote(tmp)  # 还原
        self.输出("解密结果为：" + result)
    except Exception:
        self.输出("输入错误")


def fuck解码(self, file_data):
    try:
        if not file_data:
            file_data = 文件读取(self).decode("utf-8")
    except Exception:
        self.输出("fuck解码文件读取错误,请检查文件是否为空")
    try:
        li = [0]
        index = 0
        kuo = []
        output = []
        结果 = []
        i = 0
        while i < len(file_data):
            if file_data[i] == "+" or file_data[i] == "-":
                li[index] = eval(str(li[index]) + file_data[i] + "1")
            elif file_data[i] == ">":
                index += 1
                if len(li) <= index:
                    li.append(0)
            elif file_data[i] == "<":
                index -= 1
            elif file_data[i] == ".":
                output.append(li[index])
            elif file_data[i] == ",":
                i += 1
                li[index] = ord(file_data[i])
            elif file_data[i] == "[":
                if li[index] == 0:
                    while file_data[i] != "]":
                        i += 1
                    i += 1
                else:
                    kuo.append(i)
            elif file_data[i] == "]":
                if li[index] != 0:
                    i = kuo.pop() - 1
                else:
                    i = kuo.pop() - 1
            else:
                raise Exception("发生异常")
            i += 1
        for i in output:
            结果.append(chr(i))
        self.输出("fuck解码成功 , 得到结果为:")
        self.输出("".join(结果))
    except Exception:
        self.输出("fuck解码错误,请确认字符串是否正确")


def ook解码(self):
    try:
        file_data = 文件读取(self).decode("utf-8")
    except Exception:
        self.输出("ook解码文件读取错误,请检查文件是否为空")
    try:
        ook_data = []
        words = re.findall("[.?!]", file_data)
        if not words:
            self.输出("ook解码失败,输入的字符串为空")
        else:
            for i in range(0, len(words), 2):
                pair = "".join(words[i : i + 2])
                if pair == ".?":
                    ook_data.append(">")
                elif pair == "?.":
                    ook_data.append("<")
                elif pair == "..":
                    ook_data.append("+")
                elif pair == "!!":
                    ook_data.append("-")
                elif pair == "!.":
                    ook_data.append(".")
                elif pair == ".!":
                    ook_data.append(",")
                elif pair == "!?":
                    ook_data.append("[")
                elif pair == "?!":
                    ook_data.append("]")
                else:
                    raise Exception("发生异常")
            self.输出("ook转码为fuck成功,开始使用fuck解码")
            try:
                fuck解码(self, ook_data)
            except Exception:
                self.输出("ook转码为fuck错误,请确认字符串是否正确")
    except Exception:
        self.输出("ook转码为fuck错误,请确认字符串是否正确")


def url解码(self, 数据):
    if 数据 == "":
        try:
            数据 = self.ui.input_text.toPlainText()
            if 数据 == "":
                数据 = 文件读取(self).decode("utf-8")
        except Exception:
            self.输出("文件读取失败")
    try:
        if "%20" or "%23" or "%27" or "%3D" in 数据:  # 判断是否需要url解码
            prev = None
            while prev != 数据:
                prev = 数据
                数据 = parse.unquote(数据)
        self.输出(数据)
        return 数据
    except Exception:
        self.输出("url解码错误")


def html解码(self):
    try:
        file_data = self.ui.input_text.toPlainText()
        if file_data == "":
            file_data = 文件读取(self).decode("utf-8")
    except Exception:
        self.输出("文件读取失败")
    if file_data:
        try:
            解码后字符串 = []
            字符 = re.findall("[0-9]+", file_data)
            for i in 字符:
                解码后字符串.append(chr(int(i)))
            self.输出("".join(解码后字符串))
        except Exception:
            self.ui.str_echo.append("hex解码错误,请检查编码格式")
    else:
        self.ui.str_echo.append("没有选中任何内容。")


"""----------------------------------图片分析-------------------------------"""


def 图片元数据(self):
    try:
        img = pyexiv2.Image(self.file_name, encoding="GBK")
        exif = img.read_exif()
        self.输出("[*] 图片元数据 - EXIF信息：")
        命令 = [
            ("高度", exif["Exif.Image.ImageWidth"]),
            ("宽度", exif["Exif.Image.ImageLength"]),
            ("拍摄时间", exif["Exif.Photo.DateTimeOriginal"]),
            ("写入时间", exif["Exif.Photo.DateTimeDigitized"]),
            ("秒时间", exif["Exif.Photo.SubSecTime"]),
            ("GPS时间", exif["Exif.GPSInfo.GPSDateStamp"]),
            ("拍摄设备制造商", exif["Exif.Image.Make"]),
            ("拍摄设备软件", exif["Exif.Image.Software"]),
            (
                "纬度N",
                ".".join(
                    exif["Exif.GPSInfo.GPSLatitude"].split("/1 ", 3).split("/")[0],
                ),
            ),
            (
                "经度E",
                ".".join(
                    exif["Exif.GPSInfo.GPSLongitude"].split("/1 ", 3).split("/")[0],
                ),
            ),
            ("海拔", exif["Exif.GPSInfo.GPSAltitude"]),
        ]
        for key, value in 命令:
            self.输出("{}:{}".format(key, value))
        iptc = img.read_iptc()
        self.输出("[*] 图片元数据 - IPTC信息：")
        for key, value in iptc.items():
            self.输出("{}:{}".format(key, value))
        xmp = img.read_xmp()
        self.输出("[*] 图片元数据 - XMP信息：")
        for key, value in xmp.items():
            self.输出("{}:{}".format(key, value))
        img.close()
    except Exception:
        self.输出("[*] 图片元数据 - 读取失败或文件没有元数据")


def bin_image(self):  # 二进制转图片
    try:
        data = 文件读取(self).decode()
        x = y = int(len(data) ** 0.5)  # 定义二维码的长短
        # print('\n')
        self.输出("图片大小为:{}*{}".format(x, y))
        rgb = []
        for i in range(0, len(data)):  # 为了保证有rgb颜色,所以只能拓展了
            if data[i] == "0":
                rgb.append(255)
                rgb.append(255)
                rgb.append(255)
            elif data[i] == "1":
                rgb.append(0)
                rgb.append(0)
                rgb.append(0)
    except Exception:
        self.输出("文件读取失败")
    制图(self, x, y, rgb)


def RGB转图片(self):
    filedata = 文件读取(self)
    rgb_list = re.findall(r"\d+", "".join(filedata.decode()))
    try:
        rgb = []
        col = 0
        for i in rgb_list:
            if i == "0" or i == "255":
                if i == "0":
                    rgb.append("000")
                else:
                    rgb.append(i)
            else:
                rgb.append(i)
                col = 1
    except Exception:
        self.输出("文件读取失败")
    try:
        if col == 1:
            num = int(len(rgb_list) / 3)
            factor = []
            while num > 1:
                for i in range(num - 1):
                    k = i + 2
                    if num % k == 0:
                        factor.append(k)
                        num = int(num / k)
            self.输出("图片大小为:{}*{}".format(factor[2], factor[1] * factor[0]))
            制图(self, factor[2], factor[1] * factor[0], rgb)
        else:
            x = y = int(len(rgb_list) ** 0.5)
            self.输出("图片大小为:{}*{}".format(x, y))
            rgb2 = []
            for i in rgb:
                rgb2.append(i)
                rgb2.append(i)
                rgb2.append(i)
            制图(self, x, y, rgb2)
    except Exception:
        self.输出("图片分析失败")


def 制图(self, x, y, rgb):
    self.输出("正在生成图片,请稍后...")
    try:
        im = Image.new("RGB", (x, y))  # 创建图片
        z = 0
        for i in range(0, x):
            for j in range(0, y):
                im.putpixel((i, j), (int(rgb[z]), int(rgb[z + 1]), int(rgb[z + 2])))  # rgb转化为像素
                z += 3
        im.save(self.file_path + "转换后图片.png")
        self.输出(f"图片生成成功,请查看{self.file_path}/转换后图片.png")
    except Exception:
        self.输出("图片生成失败")


def jpg高宽爆破(self):
    if file_type == "jpg" or "jpeg" or "JPG" or "JPEG":
        self.输出("正在探测图片宽高,请稍后...")
        文件读取(self)
        try:
            img = Image.open(self.file_name)
            宽度 = img.size[0]
            高度 = img.size[1]
            self.输出("已探测图片宽:{} 高:{}".format(宽度, 高度))
            with open(self.file_name, "rb") as f:
                content = f.read()
                data = binascii.hexlify(content).decode()
        except Exception:
            self.输出("图片打开失败")
        try:
            高度_data = data.replace(hex2str(宽度, 高度), hex2str(宽度, 高度 * 2))
            宽度_data = data.replace(hex2str(宽度, 高度), hex2str(宽度 * 2, 高度))
            self.输出("正在修改图片高度,请稍后...")
            制作图片(高度_data, self.file_path, "高度")
            self.输出("正在修改图片宽度,请稍后...")
            制作图片(宽度_data, self.file_path, "宽度")
            self.输出(f"修改完毕,请在{self.file_path}目录中查看")
        except Exception:
            self.输出("图片宽高修正失败")
    else:
        self.输出("你打开的不是jpg图片,请检查")


def hex2str(width, height):
    width_hex = format(width, "04x")  # 使用format函数将宽度转换为4位十六进制字符串
    height_hex = format(height, "04x")  # 使用format函数将高度转换为4位十六进制字符串
    return height_hex + width_hex  # 返回高度+宽度的组合字符串


def 制作图片(self, 图片, file_path, 类型):
    try:
        with open(file_path + "/{}放大后.jpg".format(类型), "wb") as f:
            pic = binascii.a2b_hex(图片.encode())
            f.write(pic)
    except Exception:
        self.输出("图片生成失败")


def png高宽爆破(self):
    file_data = 文件读取(self)
    try:
        crc32key = zlib.crc32(file_data[12:29])  # 计算crc
        original_crc32 = int(file_data[29:33].hex(), 16)  # 原始crc
        if crc32key == original_crc32:  # 计算crc对比原始crc
            self.输出("宽高没有问题!")
        else:
            self.输出("图片宽高被修改,正在解析")
            for i, j in itertools.product(range(1920), range(1080)):  # 理论上0x FF FF FF FF，但考虑到屏幕实际/cpu，0x 0F FF就差不多了，也就是4095宽度和高度
                data = file_data[12:16] + struct.pack(">i", i) + struct.pack(">i", j) + file_data[24:29]
                crc32 = zlib.crc32(data)
                self.进度信号.emit(i)
                if crc32 == original_crc32:  # 计算当图片大小为i:j时的CRC校验值，与图片中的CRC比较，当相同，则图片大小已经确定
                    self.输出(f"\nCRC32: {hex(original_crc32)}")
                    self.输出(f"正确宽度为: {i}, hex: {hex(i)}")
                    self.输出(f"正确高度为: {j}, hex: {hex(j)}")
                    # 修改宽高,并生成新的图片保存
                    self.输出(f"正在生成修改后的图片,保存在:{self.file_path}png修正生成图.png")
                    image_byte = file_data[:16] + i.to_bytes(4, "big") + j.to_bytes(4, "big") + file_data[24:]
                    try:
                        with open(self.file_path + "png修正生成图.png", "wb") as f:
                            f.write(image_byte)
                        self.输出("图片生成成功,请查看")
                        # self.输出(f"<p><img src={self.file_path}png修正生成图.png" + "/></p>")
                    except Exception:
                        self.输出("图片生成失败,请检查路径")

    except Exception:
        self.输出("图片宽高爆破失败,请检查图片格式")


def GIF帧分离(self):
    try:
        im = Image.open(self.file_name)
        iter = ImageSequence.Iterator(im)

        def mkdirlambda(x):
            if not os.path.exists(x):
                os.makedirs(x)
            return True

        mkdirlambda(self.file_path + "gif分离")
        index = 1
        for frame in iter:
            frame.save(f"{self.file_path}gif分离/frame{index}.png")
            index += 1
        self.输出("gif图片分离完毕,请打开原图位置查看GIF文件夹")
    except Exception:
        self.输出("gif图片分离失败")


def GIF合并(self):
    try:
        imagefiles = os.listdir(self.file_path)
        imagefiles.sort(key=lambda x: int(x[5:-4]))
        图片组 = []
        for i in imagefiles:
            图片组.append(Image.open(self.file_path + i))
        # 计算要合并的文件宽高
        单图高 = 图片组[0].height
        单图宽 = 图片组[0].width
        # 创建图片 宽为单图*图数量，高为单图高
        im = Image.new("RGBA", (单图宽 * len(imagefiles), 单图高))
        width = 0  # 图片宽度
        for 单图 in 图片组:
            im.paste(单图, (width, 0, 单图宽 + width, 单图高))
            width = width + 单图宽
        im.save(self.file_path + "gif合并.png")
        self.输出(f"gif图片合并成功,请打开原图位置查看 {self.file_path + 'gif合并.png'} 文件")
        im.show()
    except Exception:
        self.输出("gif图片合并失败")


def 图片逆序(self):
    f1 = open(self.file_name, "rb+")
    f2 = open(self.file_path + "flag.jpg", "wb+")
    f2.write(f1.read()[::-1])
    self.输出("图片逆序成功,请打开原图位置查看flag.jpg")
    f1.close()
    f2.close()


def 黑白图(self):
    imagefiles = os.listdir(self.file_path)
    imagefiles.sort(key=lambda x: int(x[5:-4]))
    二进制a = []
    二进制b = []
    for i in imagefiles:
        x = Image.open(self.file_path + i)
        if x.getcolors()[0][1][0] > 10:
            二进制a.append("1")
            二进制b.append("0")
        elif x.getcolors()[0][1][0] < 10:
            二进制a.append("0")
            二进制b.append("1")
    # 转字符串
    try:
        print(hex(eval(二进制a)[2:-1]).decode("hex"))
        print(hex(eval(二进制b)[2:-1]).decode("hex"))
    except Exception:
        self.输出("不能转换为字符串,尝试转换图片")
    try:
        x = y = int(len(二进制a) ** 0.5)
        rgb = []
        for i in range(0, len(二进制a)):  # 为了保证有rgb颜色,所以只能拓展了
            if 二进制a[i] == "0":
                rgb.append(255)
                rgb.append(255)
                rgb.append(255)
            elif 二进制a[i] == "1":
                rgb.append(0)
                rgb.append(0)
                rgb.append(0)
        制图(self, x, y, rgb)
    except Exception:
        self.输出("不能生成图片")


#! todo: 16进制转图片
def 进制转图片(self, ttl):
    图像坐标 = ""
    for ttl_str in ttl:
        图像坐标 += bin(int(ttl_str)[2:].zfill(8))  # 将16进制转成二进制,去除0b，并补全到8位
    MAX = int(math.sqrt(len(图像坐标)))  # 计算出图片最大边长
    img = Image.new("RGB", (MAX, MAX))  # 创建图片
    i = 0
    for y in range(0, MAX):
        for x in range(0, MAX):
            if 图像坐标[i] == "1":  # 判断像素点颜色 1为白色，0为黑色
                img.putpixel([x, y], (0, 0, 0))
            else:
                img.putpixel([x, y], (255, 255, 255))
            i = i + 1
    img.show()


def hide_str(self):
    self.ui.print_echo.clear()
    im = Image.open(self.file_name)
    width, height = im.size
    binary_data = ""
    im.close()

    for h in range(height):
        for w in range(width):
            pixel = im.getpixel((w, h))
            # 提取每个颜色通道的LSB
            for color in pixel[:3]:  # 只取RGB三个通道
                binary_data += str(color % 2)

    # 将二进制数据转换为字节
    flag_bytes = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i : i + 8]
        if len(byte) == 8:
            flag_bytes.append(int(byte, 2))

    # 将字节转换为字符串
    flag = bytes(flag_bytes).decode("utf-8", errors="ignore")
    flag = flag.split("\x00")[0]  # 去除可能的空字符

    self.输出(f"提取的flag内容为:\n{flag}")


"""----------------------------------压缩包处理-------------------------------"""


def 单压缩包内CRC爆破(self):
    CRC_str = ""
    try:
        f = zipfile.ZipFile(self.file_name, "r")  # 读取单个文件
        self.输出("开始执行CRC爆破")
        for i in range(0, len(f.filelist)):
            crc = f.filelist[i].CRC
            CRC_ASK_str = CRC_ASK(hex(crc))  # 获取CRC值
            self.输出(f"第{i + 1}个CRC的值为:{CRC_ASK_str}")
            CRC_str += CRC_ASK_str
        self.输出(f"最终结果为:{CRC_str}")
    except Exception as e:
        self.输出(f"CRC读取失败,原因:{e}")


def 多文件压缩包CRC爆破(self):
    CRC_str = ""
    try:
        self.输出("开始执行CRC爆破")
        files = os.listdir(self.file_path)  # 读取文件夹内所有文件                   # 计算文件个数
        self.设置进度.emit(len(files))
        files.sort(key=lambda x: int(re.findall("([0-9]+)", x)[0]))
        for i in range(0, len(files)):
            f = zipfile.ZipFile(self.file_path + files[i], "r")  # 读取单个文件
            zipinfo = f.getinfo(" ".join(list(f.NameToInfo.keys())))  # 获取文件信息
            CRC_ASK_str = CRC_ASK(hex(zipinfo.CRC))  # 获取CRC值
            self.输出(f"第{i + 1}个CRC的值为:{CRC_ASK_str}")
            CRC_str += CRC_ASK_str
            self.进度信号.emit(i + 1)
        self.输出(f"最终结果为:{CRC_str}")
    except Exception as e:
        self.输出("CRC爆破失败,原因:{}".format(e))


def CRC_ASK(self, crc):
    try:
        dic = string.ascii_letters + string.digits + "+/="  # 打印出字符表  string.ascii_letters + string.digits + '+/='
        for a in dic:
            for b in dic:
                for c in dic:
                    for d in dic:
                        s = a + b + c + d
                        s = str(s).encode()
                        if crc == hex(binascii.crc32(s)):
                            return s.decode("utf-8")
    except Exception as e:
        self.输出("CRC爆破失败,原因:{}".format(e))


def 伪加密(self):
    self.输出("尝试破解伪加密")
    try:
        data = 文件读取(self)
        data = bytearray(data)
        index = data.find(b"PK\x03\x04")  #  504B0304后的第3、4个byte改成0000
        if not index:
            i = index + 4
            data[i + 2 : i + 4] = b"\x00\x00"
        index1 = data.find(b"PK\x01\x02")  #  504B0102后的第5、6个byte改成0000
        if index1:
            i = index1 + 4
            data[i + 4 : i + 6] = b"\x00\x00"
        # 将修改后的十六进制文件 写入zip文件
        with open(f"{self.file_path}伪加密破解.zip", "wb") as f1:
            f1.write(data)
        self.输出(f"文件写入成功，请查看:{self.file_path}伪加密破解.zip")
    except Exception:
        self.输出("伪加密破解失败")


"""
def 盲水印(self,实时输出=None):
    原图 = config.str1
    加密图 = config.str2
    try:  # 检测是否输入了路径
        if not 原图:
            self.输出("请在变量1中输入原图路径,路径不能有中文")
        if not 加密图:
            self.输出("请在变量2中输入加密图路径,路径不能有中文")
    except Exception:
        pass
    try:
        保存路径 = os.path.split(原图)[0]
        os.system(
            "python ./tools/jiaoben/bwmforpy3.py decode {} {} {} --oldseed".format(
                原图, 加密图, 保存路径 + "/decode.png"
            )
        )
        self.输出("<p><img src=" + 保存路径 + "/decode.png" + "/></p>")
    except Exception:
        self.输出("图片路径错误,路径不能有中文")
    
"""


if __name__ == "__main__":
    pass
