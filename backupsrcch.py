try:
    from random import *
    from string import *
    import secrets
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
        ./ Made By b.bc & Rayan      
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









class generate():
    def __init__(self, fuc):
        self.TARGET = fuc
        self.threads_list = []

    def Generate_threds(self, Attack):
        for i in range(0, Attack):
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


class Auto():
    def __init__(self, session):
        self.attempt = 0
        self.Ratelimt = 0
        self.sessionid = session
        self.Rs = 0
        self.run = 1
        self.usernames = open("list.txt", "r").read().splitlines()
        self.proxies = open("proxies.txt", "r").read().splitlines()
        self.contorlthreads = threading.Event()
        self.Locks = threading.Lock()
        self.url = ["https://i.instagram.com/api/v1/accounts/username_suggestions/","https://i.instagram.com/accounts/username_suggestions/"]
        self.askproxy = int(input("1=http/s - 2=Socks4 : "))
        self.askpr = input("If You Want Swap With Proxy Click yes (Y/N) : ")
        self.ask = input(f"Do you want print Counter In console (Y/N) :  ")
        self.q = input(f"Do you want Auto settings  (Y/N) :  ")
        if self.q.lower() == "y":
            threading.Thread(target=self.PRINT).start()
            threading.Thread(target=self.requestpersec).start()
            for i in range(1,500):
                gen = generate(self.Clim)
                gen.Generate_threds(1000)
                gen.started()

        else:
            self.threads = int(input(f"Threads (Max = 1000) : "))
            self.loops = int(input(f"loops (Max = 200) : "))
            threading.Thread(target=self.PRINT).start()
            threading.Thread(target=self.requestpersec).start()
            for i in range(0,self.loops):
                gen = generate(self.Clim)
                gen.Generate_threds(self.threads)
                gen.started()
    def PRINT(self):
        print(f'Started Running = True\n')
        while self.run:
            if self.ask.lower() == "y":
                print(f"\rAttempts {self.attempt}  Rate {self.Ratelimt}  R/s {self.Rs} ", end="", flush=True)
            else:
                os.system(f"title Attempts {self.attempt}  Rate {self.Ratelimt}  R/s {self.Rs} ")
            sleep(0.005)
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
    def remove_user(self, user):
        if user not in self.usernames:
            return
        self.sessionid.remove(user)

        if len(self.usernames) == 0:
            self.run = False

            print("\n".join(self.usernames), file=open(dir_path + "/list.txt", "w"))
    def cookiess(self):
        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token, "mid": self.mid, "ds_user_id": f"{self.ds_user}", "rur": "FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"}
        return cookies
    def proxy(self):
        self.prox = random.choice(self.proxies)
        if self.askproxy == 1:
            self.erp = {"http": f"{self.prox}", "https": f"{self.prox}"}
        elif self.askproxy == 2:
            self.erp = {f"http":f"socks4://{self.prox}","https":f"socks4://{self.prox}"}
        else:
            print("NOTHING CHOICE PROXY")
        return self.erp
    def swap_with_proxy(self,Sessions,user):
        res = requests.post("https://i.instagram.com/api/v1/accounts/set_username/",headers={"User-Agent": "Instagram 152.0.0.1.60 Android"},cookies={"sessionid": Sessions},data={"username": f"{user}"},proxies=self.proxy()).text
        if res.__contains__('"status":"ok"'):
            print(f"\nClaimed @{user}")
            requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"im Faster"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + Sessions})
            self.remove_session("".join(Sessions))
            return False
    def swap_without_proxy(self,Sessions,user):
        res = requests.post("https://i.instagram.com/api/v1/accounts/set_username/",headers={"User-Agent": "Instagram 152.0.0.1.60 Android"}, cookies={"sessionid": Sessions},data={"username": f"{user}"}).text
        if res.__contains__('"status":"ok"'):
            print(f"\nClaimed @{user}")
            requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"im Faster"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + Sessions})
            self.remove_session("".join(Sessions))
            return False
    def headers(self):
        cookie = secrets.token_hex(16) * 2
        num = random.randint(10000000, 9999999999)
        head = {}
        head["Host"] = "i.instagram.com"
        head["cookie"] = cookie
        head["user-agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        head["x-csrftoken"] = cookie
        return head
    def Clim(self):
        while self.run:
            Sessions = self.random_session()
            try:
                with self.Locks:
                    user = random.choice(self.usernames)
                    user2 = random.choice(self.usernames)
                Response = requests.post(secrets.choice(self.url),data={"name": f"{user}","email": f"{user2}@gmail.com"},cookies=self.cookiess(),headers=self.headers(),proxies=self.proxy(),timeout=10000)
                if Response.text.__contains__("wait") or Response.text.__contains__("spam"):
                    with self.Locks:
                        self.Ratelimt += 1
                #print(Response.text)
                if Response.json()['suggestions'].__contains__(user):
                    if self.askpr.lower() == "y":
                        self.swap_with_proxy(Sessions,user)
                        if len(user) < 5:
                            webhook = DiscordWebhook(
                                url="https://discord.com/api/webhooks/874844436989874246/R-EQzDQJXHQ8cqCLam69DbRHNW7WjnCBIJJAy7TLU9f_PvRvN1B_dMCxVONJT0ffVBEG")
                            embed = DiscordEmbed(
                                title=f'Claimed @{user}\n | Attempts  {self.attempt}\nR/S  {self.Rs} \nCoded By Rayan , b.bc',
                                color=000000)
                            embed.set_thumbnail(url=im)
                            embed.set_footer(text="Date claim")
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            webhook.execute()
                            with open(f"{user}.txt", "a") as wr:
                                wr.write(f"New user : {user}\nSession : {Sessions}")
                                self.remove_user("".join(user))
                    else:
                        self.swap_without_proxy(Sessions,user)
                        if len(user) < 5:
                            webhook = DiscordWebhook(
                                url="https://discord.com/api/webhooks/874844436989874246/R-EQzDQJXHQ8cqCLam69DbRHNW7WjnCBIJJAy7TLU9f_PvRvN1B_dMCxVONJT0ffVBEG")
                            embed = DiscordEmbed(
                                title=f'Claimed @{user}\n | Attempts  {self.attempt}\nR/S  {self.Rs} \nCoded By Rayan , b.bc',
                                color=000000)
                            embed.set_thumbnail(url=im)
                            embed.set_footer(text="Date claim")
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            webhook.execute()
                            with open(f"{user}.txt", "a") as wr:
                                wr.write(f"New user : {user}\nSession : {Sessions}")
                                self.remove_user("".join(user))
                if Response.json()['suggestions'].__contains__(user2):
                    if self.askpr.lower() == "y":
                        self.swap_with_proxy(Sessions, user2)
                        if len(user2) < 5:
                            webhook = DiscordWebhook(
                                url="https://discord.com/api/webhooks/874844436989874246/R-EQzDQJXHQ8cqCLam69DbRHNW7WjnCBIJJAy7TLU9f_PvRvN1B_dMCxVONJT0ffVBEG")
                            embed = DiscordEmbed(
                                title=f'Claimed @{user2}\n | Attempts  {self.attempt}\nR/S  {self.Rs} \nCoded By Rayan , b.bc',
                                color=000000)
                            embed.set_thumbnail(url=im)
                            embed.set_footer(text="Date claim")
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            webhook.execute()
                            with open(f"{user2}.txt", "a") as wr:
                                wr.write(f"New user : {user2}\nSession : {Sessions}")
                                self.remove_user("".join(user2))
                    else:
                        self.swap_without_proxy(Sessions, user2)
                        if len(user2) < 5:
                            webhook = DiscordWebhook(
                                url="https://discord.com/api/webhooks/874844436989874246/R-EQzDQJXHQ8cqCLam69DbRHNW7WjnCBIJJAy7TLU9f_PvRvN1B_dMCxVONJT0ffVBEG")
                            embed = DiscordEmbed(
                                title=f'Claimed @{user2}\n | Attempts  {self.attempt}\nR/S  {self.Rs} \nCoded By Rayan , b.bc',
                                color=000000)
                            embed.set_thumbnail(url=im)
                            embed.set_footer(text="Date claim")
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            webhook.execute()
                            with open(f"{user2}.txt", "a") as wr:
                                wr.write(f"New user : {user2}\nSession : {Sessions}")
                                self.remove_user("".join(user2))

                else:
                    with self.Locks:
                        self.attempt += 1
            except:
                pass







session = open("sessions.txt", "r").read().splitlines()
def for_ask():
    Auto(session)

for_ask()
