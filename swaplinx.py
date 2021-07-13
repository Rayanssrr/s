try:
    import random, os, socket, requests, threading, ctypes
    from time import sleep
    from termcolor import colored
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import as_completed
    from discord_webhook import DiscordWebhook
    from discord_webhook import DiscordEmbed
    from tqdm import tqdm


except Exception as W:
    print(W)
    input()
    exit(0)

os.system('mode con: cols=85 lines=33')

# dir_path = os.path.dirname(os.path.realpath(__file__))
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
clearConsle = lambda: os.system('clear')

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
g = requests.get('https://pastebin.com/jjeXSVhj')
if ip in g.text:
    pass
else:
    print(ip)
    print(f'{INPUT2}{red} Ip not active ')
    #sleep(23)
    #os._exit(0)
print("\n")

dude = """
    * Swap Instagram * 
        Target Mode 
        ./ Made By FD § FBI 
"""
by = """
    * SWAPPED *\n
    ./ Made By FD § FBI \n
    ./ @31421  @m1c1
   i can change dude :) 
"""

# banner = open("banner.txt", "r").read()
clearConsle()
ban = ''
print(GREEN + dude + red + ban)
print(under * 70)


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

api_list = [
    'https://i.instagram.com/api/v1/accounts/set_username/',
    'https://i.instagram.com/api/v1/accounts/edit_profile/'
]
head = {
    'User-Agent': f'Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com'
    
}


