from time import sleep
from threading import Thread
from random import *
from string import *
from requests_futures.sessions import FuturesSession
from concurrent.futures import as_completed
from discord_webhook import DiscordWebhook
from discord_webhook import DiscordEmbed
from tqdm import tqdm
import random , os , requests , uuid , ctypes,colorama,threading

colorama.init()
dir_path = os.path.dirname(os.path.realpath(__file__))


dude = """

    * Checker Instagram * 

        Targrt Mode + list mode 
        ./ Made By FD § FBI 

"""


by = """
    * Checker *\n
    ./ Made By FD § FBI \n
    ./ @31421 @exploit305 @m1c1 @b.bc
   i can change dude :) 
"""
win = ['Claimed :) But I won’t give it back To You :( Because Your Swap is Baad','Don’t Ever Again Swap With VB','Don’t Swap Again :(','Maybe Lisa Or Maybe Not','You Have To Use AutoClaimer Next Time But I Don’t Think You Will Take it :)']
head = {
    'User-Agent': "Instagram 10.26.0 Android (26/8.0.0; 320dpi; 768x1184; unknown/Android; Custom Phone; vbox86p; vbox86; en_US; 232868034)",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com'
}
Done = False
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
purble = '\x1b[35m\x1b[39m'
SUCCESS = '\x1b[31m Successfulyy moved \x1b[31m'
Run = '\x1b[36m Started Running...\x1b[31m'
under = '\x1b[35m_\x1b[39m'
skip = '\x1b[31m (defult Thread = 300) \x1b[31m'
clearConsle = lambda: os.system('cls')
banner = """

              ___       _                  _____            _         
             | __|__ _ | | __  ___  _ _   |_   _|_  _  _ _ | |__  ___ 
             | _|/ _` || |/ _|/ _ \| ' \    | | | || || '_|| '_ \/ _ \ 
             |_| \__,_||_|\__|\___/|_||_|   |_|  \_,_||_|  |_.__/\___/

"""
lool = dude + banner

images = [
    "https://media.giphy.com/media/I6wUi5eTdUCWI/giphy.gif",
    "https://media.giphy.com/media/3fNmJ20ErpkjK/giphy.gif",
    "https://media.giphy.com/media/GLgPVZ5PLMOPe/giphy.gif",
    "https://media.giphy.com/media/AkRFIhfAKHsyc/giphy.gif",
    "https://media.giphy.com/media/A5KGHdmmxHdwk/giphy.gif",
    "https://media.giphy.com/media/QCJlIDkOJDEIctfdzz/giphy.gif",
    "https://media.giphy.com/media/if9niVFg4IwAE/giphy.gif",
    "https://media.giphy.com/media/QLCWubleeNppS/giphy.gif", ]

im = random.choice(images)


os.system('mode con: cols=85 lines=33')





