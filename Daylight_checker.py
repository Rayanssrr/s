from time import sleep
from threading import Thread,Lock,Event
from random import *
from string import *
import string,json,re
from termcolor import colored
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
import secrets
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
from tqdm import tqdm
import random , os , requests , uuid , ctypes,colorama,threading

colorama.init()
dir_path = os.path.dirname(os.path.realpath(__file__))

Done = False

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
    clearConsle = lambda: os.system('cls')

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
            ____________    __ -+-  ____________ 
            \_____     /   /_ \ |   \     _____/
             \_____    \____/  \____/    _____/
              \_____                    _____/
                \___________  ___________/
                          /____\ 

                        FALCON DIGITAL ORG
                        
                            IG : [@m1c1 - @31421]
                            Daylight checker swap 
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
    return '{Host} 10.26.0 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format( **DEVICE_SETTINTS)




class Checkr(object):
    def __init__(self):
        super(Checkr, self).__init__()
        self.claimed = False
        self.run = 1
        self.attempts = 0
        self.Locks = Lock()
        self.Event_Handler = Event()
        self.rl = 0
        self.rs = 0
    
        self.sessionid = [i.strip() for i in open(dir_path + "/sessions.txt", "r") if i]
        sleep(0.5)
        inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'sessions.txt'{Design.WHITE} : {Design.reda} {len(self.sessionid)}\n")
        self.usernames = [i.strip() for i in open(dir_path + "/list.txt", "r") if i]
        sleep(0.5)
        inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'list.txt'{Design.WHITE} : {Design.reda} {len(self.usernames)}\n")
        self.proxies = [i.strip() for i in open(dir_path + "/proxies.txt", "r") if i]
        try:
            self.sesstings = open("sesstings.txt","r").read()
            inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'sesstings.txt'\n")
        except:
            inputc("-",Design.red,f"{Design.reda}Error loded 'sesstings.txt'\n")
            open("sesstings.txt","a").write('{"sesstings" : {\n\t"name": "FALCON DIGITAL ORG",\n\t"bio": "Rayan", \n\t"Threads": "250",\n\t"Loops": "350",\n\t"MSG": "Successfully Claimed",\n\t"Proxy_Mode":"1"\n}}')
        print("\n");inputc("?",Design.yellow,f"Do You Want Swap with proxy? {Design.reda}[Y/n]{Design.WHITE} : ");self.ask = input()
        
        
        
        self.json_sesstings = json.loads(self.sesstings)
        self.bio = self.json_sesstings["sesstings"]["bio"]
        self.loops = self.json_sesstings["sesstings"]["Loops"]
        self.threads = self.json_sesstings["sesstings"]["Threads"]
        self.Msg = self.json_sesstings["sesstings"]["MSG"]
        self.Proxy_Mode = self.json_sesstings["sesstings"]["Proxy_Mode"]
        self.name = self.json_sesstings["sesstings"]["name"]
        self.future_session = FuturesSession(max_workers=int(self.loops))
        
        
    
    def random_session(self):
        return random.choice(self.sessionid)
    
    def remove_session(self, Sessions):
        if Sessions not in self.sessionid:
            return
        self.sessionid.remove(Sessions)

        if len(self.sessionid) == 0:
            self.run = False

            print("\n".join(self.sessionid), file=open(dir_path + "/sessions.txt", "w"))
    def remove_user(self,user):
        if user not in self.usernames:
            return
        self.usernames.remove(user)
        
        if len(self.usernames) == 0:
            self.run = False
            
            print("\n".join(self.usernames), file=open(dir_path + "/list.txt", "w"))

    def proxy(self):
        if self.Proxy_Mode.__contains__("1"):
            self.erp = {"http": f"{random.choice(self.proxies)}", "https": f"{random.choice(self.proxies)}"}
        else:
            self.erp = {f"http":f"socks4://{random.choice(self.proxies)}","https":f"socks4://{random.choice(self.proxies)}"}
        return self.erp
    
    def Successfully_Claimed(self,user,session):
        print(f"\n[ {Design.reda}${Design.WHITE} ] {self.Msg}  {Design.blueq}@{user}")
        get = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers={"User-Agent": generateUSER_AGENT()},cookies={"sessionid":session}).text
        self.email = re.search(r'"email":"(.*?)",',get).group(1)
        open(f"@{user}.txt","a").write(f"username:{user}\nemail:{self.email}\nsession:{session}")
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{self.bio}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + session})
        requests.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/",data={"first_name":f"{self.name}"},headers={"User-Agent": generateUSER_AGENT(),"Cookie": "sessionid=" + session})
        if len(user) < 5:
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/896869437129519154/_V_nG4WJMlNB0E9-KncwBhsmq8LiaHbQ2lomrZKyRV4aIY2yxHbtlj4p9-64jUjJfx7i')
            embed = DiscordEmbed(title=f'Claimed @{user}\n`Attempts -> {self.attempts}`', color=242424)
            embed.set_author(name="Daylight_Checker")
            embed.set_image(url=f"{random.choice(imge)}")
            embed.set_footer(text='Made By Rayan@m1c1')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
        
        self.remove_session("".join(session))
        self.remove_user("".join(user))
        return False
    
    def just_loop(self):
        user = random.choice(self.usernames)
        session = self.random_session()
        cookie = secrets.token_hex(16)*2
        num = random.randint(10000000,9999999999)
        self.check_username2(user,session,cookie,num);self.check_username(user,session,cookie,num)
        
    def swap(self,user,session):
        self.Event_Handler.wait()
        if self.ask.lower() == "y":
                res = requests.post("https://i.instagram.com/api/v1/accounts/set_username/",headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + session},data={"username": f"{user}"},proxies=self.proxy())
                if res.status_code == 200:
                    self.Successfully_Claimed(user,session)
                elif res.text.__contains__("username"):
                    inputc("x",Design.red,f"{Design.reda}Someone claimed ")
                else:
                    inputc("x",Design.red,f"{Design.reda}Ican't Claim This User Because Youre Acc is Blocked")
        else:
            res = requests.post("https://i.instagram.com/api/v1/accounts/set_username/",headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + session},data={"username": f"{user}"})
            if res.status_code == 200:
                self.Successfully_Claimed(user,session)
            elif res.text.__contains__("username"):
                inputc("x",Design.red,f"{Design.reda}Someone claimed ")
            else:
                inputc("x",Design.red,f"{Design.reda}Ican't Claim This User Because Youre Acc is Blocked")
        
        

        

    def check_username(self,user,session,cookie,num):
        try:
            future = []
            i = True
            while i:
                futures = self.future_session.post("https://i.instagram.com/api/v1/accounts/username_suggestions/", data={"name":f"{user}"},proxies=self.proxy(), headers={
                "cookie":f'mid={cookie}; ig_did={str(uuid.uuid4).upper()}; ig_nrcb=1; datr=JUqyYNZAXmJNE4HpggCahOkI; csrftoken={cookie}; ds_user_id={num};',
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                "x-csrftoken":f"{cookie}",},cookies={"ig_did":str(uuid.uuid4()).upper(),"ds_user_id":f"{random.randint(10,999999999)}"},timeout=10)
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as response:
                        os.system(f"title Attempts : {self.attempts} / Ratelimt : {self.rl} / R/S : {self.rs}")
                        json_Response = json.loads(response.text)
                        if json_Response.__contains__('spam') or json_Response.__contains__('Please wait'):
                            self.rl +=1
                        elif json_Response.__contains__('suggestions'):
                            self.attempts  +=1
                        if json_Response["suggestions"].__contains__(user):
                            inputc("+",Design.green,f"{Design.blueq}Try To Hunt It {Design.GREEN}@{user}")
                            with self.Locks:
                                self.Event_Handler.set()
                                self.swap(user,session)

        
        except:
            pass
    
    def check_username2(self,user,session,cookie,num):
        try:
            future = []
            i = True
            while i:
                futures = self.future_session.post("https://i.instagram.com/accounts/username_suggestions/", data={"name":f"{user}"},proxies=self.proxy(), headers={
                "cookie":f'mid={cookie}; ig_did={str(uuid.uuid4).upper()}; ig_nrcb=1; datr=JUqyYNZAXmJNE4HpggCahOkI; csrftoken={cookie}; ds_user_id={num};',
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                "x-csrftoken":f"{cookie}",},cookies={"ig_did":str(uuid.uuid4()).upper(),"ds_user_id":f"{random.randint(10,999999999)}"},timeout=10)
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as response:
                        print(f"\r Attempts : {self.attempts} / Ratelimt : {self.rl} / R/S : {self.rs}",end="")
                        json_Response = json.loads(response.text)
                        if json_Response.__contains__('spam') or json_Response.__contains__('Please wait'):
                            self.rl +=1
                        elif json_Response.__contains__('suggestions'):
                            self.attempts  +=1
                        if json_Response["suggestions"].__contains__(user):
                            inputc("+",Design.green,f"{Design.blueq}Try To Hunt It {Design.GREEN}@{user}")
                            with self.Locks:
                                self.Event_Handler.set()
                                self.swap(user,session)              
        except:
            pass

                            
                            





