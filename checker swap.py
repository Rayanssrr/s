try:
    import random, os, socket, requests, threading, ctypes
    from time import sleep
    from termcolor import colored
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import as_completed
    from discord_webhook import DiscordWebhook
    from discord_webhook import DiscordEmbed


except Exception as W:
    print(W)
    os.system("pip install termcolor")
    os.system("pip install requests_futures")
    os.system("pip install discord_webhook")

os.system('mode con: cols=85 lines=33')

dir_path = os.path.dirname(os.path.realpath(__file__))
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

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
g = requests.get('https://pastebin.com/kEdfngFt')
if ip in g.text:
    pass
else:
    print(ip)
    print(f'{INPUT2}{red} Ip not active ')
    #sleep(23)
    #os._exit(0)
print("\n")

dude = """

    * Cheker Instagram * 

        List mode
           Made By @CokePokes_

"""
ban = """""""""
                 ______  __       ____    __  __  ______     
                /\  _  \/\ \     /\  _`\ /\ \/\ \/\  _  \    
                \ \ \L\ \ \ \    \ \ \L\ \ \ \_\ \ \ \L\ \   
                 \ \  __ \ \ \  __\ \ ,__/\ \  _  \ \  __ \  
                  \ \ \/\ \ \ \L\ \ \ \ \/  \ \ \ \ \ \ \/\ \ 
                   \ \_\ \_\ \____/ \ \_\   \ \_\ \_\ \_\ \_\ 
                    \/_/\/_/\/___/   \/_/    \/_/\/_/\/_/\/_/

                                """""""""
print(GREEN + dude + red + ban)
print(under * 75)

design = open("design.txt", "r").read()
title = design.split("\n")[0]
msg = design.split("\n")[1]
by = design.split("\n")[2]

