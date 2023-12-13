import os
import socket
import time

host = "192.168.1.110"
port1 = 8888
port2 = 7777

dir_path = 'save' 
for filename in os.listdir(dir_path):
    filepath = os.path.join(dir_path, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'rb') as file:
            data = file.read(os.path.getsize(filepath))
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((host, port1))
    s2.connect((host, port2))

    s1.send(data)
    str = "tiny:yawning"  #这里填违法类型
    s2.sendall(str.encode("utf-8"))
    print(f'文件"{filename}"发送成功')
    s1.close()
    s2.close()
    time.sleep(5)
