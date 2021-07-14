try:
    import os, socket, requests, threading, ctypes,uuid
    from time import sleep
    from termcolor import colored
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import as_completed
    from discord_webhook import DiscordWebhook
    from discord_webhook import DiscordEmbed
    from random import *
    from string import *
    import random
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
    "minutes"]

h = {
        'Host': 'www.instagram.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US;q=0.7,en;q=0.3',
        'X-CSRFToken': 'jeagRYeHcMF4yZmO4UJbNY6DBCbYivNA',
        'Content-Type': "application/x-www-form-urlencoded",
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.instagram.com/accounts/emailsignup/',
        'Cookie': 'csrftoken=jeagRYeHcMF4yZmO4UJbNY6DBCbYivNA; mid=YHv_AwALAAFmtVEzOC0HhIUrKHs4; ig_did=7741DF1B-DA96-4EEA-A42A-799C654EBFBB; ig_nrcb=1'}

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
ds = """
    Made By Maybe Lisa Or Maybe Not Lisa \n
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
    def __init__(self):
        self.uuid = uuid.uuid1()
        self.attempts = 0
        self.Ratelimt = 0
        self.for_login()
        if self.login(username,password):
            self.get_info()
        self.checkkblock()
        self.threads = int(input(f"{INPUT1} Threads {red}(Max = 500) : "))
        self.uuid = uuid.uuid1()
        self.run = True
        self.timeout = 0
        self.usernames = open("list.txt", "r").read().splitlines()
        self.proxies = open("proxies.txt", "r").read().splitlines()
        self.Silnt = int(input(f"{INPUT1} SILNT {red}(MAX = 1500 ) : "))
        self.skip = int(input(f"{INPUT1} Skip {red}(MAX = 1500 ) : "))
        self.install()
        self.RequestPerSecound = 0
        self.contorlthreads = threading.Event()
        self.Locks = threading.Lock()
        self.subDomin = ["i.instagram.com", "b.i.instagram.com"]
        threading.Thread(target=self.RequestPerSecounD).start()
        self.future_session = FuturesSession(max_workers=self.Silnt)
        print(f"{INPUT}{red} Priavte Checker  © {INPUT}")
        self.thr = []
        for i in range(self.threads):
            t = threading.Thread(target=self.check)
            self.thr.append(t)
            t.start()
        for i in self.thr:
            i.join()

    def for_login(self):
        global username
        global password
        username = input(f'{INPUT1}{GREEN} UserName? : ')
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
            print(GREEN + dude + red + banner)
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
                      'password': f"{password}",
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
            print(blue + dude + red + banner)
            print(under * 75)
            print(f"{INPUT}{blue} Login Successfly as (@{username}) Click Enter to continue")
            coo = loginc.cookies
            return True
        elif ("Incorrect Username") in login1:
            print(f"{INPUT2}{red}The username you entered doesn't appear to belong to an account. Please check your username and try again.")
            input()
            exit(0)
        elif ('Incorrect password') in login1:
            print(f"{INPUT2}{red} The password you entered is incorrect. Please try again.")
            input()
            exit(0)
        elif ('"inactive user"') in login1:
            print('Your account has been disabled for violating our terms. Learn how you may be able to restore your account.')
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
        global num
        self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers=head,cookies=coo).json()
        email = self.r['user']['email']
        user = self.r['user']['username']
        num = self.r['user']['phone_number']
    def RequestPerSecounD(self):
        while 1:
            self.befor = self.attempts
            sleep(1)
            self.RequestPerSecound = self.attempts - self.befor
            print(f"\r{blue}{INPUT1} Attempts : {self.attempts} | Ratelimt : {self.Ratelimt} | R/S : {self.RequestPerSecound} | Timeout : {self.timeout}",end="")
    def install(self):
        print(f"{INPUT1}{red} Please wait to download all settings... ")
        for _ in tqdm(range(100), desc=f"{INPUT1}", ascii=False, ncols=65):
            sleep(0.01)
        input(f"{INPUT}{GREEN} All settings have been downloaded , Click Enter to continue ")
    def proxy(self):
        self.prox = random.choice(self.proxies)
        self.erp = {"http": f"{self.prox}", "https": f"{self.prox}"}
        return self.erp
    def checkkblock(self):
        global coo
        global email
        global user
        global num
        ask = input(f"{INPUT1}{blue} I wanna Checkblock <Y/N> I DO NOT wanna checkblock : ")
        if ask.lower() == "y":
            ch = requests.post('https://i.instagram.com/api/v1/accounts/edit_profile/',headers=head,data={"external_url": "","phone_number": f"{num}","username": f"{user}","first_name": "","_uid": f"47641699268","device_id": "android-d595db3f5c276071","biography": f"{by}","_uuid": str(uuid.uuid4()),"email": f"{email}"},cookies=coo).status_code
            if ch == 200:
                print(f"{INPUT}{GREEN} The account is working")
            elif ch == 429:
                print(f"{INPUT2}{red} Account is Not work because to too many requests")
                input()
                exit(0)
        elif ask.lower() == "n":
            pass



    def Done(self, user):
        webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/810840907887804426/TwSqCHrKD1QR4hMnkHP48t8OnrrjsO4QcpjRlGJHh2vS9z4w9-gvEINazuaOp_P2gDlf")
        embed = DiscordEmbed(title=f'Claimed @{user}\nBy Falcon Group | Attempts  {self.attempts}\nR/S  {self.RequestPerSecound} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date claim")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT} Claimed @{user} \x1b[35mAfter {self.attempts} Attempts \x1b[39m")
        ctypes.windll.user32.MessageBoxW(0, f"Hhh Im win : @{user}  ", f"Auto", 0x1000)
        return False
    def Done2(self, user2):
        webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/810840907887804426/TwSqCHrKD1QR4hMnkHP48t8OnrrjsO4QcpjRlGJHh2vS9z4w9-gvEINazuaOp_P2gDlf")
        embed = DiscordEmbed(title=f'Claimed @{user2}\nBy Falcon Group | Attempts  {self.attempts}\nR/S  {self.RequestPerSecound} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date claim")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT} Claimed @{user2} \x1b[35mAfter {self.attempts} Attempts \x1b[39m")
        ctypes.windll.user32.MessageBoxW(0, f"Hhh Im win : @{user2}  ", f"Auto", 0x1000)
        return False
    def headers(self):
        head = {}
        head['X-Ig-App-Locale'] = 'en_US'
        head['X-Ig-Device-Locale'] = "en_US"
        head["X-Pigeon-Session-Id"] = "e7a9a8b1-8ed1-47ab-9211-b83195c7f398"
        head["X-Pigeon-Rawclienttime"] = "1619296670.654"
        head["X-Ig-Bandwidth-Speed-Kbps"] = "-1.000"
        head["X-Ig-Bandwidth-Totalbytes-B"] = "0"
        head["X-Ig-Bandwidth-Totaltime-Ms"] = "0"
        head["X-Ig-App-Startup-Country"] = "unknown"
        head["X-Bloks-Version-Id"] = "befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30"
        head["X-Ig-Www-Claim"] = "0"
        head["X-Bloks-Is-Layout-Rtl"] = "false"
        head["X-Bloks-Is-Panorama-Enabled"] = "true"
        head["X-Ig-Device-Id"] = "bd76a155-e663-4192-b610-f6a1d5190d3d"
        head["X-Ig-Android-Id"] = "android-7a74997eee76b904"
        head["X-Ig-Timezone-Offset"] = "72000"
        head['X-IG-Connection-Type'] = 'WIFI'
        head['X-IG-Capabilities'] = '3brTBw=='
        head["X-Ig-App-Id"] = "567067343352427"
        head["User-Agent"] = "Instagram 133.0.0.34.124 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)"
        head["Accept-Language"] = "en-US"
        head["X-Mid"] = "YIR9qQABAAGBErx-6UqG4MXIsQLY"
        head["Ig-Intended-User-Id"] = "0"
        head["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        head["Content-Length"] = "1698"
        head["Accept-Encoding"] = "gzip, deflate"
        head["X-Fb-Http-Engine"] = "Liger"
        head["X-Fb-Client-Ip"] = "True"
        head["X-Fb-Server-Cluster"] = "True"
        head["Connection"] = "close"
        return head

    def cookies(self):
        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token, "mid": self.mid, "ds_user_id": f"{self.ds_user}", "rur": "FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"}
        return cookies

    def check(self):
        global email
        global coo
        global num
        while self.run:
             user = random.choice(self.usernames)
             user2 = random.choice(self.usernames)
             try:
                 future = []
                 for i in range(self.skip):
                     futures = self.future_session.post("https://b.i.instagram.com/api/v1/accounts/username_suggestions/",data={"name":f"{user}","email":f"{user2}@gmail.com"},proxies = self.proxy(),cookies=self.cookies(),headers=self.headers())
                     futures.i = i
                     future.append(futures)
                 for futures in as_completed(future):
                     with futures.result() as resp:
                         if (f'"username":"{user}","prototype":"last"') in resp.text:
                             res = requests.post("https://i.instagram.com/api/v1/accounts/edit_profile/",headers=head,cookies=coo, data={"external_url": "","phone_number": f"{num}","username": f"{user}","first_name": "","_uid": f"47641699268","device_id": "android-d595db3f5c276071","biography": f"{by}","_uuid": str(uuid.uuid4()),"email": f"{email}"})
                             if res.status_code == 200:
                                 with self.Locks:
                                     self.Done(user)
                                     return self.check()
                             else:
                                 with self.Locks:
                                    print(f"response edit{res.text})")
                         elif (f'"username":"{user2}","prototype":"email"') in resp.text:
                             resp = requests.post("https://i.instagram.com/api/v1/accounts/edit_profile/", headers=head,
                                                 cookies=coo, data={"external_url": "", "phone_number": f"{num}",
                                                                    "username": f"{user2}", "first_name": "",
                                                                    "_uid": f"47641699268",
                                                                    "device_id": "android-d595db3f5c276071",
                                                                    "biography": f"{by}", "_uuid": str(uuid.uuid4()),
                                                                    "email": f"{email}"})
                             if resp.status_code == 200:
                                 with self.Locks:
                                     self.Done2(user2)
                                     return self.check()
                             else:
                                 with self.Locks:
                                     print(f"response edit{res.text})")

                         elif resp.status_code == 429:
                             self.Ratelimt +=1
                         else:
                             self.attempts +=1
             except requests.Timeout:
                 self.timeout +=1
             except:
                 pass
    # def check(self):
    #     while self.run:
    #         user = random.choice(self.usernames)
    #         try:
    #             self.request = [self.future_session.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',headers=h,data ={'email': '','username': user,'first_name': '','opt_into_one_tap': 'false'},proxies=self.proxy()) for _ in range(self.skip)]
    #             for self.req in as_completed(self.request):
    #                 with self.req.result() as self.response:
    #                     #print(self.response.text)
    #                     if '{"account_created": false, "errors": {"email": [{"message": "This field is required.", "code": "email_required"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}' in self.response.text:
    #                         #print("GG")
    #                         res = requests.post('https://i.instagram.com/api/v1/accounts/set_username/',headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.sessionid},data={"username": f"{user}"})
    #                         if res.status_code == 200:
    #                             with self.Locks:
    #                                 self.Done(user)
    #                                 return self.response.text
    #                         else:
    #                             print(res.text)
    #                     elif "isn't" in self.response.text:
    #                         self.attempts += 1
    #                     else:
    #                         self.Ratelimt += 1
    #         except:
    #             pass



class ch():
    def __init__(self, session):
        self.attempts = 0
        self.Ratelimt = 0
        self.sessionid = session
        self.get_info()
        self.checkkblock()
        self.threads = int(input(f"{INPUT1} Threads {red}(Max = 500) : "))
        self.uuid = uuid.uuid4()
        self.run = True
        self.timeout = 0
        self.usernames = open("list.txt", "r").read().splitlines()
        self.proxies = open("proxies.txt", "r").read().splitlines()
        self.Silnt = int(input(f"{INPUT1} SILNT {red}(MAX = 1500 ) : "))
        self.skip = int(input(f"{INPUT1} Skip {red}(MAX = 1500 ) : "))
        self.install()
        self.Target = ''
        self.RequestPerSecound = 0
        self.contorlthreads = threading.Event()
        self.Locks = threading.Lock()
        self.subDomin = ["i.instagram.com", "b.i.instagram.com"]
        threading.Thread(target=self.RequestPerSecounD).start()
        self.future_session = FuturesSession(max_workers=self.Silnt)
        print(f"{INPUT}{red} Priavte Checker  © {INPUT}")
        self.thr = []
        for i in range(self.threads):
            t = threading.Thread(target=self.check)
            self.thr.append(t)
            t.start()
        for i in self.thr:
            i.join()


    def RequestPerSecounD(self):
        while 1:
            self.befor = self.attempts
            sleep(1)
            self.RequestPerSecound = self.attempts - self.befor
            print(f"\r{blue}{INPUT1} Attempts : {self.attempts} | Ratelimt : {self.Ratelimt} | R/S : {self.RequestPerSecound} | Timeout : {self.timeout}",end="")

    def install(self):
        print(f"{INPUT1}{red} Please wait to download all settings... ")
        for _ in tqdm(range(100), desc=f"{INPUT1}", ascii=False, ncols=65):
            sleep(0.01)
        input(f"{INPUT}{GREEN} All settings have been downloaded , Click Enter to continue ")

    def proxy(self):
        self.prox = random.choice(self.proxies)
        self.erp = {"http": f"{self.prox}", "https": f"{self.prox}"}
        return self.erp
    def get_info(self):
        global email
        global num
        try:
            self.r = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.sessionid}).json()
            user = self.r['user']['username']
            email = self.r['user']['email']
            num = self.r['user']['phone_number']
            clearConsle()
            print(blue + dude + red + banner)
            print(f"{INPUT}{GREEN} Login Successfly as (@{user}) Click Enter to continue")
        except Exception as a:
            # print(a)
            # print(self.user)
            input(f"{INPUT2}{red} Error Session id")
            pass
    def checkkblock(self):
        self.userxx = lambda len: ''.join(choices(list(ascii_lowercase + digits), k=len))
        self.kk = self.userxx(7)
        ask = input(f"{INPUT1}{blue} I wanna Checkblock <Y/N> I DO NOT wanna checkblock : ")
        if ask.lower() == "y":
            ch = requests.post('https://i.instagram.com/api/v1/accounts/set_username/',
                               headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                        "Cookie": "sessionid=" + self.sessionid},
                               data={"external_url": "", "phone_number": f"{num}",
                                     "username": f"{self.kk}", "first_name": "",
                                     "_uid": f"47641699268",
                                     "device_id": "android-d595db3f5c276071",
                                     "biography": f"", "_uuid": str(uuid.uuid4()),
                                     "email": f"{email}"}).status_code
            if ch == 200:
                print(f"{INPUT}{GREEN} The account is working")
            elif ch == 429:
                print(f"{INPUT2}{red} Account is Not work because to too many requests")
                input()
                exit(0)
        elif ask.lower() == "n":
            pass
    def headers(self):
        head = {}
        head['X-Ig-App-Locale'] = 'en_US'
        head['X-Ig-Device-Locale'] = "en_US"
        head["X-Pigeon-Session-Id"] = "e7a9a8b1-8ed1-47ab-9211-b83195c7f398"
        head["X-Pigeon-Rawclienttime"] = "1619296670.654"
        head["X-Ig-Bandwidth-Speed-Kbps"] = "-1.000"
        head["X-Ig-Bandwidth-Totalbytes-B"] = "0"
        head["X-Ig-Bandwidth-Totaltime-Ms"] = "0"
        head["X-Ig-App-Startup-Country"] = "unknown"
        head["X-Bloks-Version-Id"] = "befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30"
        head["X-Ig-Www-Claim"] = "0"
        head["X-Bloks-Is-Layout-Rtl"] = "false"
        head["X-Bloks-Is-Panorama-Enabled"] = "true"
        head["X-Ig-Device-Id"] = "bd76a155-e663-4192-b610-f6a1d5190d3d"
        head["X-Ig-Android-Id"] = "android-7a74997eee76b904"
        head["X-Ig-Timezone-Offset"] = "72000"
        head['X-IG-Connection-Type'] = 'WIFI'
        head['X-IG-Capabilities'] = '3brTBw=='
        head["X-Ig-App-Id"] = "567067343352427"
        head["User-Agent"] = "Instagram 133.0.0.34.124 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)"
        head["Accept-Language"] = "en-US"
        head["X-Mid"] = "YIR9qQABAAGBErx-6UqG4MXIsQLY"
        head["Ig-Intended-User-Id"] = "0"
        head["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        head["Content-Length"] = "1698"
        head["Accept-Encoding"] = "gzip, deflate"
        head["X-Fb-Http-Engine"] = "Liger"
        head["X-Fb-Client-Ip"] = "True"
        head["X-Fb-Server-Cluster"] = "True"
        head["Connection"] = "close"
        return head
    def Done(self, user):
        webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/810840907887804426/TwSqCHrKD1QR4hMnkHP48t8OnrrjsO4QcpjRlGJHh2vS9z4w9-gvEINazuaOp_P2gDlf")
        embed = DiscordEmbed(title=f'Claimed @{user}\nBy Falcon Group | Attempts  {self.attempts}\nR/S  {self.RequestPerSecound} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date claim")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT} Claimed @{user} \x1b[35mAfter {self.attempts} Attempts \x1b[39m")
        ctypes.windll.user32.MessageBoxW(0, f"Hhh Im win : @{user}  ", f"Auto", 0x1000)
        return False
    def Done2(self,user2):
        webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/810840907887804426/TwSqCHrKD1QR4hMnkHP48t8OnrrjsO4QcpjRlGJHh2vS9z4w9-gvEINazuaOp_P2gDlf")
        embed = DiscordEmbed(title=f'Claimed @{user2}\nBy Falcon Group | Attempts  {self.attempts}\nR/S  {self.RequestPerSecound} \nCoded By | FD § FBI',color=000000)
        embed.set_thumbnail(url=im)
        embed.set_footer(text="Date claim")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"\n{INPUT} Claimed @{user2} \x1b[35mAfter {self.attempts} Attempts \x1b[39m")
        ctypes.windll.user32.MessageBoxW(0, f"Hhh Im win : @{user2}  ", f"Auto", 0x1000)

    def cookies(self):
        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token, "mid": self.mid, "ds_user_id": f"{self.ds_user}", "rur": "FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"}
        return cookies


    def check(self):
        global email
        global num
        while self.run:
            user = random.choice(self.usernames)
            user2 = random.choice(self.usernames)
            try:
                future = []
                for i in range(self.skip):
                    futures = self.future_session.post("https://b.i.instagram.com/api/v1/accounts/username_suggestions/", data={"name":f"{user}","email":f"{user2}@gmail.com"},proxies=self.proxy(), headers=self.headers(),cookies=self.cookies())
                    futures.i = i
                    future.append(futures)
                for futures in as_completed(future):
                    with futures.result() as resp:
                        #print(resp.text)
                        if (f'"username":"{user}","prototype":"last"') in resp.text:
                            res = requests.post("https://i.instagram.com/api/v1/accounts/edit_profile/",headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.sessionid}, data={"external_url": "", "phone_number": f"{num}","username": f"{user}", "first_name": "","_uid": f"47641699268","device_id": "android-d595db3f5c276071","biography": f"{by}", "_uuid": str(uuid.uuid4()),"email": f"{email}"})
                            if res.status_code == 200:
                                with self.Locks:
                                    self.Done(user)
                                    return self.check()
                            else:
                                with self.Locks:
                                    print(f"response edit{res.text})")
                        elif (f'"username":"{user2}","prototype":"email"') in resp.text:
                            respp = requests.post("https://i.instagram.com/api/v1/accounts/edit_profile/",
                                                headers={"User-Agent": "Instagram 152.0.0.1.60 Android",
                                                         "Cookie": "sessionid=" + self.sessionid},
                                                data={"external_url": "", "phone_number": f"{num}",
                                                      "username": f"{user}", "first_name": "", "_uid": f"47641699268",
                                                      "device_id": "android-d595db3f5c276071", "biography": f"{by}",
                                                      "_uuid": str(uuid.uuid4()), "email": f"{email}"})
                            if respp.status_code == 200:
                                with self.Locks:
                                    self.Done2(user2)
                                    return self.check()
                            else:
                                with self.Locks:
                                    print(f"response edit{respp.text})")

                        elif resp.status_code == 429:
                            self.Ratelimt += 1
                        else:
                            self.attempts += 1
            except requests.Timeout:
                self.timeout += 1
            except:
                pass








    # def check(self):
    #     while self.run:
    #         user = random.choice(self.usernames)
    #         try:
    #             self.request = [self.future_session.post(f'https://www.instagram.com/accounts/web_create_ajax/attempt/',headers=h,data ={'email': '','username': user,'first_name': '','opt_into_one_tap': 'false'},proxies=self.proxy()) for _ in range(self.skip)]
    #             for self.req in as_completed(self.request):
    #                 with self.req.result() as self.response:
    #                     #print(self.response.text)
    #                     if '{"account_created": false, "errors": {"email": [{"message": "This field is required.", "code": "email_required"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}' in self.response.text:
    #                         #print("GG")
    #                         res = requests.post('https://i.instagram.com/api/v1/accounts/set_username/',headers={"User-Agent": "Instagram 152.0.0.1.60 Android","Cookie": "sessionid=" + self.sessionid},data={"username": f"{user}"})
    #                         if res.status_code == 200:
    #                             with self.Locks:
    #                                 self.Done(user)
    #                                 return self.response.text
    #                         else:
    #                             print(res.text)
    #                     elif "isn't" in self.response.text:
    #                         self.attempts += 1
    #                     else:
    #                         self.Ratelimt += 1
    #         except:
    #             pass





def ss():
    ask = input(f"{INPUT1}{blue}[S] SessionID | [L] Login  : ")
    if ask.lower() == 's':
        session = input(f"{INPUT1} Sessionid : ")
        ch(session)
    elif ask.lower() == 'l':
        Auto()
    else:
        print(f" {INPUT2}{red} Try agin")
        return ss()


ss()

















