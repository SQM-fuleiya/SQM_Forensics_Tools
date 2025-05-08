import pyshark , re 
file_path= './test.pcapng'
流量数据 = pyshark.FileCapture(file_path, display_filter='http.response')
# 获取响应内返回的html数据
def 获取响应数据(流量数据):
    数据 = []
    for packet in 流量数据:
        数据.append(re.findall(r'\t(.+)\r' , str(packet.layers[4]),re.I)[0])
    print("".join(数据))
获取响应数据(流量数据)
