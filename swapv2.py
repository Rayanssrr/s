try:
    import random, os, socket, requests, threading, ctypes
    from time import sleep
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
WHITE = '\x1b[1;37;40m'
YELLOW = '\x1b[1;33;40m'
RED = '\x1b[1;31;40m'
s1 = '\x1b[31m[]\x1b[40m'
plus = '\x1b[32m+\x1b[39m'
mains = '\x1b[36m-\x1b[31m'
SL = '\x1b[35m/\x1b[39m'
INPUT = f"\x1b[39m[{plus}]\x1b[39m"
INPUT1 = f"\x1b[39m[{SL}]\x1b[39m"
INPUT2 = f"\x1b[31m[{mains}]\x1b[39m"
blue = '\x1b[36m\x1b[40m'
red = '\x1b[31m\x1b[40m'
GREEN = '\x1b[32m\x1b[40m'
SUCCESS = '\x1b[31m Successfulyy moved \x1b[31m'
Run = '\x1b[36m Started Running...\x1b[31m'
skip = '\x1b[31m (defult Thread = 300) \x1b[31m'
clearConsle = lambda: os.system('cls')

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
g = requests.get('https://pastebin.com/kEdfngFt')
if ip in g.text:
    print(f'{INPUT}{GREEN} Welcome ')
    sleep(0.6)
else:
    print(ip)
    print(f'{INPUT2}{red} Ip not active ')
    sleep(23)
    os._exit(0)
print("\n")
print("\n")
print("\n")
print("\n")
ban = """""""""

                                ,.   .      .   
                               / |   |  ,-. |-. 
                              /~~|-. |  | | | | 
                            ,'   `-' `' |-' ' ' 
                                        |       
                                        '       


"""""""""
by = input(f"{INPUT}Swapped By:")
clearConsle()
print(red + ban)
design = open("design.txt", "r").read()
title = design.split("\n")[0]
msg = design.split("\n")[1]


images = [

    "https://media1.tenor.com/images/b94935d6d92eeadb6d1d66bccad31abe/tenor.gif?itemid=21002889",
    "https://media1.tenor.com/images/035ce3059d332b083b19c6554effa529/tenor.gif?itemid=17350123",
    "https://media1.tenor.com/images/4f6c21aadc93f859c406bc112ae19d01/tenor.gif?itemid=17599933",
    "https://media1.tenor.com/images/6fe425c1c6b2e11a425aedb0697a6826/tenor.gif?itemid=20653094",
    "https://media1.tenor.com/images/fca842af645452d50ccc48c6b714a9f1/tenor.gif?itemid=12793353",
    "https://media1.tenor.com/images/77ec220a957c415c3f81ec2e9312d5ba/tenor.gif?itemid=10666007",
]
im = random.choice(images)


