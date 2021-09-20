
import random, os, requests, threading, ctypes,string,json,hashlib,hmac,urllib,urllib.parse,uuid,re
from time import sleep
from requests.sessions import session
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
from colorama import init
from termcolor import colored
from discord_webhook import DiscordWebhook , DiscordEmbed

init()
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


dir_path = os.path.dirname(os.path.realpath(__file__))



class THRIDING():
    def __init__(self, fuc):
        self.TARGET = fuc
        self.threads_list = []

    def Generate_threads(self, Attack):
        for i in range(Attack):
            threads = threading.Thread(target=self.TARGET)
            threads.setDaemon(True)
            self.threads_list.append(threads)
        return self.threads_list

    def started(self):
        for threads_Attack in self.threads_list:
            threads_Attack.start()

    def joined(self):
        for thread_join in self.threads_list:
            thread_join.join()
    
    
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


    right = "#DayLight"

    banner = """
               __               ___       __    __ 
          ____/ /___ ___  __   / (_)___ _/ /_  / /_
         / __  / __ `/ / / /  / / / __ `/ __ \/ __/
        / /_/ / /_/ / /_/ /  / / / /_/ / / / / /_  
        \__,_/\__,_/\__, /  /_/_/\__, /_/ /_/\__/  
                   /____/       /____/             
    """



imge = [
    "https://c.tenor.com/mD1iWcEHA6MAAAAC/anime-girl.gif",
        "https://c.tenor.com/ynltIl-WTboAAAAC/anime-sad.gif",
        "https://c.tenor.com/oaDTsvOKy20AAAAC/lightning-glitch.gif",
        ]
        
def inputc(mark,color,text):
    print(f"\r{Design.qube} {colored(text=f'{mark}',color=f'{color}')} {Design.qube2} {text} {colored(text='',color=Design.white)}",end='')









    


