import requests,uuid,random,re,ctypes,json,urllib,hashlib,hmac,urllib.parse,base64,os
from time import sleep
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import time



active = requests.get("https://api.ipify.org/?format=json").json()
ip = active["ip"]
scan = requests.get("https://pastebin.com/raw/uJsmaEwq").text
if ip in scan:
    pass
else:
    print(f"{ip} This ip is not active")
    input()
    exit(0)

















def password_publickeys():
    resp = requests.get('https://i.instagram.com/api/v1/qe/sync/')
    publickeyid = int(resp.headers.get('ig-set-password-encryption-key-id'))
    publickey = resp.headers.get('ig-set-password-encryption-pub-key')
    return publickeyid, publickey
def password_encrypt(password):
    publickeyid, publickey = password_publickeys()
    session_key = get_random_bytes(32)
    iv = get_random_bytes(12)
    timestamp = str(int(time.time()))
    decoded_publickey = base64.b64decode(publickey.encode())
    recipient_key = RSA.import_key(decoded_publickey)
    cipher_rsa = PKCS1_v1_5.new(recipient_key)
    rsa_encrypted = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
    cipher_aes.update(timestamp.encode())
    aes_encrypted, tag = cipher_aes.encrypt_and_digest(password.encode("utf8"))
    size_buffer = len(rsa_encrypted).to_bytes(2, byteorder='little')
    payload = base64.b64encode(b''.join([b"\x01", publickeyid.to_bytes(1, byteorder='big'), iv, size_buffer, rsa_encrypted, tag, aes_encrypted]))
    return f"#PWD_INSTAGRAM:4:{timestamp}:{payload.decode()}"







uu = '83f2000a-4b95-4811-bc8d-0f3539ef07cf'

print("Version 3 ")
sleep(2)