images = [

    "https://media1.tenor.com/images/b94935d6d92eeadb6d1d66bccad31abe/tenor.gif?itemid=21002889",
    "https://media1.tenor.com/images/035ce3059d332b083b19c6554effa529/tenor.gif?itemid=17350123",
    "https://media1.tenor.com/images/4f6c21aadc93f859c406bc112ae19d01/tenor.gif?itemid=17599933",
    "https://media1.tenor.com/images/6fe425c1c6b2e11a425aedb0697a6826/tenor.gif?itemid=20653094",
    "https://media1.tenor.com/images/fca842af645452d50ccc48c6b714a9f1/tenor.gif?itemid=12793353",
    "https://media1.tenor.com/images/77ec220a957c415c3f81ec2e9312d5ba/tenor.gif?itemid=10666007",
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
        self.PROXIES = open("proxies.txt", "r").read().splitlines()
        self.usernames = open("list.txt","r").read().splitlines()
        self.ask2 = int(input(f"{blue}[1] Wriht Session | [2] Take Session In txt File : "))
        if self.ask2 == 1:
            self.session = input(f"{INPUT1}{GREEN} SessionID : ")
        elif self.ask2 == 2:
            self.found = open("cookies.txt","r").read()
            self.session = self.found.split("\n")[0]
        self.get_info()
        self.checkblock()
        self.threads = int(input(f"{INPUT}{blue} Threads? : "))
        print(under * 75)
        # input(f"{INPUT}{red} Are Yoy Ready?")
        ctypes.windll.user32.MessageBoxW(0, f"Are You Ready ?", "Alpha Swap", 0x1000)
        print(f"{INPUT}{Run}")
        self.attempt = 0
        self.rl = 0
        self.Rs = 0
        self.email = None
        self.pro = "@CokePokes_"
        self.run = True
        self.controll = threading.Event()
        self.locks = threading.Lock()
        self.num = None
        self.future_session = FuturesSession(max_workers=self.threads * 4)
        threading.Thread(target=self.RequestperSec).start()
        self.thredas = []
        for i in range(int(self.threads)):
            t = threading.Thread(target=self.check)
            t.setDaemon = True
            t.start()
            self.controll.set()
            self.thredas.append(t)
        for t in self.thredas:
            t.join()

    def get_info(self):
        global email
        global user
        try:
            self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers=head,cookies={"sessionid": f"{self.session}"}).json()
            user = self.r['user']['username']
            email = self.r['user']['email']
            print(f"{INPUT}{GREEN} Login Successfly as (@{user}) Click Enter to continue")
            print(under * 75)
            # clearConsle()
        except Exception as a:
            # print(a)
            # print(self.user)
            input(f"{INPUT2}{red} Error Session id")
            exit()


    def checkblock(self):
        global user
        ask = int(input(f"{blue}[1] I wanna Checkblock | [2] I DO NOT wanna checkblock : "))
        if ask == 1:
            ch = requests.post('https://i.instagram.com/api/v1/accounts/set_username/',data={"username":user + "checkblock"},headers=head,cookies={"sessionid": f"{self.session}"}).status_code
            if ch == 200:
                print(f"{INPUT}{GREEN} The account is working")
            elif ch == 429:
                print(f"{INPUT2}{red} Account is Not work because to too many requests")
                input()
                exit(0)
        elif ask == 2:
            pass


    def RequestperSec(self):
        while 1:
            self.per = self.attempt
            sleep(1)
            self.Rs = self.attempt - self.per
            os.system(f"title #Counter : {self.attempt} / #Counter Rl : {self.rl} / R/S : {self.Rs}")

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
            "_uid": f"{self.uuid}",
            "device_id": self.uuid,
            "biography": "",
            "_uuid": self.uuid,
            "email": f"{email}"
        }
        return data

    def Successfulyy_cliamed(self,Target):
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/',
                      data={"raw_text": f"# By {by}"}, headers=head,cookies={"sessionid": self.session})
        webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/851258037964111942/44KPehb5OIleohmn3fLTuE-EusEsICqTMCFQN-Snkm7BR_mkdYIbU7W6N5t3tpX0r_5o")
        embed = DiscordEmbed(
            title=f'Swapped  @{Target}\nBy {by} | Counter  {self.attempt}\nAlphaTeam | R/S  {self.Rs} \nCoded By | {self.pro}',
            color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date swap")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT1} Claimed:@{Target} \x1b[35mAfter {self.attempt} Attempts \x1b[39m")
        print(under * 75)
        ctypes.windll.user32.MessageBoxW(0, f"{msg} : @{Target}  ", f"{title}", 0x1000)
        sleep(20)
        os._exit(0)


    def check(self):
        global coo
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
        while self.run:
            Target = random.choice(self.usernames)
            
            try:
                    futures = [self.future_session.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',data ={
        'email': '',
        'username': Target,
        'first_name': '',
        'opt_into_one_tap': 'false'
                        }, headers=h,proxies=self.proxies())for _ in range(5)]
                    for futures in as_completed(futures):
                        with futures.result() as resp:
                            #print(resp.text)
                            if '{"account_created": false, "errors": {"email": [{"message": "This field is required.", "code": "email_required"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}' in resp.text:
                                req = requests.post('https://b.i.instagram.com/api/v1/accounts/set_username/', data={"username": Target}, headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.session})
                                with req as respo:
                                    #print(f"RESPONSE FOR set_username {req.text}")
                                    if respo.status_code == 200:
                                        with self.locks:
                                            self.Successfulyy()
                                            self.run = False
                            elif "isn't" in resp.text:
                                self.attempt += 1
                            else:
                                self.rl += 1
                                #print(resp.text)
            except Exception as a:
                pass


