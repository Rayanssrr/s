from time import sleep
from threading import Thread,Lock,Event
from random import *
from string import *
from requests.sessions import session
from termcolor import colored
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
import string,json,re,ctypes
import random , os , requests , uuid ,colorama
colorama.init()

dir_path = os.path.dirname(os.path.realpath(__file__))

Done = False

Bad = [
    "/challenge/",
    "consent_required",
    "feedback_required",
    "login_required",
    "nother account",
    "minutes"
]

class Design:
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    s1 = '\x1b[36m1\x1b[31m'
    s2 = '\x1b[36m2\x1b[31m'
    one = f"\x1b[31m[{s1}]\x1b[31m"
    tow = f"\x1b[31m[{s2}]\x1b[31m"
    eq = '\x1b[36m≈\x1b[31m'
    eq1 = f"\x1b[31m[{eq}]\x1b[31m"
    equl = '\x1b[36m=\x1b[31m'
    equl1 = f"\x1b[31m[{equl}]\x1b[31m"
    du = '\x1b[36m≠\x1b[31m'
    du1 = f"\x1b[31m[{du}]\x1b[31m"
    plus = '\x1b[36m+\x1b[31m'
    plus2 = '\x1b[32m+\x1b[36m'
    mains = '\x1b[36m-\x1b[31m'
    SL = '\x1b[36m/\x1b[31m'
    INPUT = f"\x1b[31m[ {plus} ]\x1b[31m"
    INPUT0 = f"\x1b[36m[{plus2}]\x1b[36m"
    INPUT1 = f"\x1b[31m[{SL}]\x1b[31m"
    INPUT2 = f"\x1b[31m[{mains}]\x1b[39m"
    marka = '\x1b[32m✓\x1b[36m'
    INPUT3 = f"\x1b[36m[{marka}]\x1b[36m"
    blueq = '\x1b[36m\x1b[40m'
    reda = '\x1b[31m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    purble = '\x1b[35m\x1b[39m'
    SUCCESS = '\x1b[31m Successfulyy moved \x1b[31m'
    Run = '\x1b[36m Started Running...\x1b[31m'
    under = '\x1b[35m_\x1b[39m'
    skip = '\x1b[31m (defult Thread = 300) \x1b[31m'
    clearConsle = lambda: os.system('clear')

    qube = '['
    qube2 = ']'

    grey = 'gray'
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'
    magenta = 'magenta'
    cyan = 'cyan'
    white = 'white'
    
    right = "Made By Psycho Rayan"
    
    banner = """
                        
                                
            ,-.          ,          .   .   
            |  \         |    o     |   |   
            |  | ,-: . . |    . ,-: |-. |-  
            |  / | | | | |    | | | | | |   
            `-'  `-` `-| `--' ' `-| ' ' `-' 
                    `-'        `-'   
                 
"""

imge = [
    "https://c.tenor.com/mD1iWcEHA6MAAAAC/anime-girl.gif",
    "https://c.tenor.com/ynltIl-WTboAAAAC/anime-sad.gif",
    "https://c.tenor.com/oaDTsvOKy20AAAAC/lightning-glitch.gif",
    "https://media.giphy.com/media/I6wUi5eTdUCWI/giphy.gif",
    "https://media.giphy.com/media/3fNmJ20ErpkjK/giphy.gif",
    "https://media.giphy.com/media/GLgPVZ5PLMOPe/giphy.gif",
    "https://media.giphy.com/media/AkRFIhfAKHsyc/giphy.gif",
    "https://media.giphy.com/media/A5KGHdmmxHdwk/giphy.gif",
    "https://media.giphy.com/media/QCJlIDkOJDEIctfdzz/giphy.gif",
    "https://media.giphy.com/media/if9niVFg4IwAE/giphy.gif",
    "https://media.giphy.com/media/QLCWubleeNppS/giphy.gif"]
def inputc(mark,color,text):
    print(f"\r{Design.qube} {colored(text=f'{mark}',color=f'{color}')} {Design.qube2} {text} {colored(text='',color=Design.white)}",end='')
def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))
def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result
win = ['Claimed :) But I won’t give it back To You :( Because Your Swap is Baad','Don’t Ever Again Swap With VB','Don’t Swap Again :(','Maybe Lisa Or Maybe Not','You Have To Use AutoClaimer Next Time But I Don’t Think You Will Take it :)']
def generateUSER_AGENT():
    Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
    DPIs = [
        '480', '320', '640', '515', '120', '160', '240', '800'
    ]
    randResolution = random.randrange(2, 9) * 180
    lowerResolution = randResolution - 180
    DEVICE_SETTINTS = {
        'system': "Android",
        'Host': "Instagram",
        'manufacturer': f'{random.choice(Devices_menu)}',
        'model': f'{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}',
        'android_version': random.randint(18, 25),
        'android_release': f'{random.randint(1, 7)}.{random.randint(0, 7)}',
        "cpu": f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
        'resolution': f'{randResolution}x{lowerResolution}',
        'randomL': f"{RandomString(6)}",
        'dpi': f"{random.choice(DPIs)}"
    }
    return '{Host} 133.0.0.34.124 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format( **DEVICE_SETTINTS)
