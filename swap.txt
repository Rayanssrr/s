try:
    import random, os, socket, requests, threading, ctypes, uuid,certifi,pycurl
    from time import sleep
    from io import BytesIO
    from termcolor import colored
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import as_completed
    from discord_webhook import DiscordWebhook
    from discord_webhook import DiscordEmbed
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
    sleep(0.6)
    clearConsle()
else:
    print(ip)
    print('Ip not active send to @M1c1 on instagram to acive your ip :)')
    exit(0)


uid = str(uuid.uuid1)



class normalswap():
    def __init__(self):
        try:
            self.name = input("[+] Swapped by : ")
            clearConsle()
            self.search = input("[+] username : ")
            self.found = open(f"{self.search}.txt","r").read()
            self.session = self.found.split("\n")[0]
            #print(self.session)
        except Exception as E:
            print(E)
        self.fuc = [self.get_info()]
        self.Target = input(f'[+] Target : ')
        self.threads = input(f"[+] Enter Threads (if skip = 30): ")
        ctypes.windll.user32.MessageBoxW(0, f"Are You Ready ? \nTarget: @{self.Target} \nThread : {self.threads}  ", "ELECTRA SWAP", 0x1000)
        self.attempt = 0
        self.api_list= \
            ["https://i.instagram.com/api/v1/accounts/set_username/","https://i.instagram.com/api/v1/accounts/edit_profile/"]
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
        self.uid = str(uuid.uuid4())
        self.thredas = []
        for i in range(int(self.threads or 30)):
            t = threading.Thread(target=self.runn)
            t.setDaemon = True
            t.start()
            self.controll.set()
            self.thredas.append(t)
    def Special_Request(self,url, headers, data=None):
        curl = pycurl.Curl()
        response = BytesIO()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.ENCODING, '')
        curl.setopt(pycurl.WRITEDATA, response)
        curl.setopt(pycurl.HTTPHEADER, headers)
        curl.setopt(pycurl.CAINFO, certifi.where())
        if data:
            curl.setopt(pycurl.POST, True)
            curl.setopt(pycurl.POSTFIELDS, data)
            try:
                curl.perform()
                curl.close()
            except:
                pass
        return response.getvalue().decode('utf-8')
            
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
            #print(a)
            #print(self.user)
            input(f"[-] Error Session id")
            exit()
    def runn(self):
        while self.run:
            api = random.choice(self.api_list)
            resp = self.Special_Request(api, [
            "Accept: */*",
            "Accept-Language: en-US",
            "User-Agent: Instagram 85.0.0.21.100 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)",
            "Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie: sessionid=" + self.session
        ], "username=" + self.Target)
            #print(resp)
            if "isn't" in resp:
                self.attempt +=1
                with self.locks:
                    print(f"\r Attempts : {self.attempt} / rl : {self.rl} ", end="")
            if '"status":"ok"' in resp:
                with print_lock:
                    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/801325407151980575/T6crANE1anIvcyPUyM5BzOFTYU-j6ItwWX4eyKEvrtUl0fLbaCPCfLJwxKBKAQBYM2OH')
                    embed = DiscordEmbed(title='#Electra SWAPPER', color=581845)
                    embed.add_embed_field(name=f'@{self.Target}', value=f"Attempts: {self.attempt}\nSwapped By {self.name}")
                    embed.add_embed_field(name='coded By : Rayan ', value=f"Thx for swap")
                    embed.set_image(url='https://media1.tenor.com/images/70493a75eb9badec8ebea2ca35e41379/tenor.gif?itemid=16327408')
                    embed.set_footer(text="Date swap")
                    embed.set_timestamp()
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    print(f"[+] Swapped > @{self.Target}")
                    ctypes.windll.user32.MessageBoxW(0, f"Swapped Successfully : @{self.Target}  ", "ELECTRA SWAP", 0x1000)
                    os._exit(0)
            if "few minutes" in resp:
                self.rl +=1
                with self.locks:
                    print(f"\r Attempts : {self.attempt} / rl : {self.rl} ", end="")
            
        


def ss():
    s = normalswap()

ss()





