import requests,uuid,random,re,ctypes,json,urllib,hashlib,hmac,urllib.parse,base64,os




active = requests.get("https://api.ipify.org/?format=json").json()
ip = active["ip"]
scan = requests.get("https://pastebin.com/raw/uJsmaEwq").text
if ip in scan:
    input("Call @m1c1 sent new tool")
else:
    print(f"{ip} This ip is not active")
    input()
    exit(0)
