class sessionlogin():
    def __init__(self):
        self.u = requests.get("https://httpbin.org/uuid").json()
        self.uuid = self.u["uuid"]
        self.subDomin = ["i.instagram.com", "b.i.instagram.com"]
        self.apilist = ['set_username', 'edit_profile']
        self.ask = int(input(f"\x1b[35m[1] Without Proxy | [2] With Proxy : \x1b[39m"))
        self.PROXIES = open("proxies.txt", "r").read().splitlines()
        self.ask2 = int(input(f"{blue}[1] Wriht Session | [2] Take Session In txt File : "))
        if self.ask2 == 1:
            self.session = input(f"{INPUT1}{GREEN} SessionID : ")
        elif self.ask2 == 2:
            self.found = open("cookies.txt", "r").read()
            self._csrftoken = self.found.split("\n")[0]
            self.session = self.found.split("\n")[1]
            self.ds = self.found.split("\n")[2]
            self.mid = self.found.split("\n")[3]
        self.get_info()
        self.checkblock()
        self.Target = input(f'{INPUT1}{blue} Target? : ')
        self.threads = int(input(f"{INPUT}{blue} Threads? {red}(MAX = 15) : "))
        self.Silnt = int(input(f"{INPUT}{blue} SILNT? {red}(MAX = 800) : "))
        self.loops = int(input(f"{INPUT}{blue} Loops? {red}(MAX = 80) : "))
        self.install()
        print(under * 70)
        #input(f"{INPUT}{red} Are Yoy Ready?")
        # ctypes.windll.user32.MessageBoxW(0, f"Are You Ready ?", "Sharingan Swap", 0x1000)
        print(f"{INPUT}{Run}")
        self.attempt = 0
        self.rl = 0
        self.Rs = 0
        self.email = None
        self.run = True
        self.controll = threading.Event()
        self.locks = threading.Lock()
        self.num = None
        self.future_session = FuturesSession(max_workers=self.Silnt)
        threading.Thread(target=self.RequestperSec).start()
        for i in range(int(self.threads)):
            threading.Thread(target=self.runn, daemon=True).start()
            self.controll.set()

    def get_info(self):
        global email
        global user
        try:
            self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers=head,
                                  cookies={"sessionid": f"{self.session}"}).json()
            user = self.r['user']['username']
            email = self.r['user']['email']

            clearConsle()
            print(GREEN + dude + red + ban)
            print(under * 70)
            print(f"{INPUT}{GREEN} Login Successfly as (@{user}) Click Enter to continue")
        except Exception as a:
            # print(a)
            # print(self.user)
            input(f"{INPUT2}{red} Error Session id")
            exit()
            
    def install(self):
        print(f"{INPUT1}{red} Please wait to download all settings... ")
        for _ in tqdm(range(100), desc=f"{INPUT1}", ascii=False, ncols=65):
            sleep(0.01)
        input(f"{INPUT}{GREEN} All settings have been downloaded , Click Enter if You Ready ")


    def checkblock(self):
        global user
        ask = input(f"{INPUT1}{blue} I wanna Checkblock <Y/N> I DO NOT wanna checkblock : ")
        if ask.lower() == 'y':
            ch = requests.post('https://i.instagram.com/api/v1/accounts/set_username/',
                               data={"username": user + ".checkblock"}, headers=head,
                               cookies={"sessionid": f"{self.session}"}).status_code
            if ch == 200:
                print(f"{INPUT}{GREEN} The account is working")
            elif ch == 429:
                print(f"{INPUT2}{red} Account is Not work because to too many requests")
                input()
                exit(0)
        elif ask == 'n':
            pass
        else:
            print(f"{INPUT2}{red} Chose Any One")
            return self.checkblock()

    def RequestperSec(self):
        while 1:
            self.per = self.attempt
            sleep(1)
            self.Rs = self.attempt - self.per
            print(f"\r{GREEN}{INPUT1} Counter : {self.attempt} / Counter Rl : {self.rl} / R/S : {self.Rs}", end="")

    def sub(self):
        return random.choice(self.subDomin)

    def api(self):
        return random.choice(self.apilist)

    def proxies(self):
        self.proxy = random.choice(self.PROXIES)
        self.erp = {"http": f"{self.proxy}", "https": f"{self.proxy}"}
        return self.erp

    def data(self):
        global email
        data = {
            "external_url": "",
            "phone_number": "",
            "username": f"{self.Target}",
            "first_name": "",
            "_uid": f"{str(self.uuid)}",
            "device_id": f"{str(self.uuid)}",
            "biography": "",
            "_uuid": f"{str(self.uuid)}",
            "email": f"{email}"
        }
        return data

    def Successfulyy(self):
        value = {"raw_text": f"{by}"}
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data=value, headers=head,cookies={"sessionid": self.session})
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/864315005137453056/ZRgAQtkv8KuZeBw8QQvVYOpgHo-GinsX48TNERb-rQ7Qdm96WuU-1VjzXgA3qxZao4sZ")
        embed = DiscordEmbed(title=f'Claimed @{self.Target}\nBy FD § FBI | Attempts  {self.attempt}\nR/S  {self.rl} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date swap")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT1} Swapped @{self.Target} \x1b[35mAfter {self.attempt} Attempts \x1b[39m")
        print(under * 70)
        os._exit(0)
        # ctypes.windll.user32.MessageBoxW(0, f"{msg} : @{self.Target}  ", f"{title}", 0x1000)

    def runn(self):
        self.controll.wait()
        while self.run:
            try:
                future = []
                for i in range(self.loops):
                    if self.ask == 1:
                        futures = self.future_session.post(f"https://{self.sub()}/api/v1/accounts/{self.api()}/",
                                                           data=self.data(),
                                                           headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                                                    "Cookie": "sessionid=" + self.session})
                    else:
                        futures = self.future_session.post(f"https://{self.sub()}/api/v1/accounts/{self.api()}/",
                                                           data=self.data(),
                                                           headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                                                    "Cookie": "sessionid=" + self.session},
                                                           proxies=self.proxies(), timeout=3)
                    futures.i = i
                    future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as resp:
                        # print(resp.text)
                        if resp.status_code == 200:
                            with self.locks:
                                self.Successfulyy()
                        if resp.status_code == 400:
                            self.attempt += 1
                            print(f"\r{GREEN}{INPUT1} Counter : {self.attempt} / Counter Rl : {self.rl} / R/S : {self.Rs}",end="")
                        if resp.status_code == 429:
                            self.rl += 1
                            print(f"\r{GREEN}{INPUT1} Counter : {self.attempt} / Counter Rl : {self.rl} / R/S : {self.Rs}",end="")
            except Exception as E:
                # print(E)
                pass