class Daylight(object):
    def __init__(self):
        super(Daylight, self).__init__()
        self.claimed = False
        self.Done = False
        self.run = 1
        self.attempts = 0
        self.Locks = Lock()
        self.Event_Handler = Event()
        self.rl = 0
        self.rs = 0
        self.sessionid = [i.strip() for i in open(dir_path + "/sessions.txt", "r") if i]
        sleep(0.5)
        inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'sessions.txt'{Design.WHITE} : {Design.reda} {len(self.sessionid)}\n")
        self.proxies = [i.strip() for i in open(dir_path + "/proxies.txt", "r") if i]
        sleep(0.5)
        inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'proxies.txt'{Design.WHITE} : {Design.reda} {len(self.proxies)}\n")
        try:
            self.sesstings = open("sesstings.txt","r").read()
            inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'sesstings.txt'\n")
        except:
            inputc("-",Design.red,f"{Design.reda}Error loded Press Enter To Create 'sesstings.txt'\n");input()
            open("sesstings.txt","a").write('{"sesstings" : {\n\t"name": "FALCON DIGITAL ORG",\n\t"bio": "Maybe Rayan",\n\t"MSG": "Successfully Claimed",\n\t"Proxy_Mode":"1",\n\t"Webhook": "Here",\n\t"url_imge": ""\n}}')
        self.json_sesstings = json.loads(self.sesstings)
        self.bio = self.json_sesstings["sesstings"]["bio"]
        self.Msg = self.json_sesstings["sesstings"]["MSG"]
        self.Proxy_Mode = self.json_sesstings["sesstings"]["Proxy_Mode"]
        self.name = self.json_sesstings["sesstings"]["name"]
        self.Web_hook = self.json_sesstings["sesstings"]["Webhook"]
        self.url_imge = self.json_sesstings["sesstings"]["url_imge"]
        
        inputc("\\\\",Design.red,f"If Use Proxy {Design.reda}    (MAX Threads  = 500 | MAX Loop = 5){Design.WHITE}\n")
        inputc("\\\\",Design.red,f"If Not Use Proxy {Design.reda}(Max Threads = 30 | MAX Loop = 5){Design.WHITE}\n")
        inputc("?",Design.yellow,f"Do You Want Swap with proxy? {Design.reda}[Y/n]{Design.WHITE} : ");self.ask = input()
        Design.clearConsle()
        print(colored(f"{Design.banner}","red"))
        
        print("\n");inputc("?",Design.red,f"Target : ");self.Target = input()
        inputc("?",Design.red,f"Threads : ");self.threads = int(input())
        inputc("?",Design.red,f"Loops : ");self.loops = input();self.future_session = FuturesSession(max_workers=int(self.loops *4))  
        
    def remove_session(self, Sessions):
        if Sessions not in self.sessionid:
            return
        self.sessionid.remove(Sessions)
        
        if len(self.sessionid) == 0:
            self.run = False
            
            print("\n".join(self.sessionid), file=open(dir_path + "/sessions.txt", "w"))
    def proxy(self):
        if self.Proxy_Mode.__contains__("1"):
            self.erp = {"http": f"{random.choice(self.proxies)}", "https": f"{random.choice(self.proxies)}"}
        else:
            self.erp = {f"http":f"socks4://{random.choice(self.proxies)}","https":f"socks4://{random.choice(self.proxies)}"}
        return self.erp
    
    def Sucessfully_Claimed(self,session):
        self.run = False
        self.claimed = False
        self.just_loop = False
        print(f"\n\n{Design.WHITE}[ {Design.reda}${Design.WHITE} ] {self.Msg}  {Design.blueq}@{self.Target}{Design.WHITE} After {Design.reda}{self.attempts}{Design.WHITE} Attempts\n\n")
        open(f"@{self.Target}.txt","a").write(f"username:{self.Target}\nsession:{session}\n")
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{self.bio}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + session})
        requests.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/",data={"first_name":f"{self.name}"},headers={"User-Agent": generateUSER_AGENT(),"Cookie": "sessionid=" + session})
        self.sent_Discord()
        # webhook = DiscordWebhook(url='https://discord.com/api/webhooks/899788444966985730/Uy9-NNXthTA3ncdGqNSTfteDFZYcWASapaKaJObTMr_fuIxJ7dIkzcLtDMT8OOURuJIr')
        # embed = DiscordEmbed(title=f'',description=f"**Swapped [@{self.Target}](https://instagram.com/{self.Target}\nSwapped By {by})**", color=242424)
        # embed.set_author(name="Daylight")
        # embed.set_footer(text=f'Attempts : {self.attempts} | R/s : {self.rs}',icon_url=f"{random.choice(imge)}")
        # embed.set_thumbnail(url=f"{random.choice(imge)}")
        # webhook.add_embed(embed)
        # webhook.execute()
        try:
            webhook = DiscordWebhook(url=f'{self.Web_hook}')
            embed = DiscordEmbed(title=f'',description=f"**Swapped [@{self.Target}](https://instagram.com/{self.Target})**", color=242424)
            embed.set_author(name=f"{self.name}")
            embed.set_footer(text=f'Attempts : {self.attempts} | R/s : {self.rs}',icon_url=f"{self.url_imge}")
            embed.set_thumbnail(url=f"{self.url_imge}")
            webhook.add_embed(embed)
            webhook.execute()
        except:
            pass
        self.remove_session("".join(session))
        os._exit(0)
    
    def headers_Api(self):
        headers = {}
        headers["Connection"] = "close"
        headers["Accept"] = "*/*"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["Cookie2"] = "$Version=1"
        headers["Accept-Language"] = "en-US"
        headers["User-Agent"] = generateUSER_AGENT()
        headers["ig-u-ds-user-id"] = f"{RandomString(3)}-@-{RandomStringUpper(2)}#"
        return headers
    def get_email(self,sessionid):
        get = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers=self.headers_Api(),cookies={"sessionid":sessionid}).text
        try:
            self.email = re.search(r'"email":"(.*?)",',get).group(1)
        except:
            pass
        return self.email
    def get_phone(self,sessionid):
        get = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers=self.headers_Api(),cookies={"sessionid":sessionid}).text
        try:
            self.phone = re.search(r'"phone_number":"(.*?)",',get).group(1)
        except:
            pass
        return self.phone
    

    def just_loop(self,session):
        if self.ask.lower() == "y":
            self.Set_username_with_proxy(session)
        else:
            random.choice([self.Edit_Profile_without_proxy(session),self.Set_username_without_proxy(session),self.Edit_Web_without_proxy(session)])

        
    def Set_username_without_proxy(self,sessionid):
            future = []
            for i in range(int(self.threads)):
                futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/set_username/', data={"username": self.Target}, headers=self.headers_Api(),cookies={"sessionid":sessionid})
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as response:
                        #self.Edit_Profile_without_proxy(sessionid)
                        if response.text.__contains__('"status":"ok"'):
                            with self.Locks:
                                return self.Sucessfully_Claimed(sessionid)
                        elif response.status_code == 400:
                            with self.Locks:
                                self.attempts +=1
                        else:
                            self.rl +=1
                            
    def Edit_Profile_without_proxy(self,sessionid):
        try:
            email = self.get_email(sessionid)
            phone = self.get_phone(sessionid)
            data = {}
            data["_uid"] = f"47641699268"
            data["device_id"] = "android-d595db3f5c276071"
            data["_uuid"]= str(uuid.uuid4()),
            data["external_url"] = ""
            data['_csrftoken'] = 'massing'
            data["phone_number"] = str(phone)
            data["username"] = str(self.Target)
            data["first_name"] = ""
            data["biograph"] = ""
            data["email"] = str(email)
            future = []
            for i in range(int(self.threads)):
                futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/edit_profile/', data=data, headers=self.headers_Api(),cookies={"sessionid":sessionid})
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as response:
                        if response.text.__contains__('"status":"ok"'):
                            with self.Locks:
                                return self.Sucessfully_Claimed(sessionid)
                        elif response.status_code == 400:
                            with self.Locks:
                                self.attempts +=1
                        else:
                            self.rl +=1
        except:
            pass
    def sent_Discord(self):
        url = "https://discord.com/api/webhooks/899788444966985730/Uy9-NNXthTA3ncdGqNSTfteDFZYcWASapaKaJObTMr_fuIxJ7dIkzcLtDMT8OOURuJIr" #webhook url, from here: https://i.imgur.com/f9XnAew.png

        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        data = {}
        #leave this out if you dont want an embed
        #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
        data["embeds"] = [
            {
                "title" : f"Details...",
                "description" : f"\n*** Sucssfully Swapped => [ [@{self.Target}](https://instagram.com/{self.Target}) ]***\n**(``Devloped By Mexaw & RoRo``)**",
                "color": 2895667,
                "thumbnail" : {
                    "url": "https://cdn.discordapp.com/attachments/873022739349381173/873507948700262430/ezgif.com-gif-maker.gif"},
        
                "footer" : {
                "text": f'Attempts : {self.attempts} | R/s : {self.rs}',
                #"icon_url": "https://cdn.discordapp.com/attachments/873022739349381173/873507948700262430/ezgif.com-gif-maker.gif"
                    
                },
                "author" :{
                    "name" : "DayLight Swap"
                }
                
            }
        ]
        result = requests.post(url, json=data)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            pass
                        
    def Set_username_with_proxy(self,sessionid):
            future = []
            for i in range(int(self.threads)):
                futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/set_username/', data={"username": self.Target}, headers=self.headers_Api(),cookies={"sessionid":sessionid},proxies=self.proxy())
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    try:
                        with futures.result() as response:
                            if response.text.__contains__('"status":"ok"'):
                                with self.Locks:
                                    return self.Sucessfully_Claimed(sessionid)
                            elif response.status_code == 400:
                                with self.Locks:
                                    self.attempts +=1
                            else:
                                self.rl +=1
                    except:
                        pass
                            
    def Edit_Profile_with_proxy(self,sessionid):
        try:
            email = self.get_email(sessionid)
            phone = self.get_phone(sessionid)
            data = {}
            data["_uid"] = f"47641699268"
            data["device_id"] = "android-d595db3f5c276071"
            data["_uuid"]= str(uuid.uuid4()),
            data["external_url"] = ""
            data['_csrftoken'] = 'massing'
            data["phone_number"] = str(phone)
            data["username"] = str(self.Target)
            data["first_name"] = ""
            data["biograph"] = ""
            data["email"] = str(email)

            future = []
            for i in range(int(self.threads)):
                futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/edit_profile/', data=data, headers=self.headers_Api(),cookies={"sessionid":sessionid},proxies=self.proxy())
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                        with futures.result() as response:
                            if response.text.__contains__('"status":"ok"'):
                                with self.Locks:
                                    return self.Sucessfully_Claimed(sessionid)
                            elif response.status_code == 400:
                                with self.Locks:
                                    self.attempts +=1
                            else:
                                self.rl +=1
        except:
            pass
    def Edit_Web_without_proxy(self,sessionid):
        try:
            email = self.get_email(sessionid)
            phone = self.get_phone(sessionid)
            data = {}
            data['first_name'] = ""
            data['email'] = email
            data["username"] = self.Target
            data['phone_number'] = phone
            data['biography'] = ''
            data['external_url'] = ""
            data['chaining_enabled'] = ''
            future = []
            for i in range(int(self.threads)):
                futures = self.future_session.post('https://www.instagram.com/accounts/edit/', data=data, headers={
                                'accept':'*/*', 
                                'accept-encoding':'gzip, deflate, br', 
                                'accept-language':'ar,en-US;q=0.9,en;q=0.8', 
                                'content-length':'135', 
                                'content-type':'application/x-www-form-urlencoded', 
                                'cookie':f'ig_did=; ig_nrcb=1; mid=YNt8YQALAAHpMfzMX5-nq-UvVpPv; csrftoken=missing; ds_user_id={RandomString(3)}-@-{RandomStringUpper(2)}#;sessionid={sessionid}; rur="VLL"', 
                                'origin':'https://www.instagram.com', 
                                'referer':'https://www.instagram.com/accounts/edit/', 
                                'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 
                                'sec-ch-ua-mobile':'?0', 
                                'sec-fetch-dest':'empty', 
                                'sec-fetch-mode':'cors', 
                                'sec-fetch-site':'same-origin', 
                                'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
                                'x-asbd-id':'437806', 
                                'x-csrftoken':f"missing", 
                                'x-ig-app-id':'936619743392459', 
                                'x-ig-www-claim':'hmac.AR04gdj-gOnKqDQw6vN3YPIMMgsN3x-s19fgRfD8YFAz17sN', 
                                'x-instagram-ajax':'1cb3c391e22f', 
                                'x-requested-with':'XMLHttpRequest'})
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                        with futures.result() as response:
                            if response.text.__contains__('"status":"ok"'):
                                with self.Locks:
                                    return self.Sucessfully_Claimed(sessionid)
                            elif response.status_code == 400:
                                with self.Locks:
                                    self.attempts +=1
                            else:
                                self.rl +=1
        except:
            pass
        
        

