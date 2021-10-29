import requests,uuid,random,re,ctypes,json,urllib,hashlib,hmac,urllib.parse,base64,os,string,time,colorama,autopy
from time import sleep
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
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
"""


active = requests.get("https://api.ipify.org/?format=json").json()
ip = active["ip"]
scan = requests.get("https://pastebin.com/raw/kEdfngFt").text
if ip in scan:
    try:
        by = re.search(rf'{ip} "(.*?)"',scan).group(1)
    except:
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


def inputc(Frist_NewLine,mark,color,text):
    if Frist_NewLine:
        Frist_NewLine = "\n"
    
    
    print(f"{Frist_NewLine}\r{Design.qube} {colored(text=f'{mark}',color=f'{color}')} {Design.qube2} {text} {colored(text='',color=Design.white)}",end='')



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
                inputc(False,"0",Design.green,f"phone_number : {phone}\n")
                
            except:
                pass
        elif "email" in step_data:
            try:
                email = info.json()["step_data"]["email"]
                inputc(False,"1",Design.green,f"Email : {email}\n")
            except:
                pass

        else:
            inputc(False,"?",Design.red,f"unknown verification method\n")
            input()
            exit()
        return self.send_choice()
    def send_choice(self):
        inputc(False,"/",Design.red,f"Choice : ");choice = input()
        data = {}
        data['choice'] = str(choice)
        data['_uuid'] = uu
        data['_uid'] = uu
        data['_csrftoken'] = 'massing'
        challnge = self.req.json()['challenge']['api_path']
        self.send = requests.post(f"https://i.instagram.com/api/v1{challnge}",headers=self.headers_login(), data=data, cookies=self.coo)
        contact_point = self.send.json()["step_data"]["contact_point"]
        inputc(False,"+",Design.green,f"Code sent to : {contact_point}\n")
        return self.get_code()
    def get_code(self):
        try:
            inputc(False,"/",Design.red,f"Code : ");code = input()
            data = {}
            data['security_code'] = str(code),
            data['_uuid'] = uu,
            data['_uid'] = uu,
            data['_csrftoken'] = 'massing'
            path = self.req.json()['challenge']['api_path']
            self.send_code = requests.post(f"https://i.instagram.com/api/v1{path}", headers=self.headers_login(), data=data, cookies=self.coo)
            if "logged_in_user" in self.send_code.text:
                inputc(False,"+",Design.green,"Sucssfully Loged In Press Enter ",True)
                self.coo = self.send_code.cookies
                self.token = self.coo.get("csrftoken")
                self.mid = self.coo.get("mid")
                self.sessionid = self.coo.get("sessionid")
                #print(self.sessionid)
                os.system("cls") or Design.clearConsle()
                print(colored(Design.banner,"red"))
            else:
                regx_error = re.search(r'"message":"(.*?)",', self.send_code).group(1)
                inputc(False,"-",Design.red,f"{regx_error}")
                inputc(False,"?",Design.red,f"Do You Want Try Agin {Design.reda}[Y/N]{Design.WHITE} : ");ask = input()
                if ask.lower() == "y":
                    sleep(1)
                    return self.get_code()
                else:
                    exit()
        except:
            #print("accepted Done")
            inputc(False,"+",Design.green,f"Accepted Done\n")
            return self.Login()

        
    def Login(self):
        inputc(False,"/",Design.green,f"UserName? : ");self.username = input()
        self.DeviceID = self.sesstings.generate_DeviceId(self.username)
        inputc(False,"/",Design.green,f"Password? :  ");self.passwordd = input()
        data = {}
        data['guid'] = uu
        data['enc_password'] = f"#PWD_INSTAGRAM:0:{timestamp}:{self.passwordd}"
        data['username'] = self.username
        data['device_id'] = self.DeviceID
        data['login_attempt_count'] = '0'

        self.req = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=self.headers_login(), data=data)
        if "logged_in_user" in self.req.text:
            inputc(False,"+",Design.green,"Sucssfully Loged In Press Enter\n")
            input()
            self.coo = self.req.cookies
            self.token = self.coo.get("csrftoken")
            self.mid = self.coo.get("mid")
            self.sessionid = self.coo.get("sessionid")
            os.system("cls") or Design.clearConsle()
            print(colored(Design.banner,"red"))
        elif 'checkpoint_challenge_required' in self.req.text:
            self.coo = self.req.cookies
            self.token = self.coo.get("csrftoken")
            self.mid = self.coo.get("mid")
            self.sessionid = self.coo.get("sessionid")
            inputc(False,"/",Design.red,f"SCURE FOUND\n")
            return self.checkpoint()
        else:
            try:
                regx_error = re.search(r'"message":"(.*?)",', self.req.text).group(1)
                inputc(False,"-",Design.red,f"{regx_error}\n")
            except:
                pass
            inputc(False,"?",Design.red,f"Do You Want Try Agin {Design.reda}[Y/N]{Design.WHITE} : ");ask = input()
            if ask.lower() == "y":
                sleep(1)
                return self.Login()
            else:
                input()
                exit()



class swap:
    def __init__(self) :
        Design.clearTermnal() or os.system("cls")
        self.login = login()
        self.REQ = requests.session()
        self.sesstings1 = sessting()
        self.cookies = None
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
        #self.future_session = FuturesSession(max_workers=self.threads * 5)
        
        inputc(True,"?",Design.yellow,f"Do You want Login with Session {Design.reda}[Y/n]{Design.WHITE} : ");self.ask = input()
    

        if self.ask.__contains__("y"):
            inputc(False,"/",Design.red,f"Session : ");self.session = input()
        else:
            self.login.Login();self.session = self.login.sessionid
        self.user = None
        self.email = None
        self.run = True
        self.att = 0
        self.rl = 0
        self.Rs = 0 
        self.locks  = Lock()
        self.update_consent()
        inputc(False,"?",Design.blue,f"Do You Want Check Block {Design.reda}[Y/n]{Design.WHITE} :  ");self.check = input()
        if self.check.__contains__("y"):
            self.check_block()
        inputc(False,"?",Design.green,"Target : ");self.Target = input()
        
        
        #inputc(False,"\\\\",Design.red,f"If Not Use Auto Sesstings {Design.reda}(Max Threads = 75){Design.WHITE}\n")
        inputc(False,"?",Design.red,"Threads : ");self.Threads = int(input())
        self.future_session = FuturesSession(max_workers=self.Threads * 4)
        autopy.alert.alert(f"Are you Ready?","DayLight Swap")
        Thread(target=self.Print).start()
        Thread(target=self.request_in_one_sec).start()
        for i in range(self.Threads):
            Thread(target=self.swapper).start()


        
    def headers_Api(self):
        headers = {}
        headers["Connection"] = "close"
        headers["Accept"] = "*/*"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["Cookie2"] = "$Version=1"
        headers["Accept-Language"] = "en-US"
        headers["User-Agent"] = self.sesstings1.generateUSER_AGENT()
        return headers
    def Print(self):
        while self.run:
            for q in ["|","/","-","\\","|","/","-"]:
                sleep(0.9)
                print(f"\r[ {Design.GREEN}{q}{Design.WHITE} ] Attempt : {self.att} / Rate_Limit : {self.rl} / R/s {self.Rs}",end="",flush=True)

    def update_consent(self):
        response = requests.post("https://i.instagram.com/api/v1/consent/update_dob/", headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US",
                "User-Agent": self.sesstings1.generateUSER_AGENT(),
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-IG-Capabilities": "3brTvw==",
                "X-IG-Connection-Type": "WIFI"},data='{"current_screen_key\":\"dob\",\"day\":\"1\",\"year\":\"1998\",\"month\":\"1\""}',cookies={"sessionid": self.session}).text



        if response.__contains__('"status":"ok"'):
            inputc(False,"+",Design.green,f"Successfully updated consent to GDPR\n")
            return self.get_info()
        else:
            inputc(True,"-",Design.red,f"Failed to consent to GDPR, use an IP that is not from Europe\n")
            input(),exit(0)
 
    def get_info(self):
        headers = {}
        headers["Connection"] = "keep-alive"
        headers["Accept"] = "*/*"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["Accept-Language"] = "en-US"
        headers["User-Agent"] = self.sesstings1.generateUSER_AGENT()

        get = self.REQ.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers=headers,cookies={"sessionid":self.session}).text
        self.user = re.search(r'"username":"(.*?)",',get).group(1)
        self.email = re.search(r'"email":"(.*?)",',get).group(1)
        #print(get)
        inputc(False,"+",Design.green,f"Username : {self.user}\n");inputc(False,"+",Design.green,f"Email : {self.email}");input()
        os.system("cls")  
        Design.clearTermnal()
        print(colored(Design.banner,"red"))
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
            inputc(True,"-",Design.red,f"{Design.red} The Account Is Not Work\n");input();exit(0)

    def sucssfully_swap(self):
        self.run = False
        sleep(1)
        print(f"\n\n{Design.WHITE}[ {Design.reda}${Design.WHITE} ] {self.Msg}  {Design.blueq}@{self.Target}{Design.WHITE} After {Design.reda}{self.att}{Design.WHITE} Attempts\n\n\n")
        #print("\n");inputc(True,"$",Design.red,f"{self.Msg} {Design.reda}@{self.Target}\n\n\n\n");print("\n")
        self.REQ.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{self.bio}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + self.session})
        self.REQ.post("https://i.instagram.com/api/v1/accounts/set_phone_and_name/",data={"first_name":f"{self.name}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.session})
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/899788444966985730/Uy9-NNXthTA3ncdGqNSTfteDFZYcWASapaKaJObTMr_fuIxJ7dIkzcLtDMT8OOURuJIr')
        embed = DiscordEmbed(title=f'Swpped @{self.Target}\nSwapped By {by}', color=242424)
        embed.set_author(name="Daylight")
        embed.set_footer(text=f'Attempts : {self.att} | R/s : {self.Rs}',icon_url=f"{random.choice(imge)}")
        embed.set_thumbnail(url=f"{random.choice(imge)}")
        webhook.add_embed(embed)
        webhook.execute()
        try:
            webhook = DiscordWebhook(url=f'{self.Web_hook}')
            embed = DiscordEmbed(title=f'Swpped @{self.Target}\nSwapped By {by}', color=242424)
            embed.set_author(name=f"{self.name}")
            embed.set_footer(text=f'Attempts : {self.att} | R/s : {self.Rs}',icon_url=f"{random.choice(imge)}")
            embed.set_thumbnail(url=f"{self.url_imge}")
            webhook.add_embed(embed)
            webhook.execute()
        except:
            pass
        sleep(2)
        autopy.alert.alert(f"{self.Msg} : @{self.Target}",f"{self.name}");os._exit(0)
    def request_in_one_sec(self):
        while self.run:
            befor = self.att
            sleep(1)
            self.Rs = self.att - befor
    def Data(self):
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
        return data


    def swapper(self):
        while self.run:
            future = []
            for i in range(self.Threads):
                futures = self.future_session.post(random.choice(["https://i.instagram.com/api/v1/accounts/edit_profile/","https://i.instagram.com/api/v1/accounts/set_username/"]), data=self.Data(), headers={"User-Agent": "Instagram 187.0.0.32.120 Android (25/7.1.2; 240dpi; 1280x720; Asus; ASUS_Z01QD; ASUS_Z01QD; intel; ar_EG; 289692202)"},cookies={"sessionid": self.session})
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as resp:
                        if resp.status_code == 200:
                            with self.locks:
                                return self.sucssfully_swap()
                        if resp.status_code == 400:
                            self.att +=1
                            #os.system(f"title #Attempts : {self.att} / #Rl : {self.rl} / R/S : {self.Rs}")
                        if resp.status_code == 429:
                            self.rl += 1
                                    #os.system(f"title #Attempts : {self.att} / #Rl : {self.rl} / R/S : {self.Rs}")
        # response = self.REQ.post("https://i.instagram.com/api/v1/accounts/edit_profile/",data=data,headers=self.headers_Api(),cookies={"sessionid":self.session}).text
        # if response.__contains__('"status":"ok"'):
        #     with self.Locks:
        #         return self.sucssfully_swap()
        # elif response.__contains__('username'):
        #     self.att +=1
        # else:
        #     self.rl +=1
    
    





    

         

        
swap()
