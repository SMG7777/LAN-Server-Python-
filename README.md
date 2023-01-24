# 服务器想法
我记得以前在学校上信息课的时候，老师的服务器文件传输大小有限制，于是，我突发奇想，既然这样，那我就造一个服务器，来方便信息教室文件传输
# 使用的模块
__**Flask**__
## 安装方式
**__pip install flask__**
# 功能实现的重要函数
__**send_file()**__
# 代码（好了，不多说了，上代码）
```python
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
```
# 作者说明
我在前面添加了服务器使用说明，方便使用