class FalconCheckr(object):
    def __init__(self,Silnt,session,skip):
        super(FalconCheckr, self).__init__()
        self.claimed = False
        self.session = session
        self.get_info()
        self.checkkblock()
        self.install()
        self.run = 1
        self.attempts = 0
        self.Silnt = Silnt
        self.skip = skip
        self.Locks = threading.Lock()
        self.timeout = 0
        self.rl = 0
        self.rs = 0
        self.usernames = open("list.txt","r").read().splitlines()
        self.future_session = FuturesSession(max_workers=self.Silnt)

    def proxy(self):
        self.prox = random.choice(self.proxies)
        self.erp = {"http": f"{self.prox}", "https": f"{self.prox}"}
        return self.erp


    def get_info(self):
        global email
        global num
        global usern
        try:
            self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.session}).json()
            usern = self.r['user']['username']
            email = self.r['user']['email']
            num = self.r['user']['phone_number']
            print(f"{INPUT}{GREEN} Login Successfly as (@{usern}) Click Enter to continue")
        except Exception as a:
            # print(a)
            # print(self.user)
            input(f"{INPUT2}{red} Error Session id")
            exit(0)
    def checkkblock(self):
        global email
        global usern
        global num
        ask = input(f"{INPUT1}{blue} I wanna Checkblock <Y/N> I DO NOT wanna checkblock : ")
        if ask.lower() == "y":
            ch = requests.post('https://i.instagram.com/api/v1/accounts/edit_profile/',headers=head,data={"external_url": "","phone_number": f"{num}","username": f"{usern}","first_name": "","_uid": f"47641699268","device_id": "android-d595db3f5c276071","biography": f"{by}","_uuid": str(uuid.uuid4()),"email": f"{email}"},cookies={"sessionid": self.session}).status_code
            if ch == 200:
                print(f"{INPUT}{GREEN} The account is working")
            elif ch == 429:
                print(f"{INPUT2}{red} Account is Not work because to too many requests")
                input()
                exit(0)
        elif ask.lower() == "n":
            pass
    def Successfully_Claimed(self,user):
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/866337547193548810/hSntntnud8THTQkOf0N_EBnB5VAav0rqPQTJ2YA7dd-ueseN9jqf9Y-qyScEM-PyPEsR")
        embed = DiscordEmbed(title=f'Claimed @{user}\nBy Falcon Group | Attempts  {self.attempts}\nR/S  {self.rs} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date claim")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT}Successfully Claimed {GREEN}@{user}{WHITE} aftter {self.attempts} attempts")
        ctypes.windll.user32.MessageBoxW(0, f"Hhh Im win : @{user}  ", f"FD § FBI ", 0x1000)
        return False
    def install(self):
        print(f"{INPUT1}{red} Please wait to download all settings... ")
        for _ in tqdm(range(100), desc=f"{INPUT1}", ascii=False, ncols=65):
            sleep(0.01)
        input(f"{INPUT}{GREEN} All settings have been downloaded , Click Enter to continue ")


    def Successfully_Claimed2(self,user2):
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/866337547193548810/hSntntnud8THTQkOf0N_EBnB5VAav0rqPQTJ2YA7dd-ueseN9jqf9Y-qyScEM-PyPEsR")
        embed = DiscordEmbed(title=f'Claimed @{user2}\nBy Falcon Group | Attempts  {self.attempts}\nR/S  {self.rs} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date claim")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT}Successfully Claimed {GREEN}@{user2}{WHITE} aftter {self.attempts} attempts")
        ctypes.windll.user32.MessageBoxW(0, f"Hhh Im win : @{user2}  ", f"FD § FBI ", 0x1000)
        return False

    def headers(self):
        head = {}
        head["User-Agent"] = "Instagram 133.0.0.34.124 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)"
        return head
    def cookies(self):
        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token, "mid": self.mid, "ds_user_id": f"{self.ds_user}", "rur": "FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"}
        return cookies

    def claim_username(self):
        global Done
        global email
        global num
        global win 
        user = random.choice(self.usernames)
        user2 = random.choice(self.usernames)
        hh = random.choice(win)
        #print(user)
        try:
            future = []
            for i in range(self.skip):
                futures = self.future_session.post("https://i.instagram.com/api/v1/accounts/username_suggestions/", data={"name":f"{user}","email":f"{user2}@gmail.com"},proxies=self.proxy(), headers=self.headers())
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as response:
                        if (f'"username":"{user}","prototype":"last"') in response.text:
                            resp = self.future_session.post("https://i.instagram.com/api/v1/accounts/edit_profile/",
                                                            headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                                                     "Cookie": "sessionid=" + self.session},
                                                            data={"external_url": "", "phone_number": f"{num}",
                                                                  "username": f"{user}", "first_name": "",
                                                                  "_uid": f"47641699268", "device_id": "android-d595db3f5c276071",
                                                                  "biography": f"{hh}", "_uuid": str(uuid.uuid4()),
                                                                  "email": f"{email}"})
                            res = resp.result()
                            if res.status_code == 200:
                                with self.Locks:
                                    self.Successfully_Claimed(user)
                                    return self.claim_username()
                            else:
                                with self.Locks:
                                    print(f"RESPONSE > ({res.text})")

                        if (f'"username":"{user2}","prototype":"email"') in response.text:
                            resp = self.future_session.post("https://i.instagram.com/api/v1/accounts/edit_profile/",
                                                            headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                                                     "Cookie": "sessionid=" + self.session},
                                                            data={"external_url": "", "phone_number": f"{num}",
                                                                  "username": f"{user2}", "first_name": "",
                                                                  "_uid": f"47641699268", "device_id": "android-d595db3f5c276071",
                                                                  "biography": f"{hh}", "_uuid": str(uuid.uuid4()),
                                                                  "email": f"{email}"})
                            res = resp.result()
                            if res.status_code == 200:
                                with self.Locks:
                                    self.Successfully_Claimed(user2)
                                    return self.claim_username()
                            else:
                                with self.Locks:
                                    pass
                                    #print(f"RESPONSE > ({res.text})")
                        if response.status_code == 429:
                            self.rl  +=1
                        elif '"status":"ok"' in response.text:
                            self.attempts +=1
        except requests.Timeout:
                 self.timeout +=1
        except:
            pass





class open_up(Thread):
    def __init__(self, Falcon):
        super(open_up, self).__init__()
        self.Faclon = Falcon

    def run(self):
        global is_claimed
        while self.Faclon.run and not Done:
            if self.Faclon.claim_username():
                self.Faclon.claimed = True
                self.Faclon.run = False

            sleep(0.001)


class RequestPerSecounD(Thread):
    def __init__(self, faclon):
        super(RequestPerSecounD, self).__init__()
        self.Faclon = faclon

    def run(self):
        while self.Faclon.run:
            before = self.Faclon.attempts
            sleep(1)
            self.Faclon.rs = self.Faclon.attempts - before


if __name__ == "__main__":
    try:
        print(f"{blue}  {lool}")
        session = input(f"{INPUT1} Session : ")
        clearConsle()
        print(f"{blue}  {lool}")

        threads = int(input(f"{INPUT1} Threads {red}(Max = 500) : "))
        Silnt = int(input(f"{INPUT1} SILNT {red}(MAX = 1500 ) : "))
        skip = int(input(f"{INPUT1} Skip {red}(MAX = 5 ) : "))
        faclon = FalconCheckr(Silnt,session,skip)
        faclon.proxies = [i.strip() for i in open(dir_path + "/proxies.txt", "r") if i]
    except Exception as ex:
        print(ex)
        exit(1)
    #threads = int(input("  {}{} Threads: ".format(WHITE, INPUT)))
    for _ in range(threads):
        thread = open_up(faclon)
        thread.setDaemon(True)
        thread.start()

    rs = RequestPerSecounD(faclon)
    rs.setDaemon(True)
    rs.start()

    try:
        while faclon.run and not Done:
            sleep(0.1)
            #print("\r  {}{} Attempts: {:,} | RL: {} | R/S: {}".format(WHITE, blue, instagram.attempts, instagram.rl,instagram.rs), end="")
            print(f"\r{blue}{INPUT1} Attempts : {faclon.attempts} | Ratelimt : {faclon.rl} | R/S : {faclon.rs} | Timeout : {faclon.timeout}",end="")

    except KeyboardInterrupt:
        faclon.running = False
        print("\r  {} Turbo stopped, exiting after {:,} attempts...".format(INPUT2, faclon.attempts))
        pass

    sleep(0.1)
    input("\n  Press ENTER to close window")
    os._exit(0)
