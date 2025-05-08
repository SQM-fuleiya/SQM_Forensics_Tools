
from tools import config

def 日志分析(self):  # TODO 待完成
    self.ui.print_echo.clear()
    web关键词=['system','passthru','shell_exec','exec','popen','proc_open',
         'eval','assert','call_user_func','base64_decode','gzinflate','gzunconmpress',
         'gzdecode','srt_rot13','requiere','require_once','include_once','file_get_contents','file_put_contents','fputs','fwrite',
         'SetHandler','auto_prepend_file','auto_append_file']
    config.清理目录(self)