class login():
    def __init__(self):
        self.u = requests.get("https://httpbin.org/uuid").json()
        self.uuid = self.u["uuid"]
        self.PROXIES = open("proxies.txt", "r").read().splitlines()
        self.usernames = open("list.txt","r").read().splitlines()
        self.for_login()
        if self.login(username, password):
            self.session = coo.get("sessionid")
            self.get_info()
        self.checkblock()
        self.Target = input(f'{INPUT1}{red} Target? : ')
        self.threads = int(input(f"{INPUT}{blue} Threads? : "))
        print(under * 75)
        # input(f"{INPUT}{red} Are Yoy Ready?")
        ctypes.windll.user32.MessageBoxW(0, f"Are You Ready ?", "Alpha Swap", 0x1000)
        print(f"{INPUT}{Run}")
        self.attempt = 0
        self.rl = 0
        self.Rs = 0
        self.email = None
        self.pro = "@CokePokes_"
        self.run = True
        self.controll = threading.Event()
        self.locks = threading.Lock()
        self.num = None
        self.future_session = FuturesSession(max_workers=self.threads * 4)
        threading.Thread(target=self.RequestperSec).start()
        self.thredas = []
        for i in range(int(self.threads)):
            t = threading.Thread(target=self.check)
            t.setDaemon = True
            t.start()
            self.controll.set()
            self.thredas.append(t)
        for t in self.thredas:
            t.join()

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
            print(under * 75)
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

    def get_info(self):
        global email
        global coo
        global user
        self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers=head,cookies=coo).json()
        email = self.r['user']['email']
        user = self.r['user']['username']


    def checkblock(self):
        global user
        ask = int(input(f"{blue}[1] I wanna Checkblock | [2] I DO NOT wanna checkblock : "))
        if ask == 1:
            ch = requests.post('https://i.instagram.com/api/v1/accounts/set_username/',data={"username":user + "checkblock"},headers={"User-Agent": "Instagram 187.0.0.32.120 Android (25/7.1.2; 240dpi; 1280x720; Asus; ASUS_Z01QD; ASUS_Z01QD; intel; ar_EG; 289692202)"},cookies=coo).status_code
            if ch == 200:
                print(f"{INPUT}{GREEN} The account is working")
            elif ch == 429:
                print(f"{INPUT2}{red} Account is Not work because to too many requests")
                input()
                exit(0)
        elif ask == 2:
            pass

    def RequestperSec(self):
        while 1:
            self.per = self.attempt
            sleep(1)
            self.Rs = self.attempt - self.per
            os.system(f"title #Counter : {self.attempt} / #Counter Rl : {self.rl} / R/S : {self.Rs}")

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
            "_uid": f"{self.uuid}",
            "device_id": self.uuid,
            "biography": "",
            "_uuid": self.uuid,
            "email": f"{email}"
        }
        return data
    def Successfulyy(self,Target):
        global coo
        requests.post('https://i.instagram.com/api/v1/accounts/set_biography/',
                      data={"raw_text": f"\nSwapped By {by}"}, headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.session})
        webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/851258037964111942/44KPehb5OIleohmn3fLTuE-EusEsICqTMCFQN-Snkm7BR_mkdYIbU7W6N5t3tpX0r_5o")
        embed = DiscordEmbed(
            title=f'#AlphaSwap\nSwapped  @{Target}\nBy {by} | Counter  {self.attempt}\nAlphaTeam | R/S  {self.Rs} \nCoded By | {self.pro}',
            color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date swap")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT1} Claimed:@{self.Target} \x1b[35mAfter {self.attempt} Attempts \x1b[39m")
        print(under * 75)
        ctypes.windll.user32.MessageBoxW(0, f"{msg} : @{Target}  ", f"{title}", 0x1000)
        sleep(20)
        os._exit(0)

def check(self):
        global coo
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
        while self.run:
            Target = random.choice(self.usernames)
            
            try:
                    futures = [self.future_session.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',data ={'email': '','username': Target,'first_name': '','opt_into_one_tap': 'false'}, headers=h,proxies=self.proxies())for _ in range(5)]
                    for futures in as_completed(futures):
                        with futures.result() as resp:
                            #print(resp.text)
                            if '{"account_created": false, "errors": {"email": [{"message": "This field is required.", "code": "email_required"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}' in resp.text:
                                req = requests.post('https://b.i.instagram.com/api/v1/accounts/set_username/', data={"username": Target}, headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.session})
                                with req as respo:
                                    #print(f"RESPONSE FOR set_username {req.text}")
                                    if respo.status_code == 200:
                                        with self.locks:
                                            self.Successfulyy()
                                            self.run = False
                            elif "isn't" in resp.text:
                                self.attempt += 1
                            else:
                                self.rl += 1
                                #print(resp.text)
            except Exception as a:
                pass



class seesion_extract():
    def __init__(self):
        self.u = requests.get("https://httpbin.org/uuid").json()
        self.uuid = self.u["uuid"]
        self.for_login()
        if self.login(username, password):
            csrftoken = coo.get("csrftoken")
            session = coo.get("sessionid")
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
            print(under * 75)
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
    ask = input(f"{blue}[S] SeesionID - [L] Login - [E] Extract Cookies : ")
    if ask.lower() == "s":
        sessionlogin()
    elif ask.lower() == "l":
        login()
    elif ask.lower() == "e":
        seesion_extract()
    else:
        print(f" {INPUT2}{red} choice anyone")
        return ss()
ss()
