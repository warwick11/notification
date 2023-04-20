import json
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import datetime


class class1(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body=self.rfile.read(content_len)
        #文字列に変換する
        post_body=str(post_body)
        #文字数を計測する
        post_len=len(post_body)
        #15文字目から文字数-３を抽出し、変数に加える
        post_body=post_body[15:post_len-3]
        #jsonをパースして連想配列にする
        post_doc=json.loads(post_body)
        print(post_doc)
        f.write(post_doc)

ip = '192.168.3.12'

port = 8000

#HTTPServerhandle　引数にipアドレスとportとクラスを入れる
server = HTTPServer((ip, port), class1)

try:
    while True:
        server.serve_forever()

except KeyboardInterrupt:
    f.close()