class swap:
    def __init__(self):
        print("\n\n")
        #inputc("?",Design.green, f"seesion : ");self.sessionid = input()
        self.Lock = threading.Lock()
        self.uuid = uuid.uuid4()
        self.sessions = open("sessions.txt","r").read().splitlines()
        print(f"[{Design.GREEN} + {Design.WHITE}] session count : {len(self.sessions)}\n[{Design.GREEN} + {Design.WHITE}] press Enter To continue ");input()
        Design.clearConsle()
        print(colored(f"{Design.banner}","red"))
        print(colored(f"\tWelcome Sir {by} To Daylight Swap \n\tBy Rayan Insta  @m1c1",Design.cyan))
        print("\n\n")
        self.Attempts = 0
        self.Rate_limited = 0
        self.Rs = 0
        self.Running = True
        self.email = None
        self.phone = None
        inputc("?",Design.red,f"Target  : ");self.Target = str(input())
        inputc("+", Design.green, f"{Design.blueq}Do You Want Auto settings [Y/N] : ");self.settings = input()
        if self.settings.lower() == "y":
            print()
            self.Threads = 20
        else:
            inputc("?",Design.green,"Threads : "); self.Threads = int(input())
            print()
        self.future_session = FuturesSession(max_workers=self.Threads *4)
    
    def generateUSER_AGENT(self):
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
        return '{Host} 10.26.0 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(**DEVICE_SETTINTS)
    def random_session(self):
        return random.choice(self.sessions)

    def remove_session(self, session):
        if session not in self.sessions:
            return

        self.sessions.remove(session)

        if len(self.sessions) == 0:
            self.running = False
            return

        print("\n".join(self.sessions), file=open(dir_path + "/sessions.txt", "w"))

        


    
    def Successfulyy(self,session):
        self.Running = False
        get = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers=self.headers_Api(),cookies={"sessionid":session}).text
        self.user = re.search(r'"username":"(.*?)",',get).group(1)
        self.email = re.search(r'"email":"(.*?)",',get).group(1)
        open(f"@{self.Target}.txt","a").write(f"Username : {self.Target}\nemail : {self.email}\nsession : {session}")
        value = {"raw_text": f"Daylight"}
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data=value, headers=self.headers_Api(),cookies={"sessionid": session})
        self.remove_session("".join(session))
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/881360737606443098/XJRGDx7U8X3oIe5n71t_m9HXoAOgP3GUEUOm4gBdhG_0DKicxGa6umCtdWLtto3OnvAK')
        embed = DiscordEmbed(title=f'Swapped @{self.Target}\nAttempts -> {self.Attempts}\n\n`Swaped By Swapper {by}`', color=242424)
        embed.set_author(name="Daylight")
        embed.set_image(url=f"{random.choice(imge)}")
        embed.set_footer(text='Made By Rayan@m1c1')
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()
        print("\n")
        inputc("+",Design.green,f"{Design.GREEN}Swapped @{self.Target} \x1b[35mAfter {self.Attempts} Attempts \x1b[39m")
        ctypes.windll.user32.MessageBoxW(0, f"Swapped : @{self.Target}  ", f"Daylight", 0x1000);os._exit(0)
    def request_per_sec(self):
        while self.Running:
            befor = self.Attempts
            sleep(1)
            self.Rs = self.Attempts - befor
    def LOOP(self):
        while self.Running:
            for q in ["|","/","-","\\","|","/","-"]:
                print(f"\r[ {Design.GREEN}{q}{Design.WHITE} ] Attempt : {self.Attempts} / Rate_Limit : {self.Rate_limited} / R/S : {self.Rs}",end="",flush=True)
                sleep(0.1)
                
    
    def sent_Faster_web_Request(self):
        while self.Running:
            session = self.random_session()
            future = []
            for i in range(self.Threads):
                try:
                    futures = self.future_session.post('https://www.instagram.com/accounts/edit/', data={'first_name':"", 'email':self.email, 'username':self.Target, 'phone_number':self.phone, 'biography':f"", 'external_url':'', 'chaining_enabled':'on'}, headers={
                            'accept':'*/*', 
                            'accept-encoding':'gzip, deflate, br', 
                            'accept-language':'ar,en-US;q=0.9,en;q=0.8', 
                            'content-length':'135', 
                            'content-type':'application/x-www-form-urlencoded', 
                            'cookie':f'ig_did=; ig_nrcb=1; mid=YNt8YQALAAHpMfzMX5-nq-UvVpPv; csrftoken=missing; ds_user_id={RandomString(3)}-@-{RandomStringUpper(2)}#;sessionid={session}; rur="VLL"', 
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
                            'x-requested-with':'XMLHttpRequest'},timeout=5)
                    futures.i = i
                    future.append(futures)
                    for futures in as_completed(future):
                        with futures.result() as resp:
                            if resp.status_code == 200:
                                with self.Lock:
                                    self.Successfulyy(session)
                                    break 
                            elif resp.status_code == 400:
                                with self.Lock:
                                    self.Attempts += 1
                            elif resp.status_code == 429:
                                with self.Lock:
                                    self.Rate_limited += 1
                                    if self.Rate_limited >= 4000 :
                                        self.Running = False
                                        with self.Lock:
                                            print("\n\nBlocked Account And ip wait 2h for unblock")
                                            input("\n\nEnter To Exit");os._exit(0)
                except:
                    pass
            
    def data_edit_profile(self):
        data = {
            "external_url": "",
            "phone_number": "",
            "username": f"{self.Target}",
            "first_name": "",
            "_uid": f"47641699268",
            "device_id": "android-d595db3f5c276071",
            "biography": "",
            "_uuid": str(uuid.uuid4()),
            "email": f"{self.email}"}
        return data
    def headers_Api(self):
        headers = {}
        headers["Connection"] = "keep-alive"
        headers["Accept"] = "*/*"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["Cookie2"] = "$Version=1"
        headers["Accept-Language"] = "en-US"
        headers["User-Agent"] = self.generateUSER_AGENT()
        headers["ig-u-ds-user-id"] = f"{RandomString(3)}-@-{RandomStringUpper(2)}#"
        return headers

            
    def sent_edit_profile_Request(self):
        while self.Running:
            session = self.random_session()
            future = []
            for i in range(self.Threads):
                try:
                    futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/edit_profile/', data=self.data_edit_profile(), headers=self.headers_Api(),cookies={"sessionid":session},timeout=5)
                    futures.i = i
                    future.append(futures)
                    for futures in as_completed(future):
                        with futures.result() as resp:
                            if resp.status_code == 200:
                                with self.Lock:
                                    self.Successfulyy(session)
                                    break
                            elif resp.status_code == 400:
                                with self.Lock:
                                    self.Attempts += 1
                            elif resp.status_code == 429:
                                with self.Lock:
                                    self.Rate_limited += 1
                                    if self.Rate_limited >= 4000 :
                                        self.Running = False
                                        with self.Lock:
                                            print("\n\nBlocked Account And ip wait 2h for unblock")
                                            input("\n\nEnter To Exit");os._exit(0)
                except:
                    pass
                                    
    def sent_set_username_REQUEST(self):
        while self.Running:
            session = self.random_session()
            future = []
            for i in range(self.Threads):
                try:
                    futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/set_username/', data={"username":self.Target}, headers=self.headers_Api(),cookies={"sessionid":session},timeout=5)
                    futures.i = i
                    future.append(futures)
                    for futures in as_completed(future):
                        with futures.result() as resp:
                            if resp.status_code == 200:
                                with self.Lock:
                                    self.Successfulyy(session)
                                    
                                    break
                            elif resp.status_code == 400:
                                with self.Lock:
                                    self.Attempts += 1
                            elif resp.status_code == 429:
                                with self.Lock:
                                    self.Rate_limited += 1
                                    if self.Rate_limited >= 4000 :
                                        self.Running = False
                                        with self.Lock:
                                            print("\n\nBlocked Account And ip wait 2h for unblock")
                                            input("\n\nEnter To Exit");os._exit(0)
                except:
                    pass

    
    
if __name__ == '__main__':
    
    print(colored(f"{Design.banner}","red"))
    active = requests.get("https://api.ipify.org/?format=json").json()
    ip = active["ip"]
    scan = requests.get("https://pastebin.com/raw/jjeXSVhj").text
    try:
        by = re.search(rf'{ip} "(.*?)"',scan).group(1)
    except:
        pass
    if ip in scan:
        print(colored(f"\tWelcome Sir {by} To Daylight Swap \n\tBy Rayan Insta  @m1c1",Design.cyan))
        

    else:
        print(f"{Design.reda}{ip} This ip is not active")
        input()
        exit(0)


    
    s = swap()
    
    ctypes.windll.user32.MessageBoxW(0, f"Are You Ready?  ", f"Daylight", 0x1000)
    threading.Thread(target=s.request_per_sec).start()
    threading.Thread(target=s.LOOP).start()
    for i in range(s.Threads):
        threading.Thread(target=s.sent_edit_profile_Request).start()
        threading.Thread(target=s.sent_Faster_web_Request).start()
        threading.Thread(target=s.sent_set_username_REQUEST).start()
    
