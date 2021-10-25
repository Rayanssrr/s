import requests,uuid,random,re,ctypes,json,urllib,hashlib,hmac,urllib.parse,base64,os,string,time,colorama,autopy
from time import sleep
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
from threading import Thread,Lock
from termcolor import colored

colorama.init()











timestamp = str(int(time.time()))

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


uu = '83f2000a-4b95-4811-bc8d-0f3539ef07cf'


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
                    By {RoRo@m1c1}   
"""

os.system('mode con: cols=80 lines=27')
active = requests.get("https://api.ipify.org/?format=json").json()
ip = active["ip"]
scan = requests.get("https://pastebin.com/raw/miBm2ymP").text
if ip in scan:
    try:
        by = re.search(rf'{ip} "(.*?)"',scan).group(1)
    except:
        pass
    pass

else:
    print(f"ip {ip} Not Activet Plz Call @m1c1 in Instagram");input();exit(0)
    


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
class sessting:
    def __init__(self):
        pass
    def headers_login(self):
        headers = {}
        headers['User-Agent'] = self.UserAgent
        headers['Host'] = 'i.instagram.com'
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['accept-encoding'] = 'gzip, deflate'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        return headers
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
        return '{Host} 155.0.0.37.107 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(
            **DEVICE_SETTINTS)
    def generate_DeviceId(self , ID):
        volatile_ID = "12345"
        m = hashlib.md5()
        m.update(ID.encode('utf-8') + volatile_ID.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]


def inputc(NewLine,mark,color,text):
    if NewLine:
        NewLine = "\n"
    
    
    print(f"{NewLine}\r{Design.qube} {colored(text=f'{mark}',color=f'{color}')} {Design.qube2} {text} {colored(text='',color=Design.white)}",end='')



class login:
    def __init__(self):
        self.sesstings = sessting()
        self.coo = None
        self.token = None
        self.mid = None
        self.DeviceID = None
        self.sessionid = None
    
    
    def headers_login(self):
        headers = {}
        headers['User-Agent'] = self.sesstings.generateUSER_AGENT()
        headers['Host'] = 'i.instagram.com'
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['accept-encoding'] = 'gzip, deflate'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        return headers
        
        
        
        
    def checkpoint(self):
        info = requests.get(f"https://i.instagram.com/api/v1{self.req.json()['challenge']['api_path']}", headers=self.headers_login(), cookies=self.coo)
        step_data = info.json()["step_data"]
        if "phone_number" in step_data:
            try:
                phone = info.json()["step_data"]["phone_number"]
                print(f'[0] phone_number : {phone}')
            except:
                pass
        elif "email" in step_data:
            try:
                email = info.json()["step_data"]["email"]
                print(f'[1] email : {email}')
            except:
                pass

        else:
            print("unknown verification method")
            input()
            exit()
        return self.send_choice()
    def send_choice(self):
        choice = input('choice : ')
        data = {}
        data['choice'] = str(choice)
        data['_uuid'] = uu
        data['_uid'] = uu
        data['_csrftoken'] = 'massing'
        challnge = self.req.json()['challenge']['api_path']
        self.send = requests.post(f"https://i.instagram.com/api/v1{challnge}",headers=self.headers_login(), data=data, cookies=self.coo)
        contact_point = self.send.json()["step_data"]["contact_point"]
        print(f'code sent to : {contact_point}')
        return self.get_code()
    def get_code(self):
        try:
            code = input("code : ")
            data = {}
            data['security_code'] = str(code),
            data['_uuid'] = uu,
            data['_uid'] = uu,
            data['_csrftoken'] = 'massing'
            path = self.req.json()['challenge']['api_path']
            send_code = requests.post(f"https://i.instagram.com/api/v1{path}", headers=self.headers_login(), data=data, cookies=self.coo)
            if "logged_in_user" in send_code.text:
                print(f'[+] Login Successfully as @{self.username} press Enter');input()
                self.coo = self.req.cookies
                self.token = self.coo.get("csrftoken")
                self.mid = self.coo.get("mid")
                self.sessionid = self.coo.get("sessionid")
                print(self.sessionid)
                os.system("cls") or Design.clearConsle()
            else:
                regx_error = re.search(r'"message":"(.*?)",', send_code).group(1)
                print(regx_error)
                ask = input("Code is Not Work Do You Want Try Agin [Y/N] : ")
                if ask.lower() == "y":
                    sleep(1)
                    return self.get_code()
                else:
                    exit()
        except:
            print("accepted Done")
            return self.Login()

        
        
    def Login(self):
        self.username = input(f'[+] UserName? : ')
        self.DeviceID = self.sesstings.generate_DeviceId(self.username)
        self.passwordd = input(f'[+] Password? : ')
        data = {}
        data['guid'] = uu
        data['enc_password'] = f"#PWD_INSTAGRAM:0:{timestamp}:{self.passwordd}"
        data['username'] = self.username
        data['device_id'] = self.DeviceID
        data['login_attempt_count'] = '0'

        self.req = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=self.headers_login(), data=data)
        if "logged_in_user" in self.req.text:
            print(f'[+] Login Successfully as @{self.username} press Enter');input()
            self.coo = self.req.cookies
            self.token = self.coo.get("csrftoken")
            self.mid = self.coo.get("mid")
            self.sessionid = self.coo.get("sessionid")
            os.system("cls") or Design.clearConsle
        elif 'checkpoint_challenge_required' in self.req.text:
            self.coo = self.req.cookies
            self.token = self.coo.get("csrftoken")
            self.mid = self.coo.get("mid")
            self.sessionid = self.coo.get("sessionid")
            print("SCURE FOUND ")
            return self.checkpoint()
        else:
            try:
                regx_error = re.search(r'"message":"(.*?)",', self.req.text).group(1)
                print(regx_error)
            except:
                print(self.req.text)
            ask = input("Something has gone wrong Do You Want Try Agin [Y/N] : ")
            if ask.lower() == "y":
                sleep(1)
                os.system("cls")
                return self.login()
            else:
                input()
                exit()


class swap:
    def __init__(self) :
        Design.clearTermnal() or os.system("cls")
        self.login = login()
        self.REQ = requests.session()
        print(colored(Design.banner,"red"))
        
        try:
            self.sesstings = open("sesstings.txt","r").read()
            inputc(True,"+",Design.green,f"{Design.WHITE}Successfully loded {Design.GREEN}'sesstings.txt'")
        except:
            inputc(True,"-",Design.red,f"{Design.reda}Error loded Press Enter To Create 'sesstings.txt'\n");input()
            open("sesstings.txt","a").write('{"sesstings" : {\n\t"name": "#DayLight",\n\t"bio": "Maybe Rayan",\n\t"MSG": "Sucessfully Claimed",\n\t"Webhook": "Here",\n\t"url_imge": ""\n}}')
        self.json_sesstings = json.loads(self.sesstings)
        self.bio = self.json_sesstings["sesstings"]["bio"]
        self.Msg = self.json_sesstings["sesstings"]["MSG"]
        self.name = self.json_sesstings["sesstings"]["name"]
        self.Web_hook = self.json_sesstings["sesstings"]["Webhook"]
        self.url_imge = self.json_sesstings["sesstings"]["url_imge"]
        


        inputc(True,"?",Design.yellow,f"Do You want Login with Session {Design.reda}[Y/n]{Design.WHITE} : ");self.ask = input()
        inputc(False,"?",Design.red,f"Do You want Auto Sesstings {Design.reda}[Y/n]{Design.WHITE} : ");self.auto = input()
    

        if self.ask.__contains__("y"):
            inputc(False,"/",Design.red,f"Session : ");self.session = input()
        else:
            self.login.Login();self.session = self.login.sessionid
        self.user = None
        self.email = None
        self.run = True
        self.att = 0
        self.rl = 0
        self.Locks  = Lock()
        self.get_info()
        inputc(False,"?",Design.blue,f"Do You Want Check Block {Design.reda}[Y/n]{Design.WHITE} :  ");self.check = input()
        if self.check.__contains__("y"):
            self.check_block()
        inputc(False,"?",Design.green,"Target : ");self.Target = input()
        
        
        
        if self.auto.__contains__("y"):
            auto = random.randint(25,50)
            inputc(False,"+",Design.red,f"Threads = {auto} \n");print("\n")
            Thread(target=self.Print).start()
            autopy.alert.alert(f"Are you Ready?","DayLight Swap")
            for i in range(auto):
                Thread(target=self.swapper).start()
        if self.auto.__contains__("n"):
            inputc(False,"\\\\",Design.red,f"If Not Use Auto Sesstings {Design.reda}(Max Threads = 75){Design.WHITE}\n")
            inputc(False,"?",Design.red,"Threads : ");self.Threads = int(input())
            autopy.alert.alert(f"Are you Ready?","DayLight Swap")
            Thread(target=self.Print).start()
            for i in range(self.Threads):
                Thread(target=self.swapper).start()


        
    def headers_Api(self):
        headers = {}
        headers["Connection"] = "close"
        headers["Accept"] = "*/*"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["Cookie2"] = "$Version=1"
        headers["Accept-Language"] = "en-US"
        headers["User-Agent"] = "Instagram 152.0.0.1.60 Android"
        return headers
    def Print(self):
        while self.run:
            for q in ["|","/","-","\\","|","/","-"]:
                print(f"\r[ {Design.GREEN}{q}{Design.WHITE} ] Attempt : {self.att} / Rate_Limit : {self.rl}",end="",flush=True)
    def get_info(self):
        get = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers=self.headers_Api(),cookies={"sessionid":self.session}).text
        try:
            self.user = re.search(r'"username":"(.*?)",',get).group(1)
            self.email = re.search(r'"email":"(.*?)",',get).group(1)
            inputc(False,"+",Design.green,f"Login sucssfully as {self.user}");input()
            os.system("cls")  
            Design.clearTermnal()
            print(colored(Design.banner,"red"))
        except:
            inputc(True,"-",Design.red,f"Bad Seesion");input();exit(0)
    def check_block(self):
        data = {}
        data["_uid"] = f"47641699268"
        data["device_id"] = "android-d595db3f5c276071"
        data["_uuid"]= str(uuid.uuid4()),
        data["external_url"] = ""
        data['_csrftoken'] = 'massing'
        data["phone_number"] = ""
        data["username"] = str(self.user) + ".checkblock"
        data["first_name"] = ""
        data["biograph"] = ""
        data["email"] = str(self.email)
        response = self.REQ.post("https://i.instagram.com/api/v1/accounts/edit_profile/",data=data,headers=self.headers_Api(),cookies={"sessionid":self.session}).text
        if response.__contains__('"status":"ok"'):
            inputc(True,"+",Design.green,f"{Design.GREEN} The Account Is work \n")
        else:
            inputc(True,"-",Design.red,f"{Design.red} The Account Is Not Work\n")

    def sucssfully_swap(self):
        self.run = False
        print("\n");inputc(True,"$",Design.red,f"{self.Msg} {Design.reda}@{self.Target}\n")
        self.REQ.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{self.bio}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + self.session})
        self.REQ.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/",data={"first_name":f"{self.name}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.session})
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/899788444966985730/Uy9-NNXthTA3ncdGqNSTfteDFZYcWASapaKaJObTMr_fuIxJ7dIkzcLtDMT8OOURuJIr')
        embed = DiscordEmbed(title=f'Swpped @{self.Target}\nSwapped By {by}', color=242424)
        embed.set_author(name="Daylight")
        embed.set_footer(icon_url=f"{random.choice(imge)}")
        embed.set_thumbnail(url=f"{random.choice(imge)}")
        webhook.add_embed(embed)
        webhook.execute()
        try:
            webhook = DiscordWebhook(url=f'{self.Web_hook}')
            embed = DiscordEmbed(title=f'Swpped @{self.Target}\nSwapped By {by}', color=242424)
            embed.set_author(name=f"{self.name}")
            embed.set_footer(icon_url=f"{self.url_imge}")
            embed.set_thumbnail(url=f"{self.url_imge}")
            webhook.add_embed(embed)
            webhook.execute()
            
        except:
            pass
        autopy.alert.alert(f"{self.Msg} : @{self.Target}",f"{self.name}");os._exit(0)
    def Edit_Profile(self):
        data = {}
        data["_uid"] = f"47641699268"
        data["device_id"] = "android-d595db3f5c276071"
        data["_uuid"]= str(uuid.uuid4()),
        data["external_url"] = ""
        data['_csrftoken'] = 'massing'
        data["phone_number"] = ""
        data["username"] = str(self.Target)
        data["first_name"] = ""
        data["biograph"] = ""
        data["email"] = str(self.email)
        response = self.REQ.post("https://i.instagram.com/api/v1/accounts/edit_profile/",data=data,headers=self.headers_Api(),cookies={"sessionid":self.session}).text
        if response.__contains__('"status":"ok"'):
            with self.Locks:
                return self.sucssfully_swap()
        elif response.__contains__('username'):
            self.att +=1
        else:
            self.rl +=1
    def set_username(self):
        response = self.REQ.post("https://i.instagram.com/api/v1/accounts/set_username/",data={"username":self.Target},headers=self.headers_Api(),cookies={"sessionid":self.session}).text
        if response.__contains__('"status":"ok"'):
            with self.Locks:
                return self.sucssfully_swap()
        elif response.__contains__('username'):
            self.att +=1
        else:
            self.rl +=1
    def Edit_web(self):
        data = {}
        data['first_name'] = ""
        data['email'] = str(self.email)
        data["username"] = str(self.Target)
        data['phone_number'] = ''
        data['biography'] = ''
        data['external_url'] = ""
        data['chaining_enabled'] = ''
        response = self.REQ.post("https://www.instagram.com/accounts/edit/", data=data, headers={
                                'accept':'*/*', 
                                'accept-encoding':'gzip, deflate, br', 
                                'accept-language':'ar,en-US;q=0.9,en;q=0.8', 
                                'content-length':'135', 
                                'content-type':'application/x-www-form-urlencoded', 
                                'cookie':f'ig_did=; ig_nrcb=1; mid=YNt8YQALAAHpMfzMX5-nq-UvVpPv; csrftoken=missing; ds_user_id={RandomString(3)}-@-{RandomStringUpper(2)}#;sessionid={self.session}; rur="VLL"', 
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
        if response.text.__contains__('"status":"ok"'):
            with self.Locks:
                return self.sucssfully_swap()
        elif response.status_code == 400:
                self.att +=1
        else:
            self.rl +=1


    
    
    def merg_api(self):
        swapple = [self.set_username(),self.Edit_Profile(),self.Edit_web()]
        return random.choice(swapple)



    def swapper(self):
        while self.run:
            self.merg_api()




    

         

        
swap()