class for_loop(Thread):
    def __init__(self, loop):
        super(for_loop, self).__init__()
        self.my_loop = loop

    def run(self):
        while self.my_loop.run and not Done:
            if self.my_loop.just_loop():
                self.my_loop.claimed = True
                self.my_loop.run = False

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
        print(colored(f"{Design.banner}","red"))
        print("__"*32)
        
        var = Checkr()
        print("\n");inputc("/",Design.green,f"1 -> http/s | 2 -> Socks4 : {Design.GREEN}{var.Proxy_Mode}\n")
        inputc("+",Design.green,f"{Design.WHITE}Threads {Design.reda}(Max = 1000){Design.WHITE} : {Design.GREEN}{var.threads}\n")
        inputc("+",Design.green,f"{Design.WHITE}Loops {Design.reda}(Max = 450){Design.WHITE} : {Design.GREEN}{var.loops}\n");inputc("/",Design.red,f"Press Enter to Started !");input()
        print(f"\n[ {Design.reda}${Design.WHITE} ] Turbo is Running...\n")

        for _ in range(int(var.threads)):
            thread = for_loop(var)
            thread.start()
            
            
        rs = RequestPerSecounD(var)
        rs.run()
        thread.run()
        rs.start()
    else:
        print(f"{Design.reda}{ip} This ip is not active")
        input()
        exit(0)
    
        
        