class for_loop(Thread):
    def __init__(self, loop):
        super(for_loop, self).__init__()
        self.my_loop = loop
    def run(self):
        while self.my_loop.run:
            session = random.choice(self.my_loop.sessionid)
            if self.my_loop.just_loop(session):
                self.my_loop.claimed = True


                
            sleep(0.001)
class RequestPerSecounD(Thread):
    def __init__(self, loop):
        super(RequestPerSecounD, self).__init__()
        self.my_loop_request = loop
    def run(self):
        while self.my_loop_request.run:
            before = self.my_loop_request.attempts
            sleep(1)
            self.my_loop_request.rs = self.my_loop_request.attempts - before
if __name__ == "__main__":
    active = requests.get("https://api.ipify.org/?format=json").json()
    ip = active["ip"]
    scan = requests.get("https://pastebin.com/raw/jjeXSVhj").text
    try:
        by = re.search(rf'{ip} "(.*?)"',scan).group(1)
    except:
        pass
    if ip in scan:
        os.system('mode con: cols=83 lines=30')
        Design.clearConsle()
        print(colored(f"{Design.banner}\n","red"))
        var = Daylight()
        if var.ask.lower() == "y":
            print("\n");inputc("+",Design.green,f"Proxies = {Design.GREEN}True\n")
            inputc("/",Design.green,f"1 -> http/s | 2 -> Socks4 : {Design.GREEN}{var.Proxy_Mode}\n")
        else:
            print("\n");inputc("-",Design.green,f"Proxies = {Design.reda}False")
        
        print("\n");inputc("/",Design.red,f"Press Enter to Started !");input();#ctypes.windll.user32.MessageBoxW(0, f"Are You Ready?", f"king {by}", 0x1000)
        print(f"\n[ {Design.reda}${Design.WHITE} ] Turbo is Running...\n")
        def PrintLn():
            while var.run:
                for Dance in ["|","/","-","\\","|","/","-"]:
                    print(f"[ {Design.GREEN}{Dance}{Design.WHITE} ] Attempt : {var.attempts} / Rate_Limit : {var.rl} / R/S : {var.rs}",end="\r",flush=True)
                    sleep(0.3)
        Thread(target=PrintLn).start()
        rs = RequestPerSecounD(var)
        rs.start()
        for _ in range(int(var.threads)):
            thread = for_loop(var)
            thread.start()


        if len(var.sessionid) == 0 or None or var.sessionid == '':
            inputc("-",Design.red,"Ran out of accounts , Ican't Found Session In list\n");input(),exit(0)
            
    else:
        input(ip)
