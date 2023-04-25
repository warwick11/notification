import json
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class class1(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        
        #受信したデータを表示
        print(post_body)

#PCのIPアドレス
ip = '192.168.3.60'

#使用するポート番号
port = 8000

#HTTPServerhandle
server = HTTPServer((ip, port), class1)

try:
    while True:
        #サーバーを実行
        server.serve_forever()

except KeyboardInterrupt:
    print("StopHttpServer")
