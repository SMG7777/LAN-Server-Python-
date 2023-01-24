print("现在你可以去看一下桌面上是否生成了一个名叫服务器的文件夹")
print("此文件夹里面包含了你服务器的所有文件，如果你要将一些文件发送到局域网内的一个指定电脑里面，请先将你要发送的文件放入桌面上一个名叫服务器的文件夹里即可")
print("双击服务器的程序文件（服务器.exe）等待服务器启动，当一个窗口提示出有一个网址链接的时候，记下此链接，来到指定电脑，打开浏览器，输入'链接+要传输的文件'(如：http://192.168.1.1:5050/1.txt）")
from flask import Flask,send_file
import socket
res = socket.gethostbyname(socket.gethostname())
import os
desktop = os.path.join(os.path.expanduser('~'),"Desktop")
if not os.path.exists('{}\\服务器'.format(desktop)):    
    os.makedirs("{}\\服务器".format(desktop))

app = Flask(__name__)

@app.route("/")
def main():
    return "服务器主页"

@app.route("/<file>")
def file(file):
    return send_file("{}\\服务器\\{}".format(desktop,file))

if __name__ == "__main__":
    app.run(host=res,port=5050)
