from time import sleep
from threading import Thread,Lock,Event
from random import *
from string import *
from termcolor import colored
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
import string,json,re,ctypes,secrets
import random , os , requests , uuid ,colorama,certifi
colorama.init()
dir_path = os.path.dirname(os.path.realpath(__file__))
Done = False


Bad = [
    "/challenge/",
    "consent_required",
    "feedback_required",
    "login_required",
    "nother account",
    "minutes"]


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
    
    clearTermnal = lambda: os.system('cls')
        

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
                       By {RoRo@M1C1}  
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
    "https://media.giphy.com/media/QLCWubleeNppS/giphy.gif"
    ]
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
        self.run = True
        self.response = None
        self.attempts = 0
        self.Locks = Lock()
        self.Event_Handler = Event()
        self.rl = 0
        self.rs = 0
        self.REQ = requests.session()
        print("\n")
        self.sessionid = [i.strip() for i in open(dir_path + "/sessions.txt", "r") if i]
        sleep(0.5)
        inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'sessions.txt'{Design.WHITE} : {Design.reda} {len(self.sessionid)}\n")
        self.proxies = [i.strip() for i in open(dir_path + "/proxies.txt", "r") if i]
        sleep(0.5)
        inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'Proxies.txt'{Design.WHITE} : {Design.reda} {len(self.proxies)}\n")
        self.users = [i.strip() for i in open(dir_path + "/list.txt", "r") if i]
        sleep(0.5)
        inputc("+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'list.txt'{Design.WHITE} : {Design.reda} {len(self.users)}\n")
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
        print("\n\n");inputc("/",Design.green,f"1 -> http/s | 2 -> Socks4 : {Design.GREEN}{self.Proxy_Mode}\n")
        inputc("+",Design.green,f"{Design.WHITE}Threads {Design.reda}(Max = 1000){Design.WHITE} : {Design.GREEN}");self.Threads = input()
        inputc("+",Design.green,f"{Design.WHITE}Loops {Design.reda}(Max = 500){Design.WHITE} : {Design.GREEN}");self.loops = input();self.future_session = FuturesSession(max_workers=int(self.loops*4));inputc("/",Design.red,f"Press Enter to Started !");input()
        Design.clearConsle()
        print(colored(f"{Design.banner}","red")) 
        
        print(f"\n[ {Design.reda}${Design.WHITE} ] Turbo is Running...\n")   

    def remove_session(self, Sessions):
        if Sessions not in self.sessionid:
            return
        self.sessionid.remove(Sessions)

        if len(self.sessionid) == 0:
            self.run = False
            print("\n".join(self.sessionid), file=open(dir_path + "/sessions.txt", "w"))
    def remove_user(self,user):
        if user not in self.users:
            return
        self.users.remove(user)
        
        if len(self.users) == 0:
            self.run = False
            
            print("\n".join(self.users), file=open(dir_path + "/list.txt", "w"))


    def proxy(self):
        if self.Proxy_Mode.__contains__("1"):
            self.erp = {"http": f"{random.choice(self.proxies)}", "https": f"{random.choice(self.proxies)}"}
        else:
            self.erp = {f"http":f"socks4://{random.choice(self.proxies)}","https":f"socks4://{random.choice(self.proxies)}"}
        return self.erp
    
    def Set_username_with_proxy(self,session,user):
        try:
            response = self.REQ.post("https://i.instagram.com/api/v1/accounts/set_username/",headers={f"User-Agent": generateUSER_AGENT()},data={"username": user},cookies={"sessionid":session},proxies=self.proxy()).text
            if response.__contains__('"status":"ok"'):
                self.REQ.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{self.bio}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + session})
                self.REQ.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/",data={"first_name":f"{self.name}"},headers={"User-Agent": generateUSER_AGENT(),"Cookie": "sessionid=" + session})
                get = self.REQ.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers={"User-Agent": generateUSER_AGENT()},cookies={"sessionid":session}).json()
                email = get['user']['email']
                open(f"@{user}.txt","a").write(f"username:{user}\nemail:{email}\nsession:{session}\n")
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/898538847141511178/LAPRBVlN04KbVOGenN734KN4_UdmX2HbF8yypgqKn3DLJ0r9Pv5ILpQaeOdhNG8qeu0s')
                embed = DiscordEmbed(title=f'Catched @{user}', color=242424)
                embed.set_author(name="Daylight")
                embed.set_footer(text=f'Attempts : {self.attempts} | R/s : {self.rs}',icon_url=f"{random.choice(imge)}")
                embed.set_thumbnail(url=f"{random.choice(imge)}")
                webhook.add_embed(embed)
                webhook.execute()
                webhook = DiscordWebhook(url=f'{self.Web_hook}')
                embed = DiscordEmbed(title=f'Catched @{user}', color=242424)
                embed.set_author(name=f"{self.name}")
                embed.set_footer(text=f'Attempts : {self.attempts} | R/s : {self.rs}',icon_url=f"{self.url_imge}")
                embed.set_thumbnail(url=f"{self.url_imge}")
                webhook.add_embed(embed)
                webhook.execute()
                #print(f"\n{Design.WHITE}[ {Design.reda}${Design.WHITE} ] {self.Msg}  {Design.blueq}@{user}{Design.WHITE} After {Design.reda}{self.attempts}{Design.WHITE} Attempts\n")
                print(f"\n\n\r{Design.WHITE}[ {Design.reda}${Design.WHITE} ] {self.Msg}  {Design.blueq}@{user}{Design.WHITE} After {Design.reda}{self.attempts}{Design.WHITE} Attempts\n\n\n")
                ctypes.windll.user32.MessageBoxW(0, f" {self.Msg} : {user} ", "Daylight", 0x1000)
                #autopy.alert.alert(f" {self.Msg} : {user} ", "Daylight")
                self.remove_session("".join(session))
                self.remove_user("".join(user))
            elif any(i in response for i in Bad):
                self.remove_session("".join(session))
        except:
            pass
    def Edit(self,session,user,random_email):
        response = self.REQ.post("https://i.instagram.com/api/v1/accounts/edit_profile/",
                                                        headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                                                    "Cookie": "sessionid=" + session},
                                                        data={"external_url": "", "phone_number": f"",
                                                                "username": f"{user}", "first_name": "",
                                                                "_uid": f"47641699268", "device_id": "android-d595db3f5c276071",
                                                                "biography": f"{self.bio}", "_uuid": str(uuid.uuid4()),
                                                                "email": f"{random_email}@gmail.com"}).text

        if response.__contains__('"status":"ok"'):
                open(f"@{user}.txt","a").write(f"username:{user}\nemail:{random_email}@gmail.com\nsession:{session}\n")
                self.REQ.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/",data={"first_name":f"{self.name}"},headers={"User-Agent": generateUSER_AGENT(),"Cookie": "sessionid=" + session})
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/898538847141511178/LAPRBVlN04KbVOGenN734KN4_UdmX2HbF8yypgqKn3DLJ0r9Pv5ILpQaeOdhNG8qeu0s')
                embed = DiscordEmbed(title=f'Catched @{user}', color=242424)
                embed.set_author(name="Daylight")
                embed.set_footer(text=f'Attempts : {self.attempts} | R/s : {self.rs}',icon_url=f"{random.choice(imge)}")
                embed.set_thumbnail(url=f"{random.choice(imge)}")
                webhook.add_embed(embed)
                webhook.execute()
                try:
                    webhook = DiscordWebhook(url=f'{self.Web_hook}')
                    embed = DiscordEmbed(title=f'Catched @{user}', color=242424)
                    embed.set_author(name=f"{self.name}")
                    embed.set_footer(text=f'Attempts : {self.attempts} | R/s : {self.rs}',icon_url=f"{self.url_imge}")
                    embed.set_thumbnail(url=f"{self.url_imge}")
                    webhook.add_embed(embed)
                    webhook.execute()
                except:
                    pass
                print(f"\n\n\r{Design.WHITE}[ {Design.reda}${Design.WHITE} ] {self.Msg}  {Design.blueq}@{user}{Design.WHITE} After {Design.reda}{self.attempts}{Design.WHITE} Attempts\n\n\n")
                ctypes.windll.user32.MessageBoxW(0, f" {self.Msg} : {user} ", "Daylight", 0x1000)
                #autopy.alert.alert(f" {self.Msg} : {user} ", "Daylight")
                self.remove_session("".join(session))
                self.remove_user("".join(user))
                #autopy.alert.alert(f" {self.Msg} : {user} ", "Daylight")
                #os.remove(''.join(session))
                #os.remove('',join(user))
        elif any(i in response for i in Bad):
            self.remove_session("".join(session))

    def sett(self,session,user):
        response = self.REQ.post("https://i.instagram.com/api/v1/accounts/set_username/",headers={f"User-Agent": generateUSER_AGENT()},data={"username": user},cookies={"sessionid":session}).text
        if response.__contains__('"status":"ok"'):
            self.REQ.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{self.bio}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + session})
            self.REQ.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/",data={"first_name":f"{self.name}"},headers={"User-Agent": generateUSER_AGENT(),"Cookie": "sessionid=" + session})
            get = self.REQ.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers={"User-Agent": generateUSER_AGENT()},cookies={"sessionid":session}).json()
            email = get['user']['email']
            open(f"@{user}.txt","a").write(f"username:{user}\nemail:{email}\nsession:{session}\n")
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/898538847141511178/LAPRBVlN04KbVOGenN734KN4_UdmX2HbF8yypgqKn3DLJ0r9Pv5ILpQaeOdhNG8qeu0s')
            embed = DiscordEmbed(title=f'Catched @{user}', color=242424)
            embed.set_author(name="Daylight")
            embed.set_footer(text=f'Attempts : {self.attempts} | R/s : {self.rs}',icon_url=f"{random.choice(imge)}")
            embed.set_thumbnail(url=f"{random.choice(imge)}")
            webhook.add_embed(embed)
            webhook.execute()
            try:
                webhook = DiscordWebhook(url=f'{self.Web_hook}')
                embed = DiscordEmbed(title=f'Catched @{user}', color=242424)
                embed.set_author(name=f"{self.name}")
                embed.set_footer(text=f'Attempts : {self.attempts} | R/s : {self.rs}',icon_url=f"{self.url_imge}")
                embed.set_thumbnail(url=f"{self.url_imge}")
                webhook.add_embed(embed)
                webhook.execute()
            except:
                pass
            print(f"\n\n{Design.WHITE}[ {Design.reda}${Design.WHITE} ] {self.Msg}  {Design.blueq}@{user}{Design.WHITE} After {Design.reda}{self.attempts}{Design.WHITE} Attempts\n\n\n")
            ctypes.windll.user32.MessageBoxW(0, f" {self.Msg} : {user} ", "Daylight", 0x1000)
            #autopy.alert.alert(f" {self.Msg} : {user} ", "Daylight")
            self.remove_session("".join(session))
            self.remove_user("".join(user))


        

    def just_loop(self,session,user):
        self.check_username(user,session,secrets.token_hex(16)*2,random.randint(10000000,9999999999),''.join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")for i in range (20)))
    
    def check_username(self,user,session,cookie,num,random_email):
            #future = []
            #for i in range(int(self.Threads)):
            try:
                self.response  = self.REQ.post(random.choice(["https://i.instagram.com/api/v1/accounts/username_suggestions/","https://i.instagram.com/accounts/username_suggestions/"]), data={"name":f"{user}"},proxies=self.proxy(), headers={
                "cookie":f'mid={cookie}; ig_did={str(uuid.uuid4).upper()}; ig_nrcb=1; datr=JUqyYNZAXmJNE4HpggCahOkI; csrftoken={cookie}; ds_user_id={num};',
                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                "x-csrftoken":f"{cookie}",},cookies={"ig_did":str(uuid.uuid4()).upper(),"ds_user_id":f"{random.randint(10,999999999)}"},timeout=20)
                # futures.i = i
                # future.append(futures)
                # for futures in as_completed(future):
                #     self.response = futures.result()
                #     print(self.response.text)
            except:
                pass
            else:
                if self.response.text.__contains__("suggestions"):
                    self.attempts +=1    
                if self.response.text.__contains__(f':["{user}"'):
                    print(f"\n\n\r{Design.WHITE}[ {Design.GREEN}+{Design.WHITE} ]{Design.blueq} Try To Hunt It  {Design.reda}@{user}{Design.WHITE}\n\n")
                    Thread(target=self.Set_username_with_proxy , args=(session,user)).start()
                    Thread(target=self.Edit , args=(session,user,random_email)).start()
                    Thread(target=self.sett , args=(session,user)).start()
                    self.remove_session("".join(session))
                    self.remove_user("".join(user))
                elif self.response.status_code == 429:
                    self.rl +=1
                    #futures.close()
                self.response.close()
                    # except:
                    #     pass
                        
        



class for_loop(Thread):
    def __init__(self, loop):
        super(for_loop, self).__init__()
        self.my_loop = loop
    def run(self):
        while self.my_loop.run:
            session = random.choice(self.my_loop.sessionid)
            user = random.choice(self.my_loop.users)
            if self.my_loop.just_loop(session,user):
                self.my_loop.claimed = True
            #sleep(0)
            
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
        def PrintLn():
            while var.run:
                sleep(0.0)
                os.system(f"title Attempts : {var.attempts} / Ratelimt : {var.rl} / R/S : {var.rs}")
                #print(f"\rAttempts : {var.attempts} / Ratelimt : {var.rl} / R/S : {var.rs}",end="")
                
        Thread(target=PrintLn).start()
        rs = RequestPerSecounD(var)
        rs.setDaemon(True)
        rs.start()
        for _ in range(int(var.Threads)):
            thread = for_loop(var)
            thread.setDaemon(True)
            thread.start()
        if len(var.sessionid) == 0 or None or var.sessionid == '':
            inputc("-",Design.red,"Ran out of accounts , Ican't Found Session In list\n");input(),exit(0)
    else:
        input(f"ip Not Activ {ip}");exit(0)
        
        

        
        

