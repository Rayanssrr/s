try:
    import uuid
    import threading,requests
    import socket
    from time import sleep
    import os,asyncio
    import ctypes
    from discord_webhook import DiscordWebhook
    from discord_webhook import DiscordEmbed
    from string import *
    from random import *
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import as_completed
    import random
    import string
except Exception as a:
    print(a)
clear = lambda: os.system('cls')
url_two = ''
maxthreads = 3000
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
#g = requests.get('https://pastebin.com/kEdfngFt')

class List_Reg():
    def __init__(self):
        self.attemp = 0
        self.per = None
        self.Rs = None
        self.name = str("Dady Rayan is Hare")
        self.name1 = "Rayan@m1c1"
        self.SB = 0
        self.api_list = [
            "https://b.i.instagram.com/api/v1/accounts/create_business/",
            "https://i.i.instagram.com/api/v1/accounts/create_business/",
        ]
        self.ds = string.ascii_lowercase
        self.ask = int(input("[1] Proxy Asia | [2] Proxy Erupe : "))
        self.threads = int(input("Threads : "))
        self.locks = threading.Lock()
        self.Er = 0
        self.list = open("list.txt","r").read().splitlines()
        self.SUCCESS_responses = ["challenge_required", "challenge", "email_is_taken, username_is_taken", ]
        self.bad = ["few minutes", "feedback_required", "generic_request_error", ]
        self.PROXIES = open("proxies.txt", "r").read().splitlines()
        self.run = 1
        self.uid = uuid.uuid4()
        self.email = lambda len: ''.join(choices(list(ascii_lowercase + digits), k=len))
        self.controll = threading.Event()
        threading.Thread(target=self.Requestpersec).start()
        self.thredas_list = []
        for i in range(self.threads * 10):
            self.future_session = FuturesSession(max_workers=self.threads * 10)
            t = threading.Thread(target=self.be_for_Attack)
            self.thredas_list.append(t)
            t.setDaemon = True
            t.start()
        for t in self.thredas_list:
            t.join()

    def proxy_Asia(self):
        self.proxy = random.choice(self.PROXIES)
        proxyDict = {
            "http": f"http://{self.proxy}",
            "https": f"http://{self.proxy}"
        }
        return proxyDict

    def proxy_Erupe(self):
        self.proxy = random.choice(self.PROXIES)
        proxyDict = {
            "http": f"{self.proxy}", "https": f"{self.proxy}"
        }
        return proxyDict

    def send_discord_webhook(self):
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/837368687605710849/KucsMvDc9kJ9PgJrtSOKZWHavOy7uN56u_Kg_iwZU1bZC-iut78tSWIZ0t6bkw8ZkYLX')
        embed = DiscordEmbed(title='#Reg ', description='@{}\n Attempt >> {}'.format(self.user, self.attemp),color=9109504)
        embed.set_footer(text="#Rayan|")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()

    def Requestpersec(self):
        while 1:
            self.per = self.attemp
            sleep(1)
            self.Rs = self.attemp - self.per
            os.system(f"title  Attempt : {self.attemp} / Error : {self.Er} / R/S : {self.Rs} / S/B : {self.SB}")

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
        # "signed_body=SIGNATURE.{"jazoest":"22434","tos_version":"row","suggestedUsername":"","sn_result":"API_ERROR: class X.7Na:7: ","phone_id":"35a6f462-5bbe-41a9-b47f-87a6b856bf46","professional_signup_source_account_id":"47258184425","fb_auth_token":"",,"page_id":"","entry_point":"setting","phone_number":"","professional_signup_source_user_type":"instagram","_csrftoken":"Of20bpO9gIlEKkJeIUBCvHcjZz0Kfcgr","username":"e451fc37a3","first_name":"MoonWalker","day":"24","guid":"bd76a155-e663-4192-b610-f6a1d5190d3d","year":"1999","device_id":"android-7a74997eee76b904","email":"e451fc37a3@firemailbox.club","month":"4","sn_nonce":"ZTQ1MWZjMzdhM0BmaXJlbWFpbGJveC5jbHVifDE2MTkyOTY1NzR8a5usCxcbiVGUuPb61ZKrvEvAdmZBUAgL","should_show_public_contacts":"0","force_sign_up_code":"sOZRDrzU","should_show_category":"0","qs_stamp":"","category_id":"1314020451960517","to_account_type":"3"}"
    def cookies(self):

        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token, "mid": self.mid, "ds_user_id": f"{self.ds_user}", "rur": "FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"}
        return cookies
    def SaveInfo(self, random_em):
        try:
            print(f" Claimed @{self.user} After {self.attemp} Attempts ")
            file = "./Reg/"
            os.mkdir(file)
            with open(f'./{file}/@{self.user}.txt', 'a') as file3:
                file3.write(
                    'Username:' + self.user + '\n' + 'Email:' + random_em + "@gmail.com" + '\n' + 'password:' + random_em + self.name1 + '\n')
        except Exception as P:
            with open(f'./{file}/@{self.user}.txt', 'a') as file3:
                file3.write('Username:' + self.user + '\n' + 'Email:' + random_em + "@gmail.com" +  '\n' + 'password:' + random_em + self.name1 + '\n')
    def data(self,random_em):
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        uid = uuid.uuid4()
        self.user = choice(self.list)
        # signed_body = {"jazoest":"22434","tos_version":"row","suggestedUsername":"","sn_result":"API_ERROR: class X.7Na:7: ","phone_id":"35a6f462-5bbe-41a9-b47f-87a6b856bf46","professional_signup_source_account_id":"47258184425","fb_auth_token":"",,"page_id":"","entry_point":"setting","phone_number":"","professional_signup_source_user_type":"instagram","_csrftoken":"Of20bpO9gIlEKkJeIUBCvHcjZz0Kfcgr","username":"e451fc37a3","first_name":"MoonWalker","day":"24","guid":"bd76a155-e663-4192-b610-f6a1d5190d3d","year":"1999","device_id":"android-7a74997eee76b904","email":"e451fc37a3@firemailbox.club","month":"4","sn_nonce":"ZTQ1MWZjMzdhM0BmaXJlbWFpbGJveC5jbHVifDE2MTkyOTY1NzR8a5usCxcbiVGUuPb61ZKrvEvAdmZBUAgL","should_show_public_contacts":"0","force_sign_up_code":"sOZRDrzU","should_show_category":"0","qs_stamp":"","category_id":"1314020451960517","to_account_type":"3"}
        value = {}
        value['phone_id'] = uid
        value['device_id'] = uid
        value['_csrftoken'] = self.token
        value['email'] = random_em + "@gmail.com"
        value["password"] = f'{random_em}{self.name1}'
        value['username'] = self.user
        value['first_name'] = 'Rayan'
        return value
    def be_for_Attack(self):
        while 1:
            try:
                random_em = self.email(20)
                future = []
                api = choice(self.api_list)
                for i in range(self.threads):
                    if self.ask == 1:
                        futures = self.future_session.post(api,
                                                           data=self.data(random_em), cookies=self.cookies(),
                                                           headers=self.headers(), timeout=None,
                                                           proxies=self.proxy_Asia())
                    elif self.ask == 2:
                        futures = self.future_session.post(api,
                                                           data=self.data(random_em), cookies=self.cookies(),
                                                           headers=self.headers(), timeout=None,
                                                           proxies=self.proxy_Erupe())
                    futures.i = i
                    future.append(futures)
                    for futures in as_completed(future):
                        with futures.result() as resp:
                            #print(resp.text)
                            if resp.status_code == 429:
                                self.Er += 1
                            if resp.status_code == 200:
                                self.attemp += 1
                            if resp.status_code == 400:
                                if any(i in resp.text for i in self.SUCCESS_responses):
                                    self.SaveInfo(random_em)
                                    self.send_discord_webhook()
                                    ctypes.windll.user32.MessageBoxW(0, f"claimed successfully: {self.user} ", "Reg",
                                                                     0x1000)
                                    return futures
                            if "Sorry, there was a problem with your request" in resp.text:
                                self.Er += 1
                            if "signup_block" in resp.text:
                                # print(resp.text)
                                self.SB += 1

                # print(resp.text)
            except Exception as a:
                # print(a)
                pass

