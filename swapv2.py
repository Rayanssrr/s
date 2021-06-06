try:
    import random, os, socket, requests, threading, ctypes
    from termcolor import colored
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import as_completed
    from discord_webhook import DiscordWebhook
    from discord_webhook import DiscordEmbed
    os.system("pip install requests_futures ")
except:
    pass

os.system('mode con: cols=80 lines=28')
dir_path = os.path.dirname(os.path.realpath(__file__))
attempts = 0
Error = 0
print_lock = threading.Lock()
GREEN = '32 m'
WHITE = '\x1b[1;37;40m'
YELLOW = '\x1b[1;33;40m'
RED = '\x1b[1;31;40m'
s1 = '\x1b[31m[]\x1b[40m'
plus = '\x1b[36m+\x1b[31m'
mains = '\x1b[36m-\x1b[31m'
INPUT = f"\x1b[31m[{plus}]\x1b[39m"
INPUT1 = f"\x1b[31m[{mains}]\x1b[39m"
INPUTd = '\x1b[31m\x1b[40m'
INPUTd1 = '\x1b[36m\x1b[40m'
SUCCESS = '\x1b[36m Swapped > @\x1b[31m'
SUCCESS1 = f'\x1b[36m \n > Try Agin Later \x1b[31m'
SU = '\x1b[36m Fetched all proxies succesfully \x1b[31m'
Run = '\x1b[36m Started Running...\x1b[31m'
skip = '\x1b[1;37;40m[\x1b[35m(if skip Thread = 250)\x1b[1;37;40m\x1b[1;37;40m]'
clearConsle = lambda: os.system('cls')
print("\n")
print("\n")
print("\n")
print("\n")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
g = requests.get('https://pastebin.com/kEdfngFt')
if ip in g.text:
    print(f'[+] Welcome')
    clearConsle()
else:
    print(ip)
    print('Ip not active send to @M1c1 on instagram to acive your ip :)')
    exit(0)


design = open("design.txt","r").read()
title = design.split("\n")[0]
msg = design.split("\n")[1]

PROXIES = open("proxies.txt","r").read().splitlines()