class open_tikt():
    def __init__(self):
        self.coo = None
        self.token = None
        self.mid = None
        self.sessionid = None
        self.uuid = uuid.uuid4()
        self.login()
        self.choice()
        self.change_password()
    def headers_login(self):
        head = {}
        head["Host"] = "i.instagram.com"
        head["User-Agent"] = 'Instagram 135.0.0.34.124 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)'
        head["Accept-Language"] = "en-US"
        head["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        head["Connection"] = "keep-alive"
        head['X-Ig-App-Locale'] = 'en_US'
        return head
    def checkpoint(self):
        info = requests.get(f"https://i.instagram.com/api/v1{self.req.json()['challenge']['api_path']}", headers=self.headers_login(), cookies=self.coo)
        step_data = info.json()["step_data"]
        if "phone_number" in step_data:
            try:
                phone = info.json()["step_data"]["phone_number"]
                print(f'[0] phone_number : {phone}')
            except:
                pass
        elif "email" in step_data:
            try:
                email = info.json()["step_data"]["email"]
                print(f'[1] email : {email}')
            except:
                pass

        else:
            print("unknown verification method")
            input()
            exit()
        return self.send_choice()
    def send_choice(self):
        choice = input('choice : ')
        data = {}
        data['choice'] = str(choice)
        data['_uuid'] = uu
        data['_uid'] = uu
        data['_csrftoken'] = 'massing'
        challnge = self.req.json()['challenge']['api_path']
        self.send = requests.post(f"https://i.instagram.com/api/v1{challnge}",headers=self.headers_login(), data=data, cookies=self.coo)
        contact_point = self.send.json()["step_data"]["contact_point"]
        print(f'code sent to : {contact_point}')
        return self.get_code()
    def get_code(self):
        code = input("code : ")
        data = {}
        data['security_code'] = str(code),
        data['_uuid'] = uu,
        data['_uid'] = uu,
        data['_csrftoken'] = 'massing'
        path = self.req.json()['challenge']['api_path']
        send_code = requests.post(f"https://i.instagram.com/api/v1{path}", headers=self.headers_login(), data=data, cookies=self.coo)
        if "logged_in_user" in send_code.text:
            print(f'Login Successfully as @{self.username}')
            self.coo = self.req.cookies
            self.token = self.coo.get("csrftoken")
            self.mid = self.coo.get("mid")
            self.sessionid = self.coo.get("sessionid")
            return self.Account_recovery()
        else:
            regx_error = re.search(r'"message":"(.*?)",', send_code).group(1)
            print(regx_error)
            ask = input("Code is Not Work Do You Want Try Agin [Y/N] : ")
            if ask.lower() == "y":
                sleep(1)
                return self.get_code()
            else:
                exit()



    def login(self):
        self.username = input(f'UserName? : ')

        self.passwordd = input(f'Password? : ')

        data = {}
        data['guid'] = uu
        data['enc_password'] = f'{password_encrypt(self.passwordd)}'
        data['username'] = self.username
        data['device_id'] = f"android-psycho@m1c1"
        data['login_attempt_count'] = '0'

        self.req = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=self.headers_login(), data=data)
        if "logged_in_user" in self.req.text:
            print(f'Login Successfully as @{self.username}')
            self.coo = self.req.cookies
            return self.Account_recovery()
        elif 'checkpoint_challenge_required' in self.req.text:
            self.coo = self.req.cookies
            self.coo = self.req.cookies
            self.token = self.coo.get("csrftoken")
            self.mid = self.coo.get("mid")
            self.sessionid = self.coo.get("sessionid")
            return self.checkpoint()
        else:
            try:
                regx_error = re.search(r'"message":"(.*?)",', self.req.text).group(1)
                print(regx_error)
            except:
                print(self.req.text)
            ask = input("Something has gone wrong Do You Want Try Agin [Y/N] : ")
            if ask.lower() == "y":
                sleep(1)
                os.system("cls")
                return self.login()
            else:
                input()
                exit()


    def headers(self):
        self.head = {}
        self.head["Host"] = "i.instagram.com"
        self.head["User-Agent"] = 'Instagram 187.0.0.32.120 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)'
        self.head["Accept-Language"] = "en-US"
        self.head["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        self.head["Connection"] = "keep-alive"
        self.head['X-Ig-App-Locale'] = 'en_US'
        self.head['X-Ig-Device-Locale'] = "en_US"
        self.head["X-Pigeon-Rawclienttime"] = "1619296670.654"
        self.head["X-Ig-Bandwidth-Speed-Kbps"] = "-1.000"
        self.head["X-Ig-Bandwidth-Totalbytes-B"] = "0"
        self.head["X-Ig-Bandwidth-Totaltime-Ms"] = "0"
        self.head["X-Ig-App-Startup-Country"] = "unknown"
        self.head["X-Bloks-Version-Id"] = "befa8522d3a650f9592e33e4540d527c5b93babbdd6233a1bd40e955c9567f30"
        self.head["X-Ig-Www-Claim"] = "0"
        self.head["X-Bloks-Is-Layout-Rtl"] = "false"
        self.head["X-Bloks-Is-Panorama-Enabled"] = "true"
        self.head["X-Mid"] = "YMXJVQABAAGa6Frp6LAbn3r6iCWR"
        return self.head


    def Account_recovery(self):
        data = {}
        data["source"] = "login_help"
        data["_csrftoken"] = ""
        data["guid"] = uu
        data["device_id"] = f"android-psycho@m1c1"
        data["query"] = self.username
        sleep(1)

        Accountt = requests.post("https://i.instagram.com/api/v1/accounts/assisted_account_recovery/", data=data,headers=self.headers())
        Account = Accountt.text
        b = Accountt.json()
        if "show_recovery_challenge" in Account:
            self.path = re.search(r'"uri":"(.*?)",', Accountt.text).group(1)
            self.jsondata = b["challenge_context"]
            return self.print_info()
        else:
            print(Account)
            input()
    def print_info(self):
        req = requests.get(f'https://i.instagram.com/api/v1{self.path}', headers=self.headers())
        try:
            pp = req.json()["step_data"]["options"][0]
            self.contact_point = pp["contact_point"]
            self.cho = pp["choice"]
            print(f'[{self.cho}] {self.contact_point}')
        except:
            pass
        try:
            dd = req.json()["step_data"]["options"][1]
            self.contact_point = dd["contact_point"]
            self.cho = dd["choice"]
            print(f'[{self.cho}] {self.contact_point}')
        except:
            pass
        try:
            dd = req.json()["step_data"]["options"][2]
            self.contact_point = dd["contact_point"]
            self.cho = dd["choice"]
            print(f'[{self.cho}] {self.contact_point}')
        except:
            pass


    def choice(self):
        choice = input("Choice : ")
        data = {}
        data["choice"] = choice
        data["_csrftoken"] = ""
        data["is_bloks_web"] = 'False'
        data["bk_client_context"] = '{"bloks_version":"e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931","styles_id":"instagram"}'
        data["nest_data_manifest"] = 'true'
        data["challenge_context"] = f"{self.jsondata}"
        data["bloks_versioning_id"] = 'e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931'
        sleep(1.5)
        req = requests.post("https://instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/",data=data,headers=self.headers()).text
        if req.__contains__("It may take up to a minute for you to receive this code"):
            print(f"Code Sent To {self.contact_point}")
            return self.put_code()
        else:
            print(req)
            input()
            exit()
    def put_code(self):
        self.code = input("Code : ")
        data = {}
        data["security_code"] = self.code
        data["_csrftoken"] = ""
        data["is_bloks_web"] = "False"
        data["bk_client_context"] = '{"bloks_version":"e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931","styles_id":"instagram"}'
        data["nest_data_manifest"] = "true"
        data["challenge_context"] = f"{self.jsondata}"
        data["bloks_versioning_id"] = 'e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931'



        request_code = requests.post("https://instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/", data=data,headers=self.headers()).text
        if request_code.__contains__("user_id"):
            print("Code Is True ")
            return self.informations()


        elif request_code.__contains__("Please check the code we sent you and try again"):
            print(" Please check the code we sent you and try again.")
            ask = input("Do You Want try Agin [Y/N] : ")
            if ask.lower() == "y":
                sleep(1)
                return self.put_code()
            else:
                input()
                exit()

        else:
            print(f"Error send_code")
            input()
            exit()
    def informations(self):
        info = requests.get(f'https://i.instagram.com/api/v1{self.path}', headers=self.headers())
        try:

            self.email = info.json()["step_data"]["contact_point"]

            self.phone = info.json()["step_data"]["contact_point"]

        except:
            print("Nothing Info")
            input()
            exit()
        try:
            self.confirm_mode_email = input(f"Confirm {self.email} [Y/N] : ")
        except:
            self.confirm_mode_email = input(f"Confirm New Email [Y/N] : ")
        return self.confirm()


    def confirmed(self, contact):
        data = {}
        data["_csrftoken"] = ""
        data["is_bloks_web"] = 'False'
        data["skip"] = '0'
        data["type"] = self.type
        data["contact_point"] = f'{contact}'
        data["bk_client_context"] = '{"bloks_version":"e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931","styles_id":"instagram"}',
        data["nest_data_manifest"] = 'true',
        data["challenge_context"] = f"{self.jsondata}",
        data["bloks_versioning_id"] = 'e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931'
        sleep(1.5)
        Response = requests.post("https://instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/",data=data, headers=self.headers()).text

        if Response.__contains__("Add New Phone Number") or Response.__contains__("Confirm Your Phone Number") or Response.__contains__("Confirm Your Phone Number"):
            print(f"{contact} Confirmed")
        elif Response.__contains__("It may take up to a minute for you to receive this code"):
            return self.put_code()

    def skip(self, contact):
        data = {}
        data["_csrftoken"] = ""
        data["is_bloks_web"] = 'False'
        data["skip"] = '1'
        data["contact_point"] = ''
        data["bk_client_context"] = '{"bloks_version":"e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931","styles_id":"instagram"}'
        data["nest_data_manifest"] = 'true'
        data["challenge_context"] = f"{self.jsondata}",
        data["bloks_versioning_id"] = 'e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931'
        sleep(1.5)
        Response = requests.post("https://instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/", data=data,headers=self.headers() ).text

        if Response.__contains__("Add New Phone Number") or Response.__contains__("Confirm Your Phone Number") or Response.__contains__("Change Your Password"):
            print(f"{contact}")
        else:
            print(f"Something has gone wrong")
            input()
            exit()
    def confirm(self):
        if self.confirm_mode_email.lower() == 'y':
            self.type = "email"

            try:
                self.confirmed(self.email)
                self.skip("phone_number Skipped")
            except:
                self.email = input("New Email : ")

                self.confirmed(self.email)
        elif self.confirm_mode_email.lower() == 'n':
            self.type = "phone_number"
            self.skip("email")
            try:
                self.confirmed(self.phone)
            except:
                self.phone = input("New PhoneNumber (ex : +966•••••••••) : ")
                self.confirmed(self.phone)
        else:
            print(f"nothing choice")
            input()
            exit()
    def change_password(self):
        ask = input("Do You Want Random password [Y/N] : ")
        if ask.lower() == "y":
            self.new_password = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*")for i in range(15))
        else:
            self.new_password = input("New Password : ")
        data_password = {}
        data_password["_csrftoken"] = ""
        data_password["is_bloks_web"] = 'False'
        data_password["bk_client_context"] = '{"bloks_version":"e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931","styles_id":"instagram"}'
        data_password["nest_data_manifest"] =  'true'
        data_password["challenge_context"] = f"{self.jsondata}"
        data_password["bloks_versioning_id"] = 'e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931'
        data_password["enc_new_password1"] = f'{password_encrypt(self.new_password)}'
        data_password["enc_new_password2"] = f'{password_encrypt(self.new_password)}'
        sleep(1)
        Respone = requests.post("https://instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/",data=data_password,headers=self.headers()).text
        if Respone.__contains__(self.username):
            print("Password Changed")
            return self.changeUsername()
        elif Respone.__contains__("Create a password at least 6 characters long"):
            print("Create a password at least 6 characters long.")
            input()
            exit()
        else:
            print(Respone)
            print(f"change_password")
            input()
            exit()

    def changeUsername(self):
        self.new_username = input("New Username : ")
        data = {}
        data["external_url"] = ''
        data["_csrftoken"] = f""
        data['username'] = self.new_username
        data["is_bloks_web"] = 'False'
        data["first_name"] = ''
        data["biography"] = 'by Falcon group  \npsycho Rayan @m1c1'
        data["bk_client_context"] = '{"bloks_version":"e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931","styles_id":"instagram"}'
        data["nest_data_manifest"] = 'true'
        data["challenge_context"] = f"{self.jsondata}"
        data["bloks_versioning_id"] = 'e097ac2261d546784637b3df264aa3275cb6281d706d91484f43c207d6661931'
        ctypes.windll.user32.MessageBoxW(0, "Are You Ready ?  ", f"change user with ticket", 0x1000)
        change_username = requests.post("https://instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/",data=data, headers=self.headers()).text
        if change_username.__contains__(self.new_username):
            print("Username Changed ")
            self.save()
            input()
            exit()
        else:
            print(f"'Something has gone wrong' ")
            input()
            exit()
    def save(self):
        with open(f"@{self.new_username}.txt","a") as Save:
            Save.write(f"old username : @{self.username}\nnew Username : @{self.new_username}\nold password : {self.passwordd}\nnew_password : {self.new_password}")










open_tikt()

