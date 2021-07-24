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

    * AutoClaimer Instagram * 

        Targrt Mode + list mode 
        ./ Made By FD § FBI 

"""


by = """
    * Checker *\n
    ./ Made By FD § FBI \n
    ./ @31421 @exploit305 @m1c1
   i can change dude :) 
"""
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
plus = '\x1b[36m+\x1b[31m'
plus2 = '\x1b[32m+\x1b[36m'
mains = '\x1b[36m-\x1b[31m'
SL = '\x1b[36m/\x1b[31m'
INPUT = f"\x1b[31m[{plus}]\x1b[31m"
INPUT0 = f"\x1b[36m[{plus2}]\x1b[36m"
INPUT1 = f"\x1b[31m[{SL}]\x1b[31m"

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


bad_responses = [
    "/challenge/",
    "consent_required",
    "feedback_required",
    "login_required",
    "nother account",
    "minutes"
]


class FalconCheckr(object):
    def __init__(self,Silnt,skip):
        super(FalconCheckr, self).__init__()
        self.claimed = False
        self.run = 1
        self.attempts = 0
        self.Silnt = Silnt
        self.skip = skip
        self.Locks = threading.Lock()
        self.timeout = 0
        self.rl = 0
        self.rs = 0
        self.usernames = open("list.txt","r").read().splitlines()
        self.future_session = FuturesSession(max_workers=self.Silnt*15)
        self.control = threading.Event()

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

    def proxy(self):
        self.prox = random.choice(self.proxies)
        self.erp = {"http": f"{self.prox}", "https": f"{self.prox}"}
        return self.erp




    def Successfully_Claimed(self,user):


        return False
    def headers(self):
        head = {}
        head["User-Agent"] = "Instagram 133.0.0.34.124 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)"
        return head
    def cookies(self,session):
        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token, "mid": self.mid, "ds_user_id": f"{self.ds_user}", "rur": "FRC","Ig-U-Ig-Direct-Region-Hint": "ASH", "sessionid": session}
        return cookies




    def claim_username(self):
        self.control.wait()
        global Done
        user = random.choice(self.usernames)
        session = self.random_session()
        try:
            future = []
            for i in range(self.skip):
                futures = self.future_session.post("https://b.i.instagram.com/api/v1/accounts/set_username/", data={"username":user},proxies=self.proxy(), headers={"User-Agent":"Instagram 133.0.0.34.124 Android"},cookies=self.cookies(session))
                futures.i = i
                future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as response:
                        #print(response.text)
                        if "isn't" in response.text:
                            self.attempts += 1
                        elif "few minutes" in response.text:
                            self.rl += 1
                        elif '"status":"ok"' in response.text:
                            with self.Locks:
                                print(f"\n\r{blue}NICE Im Faster {GREEN}(@{user})")
                                value = {"raw_text": "“If I deliver to you the impossible, then I might have earned your trust.”\n - Lelouch Vi Britannia'"}
                                requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data=value,headers={"User-Agent":"Instagram 133.0.0.34.124 Android"}, cookies=self.cookies(session))
                                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/866337547193548810/hSntntnud8THTQkOf0N_EBnB5VAav0rqPQTJ2YA7dd-ueseN9jqf9Y-qyScEM-PyPEsR")
                                embed = DiscordEmbed(title=f'Claimed @{user}\nBy FD § FBI | Attempts  {self.attempts}\nR/S  {self.rs} \nCoded By | FD § FBI',color=000000)
                                embed.set_thumbnail(url=im)
                                embed.set_footer(text="Date claim")
                                embed.set_timestamp()
                                webhook.add_embed(embed)
                                response = webhook.execute()
                                return self.claim_username()
                        elif any(i in response.text for i in bad_responses):
                            self.remove_session(":".join(session))
                        return False


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
        print(f"{RED}  {lool}")
        sleep(1)
        print(f"{INPUT0}{GREEN} Fetching all proxies form 'proxies.txt' ")
        sleep(1.5)
        print(f"{INPUT0}{GREEN} Fetched all proxies succesfully")
        threads = int(input(f"{INPUT1}{blue} Threads {red}(Max = 500) : "))
        Silnt = int(input(f"{INPUT1}{blue} SILNT {red}(MAX = 1500 ) : "))
        skip = int(input(f"{INPUT1}{blue} Skip {red}(MAX = 5 ) : "))
        print(f"{GREEN}“If I deliver to you the impossible, then I might have earned your trust.”\n - Lelouch Vi Britannia'")
        faclon = FalconCheckr(Silnt, skip)

        faclon.proxies = [i.strip() for i in open(dir_path + "/proxies.txt", "r") if i]
        faclon.sessions = [i.strip() for i in open(dir_path + "/sessions.txt", "r") if i]
    except Exception as ex:
        print(ex)
        exit(1)
    #threads = int(input("  {}{} Threads: ".format(WHITE, INPUT)))
    for _ in range(threads*15):
        thread = open_up(faclon)
        thread.setDaemon(True)
        thread.start()
    faclon.control.set()
    rs = RequestPerSecounD(faclon)
    rs.setDaemon(True)
    rs.start()

    try:
        while faclon.run and not Done:
            sleep(0.1)
            #print("\r  {}{} Attempts: {:,} | RL: {} | R/S: {}".format(WHITE, blue, instagram.attempts, instagram.rl,instagram.rs), end="")
            print(f"\r{blue}Attempts : {faclon.attempts} {red} Ratelimt : {faclon.rl} {blue} R/S : {faclon.rs}",end="")

    except KeyboardInterrupt:
        faclon.running = False
        print("\r  {} Turbo stopped, exiting after {:,} attempts...".format(INPUT2, faclon.attempts))
        pass
    if Done:
        pass


    elif len(faclon.sessions) == 0:
        print("\r  {} Ran out of accounts after \x1b[31m{:,}\x1b[37m attempts".format(INPUT2, faclon.attempts))

    sleep(0.1)
    input("\n  Press ENTER to close window")
    os._exit(0)
