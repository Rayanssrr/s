try:
    import random, os, socket, requests, threading, ctypes,uuid
    from time import sleep
    from termcolor import colored
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import as_completed
    from discord_webhook import DiscordWebhook
    from discord_webhook import DiscordEmbed
    from tqdm import tqdm
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
h = {
        'Host': 'www.instagram.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US;q=0.7,en;q=0.3',
        'X-CSRFToken': 'jeagRYeHcMF4yZmO4UJbNY6DBCbYivNA',
        'Content-Type': "application/x-www-form-urlencoded",
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.instagram.com/accounts/emailsignup/',
        'Cookie': 'csrftoken=jeagRYeHcMF4yZmO4UJbNY6DBCbYivNA; mid=YHv_AwALAAFmtVEzOC0HhIUrKHs4; ig_did=7741DF1B-DA96-4EEA-A42A-799C654EBFBB; ig_nrcb=1'
    }
os.system('mode con: cols=85 lines=33')
dir_path = os.path.dirname(os.path.realpath(__file__))
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
purble = '\x1b[35m\x1b[39m'
SUCCESS = '\x1b[31m Successfulyy moved \x1b[31m'
Run = '\x1b[36m Started Running...\x1b[31m'
under = '\x1b[35m_\x1b[39m'
skip = '\x1b[31m (defult Thread = 300) \x1b[31m'
clearConsle = lambda: os.system('cls')
dude = """

    * Checker Instagram * 

        Targrt Mode + list mode 
        ./ Made By FD § FBI

"""
by = """


    * Checker *\n
    ./ Made By FD § FBI \n
    ./ @31421 @exploit305 @m1c1
   i can change dude :) 


"""
banner = """

              ___       _                  _____            _         
             | __|__ _ | | __  ___  _ _   |_   _|_  _  _ _ | |__  ___ 
             | _|/ _` || |/ _|/ _ \| ' \    | | | || || '_|| '_ \/ _ \ 
             |_| \__,_||_|\__|\___/|_||_|   |_|  \_,_||_|  |_.__/\___/

"""
lool = dude + banner
print(f"{blue}  {lool}")
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
class Auto():
    def __init__(self, session, threads):
        self.attempts = 0
        self.Ratelimt = 0
        self.sessionid = session
        self.threads = threads
        self.uuid = uuid.uuid1()
        self.run = True
        self.usernames = open("list.txt", "r").read().splitlines()
        self.proxies = open("proxies.txt", "r").read().splitlines()
        self.Silnt = int(input(f"{INPUT1} SILNT {red}(MAX = 1500 ) : "))
        self.skip = int(input(f"{INPUT1} Skip {red}(MAX = 5 ) : "))
        self.install()
        self.Target = ''
        self.RequestPerSecound = 0
        self.contorlthreads = threading.Event()
        self.Locks = threading.Lock()
        self.subDomin = ["i.instagram.com", "b.i.instagram.com"]
        threading.Thread(target=self.RequestPerSecounD).start()
        self.future_session = FuturesSession(max_workers=self.Silnt)
        print(f"{INPUT}{red} Priavte Checker  © {INPUT}")
        for i in range(self.threads):
            threading.Thread(target=self.check).start()

    def random_usernames(self):
        return random.choice(self.usernames)

    def random_session(self):
        return random.choice(self.sessionid)

    def remove_session(self, Sessions):
        if Sessions not in self.sessionid:
            return
        self.sessionid.remove(Sessions)

        if len(self.sessionid) == 0:
            self.run = False

            print("\n".join(self.sessionid), file=open(dir_path + "/sessions.txt", "w"))

    def random_sub_domin(self):
        return random.choice(self.subDomin)

    def RequestPerSecounD(self):
        while 1:
            self.befor = self.attempts
            sleep(1)
            self.RequestPerSecound = self.attempts - self.befor
            print(f"\r{blue}{INPUT1} Attempts : {self.attempts} | Ratelimt : {self.Ratelimt} | R/S : {self.RequestPerSecound}",end="")

    def install(self):
        print(f"{INPUT1}{red} Please wait to download all settings... ")
        for _ in tqdm(range(100), desc=f"{INPUT1}", ascii=False, ncols=65):
            sleep(0.01)
        input(f"{INPUT}{GREEN} All settings have been downloaded , Click Enter to continue ")

    def proxy(self):
        self.prox = random.choice(self.proxies)
        self.erp = {"http": f"{self.prox}", "https": f"{self.prox}"}
        return self.erp

    def Done(self, Sessions, user):
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": f"{by}"},headers={"User-Agent": "Instagram 152.0.0.1.60 Android", "Cookie": "sessionid=" + Sessions})
        webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/810840907887804426/TwSqCHrKD1QR4hMnkHP48t8OnrrjsO4QcpjRlGJHh2vS9z4w9-gvEINazuaOp_P2gDlf")
        embed = DiscordEmbed(title=f'Claimed @{user}\nBy Falcon Group | Attempts  {self.attempts}\nR/S  {self.RequestPerSecound} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date claim")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT} Claimed @{user} \x1b[35mAfter {self.attempts} Attempts \x1b[39m")
        ctypes.windll.user32.MessageBoxW(0, f"Hhh Im win : @{user}  ", f"Auto", 0x1000)



    def get_info(self,Sessions):
        global email
        global user
        self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + Sessions}).json()
        email = self.r['user']['email']







    def check(self):
        global email
        while self.run:
            try:
                user = self.random_usernames()
                Sessions = self.random_session()
                self.request = [self.future_session.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',headers=h,data ={'email': '','username': user,'first_name': '','opt_into_one_tap': 'false'},proxies=self.proxy()) for _ in range(self.skip)]
                for self.req in as_completed(self.request):
                    with self.req.result() as self.response:
                        #print(self.response.text)
                        if '{"account_created": false, "errors": {"email": [{"message": "This field is required.", "code": "email_required"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}' in self.response.text:
                            re = requests.post(f'https://b.i.instagram.com/api/v1/accounts/edit_profile/',headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + Sessions}, data={"external_url": "","phone_number": "","username": f"{user}","first_name": "","_uid": f"{self.uuid}","device_id": self.uuid,"biography": "","_uuid": self.uuid,"email": f"{email}"})
                            if re == 200:
                                with self.Locks:
                                    self.Done(Sessions, user)

                        elif "isn't" in self.response.text:
                            self.attempts += 1
                        else:
                            self.Ratelimt += 1
            except:
                pass


session = open("sessions.txt", "r").read().splitlines()
threads = int(input(f"{INPUT1} Threads {red}(Max = 350) : "))
Auto(session, threads)


















