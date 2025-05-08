import datetime
import json
import os
import plistlib

import fun_file


def pyc_反编译(self):
    fun_file.文件读取(self)
    if not self.file_name:
        self.ui.print_echo.append("文件读取失败,请检查是否输入需要反编译的文件")
    else:
        self.ui.print_echo.append("文件读取正常，正在准备反编译")
        try:
            os.system(f"uncompyle6 {self.file_name} > {self.file_path}/pyc_py.py")
            self.ui.print_echo.append(f"反编译完成，请查看{self.file_path}/pyc_py.py")
        except Exception:
            self.ui.print_echo.append("反编译失败")
    fun_file.清理目录(self)


def 时间戳转换(self):
    时间戳 = int(self.ui.input_echo.toPlainText())
    if not 时间戳:
        self.ui.print_echo.append("请输入时间戳")
        raise
    try:
        if len(str(时间戳)) == 10 or len(str(时间戳)) == 13:
            if len(str(时间戳)) == 13:
                时间戳 = 时间戳 // 1000
                if len(str(时间戳)) != 10:
                    print("时间戳格式错误")
            self.ui.print_echo.append(f"UTC时间: {datetime.datetime.fromtimestamp(时间戳, datetime.timezone.utc)}")
            self.ui.print_echo.append(f"北京时间: {datetime.datetime.fromtimestamp(时间戳, datetime.timezone(datetime.timedelta(hours=8)))}")
        elif len(str(时间戳)) == 9:
            self.ui.print_echo.append(f"ios时间: {datetime.datetime.fromtimestamp(时间戳 + 978307200, datetime.timezone.utc)}")
    except Exception as e:
        self.ui.print_echo.append(f"时间戳格式错误:{e}")


def plist解析(self):
    try:
        with open(self.file_name, "rb") as f:
            plist_data = plistlib.load(f)

        def convert(obj):
            if isinstance(obj, bytes):
                return obj.hex()  # 二进制转十六进制字符串
            elif isinstance(obj, (datetime.datetime, plistlib.Uid)):
                return str(obj)  # 特殊类型转字符串
            raise TypeError

        json_output = json.dumps(plist_data, indent=2, ensure_ascii=False, default=convert)

        # 保存 JSON 文件
        save_path = os.path.join(self.file_path, "plist_json.json")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(json_output)
        self.ui.print_echo.append(f"JSON已保存至: {save_path}")

        if "Manifest.plist" in self.file_name:
            self.ui.print_echo.append("Plist重要数据提取：")
            self.ui.print_echo.append(f"BundleShortVersionString: {plist_data.get('BundleShortVersionString')}")

    except Exception as e:
        self.ui.print_echo.append(f"Plist解析失败: {str(e)}")


def facefusion解析(self):
    self.ui.print_echo.clear()
    # 查找.jobs/completed目录下的最新文件
    jobs_dir = os.path.join(self.file_path, ".jobs", "completed")
    if os.path.exists(jobs_dir):
        self.ui.print_echo.append("发现.jobs/completed文件夹,准备解析\n")
        file_list = []
        for filename in os.listdir(jobs_dir):
            file_list.append(os.path.join(jobs_dir, filename))
        self.ui.print_echo.append(f"共发现{len(file_list)}个文件\n")
        份数 = 1
        for file_name in file_list:
            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.ui.print_echo.append(f"正在输出第{份数}/{len(file_list)}文件:")
                    self.ui.print_echo.append(f"创建时间: {data.get('date_created')} ")
                    self.ui.print_echo.append(f"结束时间: {data.get('date_updated')} ")

                    self.ui.print_echo.append(f"原图目录: {data.get('steps')[0].get('args').get('source_paths')} ")
                    self.ui.print_echo.append(f"换脸目录: {data.get('steps')[0].get('args').get('target_path')} ")
                    self.ui.print_echo.append(f"输出目录: {data.get('steps')[0].get('args').get('output_path')} ")

                    self.ui.print_echo.append(f"人脸检测模型: {data.get('steps')[0].get('args').get('face_detector_model')}.onnx ")
                    self.ui.print_echo.append(f"输出图片大小: {data.get('steps')[0].get('args').get('output_image_resolution')} ")
                    self.ui.print_echo.append(f"年龄模型: {data.get('steps')[0].get('args').get('age_modifier_model')}.onnx ")
                    self.ui.print_echo.append(f"面部编辑模型: {data.get('steps')[0].get('args').get('face_editor_model')}.onnx ")
                    self.ui.print_echo.append(f"面部增强模型: {data.get('steps')[0].get('args').get('face_enhancer_model')}.onnx ")
                    self.ui.print_echo.append(f"换脸模型: {data.get('steps')[0].get('args').get('face_swapper_model')}.onnx ")
                    self.ui.print_echo.append(f"框架上色模型: {data.get('steps')[0].get('args').get('frame_colorizer_model')}.onnx ")
                    self.ui.print_echo.append(f"唇部同动模型: {data.get('steps')[0].get('args').get('lip_syncer_model')}.onnx\n")
                    份数 += 1

            except Exception as e:
                self.ui.print_echo.append(f"文件解析失败: {str(e)}")
                continue

    else:
        self.ui.print_echo.append("未发现.jobs/completed文件夹,请检查")


# 未使用
"""
import hashlib
def bt_密码生成(self):
    passwd = config.str1
    salt = config.str2
    if not passwd or not salt:
        self.ui.print_echo.append("请在变量1中设置密码,变量2中设置盐值")
    else:
        self.ui.print_echo.append("已设置密码为:{},盐值为:{}".format(passwd, salt))
        p1 = passwd + "_bt.cn"
        p2 = hashlib.md5(p1.encode(encoding="UTF-8")).hexdigest() + salt
        btpass = hashlib.md5(p2.encode(encoding="UTF-8")).hexdigest()
        self.ui.print_echo.append("bt加盐密码为:{}".format(btpass))
    file_fun.清理目录(self)
"""
