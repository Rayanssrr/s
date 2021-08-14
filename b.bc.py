try:
    from random import *
    from string import *
    import uuid
    import random, os, requests, threading,json
    from time import sleep
    from discord_webhook import DiscordWebhook,DiscordEmbed
except Exception as Error:
    print(Error)
    input()
    exit()
os.system('mode con: cols=75 lines=10')

dir_path = os.path.dirname(os.path.realpath(__file__))

clearConsle = lambda: os.system('cls')

dude = """

    * checker Instagram * 
        ./ Made By Hatim , Rayan 


"""


images = [
    "https://media.giphy.com/media/I6wUi5eTdUCWI/giphy.gif",
    "https://media.giphy.com/media/3fNmJ20ErpkjK/giphy.gif",
    "https://media.giphy.com/media/GLgPVZ5PLMOPe/giphy.gif",
    "https://media.giphy.com/media/AkRFIhfAKHsyc/giphy.gif",
    "https://media.giphy.com/media/A5KGHdmmxHdwk/giphy.gif",
    "https://media.giphy.com/media/QCJlIDkOJDEIctfdzz/giphy.gif",
    "https://media.giphy.com/media/if9niVFg4IwAE/giphy.gif",
    "https://media.giphy.com/media/QLCWubleeNppS/giphy.gif",]
im = random.choice(images)
class Auto():
    def __init__(self, session):
        self.attempt = 0
        self.Ratelimt = 0
        self.sessionid = session
        self.Rs = 0
        #self.SB = 0
        self.run = 1
        self.usernames = open("list.txt", "r").read().splitlines()
        self.proxies = open("proxies.txt", "r").read().splitlines()
        self.contorlthreads = threading.Event()
        self.Locks = threading.Lock()
        self.ask = input(f"Do you want print Counter In console (Y/N) :  ")
        self.q = input(f"Do you want Auto settings  (Y/N) :  ")
        if self.q.lower() == "y":
            threading.Thread(target=self.PRINT).start()
            threading.Thread(target=self.requestpersec).start()
            self.thr = []
            for i in range(500):
                t = threading.Thread(target=self.Clim)
                t.daemon = True
                self.thr.append(t)
                t.start()
            for i in self.thr:
                i.join()
        else:
            self.threads = int(input(f"Threads (Max = 1000) : "))
            threading.Thread(target=self.PRINT).run()
            threading.Thread(target=self.requestpersec).run()
            self.thr = []
            for i in range(self.threads):
                t = threading.Thread(target=self.Clim).start()
                self.thr.append(t)
            for i in self.thr:
                i.join()


    def PRINT(self):
        print(f'Started Running = True\n')
        while self.run:
            if self.ask.lower() == "y":
                print(f"Attempts {self.attempt}  Rate {self.Ratelimt}  R/s {self.Rs} ", end="\r", flush=True)
            else:
                os.system(f"title Attempts {self.attempt}  Rate {self.Ratelimt}  R/s {self.Rs} ")


    def requestpersec(self):
        while self.run:
            self.befor = self.attempt
            sleep(1)
            self.Rs = self.attempt - self.befor

    def random_session(self):
        return random.choice(self.sessionid)

    def remove_session(self, Sessions):
        if Sessions not in self.sessionid:
            return
        self.sessionid.remove(Sessions)

        if len(self.sessionid) == 0:
            self.run = False

            print("\n".join(self.sessionid), file=open(dir_path + "/sessions.txt", "w"))


    def Done(self, Sessions, user,email,num):
        print(f"\nClaimed @{user}")
        if len(user) < 5:
            webhook = DiscordWebhook(url="https://discord.com/api/webhooks/874844436989874246/R-EQzDQJXHQ8cqCLam69DbRHNW7WjnCBIJJAy7TLU9f_PvRvN1B_dMCxVONJT0ffVBEG")
            embed = DiscordEmbed(title=f'Claimed @{user}\n | Attempts  {self.attempt}\nR/S  {self.Rs} \nCoded By Rayan , b.bc',color=000000)
            embed.set_thumbnail(url=im)
            embed.set_footer(text="Date claim")
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            with open(f"{user}.txt", "a") as wr:
                wr.write(user + ":" + Sessions + "\n" + f"{email}:{num}")
                self.remove_session("".join(Sessions))
                return False
    def cookiess(self):
        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token, "mid": self.mid, "ds_user_id": f"{self.ds_user}", "rur": "FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"}
        return cookies
    def proxy(self):
        self.prox = random.choice(self.proxies)
        self.erp = {

            "http":f'http://{self.prox}',
            "https":f'https://{self.prox}'

        }
        return self.erp
    def headers(self):
        head = {}
        head["User-Agent"] = "Instagram 133.0.0.34.124 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)"
        head["Accept-Language"] = "en-US"
        head["X-Mid"] = "YIR9qQABAAGBErx-6UqG4MXIsQLY"
        head["Ig-Intended-User-Id"] = "0"
        head["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        head["Connection"] = "keep-alive"
        return head

    def Clim(self):
        self.reader = -1
        while self.run:
            Sessions = self.random_session()
            try:
                with self.Locks:
                    self.reader += 1
                    user = self.usernames[self.reader]
                Response = requests.post("https://b.i.instagram.com/api/v1/accounts/username_suggestions/",data={"name": f"{user}"}, proxies=self.proxy(), cookies=self.cookiess(),headers=self.headers())
                # print(self.Response.text)
                if (f'"username":"{user}","prototype":"last"') in Response.text:
                    # print("Anfk")
                    self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true",headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + Sessions}).json()
                    try:
                        email = self.r['user']['email']
                    except:
                        email = ""
                    try:
                        num = self.r['user']['phone_number']
                    except:
                        pass
                    res = requests.post("https://i.instagram.com/api/v1/accounts/edit_profile/",headers={"User-Agent": "Instagram 152.0.0.1.60 Android"},cookies={"sessionid": Sessions},data={"external_url": "", "phone_number": f"{num}", "username": f"{user}","first_name": "", "_uid": f"47641699268","device_id": "android-d595db3f5c276071", "biography": f"{dude}","_uuid": str(uuid.uuid4()), "email": f"{email}"})
                    if res.status_code == 200:
                        with self.Locks:
                            self.Done(Sessions,user,email,num)
                            self.remove_session("".join(Sessions))
                            return self.Clim()
                    else:
                        with self.Locks:
                            pass

                elif Response.status_code == 429:
                    self.Ratelimt += 1
                else:
                    self.attempt += 1
            except:
                self.reader =-1
                pass



session = open("sessions.txt", "r").read().splitlines()
def for_ask():
    Auto(session)

for_ask()
