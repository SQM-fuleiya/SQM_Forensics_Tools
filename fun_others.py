import datetime
import json
import os
import plistlib
import frida
import fun_file
import time
from PySide6.QtCore import QProcess

'-------------------------IOS功能---------------------------'

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
        self.text_输出(f"JSON已保存至: {save_path}")

        if "Manifest.plist" in self.file_name:
            self.text_输出("Plist重要数据提取：")
            self.text_输出(f"BundleShortVersionString: {plist_data.get('BundleShortVersionString')}")

    except Exception as e:
        self.text_输出(f"Plist解析失败: {str(e)}")



'-------------------------android功能---------------------------'
hook脚本 = {'获取全部字符串':'hook_strings_1.js',
          '获取字符串':'hook_strings_2.js',
          '获取AES加密':'hook_aes.js',
          '反调试':'hook_debug.js',
          '绕过frida检测':'hook_anti.js'}

def hook执行(self):
    self.ui.text_echo.clear()
    selected_hook_script = self.ui.hook_fun.currentText()
    hook_script_name = hook脚本.get(selected_hook_script)
    package_name = self.ui.hook_name.text().strip()
    if not selected_hook_script:
        self.text_输出("请选择一个hook脚本")
        return
    if not package_name:
        self.text_输出("请输入包名")
        return
    
    # 构建hook脚本的完整路径
    hook_script_path = os.path.join("./mod/hook", hook_script_name)
    if not os.path.exists(hook_script_path):
        self.text_输出(f"未找到hook脚本: {hook_script_path}")
        return
    
    try:
        # 创建 QProcess 实例并作为类的属性
        self.process = QProcess()
        # 存储待执行的命令列表
        commands = [
            "adb shell ls /data/local/tmp/fservice64",
            "adb shell chmod 755 /data/local/tmp/fservice64",
            "adb shell /data/local/tmp/fservice64 &"
        ]
        current_command_index = 0

        def check_finished(exit_code, exit_status):
            nonlocal current_command_index
            try:
                if exit_status != QProcess.NormalExit:
                    self.text_输出(f"命令执行异常退出，状态码: {exit_status}")
                    return
                if current_command_index == 0 and exit_code != 0:
                    self.text_输出("模拟器中未找到 fservice64 文件，请上传")
                    return
                if current_command_index < len(commands) - 1:
                    current_command_index += 1
                    self.process.start("cmd.exe", ["/c", commands[current_command_index]])
                else:
                    self.text_输出("模拟器中已存在 fservice64 文件")
                    try:
                        device = frida.get_usb_device(timeout=5)
                        
                        # 获取进程列表
                        processes = device.enumerate_processes()
                        
                        # 优先查找完全匹配的进程
                        target_process = next((p for p in processes if p.name == package_name), None)
                        
                        if not target_process:
                            # 如果没有直接匹配，则显示可用进程列表
                            filtered_processes = [
                                p for p in processes 
                                if not p.name.startswith(('com.android.', 'system', 'su'))
                            ]
                            
                            if not filtered_processes:
                                self.text_输出("没有找到可用的应用进程")
                                return
                                
                            self.text_输出("可用的应用进程:")
                            for p in filtered_processes:
                                self.text_输出(f"{p.pid}  {p.name}")
                            
                            self.text_输出(f"未找到包名为 {package_name} 的进程，请从上方列表中选择正确的进程名")
                            return
                            
                        # 执行hook（带重试机制）
                        max_retries = 3
                        for attempt in range(max_retries):
                            try:
                                session = device.attach(target_process.pid)
                                with open(hook_script_path, 'r', encoding='utf-8') as f:
                                    hook_code = f.read()
                                script = session.create_script(hook_code)
                                
                                # 重定向所有text_输出到UI
                                def on_message(message, data):
                                    try:
                                        if message['type'] == 'send':
                                            output = message['payload']
                                            if isinstance(output, dict):
                                                output = json.dumps(output, ensure_ascii=False)
                                            self.text_输出(str(output))
                                        elif message['type'] == 'error':
                                            self.text_输出(f"[脚本错误] {message['description']}")
                                        else:
                                            self.text_输出(f"[未知消息类型] {str(message)}")
                                    except Exception as e:
                                        self.text_输出(f"处理消息出错: {str(e)}")
                                
                                script.on('message', on_message)
                                script.set_log_handler(lambda level, text: self.text_输出(f"[Frida日志] {text}"))
                                
                                # 确保进程标准text_输出也被重定向
                                if hasattr(script, 'set_output_handler'):
                                    script.set_output_handler(lambda text: self.text_输出(f"[进程text_输出] {text}"))
                                
                                script.load()
                                self.text_输出(f"hook脚本已成功执行于进程: {target_process.name}")
                                self.text_输出("所有text_输出将显示在此处，不会出现在终端")
                                break
                            except frida.ProcessNotFoundError:
                                self.text_输出(f"尝试 {attempt + 1}/{max_retries}: 进程不存在或已终止")
                                if attempt == max_retries - 1:
                                    self.text_输出("注入失败: 进程可能已崩溃或被终止")
                                    raise
                                time.sleep(1)
                            except frida.TransportError as e:
                                self.text_输出(f"尝试 {attempt + 1}/{max_retries}: 通信错误: {str(e)}")
                                if attempt == max_retries - 1:
                                    self.text_输出("注入失败: 请检查frida-server是否正常运行")
                                    raise
                                time.sleep(1)
                            except frida.InvalidOperationError as e:
                                self.text_输出(f"尝试 {attempt + 1}/{max_retries}: 操作无效: {str(e)}")
                                if attempt == max_retries - 1:
                                    self.text_输出("注入失败: 请检查frida和frida-server版本是否匹配")
                                    raise
                                time.sleep(1)
                        
                    except frida.PermissionDeniedError:
                        self.text_输出("连接设备时权限被拒绝，请检查设备连接和权限设置")
                    except frida.ProcessNotFoundError:
                        self.text_输出("无法找到指定进程")
                    except Exception as e:
                        self.text_输出(f"执行hook脚本出错: {str(e)}")
            except Exception as inner_e:
                self.text_输出(f"处理检查结果出错: {str(inner_e)}")
            finally:
                # 安全销毁进程对象
                if hasattr(self, 'process'):
                    try:
                        if self.process.state() != QProcess.NotRunning:
                            self.process.terminate()
                            self.process.waitForFinished(1000)
                        self.process.deleteLater()
                        delattr(self, 'process')
                    except Exception as e:
                        print(f"清理进程出错: {str(e)}")

        # 开始执行第一个命令
        self.process.start("cmd.exe", ["/c", commands[current_command_index]])

        # 连接 finished 信号到处理函数
        self.process.finished.connect(check_finished)

    except Exception as e:
        self.text_输出(f"执行检查出错: {str(e)}")
        # 若出现异常，销毁进程对象
        if hasattr(self, 'process'):
            try:
                if self.process.state() != QProcess.NotRunning:
                    self.process.terminate()
                    self.process.waitForFinished(1000)
                self.process.deleteLater()
                delattr(self, 'process')
            except Exception as inner_e:
                print(f"异常清理出错: {str(inner_e)}")

