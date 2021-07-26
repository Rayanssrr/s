import time

try:
    from random import *
    from string import *
    import random, os, requests, threading
    from time import sleep
    from termcolor import colored
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import as_completed
    from discord_webhook import DiscordWebhook
    from discord_webhook import DiscordEmbed

except Exception as Error:
    print(Error)
    input()
    exit()
bad = [
    "/challenge/",
    "consent_required",
    "feedback_required",
    "login_required",
    "nother account",
    "minutes"
]
os.system('mode con: cols=85 lines=33')

dir_path = os.path.dirname(os.path.realpath(__file__))
print_lock = threading.Lock()
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
INPUT = f"\x1b[31m[{plus}]\x1b[31m"
INPUT0 = f"\x1b[36m[{plus2}]\x1b[36m"
INPUT1 = f"\x1b[31m[{SL}]\x1b[31m"
INPUT2 = f"\x1b[31m[{mains}]\x1b[39m"
mark = '\x1b[32m✓\x1b[36m'
INPUT3 = f"\x1b[36m[{mark}]\x1b[36m"
blue = '\x1b[36m\x1b[40m'
red = '\x1b[31m\x1b[40m'
GREEN = '\x1b[32m\x1b[40m'
purble = '\x1b[35m\x1b[39m'
SUCCESS = '\x1b[31m Successfulyy moved \x1b[31m'
Run = '\x1b[36m Started Running...\x1b[31m'
under = '\x1b[35m_\x1b[39m'
skip = '\x1b[31m (defult Thread = 300) \x1b[31m'
clearConsle = lambda: os.system('cls')

dude = """

    * AutoClaimer Instagram * 

        Targrt Mode + list mode 
        ./ Made By Falcon 


"""

by1 = """


    * AutoClaimer *
    \n
        ./ Made By FD § FBI\n


"""
by = "#DayLight"

banner = """
    
        __               ___       __    __ 
  ____/ /___ ___  __   / (_)___ _/ /_  / /_
 / __  / __ `/ / / /  / / / __ `/ __ \/ __/
/ /_/ / /_/ / /_/ /  / / / /_/ / / / / /_  
\__,_/\__,_/\__, /  /_/_/\__, /_/ /_/\__/  
           /____/       /____/             
       


"""
lool = dude + banner

print(f"{red}  {banner}")
images = [
    "https://media.giphy.com/media/I6wUi5eTdUCWI/giphy.gif",
    "https://media.giphy.com/media/3fNmJ20ErpkjK/giphy.gif",
    "https://media.giphy.com/media/GLgPVZ5PLMOPe/giphy.gif",
    "https://media.giphy.com/media/AkRFIhfAKHsyc/giphy.gif",
    "https://media.giphy.com/media/A5KGHdmmxHdwk/giphy.gif",
    "https://media.giphy.com/media/QCJlIDkOJDEIctfdzz/giphy.gif",
    "https://media.giphy.com/media/if9niVFg4IwAE/giphy.gif",
    "https://media.giphy.com/media/QLCWubleeNppS/giphy.gif",

]
im = random.choice(images)