ask = int(input(f"[+]  1-normal swap - 2-autoswap : "))
ask2 = int(input("[+] 1-No proxy - 2-Proxy : "))
class normalswap():
    def __init__(self):
        self.search = input("[+] username : ")
        try:
            self.found = open(f"{self.search}.txt","r").read()
            self.session = self.found.split("\n")[0]
            #print(self.session)
        except Exception as E:
            print(E)
        self.fuc = [self.get_info()]
        self.Target = input(f'[+] Target : ')
        self.threads = int(input(f"[+] Enter Threads (if skip = 30): "))
        ctypes.windll.user32.MessageBoxW(0, f"Are You Ready ? \nTarget: @{self.Target} \nThread : {self.threads}  ", "ELECTRA SWAP", 0x1000)
        self.attempt = 0
        self.headers = {'User-Agent': 'Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)',}
        self.rl = 0
        self.run = True
        self.controll = threading.Event()
        self.locks = threading.Lock()
        self.future_session = FuturesSession(max_workers=self.threads*3)
        for i in range(int(self.threads or 30)):
            t = threading.Thread(target=self.runn)
            self.controll.set()
            t.start()
    def get_info(self):
        url = "https://www.instagram.com/accounts/edit/?__a=1"
        try:
            head = {
                "Host": "www.instagram.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
                "Accept": "/",
                "Connection": "keep-alive",
                'Cookie': 'ig_cb=2; ig_did=16D17E40-38A5-485C-A777-45AD4178960F; mid=X95mggAEAAF_8_wKj0mdSkDvsc3P; shbid=482; shbts=1609071008.2531302; rur=RVA; urlgen="{"51.36.118.201": 43766}:1kuTa3:joYKtH2q27Psck3O5RlGsW7nOOc"; csrftoken=3VZnkLZtrhJYfkh3WnD48Mv24rijhm9i; ds_user_id=18324709414; sessionid=' + self.session,
            }
            self.r = requests.get(url, headers=head).json()
            self.user = self.r['form_data']['username']
            input(f"[+] Login Successfly as (@{self.user}) Click Enter to continue")
            #clearConsle()
        except Exception as a:
            print(a)
            print(self.user)
            input(f"[-] Error Session id")
            exit()
    def proxies(self):
        while self.run:
            self.proxy = random.choice(PROXIES)
            self.Reproxy = {'http': f'{self.proxy}','https': f'{self.proxy}'}
            return self.Reproxy
    def runn(self):
        while self.run:
            if ask2 == 1:
                future = []
                for i in range(self.threads):
                    futures = self.future_session.post("https://i.instagram.com/api/v1/accounts/set_username/", data={"username": self.Target}, headers=self.headers, cookies={"sessionid": self.session})
                    futures.i = i
                    future.append(futures)
                    for futures in as_completed(future):
                        with futures.result() as resp:
                            if resp.status_code == 200:
                                with print_lock:
                                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/801325407151980575/T6crANE1anIvcyPUyM5BzOFTYU-j6ItwWX4eyKEvrtUl0fLbaCPCfLJwxKBKAQBYM2OH')
                                    embed = DiscordEmbed(title='#Electra SWAPPER', color=581845)
                                    embed.add_embed_field(name=f':@{self.Target}',value=f"Attempts:{self.attempt}\nSwapped By {title}")
                                    embed.add_embed_field(name='coded By : Rayan', value=f"Thx for swap")
                                    embed.set_image(url='https://media1.tenor.com/images/70493a75eb9badec8ebea2ca35e41379/tenor.gif?itemid=16327408')
                                    embed.set_footer(text="Date swap")
                                    embed.set_timestamp()
                                    webhook.add_embed(embed)
                                    response = webhook.execute()
                                    print(f"\n[+] Swapped > @{self.Target}")
                                    ctypes.windll.user32.MessageBoxW(0, f"{msg} : @{self.Target}  ", f"{title}", 0x1000)
                                    os._exit(0)
                            elif resp.status_code == 400:
                                self.attempt +=1
                                with self.locks:
                                    print(f"\rAttempts : {self.attempt} / rl : {self.rl} ", end="")
                            else:
                                self.rl +=1
                                with self.locks:
                                    print(f"\rAttempts : {self.attempt} / rl : {self.rl} ", end="")
            elif ask2 == 2:
                try:
                    future = []
                    for i in range(self.threads):
                        futures = self.future_session.post("https://i.instagram.com/api/v1/accounts/set_username/", data={"username": self.Target}, headers=self.headers, cookies={"sessionid": self.session},proxies=self.proxies(),timeout=5)
                        futures.i = i
                        future.append(futures)
                        for futures in as_completed(future):
                            with futures.result() as resp:
                                if resp.status_code == 200:
                                    with print_lock:
                                        webhook = DiscordWebhook(
                                            url='https://discord.com/api/webhooks/801325407151980575/T6crANE1anIvcyPUyM5BzOFTYU-j6ItwWX4eyKEvrtUl0fLbaCPCfLJwxKBKAQBYM2OH')
                                        embed = DiscordEmbed(title='#Electra SWAPPER', color=581845)
                                        embed.add_embed_field(name=f':@{self.Target}',value=f"Attempts:{self.attempt}\nSwapped By {title}")
                                        embed.add_embed_field(name='coded By : Rayan', value=f"Thx for swap")
                                        embed.set_image(url='https://media1.tenor.com/images/70493a75eb9badec8ebea2ca35e41379/tenor.gif?itemid=16327408')
                                        embed.set_footer(text="Date swap")
                                        embed.set_timestamp()
                                        webhook.add_embed(embed)
                                        response = webhook.execute()
                                        print(f"\n[+] Swapped > @{self.Target}")
                                        ctypes.windll.user32.MessageBoxW(0, f"{msg} : @{self.Target}  ", f"{title}", 0x1000)
                                        os._exit(0)
                                elif resp.status_code == 400:
                                    self.attempt +=1
                                    with self.locks:
                                        print(f"\r Attempts : {self.attempt} / rl : {self.rl} ", end="")
                                else:
                                    self.rl +=1
                                    with self.locks:
                                        print(f"\r Attempts : {self.attempt} / rl : {self.rl} ", end="")
                except:
                    pass