class normalswap():
    def __init__(self):
        self.search = input(f"{INPUT1}{GREEN} username : ")
        self.found = open(f"{self.search}.txt", "r").read()
        self._csrftoken = self.found.split("\n")[0]
        self.session = self.found.split("\n")[1]
        self.ds = self.found.split("\n")[2]
        self.mid = self.found.split("\n")[3]
        self.fuc = [self.get_info()]
        self.Target = input(f'{INPUT1}{red} Target : ')
        self.threads = int(input(f"{INPUT}{blue} Enter Threads {skip}: "))
        #input(f"{INPUT}{red} Are Yoy Ready?")
        ctypes.windll.user32.MessageBoxW(0, f"Are You Ready ? \nTarget: @{self.Target} \nThread : {self.threads}  ","AlPHA SWAP", 0x1000)
        print(f"{INPUT}{Run}")
        self.attempt = 0
        self.rl = 0
        self.Rs = 0
        self.email = None
        self.pro = "Programmed By @Cokepoke_"
        self.run = True
        self.controll = threading.Event()
        self.locks = threading.Lock()
        self.num = None
        self.future_session = FuturesSession(max_workers=self.threads*4)
        threading.Thread(target=self.Requestpersec).start()
        self.thredas = []
        for i in range(int(self.threads)):
            t = threading.Thread(target=self.runn)
            t.setDaemon = True
            t.start()
            self.controll.set()
            self.thredas.append(t)
        for t in self.thredas:
            t.join()

    def get_info(self):
        url = "https://i.instagram.com/api/v1/accounts/current_user/?edit=true"
        try:
            self.r = requests.get(url, headers={
                "User-Agent": "Instagram 187.0.0.32.120 Android (25/7.1.2; 240dpi; 1280x720; Asus; ASUS_Z01QD; ASUS_Z01QD; intel; ar_EG; 289692202)"},
                                  cookies={"sessionid": f"{self.session}"}).json()
            self.user = self.r['user']['username']
            self.email = self.r['user']['email']
            input(f"{INPUT}{blue} Login Successfly as (@{self.user}) Click Enter to continue")
            # clearConsle()
        except Exception as a:
            # print(a)
            # print(self.user)
            input(f"{INPUT2}{red} Error Session id")
            exit()

    def data(self):
        data = {
            "external_url": "",
            "phone_number": "",
            "username": f"{self.Target}",
            "first_name": "",
            "_uid": "47907130936",
            "device_id": "android-1f7220131504938e",
            "biography": "",
            "_uuid": "11923c4e-5663-4757-b9f3-0b69396a6c4b",
            "email": f"{self.email}"
        }
        return data

    def Requestpersec(self):
        self.per = self.attempt
        while 1:
            sleep(1)
            self.Rs = self.attempt - self.per
            print(f"\r{INPUT1}{blue} Attempts : {self.attempt} / rl : {self.rl} / Rs : {self.Rs}", end="")

    def runn(self):
        while self.run:
            api_list = [
                'https://i.instagram.com/api/v1/accounts/set_username/',
                'https://i.instagram.com/api/v1/accounts/edit_profile/'
            ]
            api = random.choice(api_list)
            future = []
            for i in range(self.threads):
                futures = self.future_session.post('https://i.instagram.com/api/v1/accounts/edit_profile/',data=self.data(), headers={"User-Agent": "Instagram 187.0.0.32.120 Android (25/7.1.2; 240dpi; 1280x720; Asus; ASUS_Z01QD; ASUS_Z01QD; intel; ar_EG; 289692202)"},cookies={"csrftoken":self._csrftoken,"shbts":"1623419447.990988","sessionid":self.session,"ds_user_id":self.ds,"mid":self.mid})
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as resp:
                        print(resp.text)
                        if resp.status_code == 200:
                            with print_lock:
                                requests.post('https://i.instagram.com/api/v1/accounts/set_biography/',data={"raw_text": f"#AlphaTeam\nSwapped By {by}"}, headers={"User-Agent": "Instagram 187.0.0.32.120 Android (25/7.1.2; 240dpi; 1280x720; Asus; ASUS_Z01QD; ASUS_Z01QD; intel; ar_EG; 289692202)"},cookies={"sessionid": self.session})
                                webhook = DiscordWebhook(
                                    url="https://discord.com/api/webhooks/851258037964111942/44KPehb5OIleohmn3fLTuE-EusEsICqTMCFQN-Snkm7BR_mkdYIbU7W6N5t3tpX0r_5o")
                                embed = DiscordEmbed(
                                    title=f'#AlphaSwap\nSwapped  @{self.Target}\nBy {by} | Attempts  {self.attempt}\nAlphaTeam | Rs  {self.Rs} \nCoded By | @Cokepokes_',
                                    color=000000)
                                embed.set_thumbnail(url=im)
                                embed.set_footer(text="Date swap")
                                embed.set_timestamp()
                                webhook.add_embed(embed)
                                response = webhook.execute()
                                print(f"\n{INPUT}{SUCCESS}:@{self.Target}")
                                ctypes.windll.user32.MessageBoxW(0, f"{msg} : @{self.Target}  ", f"{title}", 0x1000)
                                os._exit(0)
                        elif resp.status_code == 400:
                            self.attempt += 1
                            with self.locks:
                                print(
                                    f"\r{INPUT1}{blue} Attempts : {self.attempt} / rl : {self.rl} / Rs : {self.Rs}",
                                    end="")
                        else:
                            self.rl += 1
                            with self.locks:
                                print(f"\r{INPUT1}{blue} Attempts : {self.attempt} / rl : {self.rl} / Rs : {self.Rs}",
                                      end="")


def ss():
    normalswap()


ss()
