import json
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class class1(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        

        #jsonをパースして連想配列にする
        post_dir = json.loads(post_body)
        post_doc = str(post_dir)
        #受信データを表示
        print(post_dir)

#PCのIPアドレス
ip = '192.168.3.10'

#使用するポート番号
port = 8000

#HTTPServerhandle
server = HTTPServer((ip, port), class1)

try:
    while True:
        server.serve_forever()

except KeyboardInterrupt:
    print("StopHttpServer")
