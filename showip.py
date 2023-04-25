import socket

#hostnameを取得
hostname = socket.gethostname()

#hostnameからIPアドレスを取得
ip_table = socket.gethostbyname_ex(hostname)

print(ip_table)

#sensorbrigeと同じネットワークアドレスのIPアドレスを探す
for ip_add in ip_table[2]:
  if "192.168.3" in ip_add:
    print(ip_add)