class autoswap():
    def __init__(self):
        #print("wlc")
        self.search = input("[+] username : ")
        try:
            self.found = open(f"{self.search}.txt", "r").read()
            self.session = self.found.split("\n")[0]
        except Exception as E:
            print(E)
        self.fuc = [self.get_info()]
        self.Target = input(f'[+] Target : ')
        self.seesion2 = input(f"[+] SESSION ID (Target) : ")
        ctypes.windll.user32.MessageBoxW(0, f"Are You Ready ? \n Target: @{self.Target}",
                                         "ELECTRA SWAP", 0x1000)
        self.fuc2 = [self.get_info2()]
        self.threads = 30
        self.attempt = 0
        self.api_list= ["https://i.instagram.com/api/v1/accounts/set_username/","https://i.instagram.com/api/v1/accounts/edit_profile/"]
        self.headers = {
                        'User-Agent': 'Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)',
                        "Accept": "/",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "en-US",
                        "X-IG-Capabilities": "3brTvw==",
                        "X-IG-Connection-Type": "WIFI",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        'Host': 'i.instagram.com'}
        self.rl = 0
        self.run = True
        self.controll = threading.Event()
        self.locks = threading.Lock()
        self.future_session = FuturesSession(max_workers=50)
        for i in range(int(self.threads)):
            t = threading.Thread(target=self.runn)
            self.controll.set()
            t.start()
            self.fuc1 = [self.open()]
    def get_info(self):
        url = "https://www.instagram.com/accounts/edit/?__a=1"
        head = {
            "Host": "www.instagram.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "/",
            "Connection": "keep-alive",
            'Cookie': 'ig_cb=2; ig_did=16D17E40-38A5-485C-A777-45AD4178960F; mid=X95mggAEAAF_8_wKj0mdSkDvsc3P; shbid=482; shbts=1609071008.2531302; rur=RVA; urlgen="{"51.36.118.201": 43766}:1kuTa3:joYKtH2q27Psck3O5RlGsW7nOOc"; csrftoken=3VZnkLZtrhJYfkh3WnD48Mv24rijhm9i; ds_user_id=18324709414; sessionid=' + self.seesion,
        }
        try:
            self.r = requests.get(url, headers=head).json()
            self.user = self.r['form_data']['username']
            input(f"{INPUT}{INPUTd1} Login Successfly as (@{self.user}) Click Enter to continue")
            clearConsle()
        except:
            input(f"[-] Error Session id")
            exit()
    def get_info2(self):
        url2 = "https://www.instagram.com/accounts/edit/?__a=1"
        head2 = {
            "Host": "www.instagram.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "/",
            "Connection": "keep-alive",
            'Cookie': 'ig_cb=2; ig_did=16D17E40-38A5-485C-A777-45AD4178960F; mid=X95mggAEAAF_8_wKj0mdSkDvsc3P; shbid=482; shbts=1609071008.2531302; rur=RVA; urlgen="{"51.36.118.201": 43766}:1kuTa3:joYKtH2q27Psck3O5RlGsW7nOOc"; csrftoken=3VZnkLZtrhJYfkh3WnD48Mv24rijhm9i; ds_user_id=18324709414; sessionid=' + self.seesion2,
        }
        try:
            self.r2 = requests.get(url2, headers=head2).json()
            self.user2 = self.r2['form_data']['username']
            input(f"{INPUT}{INPUTd1} Login Successfly as (@{self.user2}) Click Enter to continue")
            clearConsle()
            input(f"{INPUT}{INPUTd} Click Enter to Swap ")
        except:
            input(f"{INPUT1} Error Session id")
            exit()
    def open(self):
        self.electr = self.user2 + ".ElectraSwap"
        re = requests.post("https://i.instagram.com/api/v1/accounts/set_username/",headers=self.headers,data={"username": self.electr},cookies={"sessionid": self.seesion2}).status_code
        if re == 200:
            print(f'Successfully change user To ({self.electr})')


    def runn(self):
        while self.run:
            if ask2 == 1:
                api = random.choice(self.api_list)

                futures = [self.future_session.post(api, data={"username": self.Target}, headers=self.headers,
                                                    cookies={"sessionid": self.session}) for i in
                           range(60)]
                for future in as_completed(futures):
                    resp = future.result()
                    # print(resp.text)
                    print(f"{resp.text}\n{resp.status_code}")
                    if '"status":"ok"' in resp.text:
                        with print_lock:
                            webhook = DiscordWebhook(
                                url='https://discord.com/api/webhooks/810840907887804426/TwSqCHrKD1QR4hMnkHP48t8OnrrjsO4QcpjRlGJHh2vS9z4w9-gvEINazuaOp_P2gDlf')
                            embed = DiscordEmbed(title='#Swap ',
                                                 description=f"@{self.Target}\n Attempt >> {self.attempt}",
                                                 color=9109504)
                            embed.set_footer(text='#Thx|')
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            response = webhook.execute()
                            print(f"[+] Swapped > @{self.Target}")
                            print("\n[+] > Try Agin Later <")
                            print(f'\n{INPUT} {SUCCESS}{self.Target}{SUCCESS1}')
                            ctypes.windll.user32.MessageBoxW(0, f"Swapped Successfully : @{self.Target}  ",
                                                             "ELECTRA SWAP", 0x1000)
                            os._exit(0)
                    if "isn't" in resp.text:
                        self.attempt += 1
                        with self.locks:
                            print(f"\r Attempts : {self.attempt} / rl : {self.rl} ", end="")
                    else:
                        self.rl += 1
                        with self.locks:
                            print(f"\r Attempts : {self.attempt} / rl : {self.rl} ", end="")
            elif ask2 == 2:
                api = random.choice(self.api_list)

                resp = requests.post(api, data={"username": self.Target}, headers=self.headers,
                                     cookies={"sessionid": self.session})
                print(f"{resp.text}\n{resp.status_code}")
                if '"status":"ok"' in resp.text:
                    with print_lock:
                        webhook = DiscordWebhook(
                            url='https://discord.com/api/webhooks/810840907887804426/TwSqCHrKD1QR4hMnkHP48t8OnrrjsO4QcpjRlGJHh2vS9z4w9-gvEINazuaOp_P2gDlf')
                        embed = DiscordEmbed(title='#Swap ',
                                             description=f"@{self.Target}\n Attempt >> {self.attempt}",
                                             color=9109504)
                        embed.set_footer(text='#Thx|')
                        embed.set_timestamp()
                        webhook.add_embed(embed)
                        response = webhook.execute()
                        print(f"[+] Swapped > @{self.Target}")
                        print("\n[+] > Try Agin Later <")
                        print(f'\n{INPUT} {SUCCESS}{self.Target}{SUCCESS1}')
                        ctypes.windll.user32.MessageBoxW(0, f"Swapped Successfully : @{self.Target}  ",
                                                         "ELECTRA SWAP", 0x1000)
                        os._exit(0)
                if "isn't" in resp.text:
                    self.attempt += 1
                    with self.locks:
                        print(f"\r Attempts : {self.attempt} / rl : {self.rl} ", end="")
                else:
                    self.rl += 1
                    with self.locks:
                        print(f"\r Attempts : {self.attempt} / rl : {self.rl} ", end="")


def ss():
    if ask== 1:
        s = normalswap()
    if ask == 2:
        s = autoswap()

ss()