class Auto():
    def __init__(self, session):
        self.attempts = 0
        self.Ratelimt = 0
        self.sessionid = session
        turbo = int(input(f"{one} {GREEN}->{blue} To Target \n{tow} {GREEN}->{blue} To List\n{eq1} {GREEN}->{blue} Choice? :  "))
        self.run = 1
        self.usernames = open("list.txt", "r").read().splitlines()
        self.proxies = open("proxies.txt", "r").read().splitlines()
        self.contorlthreads = threading.Event()
        self.Locks = threading.Lock()
        self.subDomin = ["i.instagram.com", "b.i.instagram.com"]
        print(f"{equl1}{GREEN} ->{blue} Sessions : {red}{len(self.sessionid)}")
        print(f"{equl1}{GREEN} ->{blue} Proxies : {red}{len(self.proxies)}")
        self.ask = input(f"{du1} {GREEN}-> {blue}Do you want print Counter In console {red}(Y/N){blue} :  ")
        #print(RED + "[+] Priavte Auto Claimer Â© [+]")
        if turbo == 1:
            self.q = input(f"{du1} {GREEN}-> {blue}Do you want Auto settings  {red}(Y/N){blue} :  ")
            if self.q.lower() == "y":
                self.target = str(input(f"{du1} {GREEN}-> {blue}Target : "))
                self.threads = 350
                self.loops = 20
                self.future_session = FuturesSession(max_workers=self.threads)
                for _ in range(self.threads):
                    t = threading.Thread(target=self.Clim_target).start()
            else:
                self.threads = int(input(f"{du1} {GREEN}-> {blue}Threads {red}(Max = 1000){blue} : "))
                self.loops = int(input(f"{du1} {GREEN}-> {blue}Loops {red}(Max = 30){blue} : "))
                self.target = str(input(f"{du1} {GREEN}-> {blue}Target : "))
                self.future_session = FuturesSession(max_workers=self.threads)
                for _ in range(self.threads):
                    t = threading.Thread(target=self.Clim_target).start()
        else:
            self.q = input(f"{du1} {blue}-> {GREEN}Do you want Auto settings  {red}(Y/N){blue} :  ")
            if self.q.lower() == "y":
                self.threads = 350
                self.loops = 20
                self.future_session = FuturesSession(max_workers=self.threads)
                for _ in range(self.threads):
                    t = threading.Thread(target=self.Clim).start()
            else:
                self.threads = int(input(f"{du1} {GREEN}-> {blue}Threads {red}(Max = 1000){blue} : "))
                self.future_session = FuturesSession(max_workers=self.threads)
                self.loops = int(input(f"{du1} {GREEN}-> {blue}Loops {red}(Max = 30){blue} : "))
                for _ in range(self.threads):
                    t = threading.Thread(target=self.Clim).start()
        print(f'{equl1}{GREEN} -> {blue}Started Running = {red}True{blue}')
        self.contorlthreads.set()
        while self.run:
            if self.ask.lower() == "y":
                print(f"{INPUT} {GREEN}->{blue} Attempts {self.attempts}  Rate {self.Ratelimt}", end="\r", flush=True)
                sleep(0.05)
            else:
                os.system(f"title {INPUT} Attempts {self.attempts}  Rate {self.Ratelimt}")
                sleep(0.05)


    def random_session(self):
        return random.choice(self.sessionid)

    def remove_session(self, Sessions):
        if Sessions not in self.sessionid:
            return
        self.sessionid.remove(Sessions)

        if len(self.sessionid) == 0:
            self.run = False

            print("\n".join(self.sessionid), file=open(dir_path + "/sessions.txt", "w"))

    def proxy(self):
        self.erp = {"http": f"http://{random.choice(self.proxies)}",'https': f'http://{random.choice(self.proxies)}'}
        return self.erp
    def cookies(self,Sessions):
        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token, "mid": self.mid, "ds_user_id": f"{self.ds_user}", "rur": "FRC","Ig-U-Ig-Direct-Region-Hint": "ASH", "sessionid": Sessions}
        return cookies

    def Done(self, Sessions, user):
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{by}"},
                      headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + Sessions})
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/866337547193548810/hSntntnud8THTQkOf0N_EBnB5VAav0rqPQTJ2YA7dd-ueseN9jqf9Y-qyScEM-PyPEsR")
        embed = DiscordEmbed(title=f'Claimed @{user}\nBy FD § FBI | Attempts  {self.attempts}\nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date claim")
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()
        if len(user)  < 5:
            webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/808399883945902112/Mpp7d6fp2ocbLM4sUshNKgPlpahYOomgAxcHmIyDsqSXs36J2SMttOtyy5LbBMHBeKr_")
            embed = DiscordEmbed(
                title=f'Claimed @{user}\nBy By FD § FBI | Attempts  {self.attempts}\n \nCoded By | By FD § FBI',
                color=000000)
            embed.set_thumbnail(url=im)
            embed.set_footer(text="Date claim")
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
        print(f"\n{du1}{GREEN} -> {blue}NICE Im Faster {red}@{user}")
        get_data = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + Sessions})
        try:
            jeson = get_data.json()

            try:

                Email = jeson["user"]["email"]
            except:
                Email = ""

            try:

                Phone_number = jeson["user"]["phone_number"]
            except:
                Phone_number = ""
        except:
            pass

        with open(f"{user}.txt", "a") as wr:
            wr.write(user + ":" + Sessions + "\n" + f"{Email}:{Phone_number}")


    def Clim(self):
        self.contorlthreads.wait()
        self.reader = -1
        while self.run:
            Sessions = self.random_session()
            self.sub = random.choice(self.subDomin)
            try:
                with self.Locks:
                    self.reader += 1
                target = self.usernames[self.reader]
            except:
                self.reader = -1
            try:
                save_respon = []
                for i in range(self.loops):
                    try:
                        req = self.future_session.post(f'https://{self.sub}/api/v1/accounts/set_username/',
                                                       headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + Sessions},
                                                       data={"username": target}, proxies=self.proxy())
                        save_respon.append(req)
                    except requests.Timeout:
                        print("[-] Time Out [-]")
                for self.req in as_completed(save_respon):
                    with self.req.result() as self.response:
                        #print(self.response.text)
                        if self.response.status_code == 200:
                            with self.Locks:
                                self.Done(Sessions, target)
                                return self.Clim()
                        if "isn't" in self.response.text:
                            self.attempts += 1
                        elif "few minutes" in self.response.text:
                            self.Ratelimt += 1
                        elif any(i in self.response.text for i in bad):
                            self.remove_session(":".join(Sessions))
                if len(self.sessionid) == 0:
                    print(f"\r  {INPUT2} Ran out of accounts after \x1b[31m{self.attempts}\x1b[37m attempts")
            except Exception as Err:
                #print(Err)
                pass

    def Clim_target(self):
        self.contorlthreads.wait()
        while self.run:
            Sessions = self.random_session()
            self.sub = random.choice(self.subDomin)
            try:
                save_respon = []
                for i in range(self.loops):
                    try:
                        req = self.future_session.post(f'https://{self.sub}/api/v1/accounts/set_username/',data={"username": self.target}, proxies=self.proxy(),headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + Sessions})
                        save_respon.append(req)
                    except requests.Timeout:
                        print("[-] Time Out [-]")

                for self.req in as_completed(save_respon):
                    with self.req.result() as self.response:
                        # print(self.response.text)
                        if self.response.status_code == 200:
                            with self.Locks:
                                self.Done(Sessions, self.target)
                                return self.Clim()
                        if "isn't" in self.response.text:
                            self.attempts += 1
                        elif "few minutes" in self.response.text:
                            self.Ratelimt += 1
                        elif any(i in self.response.text for i in bad):

                            self.remove_session(":".join(Sessions))
                if len(self.sessionid) == 0:
                    print(f"\r  {INPUT2} Ran out of accounts after \x1b[31m{self.attempts}\x1b[37m attempts")
            except Exception as Err:
                pass
                #print(Err)


session = open("sessions.txt", "r").read().splitlines()
Auto(session)