class login():
    def __init__(self):
        self.u = requests.get("https://httpbin.org/uuid").json()
        self.uuid = self.u["uuid"]
        self.ask = int(input(f"\x1b[35m[1] Without Proxy | [2] With Proxy : \x1b[39m"))
        self.subDomin = ["i.instagram.com", "b.i.instagram.com"]
        self.apilist = ['set_username', 'edit_profile']
        self.PROXIES = open("proxies.txt", "r").read().splitlines()
        self.for_login()
        if self.login(username, password):
            self.session = coo.get("sessionid")
            self.get_info()
        self.checkblock()
        self.Target = input(f'{INPUT1}{red} Target? : ')
        self.threads = int(input(f"{INPUT}{blue} Threads? {red}(MAX = 15) : "))
        self.Silnt = int(input(f"{INPUT}{blue} SILNT? {red}(MAX = 800) : "))
        self.loops = int(input(f"{INPUT}{blue} Loops? {red}(MAX = 250) : "))
        self.install()
        print(under * 70)
        #input(f"{INPUT}{red} Are Yoy Ready?")
        # ctypes.windll.user32.MessageBoxW(0, f"Are You Ready ?", "Sharingan Swap", 0x1000)
        print(f"{INPUT}{Run}")
        self.attempt = 0
        self.rl = 0
        self.Rs = 0
        self.email = None
        self.run = True
        self.controll = threading.Event()
        self.locks = threading.Lock()
        self.num = None
        self.future_session = FuturesSession(max_workers=self.Silnt)
        threading.Thread(target=self.RequestperSec).start()
        self.thredas = []
        for i in range(int(self.threads)):
            threading.Thread(target=self.runn, daemon=True).start()
            self.controll.set()

    def for_login(self):
        global username
        global password
        username = input(f'{INPUT1}{GREEN} UserName? : ')
        sleep(0.1)
        password = input(f'{INPUT1}{GREEN} Password? : ')

    def choice_challenge(self, last_json):
        choices = []

        if last_json.get("step_name", "") == "select_verify_method":
            choices.append(colored("Secured Found", 'red'))
            if "phone_number" in last_json["step_data"]:
                choices.append("[ 0 ] Phone")
            if "email" in last_json["step_data"]:
                choices.append("[ 1 ] Email")

            if last_json.get("step_name", "") == "delta_login_review":
                choices.append("Login attempt challenge received")
                choices.append("0 - It was me")
                choices.append("0 - It wasn't me")

        if not choices:
            choices.append(
                '"{}" challenge received'.format(last_json.get("step_name", "Unknown"))
            )
            choices.append("0 - Default")

        return choices

    def challange(self, login_json):
        global coo
        challenge_url = 'https://i.instagram.com/api/v1/' + login_json["challenge"]["api_path"][1:]
        try:
            b = requests.get(challenge_url, headers=head, cookies=coo)
        except Exception as e:
            print("solve_challenge; {}".format(e))
            return False
        choiccc = self.choice_challenge(b.json())
        for choice in choiccc:
            print(choice)
        code = input("choice:")
        data_c = {
            'choice': code,
            '_uuid': self.uuid,
            '_uid': self.uuid,
            '_csrftoken': 'missing'
        }
        send_c = requests.post(challenge_url, data=data_c, headers=head, cookies=coo).json()
        u = send_c['step_data']['contact_point']
        print(f"code has been sent to {u} please check")
        code = input(f"{INPUT1} code:").strip()
        data_co = {
            'security_code': code,
            '_uuid': self.uuid,
            '_uid': self.uuid,
            '_csrftoken': 'missing'
        }
        send_o = requests.post(challenge_url, data=data_co, headers=head, cookies=coo)
        send_coj = send_o.json()
        if ('logged_in_user') in send_coj:
            'Logged in :)'
            clearConsle()
            print(GREEN + dude + red + ban)
            print(f"{INPUT}{blue} Login Successfly as (@{username}) Click Enter to continue")
            print(under * 70)
            coo = send_o.cookies
            return True
        return False

    def login(self, username, password):
        global head
        global coo
        login_url = "https://i.instagram.com/api/v1/accounts/login/"
        data_login = {'uuid': self.uuid,
                      'password': password,
                      'username': username,
                      'device_id': self.uuid,
                      'from_reg': 'false',
                      '_csrftoken': 'missing',
                      'login_attempt_count': '0'}
        loginc = requests.post(login_url, data=data_login, headers=head)
        login1 = loginc.text
        # print(login1)
        if ('"logged_in_user"') in login1:
            clearConsle()
            print(GREEN + dude + red + ban)
            print(under * 70)
            print(f"{INPUT}{blue} Login Successfly as (@{username}) Click Enter to continue")
            coo = loginc.cookies
            return True
        elif ("Incorrect Username") in login1:
            print(
                f"{INPUT2}{red}The username you entered doesn't appear to belong to an account. Please check your username and try again.")
            input()
            exit(0)
        elif ('Incorrect password') in login1:
            print(f"{INPUT2}{red} The password you entered is incorrect. Please try again.")
            input()
            exit(0)
        elif ('"inactive user"') in login1:
            print(
                'Your account has been disabled for violating our terms. Learn how you may be able to restore your account.')
            exit()
        elif ('checkpoint_challenge_required') in login1:
            coo = loginc.cookies
            return self.challange(loginc.json())
        else:
            print(login1)
            exit()
            
    def install(self):
        print(f"{INPUT1}{red} Please wait to download all settings... ")
        for _ in tqdm(range(100), desc=f"{INPUT1}", ascii=False, ncols=65):
            sleep(0.01)
        input(f"{INPUT}{GREEN} All settings have been downloaded , Click Enter if You Ready ")

    def get_info(self):
        global email
        global coo
        global user
        self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers=head,
                              cookies=coo).json()
        email = self.r['user']['email']
        user = self.r['user']['username']

    def checkblock(self):
        global user
        ask = input(f"{INPUT1}{blue} I wanna Checkblock <Y/N> I DO NOT wanna checkblock : ")
        if ask.lower() == 'y':
            ch = requests.post('https://i.instagram.com/api/v1/accounts/set_username/',
                               data={"username": user + ".checkblock"}, headers=head,
                               cookies=coo).status_code
            if ch == 200:
                print(f"{INPUT}{GREEN} The account is working")
            elif ch == 429:
                print(f"{INPUT2}{red} Account is Not work because to too many requests")
                input()
                exit(0)
        elif ask == 'n':
            pass
        else:
            print(f"{INPUT2}{red} Chose Any One")
            return self.checkblock()

    def RequestperSec(self):
        self.per = self.attempt
        while 1:
            sleep(1)
            self.Rs = self.attempt - self.per
            print(f"\r{GREEN}{INPUT1} Counter : {self.attempt} / Counter Rl : {self.rl} / R/S : {self.Rs}", end="")

    def sub(self):
        return random.choice(self.subDomin)

    def api(self):
        return random.choice(self.apilist)

    def proxies(self):
        self.proxy = random.choice(self.PROXIES)
        self.erp = {"http": f"{self.proxy}", "https": f"{self.proxy}"}
        return self.erp

    def data(self):
        global email
        data = {
            "external_url": "",
            "phone_number": "",
            "username": f"{self.Target}",
            "first_name": "",
            "_uid": f"{str(self.uuid)}",
            "device_id": f"{str(self.uuid)}",
            "biography": "",
            "_uuid": f"{str(self.uuid)}",
            "email": f"{email}"
        }
        return data

    def Successfulyy(self):
        global coo
        value = {"raw_text": f"{by}"}
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data=value, headers=head,cookies=coo)
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/864315005137453056/ZRgAQtkv8KuZeBw8QQvVYOpgHo-GinsX48TNERb-rQ7Qdm96WuU-1VjzXgA3qxZao4sZ")
        embed = DiscordEmbed(title=f'Claimed @{self.Target}\nBy FD § FBI | Attempts  {self.attempt}\nR/S  {self.rl} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date swap")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT1} Swapped @{self.Target} \x1b[35mAfter {self.attempt} Attempts \x1b[39m")
        print(under * 70)
        os._exit(0)
        # ctypes.windll.user32.MessageBoxW(0, f"{msg} : @{self.Target}  ", f"{title}", 0x1000)
        os._exit(0)

    def runn(self):
        global coo
        self.controll.wait()
        while self.run:
            try:
                future = []
                for i in range(self.loops):
                    if self.ask == 1:
                        futures = self.future_session.post(f"https://{self.sub()}/api/v1/accounts/{self.api()}/",
                                                           data=self.data(),
                                                           headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                                                    "Cookie": "sessionid=" + self.session})
                    else:
                        futures = self.future_session.post(f"https://{self.sub()}/api/v1/accounts/{self.api()}/",
                                                           data=self.data(),
                                                           headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                                                    "Cookie": "sessionid=" + self.session},
                                                           proxies=self.proxies(), timeout=3)
                    futures.i = i
                    future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as resp:
                        if resp.status_code == 200:
                            with self.locks:
                                self.Successfulyy()
                                # breakpoint()
                                # ctypes.windll.user32.MessageBoxW(0, f"{msg} : @{self.Target}  ", f"{title}", 0x1000)
                        if resp.status_code == 400:
                            self.attempt += 1
                            print(f"\r{GREEN}{INPUT1} Counter : {self.attempt} / Counter Rl : {self.rl} / R/S : {self.Rs}",end="")
                        if resp.status_code == 429:
                            self.rl += 1
                            print(f"\r{GREEN}{INPUT1} Counter : {self.attempt} / Counter Rl : {self.rl} / R/S : {self.Rs}",end="")
            except Exception as E:
                # print(E)
                pass