class Target_attack():
    def __init__(self):
        self.attemp = 0
        self.per = None
        self.Rs = None
        self.name = str("Dady Rayan is Hare")
        self.name1 = "Rayan@m1c1"
        self.SB = 0
        self.ds = string.ascii_lowercase
        self.ask = int(input("[1] Proxy Asia | [2] Proxy Erupe : "))
        self.user = input("Target : ")
        self.threads = int(input("Threads : "))
        self.api_list = [
            "https://b.i.instagram.com/api/v1/accounts/create_business/",
             "https://i.i.instagram.com/api/v1/accounts/create_business/",
        ]
        self.locks = threading.Lock()
        self.Er = 0
        self.SUCCESS_responses = ["challenge_required","challenge","email_is_taken, username_is_taken",]
        self.bad = ["few minutes","feedback_required","generic_request_error",]
        self.PROXIES = open("proxies.txt", "r").read().splitlines()
        self.run = 1
        self.uid = uuid.uuid4()
        self.email = lambda len: ''.join(choices(list(ascii_lowercase + digits), k=len))
        self.controll = threading.Event()
        threading.Thread(target=self.Requestpersec).start()
        self.thredas_list = []
        for i in range(self.threads*10):
            self.future_session = FuturesSession(max_workers=self.threads*10)
            t = threading.Thread(target=self.be_for_Attack)
            self.thredas_list.append(t)
            t.setDaemon = True
            t.start()
        for t in self.thredas_list:
            t.join()


    def proxy_Asia(self):
        self.proxy = random.choice(self.PROXIES)
        proxyDict = {
            "http": f"http://{self.proxy}",
            "https": f"http://{self.proxy}"
        }
        return proxyDict


    def proxy_Erupe(self):
        self.proxy = random.choice(self.PROXIES)
        proxyDict = {
            "http": f"{self.proxy}","https": f"{self.proxy}"
        }
        return proxyDict

    def send_discord_webhook(self):
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/837368687605710849/KucsMvDc9kJ9PgJrtSOKZWHavOy7uN56u_Kg_iwZU1bZC-iut78tSWIZ0t6bkw8ZkYLX')
        embed = DiscordEmbed(title='#Reg ', description='@{}\n Attempt >> {}'.format(self.user, self.attemp), color=9109504)
        embed.set_footer(text="#Rayan|")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()


    def Requestpersec(self):
        while 1:
            self.per = self.attemp
            sleep(1)
            self.Rs = self.attemp - self.per
            os.system(f"title  Attempt : {self.attemp} / Error : {self.Er} / R/S : {self.Rs} / S/B : {self.SB}")

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

    #"signed_body=SIGNATURE.{"jazoest":"22434","tos_version":"row","suggestedUsername":"","sn_result":"API_ERROR: class X.7Na:7: ","phone_id":"35a6f462-5bbe-41a9-b47f-87a6b856bf46","professional_signup_source_account_id":"47258184425","fb_auth_token":"",,"page_id":"","entry_point":"setting","phone_number":"","professional_signup_source_user_type":"instagram","_csrftoken":"Of20bpO9gIlEKkJeIUBCvHcjZz0Kfcgr","username":"e451fc37a3","first_name":"MoonWalker","day":"24","guid":"bd76a155-e663-4192-b610-f6a1d5190d3d","year":"1999","device_id":"android-7a74997eee76b904","email":"e451fc37a3@firemailbox.club","month":"4","sn_nonce":"ZTQ1MWZjMzdhM0BmaXJlbWFpbGJveC5jbHVifDE2MTkyOTY1NzR8a5usCxcbiVGUuPb61ZKrvEvAdmZBUAgL","should_show_public_contacts":"0","force_sign_up_code":"sOZRDrzU","should_show_category":"0","qs_stamp":"","category_id":"1314020451960517","to_account_type":"3"}"
    def cookies(self):
        self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        self.mid = ''.join(random.choice(digits) for _ in range(11))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        cookies = {"csrftoken": self.token,"mid":self.mid, "ds_user_id": f"{self.ds_user}","rur":"FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"}
        return cookies
    def data(self,random_em):
        self.token = ''.join(random.choice(hexdigits) for _ in range(32))
        uid = uuid.uuid4()
        #signed_body = {"jazoest":"22434","tos_version":"row","suggestedUsername":"","sn_result":"API_ERROR: class X.7Na:7: ","phone_id":"35a6f462-5bbe-41a9-b47f-87a6b856bf46","professional_signup_source_account_id":"47258184425","fb_auth_token":"",,"page_id":"","entry_point":"setting","phone_number":"","professional_signup_source_user_type":"instagram","_csrftoken":"Of20bpO9gIlEKkJeIUBCvHcjZz0Kfcgr","username":"e451fc37a3","first_name":"MoonWalker","day":"24","guid":"bd76a155-e663-4192-b610-f6a1d5190d3d","year":"1999","device_id":"android-7a74997eee76b904","email":"e451fc37a3@firemailbox.club","month":"4","sn_nonce":"ZTQ1MWZjMzdhM0BmaXJlbWFpbGJveC5jbHVifDE2MTkyOTY1NzR8a5usCxcbiVGUuPb61ZKrvEvAdmZBUAgL","should_show_public_contacts":"0","force_sign_up_code":"sOZRDrzU","should_show_category":"0","qs_stamp":"","category_id":"1314020451960517","to_account_type":"3"}
        value = {}
        value['phone_id'] = uid
        value['device_id'] = uid
        value['_csrftoken'] = self.token
        value['email'] = random_em + "@gmail.com"
        value["password"] = f'{random_em}{self.name1}'
        value['username'] = self.user
        value['first_name'] = 'Rayan'
        return value
    def SaveInfo(self,random_em):
        try:
            print(f"\r Claimed @{self.user} After {self.attemp} Attempts ")
            file = "./Reg/"
            os.mkdir(file)
            with open(f'./{file}/@{self.user}.txt', 'a') as file3:
                file3.write('Username:' + self.user + '\n' + 'Email:' + random_em + "@gmail.com" + '\n' + 'password:' + random_em + self.name1 + '\n')
        except Exception as P:
            with open(f'./{file}/@{self.user}.txt', 'a') as file3:
                file3.write('Username:' + self.user + '\n' + 'Email:' + random_em + "@gmail.com" + '\n' + 'password:' + random_em + self.name1 + '\n')
    def be_for_Attack(self):
        while 1:
            try:
                random_em = self.email(20)
                future = []
                for i in range(self.threads):
                    api = choice(self.api_list)
                    if self.ask == 1:
                        futures = self.future_session.post(api, data=self.data(random_em), cookies=self.cookies(),headers=self.headers(),timeout=None,proxies=self.proxy_Asia())
                    elif self.ask == 2:
                        futures = self.future_session.post(api,data=self.data(random_em), cookies=self.cookies(),headers=self.headers(), timeout=None,proxies=self.proxy_Erupe())
                    futures.i = i
                    future.append(futures)
                    for futures in as_completed(future):
                        with futures.result() as resp:
                            with self.locks:
                                #print(api)
                                if resp.status_code == 429:
                                    self.Er += 1
                                if resp.status_code == 200:
                                    self.attemp +=1
                                if resp.status_code == 400:
                                    if any(i in resp.text for i in self.SUCCESS_responses):
                                        #print(resp.text)
                                        self.SaveInfo(random_em)
                                        self.send_discord_webhook()
                                        ctypes.windll.user32.MessageBoxW(0, f"claimed successfully: {self.user} ","Reg", 0x1000)
                                        return futures
                                if "Sorry, there was a problem with your request" in resp.text:
                                    self.Er +=1
                                if "signup_block" in resp.text:
                                    #print(resp.text)
                                    self.SB += 1


                #print(resp.text)
            except Exception as a:
                #print(a)
                pass
ask = int(input("1-list - 2-Target : "))

if ask == 1:
    Reg = List_Reg()
elif ask == 2:
    Reg = Target_attack()