'-------------------------python功能---------------------------'
def pyc_反编译(self):
    fun_file.文件读取(self)
    if not self.file_name:
        self.text_输出("文件读取失败,请检查是否输入需要反编译的文件")
    else:
        self.text_输出("文件读取正常，正在准备反编译")
        try:
            os.system(f"uncompyle6 {self.file_name} > {self.file_path}/pyc_py.py")
            self.text_输出(f"反编译完成，请查看{self.file_path}/pyc_py.py")
        except Exception:
            self.text_输出("反编译失败")
    fun_file.清理目录(self)



'-------------------------人工智能---------------------------'
def facefusion解析(self):
    self.ui.print_echo.clear()
    # 查找.jobs/completed目录下的最新文件
    jobs_dir = os.path.join(self.file_path, ".jobs", "completed")
    if os.path.exists(jobs_dir):
        self.text_输出("发现.jobs/completed文件夹,准备解析\n")
        file_list = []
        for filename in os.listdir(jobs_dir):
            file_list.append(os.path.join(jobs_dir, filename))
        self.text_输出(f"共发现{len(file_list)}个文件\n")
        份数 = 1
        for file_name in file_list:
            try:
                with open(file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    self.text_输出(f"正在text_输出第{份数}/{len(file_list)}文件:")
                    self.text_输出(f"创建时间: {data.get('date_created')} ")
                    self.text_输出(f"结束时间: {data.get('date_updated')} ")

                    self.text_输出(f"原图目录: {data.get('steps')[0].get('args').get('source_paths')} ")
                    self.text_输出(f"换脸目录: {data.get('steps')[0].get('args').get('target_path')} ")
                    self.text_输出(f"text_输出目录: {data.get('steps')[0].get('args').get('output_path')} ")

                    self.text_输出(f"人脸检测模型: {data.get('steps')[0].get('args').get('face_detector_model')}.onnx ")
                    self.text_输出(f"text_输出图片大小: {data.get('steps')[0].get('args').get('output_image_resolution')} ")
                    self.text_输出(f"年龄模型: {data.get('steps')[0].get('args').get('age_modifier_model')}.onnx ")
                    self.text_输出(f"面部编辑模型: {data.get('steps')[0].get('args').get('face_editor_model')}.onnx ")
                    self.text_输出(f"面部增强模型: {data.get('steps')[0].get('args').get('face_enhancer_model')}.onnx ")
                    self.text_输出(f"换脸模型: {data.get('steps')[0].get('args').get('face_swapper_model')}.onnx ")
                    self.text_输出(f"框架上色模型: {data.get('steps')[0].get('args').get('frame_colorizer_model')}.onnx ")
                    self.text_输出(f"唇部同动模型: {data.get('steps')[0].get('args').get('lip_syncer_model')}.onnx\n")
                    份数 += 1

            except Exception as e:
                self.text_输出(f"文件解析失败: {str(e)}")
                continue

    else:
        self.text_输出("未发现.jobs/completed文件夹,请检查")






'-------------------------杂项---------------------------'
def 时间戳转换(self):
    时间戳 = int(self.ui.input_echo.toPlainText())
    if not 时间戳:
        self.text_输出("请输入时间戳")
        raise
    try:
        if len(str(时间戳)) == 10 or len(str(时间戳)) == 13:
            if len(str(时间戳)) == 13:
                时间戳 = 时间戳 // 1000
                if len(str(时间戳)) != 10:
                    print("时间戳格式错误")
            self.text_输出(f"UTC时间: {datetime.datetime.fromtimestamp(时间戳, datetime.timezone.utc)}")
            self.text_输出(f"北京时间: {datetime.datetime.fromtimestamp(时间戳, datetime.timezone(datetime.timedelta(hours=8)))}")
        elif len(str(时间戳)) == 9:
            self.text_输出(f"ios时间: {datetime.datetime.fromtimestamp(时间戳 + 978307200, datetime.timezone.utc)}")
    except Exception as e:
        self.text_输出(f"时间戳格式错误:{e}")



# 未使用
"""
import hashlib
def bt_密码生成(self):
    passwd = config.str1
    salt = config.str2
    if not passwd or not salt:
        self.text_输出("请在变量1中设置密码,变量2中设置盐值")
    else:
        self.text_输出("已设置密码为:{},盐值为:{}".format(passwd, salt))
        p1 = passwd + "_bt.cn"
        p2 = hashlib.md5(p1.encode(encoding="UTF-8")).hexdigest() + salt
        btpass = hashlib.md5(p2.encode(encoding="UTF-8")).hexdigest()
        self.text_输出("bt加盐密码为:{}".format(btpass))
    file_fun.清理目录(self)
"""