class seesion_extract():
    def __init__(self):
        self.u = requests.get("https://httpbin.org/uuid").json()
        self.uuid = self.u["uuid"]
        self.for_login()
        if self.login(username, password):
            csrftoken = coo.get("csrftoken")
            session = coo.get("sessionid")
            print(session)
            ds_user_id = coo.get("ds_user_id")
            mid = coo.get("mid")
            with open(f"cookies.txt", "a") as save:
                save.write(f"{csrftoken}\n{session}\n{ds_user_id}\n{mid}")
                print("Done")
                input()
                sleep(2)
        print(under * 75)
        # input(f"{INPUT}{red} Are Yoy Ready?")

    def for_login(self):
        global username
        global password
        username = input(f'{INPUT1}{GREEN} UserName? : ')
        sleep(0.1)
        password = input(f'{INPUT1}{GREEN} Password? : ')

    def choice_challenge(self, last_json):
        choices = []

        if last_json.get("step_name", "") == "select_verify_method":
            choices.append(colored("Secured Found", 'red'))
            if "phone_number" in last_json["step_data"]:
                choices.append("[ 0 ] Phone")
            if "email" in last_json["step_data"]:
                choices.append("[ 1 ] Email")

            if last_json.get("step_name", "") == "delta_login_review":
                choices.append("Login attempt challenge received")
                choices.append("0 - It was me")
                choices.append("0 - It wasn't me")

        if not choices:
            choices.append(
                '"{}" challenge received'.format(last_json.get("step_name", "Unknown"))
            )
            choices.append("0 - Default")

        return choices

    def challange(self, login_json):
        global coo
        challenge_url = 'https://i.instagram.com/api/v1/' + login_json["challenge"]["api_path"][1:]
        try:
            b = requests.get(challenge_url, headers=head, cookies=coo)
        except Exception as e:
            print("solve_challenge; {}".format(e))
            return False
        choiccc = self.choice_challenge(b.json())
        for choice in choiccc:
            print(choice)
        code = input("choice:")
        data_c = {
            'choice': code,
            '_uuid': self.uuid,
            '_uid': self.uuid,
            '_csrftoken': 'missing'
        }
        send_c = requests.post(challenge_url, data=data_c, headers=head, cookies=coo).json()
        u = send_c['step_data']['contact_point']
        print(f"code has been sent to {u} please check")
        code = input(f"{INPUT1} code:").strip()
        data_co = {
            'security_code': code,
            '_uuid': self.uuid,
            '_uid': self.uuid,
            '_csrftoken': 'missing'
        }
        send_o = requests.post(challenge_url, data=data_co, headers=head, cookies=coo)
        send_coj = send_o.json()
        if ('logged_in_user') in send_coj:
            'Logged in :)'
            clearConsle()
            print(GREEN + dude + red + ban)
            print(f"{INPUT}{blue} Login Successfly as (@{username}) Click Enter to continue")
            print(under * 70)
            coo = send_o.cookies
            return True
        return False

    def login(self, username, password):
        global head
        global coo
        login_url = "https://i.instagram.com/api/v1/accounts/login/"
        data_login = {'uuid': self.uuid,
                      'password': password,
                      'username': username,
                      'device_id': self.uuid,
                      'from_reg': 'false',
                      '_csrftoken': 'missing',
                      'login_attempt_count': '0'}
        loginc = requests.post(login_url, data=data_login, headers=head)
        login1 = loginc.text
        # print(login1)
        if ('"logged_in_user"') in login1:
            clearConsle()
            print(GREEN + dude + red + ban)
            print(under * 75)
            print(f"{INPUT}{blue} Login Successfly as (@{username}) Click Enter to continue")
            coo = loginc.cookies
            return True
        elif ("Incorrect Username") in login1:
            print(
                f"{INPUT2}{red}The username you entered doesn't appear to belong to an account. Please check your username and try again.")
            input()
            exit(0)
        elif ('Incorrect password') in login1:
            print(f"{INPUT2}{red} The password you entered is incorrect. Please try again.")
            input()
            exit(0)
        elif ('"inactive user"') in login1:
            print(
                'Your account has been disabled for violating our terms. Learn how you may be able to restore your account.')
            exit()
        elif ('checkpoint_challenge_required') in login1:
            coo = loginc.cookies
            return self.challange(loginc.json())
        else:
            print(login1)
            exit()


def ss():
    ask = input(f"{blue}[S] SessionID - [L] Login - [E] Extract Cookies : ")
    if ask.lower() == "s":
        sessionlogin()
    elif ask.lower() == "l":
        login()
    elif ask.lower() == "e":
        seesion_extract()
    else:
        print(f" {INPUT2}{red} Chose One")
        return ss()


ss()
