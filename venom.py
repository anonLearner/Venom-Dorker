import requests
from bs4 import BeautifulSoup
import os
import sys
import re
import random
from colorama import Fore
w = Fore.WHITE
y = Fore.YELLOW
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
color = [w, y, r, g, b]
venom = random.choice(color)
os.system('clear')
banner = '''

██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗      ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██████╗    
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗   
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██████╔╝   
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗   Created By Venom
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██████╔╝╚██████╔╝██║  ██║██║  ██╗███████╗██║  ██║   Hacker Banno Chutiya nhi
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   
              
    [+] You Have List Of Sites ?
    
    [1] Yes        
    [2] No                                                                                 
'''
print(venom + banner + venom)

site = str(input(w + '    [-] Choose : ' + w))
if site == '1':
    list = input(w + '    [+] Enter the path for the site list: ' + w)
    if os.path.exists(list) is False:
        print(w + '    [-] ' + w + r + 'Either file do not exist or path for file is invalid.' + r)
    else:
        print(w + '    [+] File found: ' + w + g + 'True' + g)
        file = open(list, 'r')
        read = file.readlines()
        x = len(read)
        x = str(x)
        print(w + '    [+] Total Domains: ' + w + g + x + g)
        dorks = '''
    [-] Choose The dork you want to search for: 
                
    [1] Directory listing vulnerabilities         [11] Finding Backdoors               [21] Find WordPress [Wayback Machine]
    [2] Exposed Configuration files               [12] Install / Setup files           [22] Find .SWF file (Google)
    [3] Exposed Database files                    [13] Open Redirects                  [23] Search SWF in WayBack Machine
    [4] Find WordPress                            [14] Apache STRUTS RCE               [24] Search in WayBack Machine #2
    [5] Exposed log files                         [15] Find Pastebin entries           [X]  For Exit
    [6] Backup and old files                      [16] Employees on LINKEDIN           
    [7] Login pages                               [17] .htaccess sensitive files       
    [8] SQL errors                                [18] Find Subdomains                 
    [9] Publicly exposed documents                [19] Find Sub-Subdomains             
    [10] phpinfo()                                [20] Find WordPress #2               
        '''
        print(venom + dorks + venom)
        dork = input(w + '    [-] Choose : ' + w)
        for target in read:
            if dork == '1':
                print(" ")
                print(
                    w + '    [+] ' + w + venom + 'Looking for Directory listing vulnerabilities in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+intitle:index.of'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '      [+] ' + w + r + 'Connection Error' + r)
            elif dork == '2':
                print(" ")
                print(
                    w + '    [+] ' + w + venom + 'Looking for Exposed Configuration files in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '3':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Exposed Database files in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+ext:sql+|+ext:dbf+|+ext:mdb'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '4':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Find WordPress in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+inurl:wp-+|+inurl:wp-content+|+inurl:plugins+|+inurl:uploads+|+inurl:themes+|+inurl:download'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '5':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Exposed log files in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+ext:log'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '6':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Backup and old files in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '7':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Login pages in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+inurl:login'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '8':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for SQL errors in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '9':
                print(" ")
                print(
                    w + '    [+] ' + w + venom + 'Looking for Publicly exposed documents in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '10':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for phpinfo() in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '11':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Finding Backdoors in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+inurl:shell+|+inurl:backdoor+|+inurl:wso+|+inurl:cmd+|+shadow+|+passwd+|+boot.ini+|+inurl:backdoor'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '12':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Install / Setup files in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+inurl:readme+|+inurl:license+|+inurl:install+|+inurl:setup+|+inurl:config'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '13':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Open Redirects in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+inurl:redir+|+inurl:url+|+inurl:redirect+|+inurl:return+|+inurl:src=http+|+inurl:r=http'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '14':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Apache STRUTS RCE in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+ext:action+|+ext:struts+|+ext:do'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '15':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Pastebin entries in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:pastebin.com+' + target
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '16':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for Employees on LINKEDIN in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:linkedin.com+employees+' + target
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '17':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for .htaccess sensitive files in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:' + target + '+inurl:%22/phpinfo.php%22+|+inurl:%22.htaccess%22+|+inurl:%22/.git%22+simple.com%20-github'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '18':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Finding Subdomains ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:*.' + target
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '19':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Finding Sub-Subdomains ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:*.*.' + target
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '20':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for WordPress #2 ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=site:simple.com+inurl:wp-content+|+inurl:wp-includes'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '21':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for WordPress [Wayback Machine] ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'http://wwwb-dedup.us.archive.org:8083/cdx/search?url=' + target + '/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx='
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '22':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Looking for .SWF file (Google) in ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://www.google.com/search?q=+inurl:' + target + '+ext:swf'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    ok = soup.find_all('div', class_='kCrYT')
                    ok = str(ok)
                    new = re.findall('<a href="(.*?)"', ok)
                    new_link = len(new)
                    if new_link > 1:
                        for i in new:
                            i = str(i)
                            if i.startswith('/url?q=') is True:
                                i = i[7:-100]
                                print(w + '    [+] Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [+] ' + w + r + 'No Link found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == '23':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Searching SWF in WayBack Machine for ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000&_=1507209148310'
                    response = requests.get(url)
                    response = response.text
                    length = len(response)
                    if length > 1:
                        response = response.splitlines()
                        for i in response:
                            print(w + '    [+]Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [-]' + w + r + ' No Link Found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '    [+] ' + w + r + 'Connection Error' + r)
            elif dork == '24':
                print(" ")
                print(w + '    [+] ' + w + venom + 'Searching in WayBack Machine #2 for ' + venom + r + target + r)
                print(w + '    [+] Target: ' + w + venom + target + venom)
                print(" ")
                try:
                    url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=mimetype:application/x-shockwave-flash&limit=100000&_=1507209148310'
                    response = requests.get(url)
                    response = response.text
                    length = len(response)
                    if length > 1:
                        response = response.splitlines()
                        for i in response:
                            print(w + '    [+]Link Found: ' + w + g + i + g)
                    else:
                        print(w + '    [-]' + w + r + ' No Link Found' + r)
                except requests.exceptions.ConnectionError as e:
                    print(w + '     [+] ' + w + r + 'Connection Error' + r)
            elif dork == 'X':
                print(w + '     [-] ' + w + r + 'KK bye.Exiting.' + r)
            else:
                print(w + "    [-] " + w + r + "I don't understand you!! Exiting" + r)
                sys.exit()
elif site == '2':
    target = input(w + '    [+] Enter the target domain: ' + w)
    dorks = '''
    [+] Choose The dork you want to search for: 

    [1] Directory listing vulnerabilities         [11] Finding Backdoors               [21] Find WordPress [Wayback Machine]
    [2] Exposed Configuration files               [12] Install / Setup files           [22] Find .SWF file (Google)
    [3] Exposed Database files                    [13] Open Redirects                  [23] Search SWF in WayBack Machine
    [4] Find WordPress                            [14] Apache STRUTS RCE               [24] Search in WayBack Machine #2
    [5] Exposed log files                         [15] Find Pastebin entries           [X]  X for Exit
    [6] Backup and old files                      [16] Employees on LINKEDIN           
    [7] Login pages                               [17] .htaccess sensitive files       
    [8] SQL errors                                [18] Find Subdomains                 
    [9] Publicly exposed documents                [19] Find Sub-Subdomains             
    [10] phpinfo()                                [20] Find WordPress #2               
        '''
    print(venom + dorks + venom)
    dork = input(w + '    [+] Choose : ' + w)
    if dork == '1':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Directory listing vulnerabilities in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+intitle:index.of'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '      [+] ' + w + r + 'Connection Error' + r)
    elif dork == '2':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Exposed Configuration files in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+ext:xml+|+ext:conf+|+ext:cnf+|+ext:reg+|+ext:inf+|+ext:rdp+|+ext:cfg+|+ext:txt+|+ext:ora+|+ext:ini'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '3':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Exposed Database files in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+ext:sql+|+ext:dbf+|+ext:mdb'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '4':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Find WordPress in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+inurl:wp-+|+inurl:wp-content+|+inurl:plugins+|+inurl:uploads+|+inurl:themes+|+inurl:download'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '5':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Exposed log files in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+ext:log'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '6':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Backup and old files in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+ext:bkf+|+ext:bkp+|+ext:bak+|+ext:old+|+ext:backup'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '7':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Login pages in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+inurl:login'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '8':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for SQL errors in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+intext:%22sql+syntax+near%22+|+intext:%22syntax+error+has+occurred%22+|+intext:%22incorrect+syntax+near%22+|+intext:%22unexpected+end+of+SQL+command%22+|+intext:%22Warning:+mysql_connect()%22+|+intext:%22Warning:+mysql_query()%22+|+intext:%22Warning:+pg_connect()%22'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '9':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Publicly exposed documents in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+ext:doc+|+ext:docx+|+ext:odt+|+ext:pdf+|+ext:rtf+|+ext:sxw+|+ext:psw+|+ext:ppt+|+ext:pptx+|+ext:pps+|+ext:csv'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '10':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for phpinfo() in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+ext:php+intitle:phpinfo+%22published+by+the+PHP+Group%22'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '11':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Finding Backdoors in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+inurl:shell+|+inurl:backdoor+|+inurl:wso+|+inurl:cmd+|+shadow+|+passwd+|+boot.ini+|+inurl:backdoor'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '12':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Install / Setup files in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+inurl:readme+|+inurl:license+|+inurl:install+|+inurl:setup+|+inurl:config'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '13':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Open Redirects in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+inurl:redir+|+inurl:url+|+inurl:redirect+|+inurl:return+|+inurl:src=http+|+inurl:r=http'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '14':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Apache STRUTS RCE in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+ext:action+|+ext:struts+|+ext:do'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '15':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Pastebin entries in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:pastebin.com+' + target
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '16':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for Employees on LINKEDIN in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:linkedin.com+employees+' + target
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '17':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for .htaccess sensitive files in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:' + target + '+inurl:%22/phpinfo.php%22+|+inurl:%22.htaccess%22+|+inurl:%22/.git%22+simple.com%20-github'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '18':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Finding Subdomains ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:*.' + target
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '19':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Finding Sub-Subdomains ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:*.*.' + target
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '20':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for WordPress #2 ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=site:simple.com+inurl:wp-content+|+inurl:wp-includes'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '21':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for WordPress [Wayback Machine] ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'http://wwwb-dedup.us.archive.org:8083/cdx/search?url=' + target + '/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx='
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '22':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Looking for .SWF file (Google) in ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://www.google.com/search?q=+inurl:' + target + '+ext:swf'
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            ok = soup.find_all('div', class_='kCrYT')
            ok = str(ok)
            new = re.findall('<a href="(.*?)"', ok)
            new_link = len(new)
            if new_link > 1:
                for i in new:
                    i = str(i)
                    if i.startswith('/url?q=') is True:
                        i = i[7:-100]
                        print(w + '    [+] Link Found: ' + w + g + i + g)
            else:
                print(w + '    [+] ' + w + r + 'No Link found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == '23':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Searching SWF in WayBack Machine for ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000&_=1507209148310'
            response = requests.get(url)
            response = response.text
            length = len(response)
            if length > 1:
                response = response.splitlines()
                for i in response:
                    print(w + '    [+]Link Found: ' + w + g + i + g)
            else:
                print(w + '    [-]' + w + r + ' No Link Found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '    [+] ' + w + r + 'Connection Error' + r)
    elif dork == '24':
        print(" ")
        print(w + '    [+] ' + w + venom + 'Searching in WayBack Machine #2 for ' + venom + r + target + r)
        print(w + '    [+] Target: ' + w + venom + target + venom)
        print(" ")
        try:
            url = 'https://web.archive.org/cdx/search?url=' + target + '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=mimetype:application/x-shockwave-flash&limit=100000&_=1507209148310'
            response = requests.get(url)
            response = response.text
            length = len(response)
            if length > 1:
                response = response.splitlines()
                for i in response:
                    print(w + '    [+]Link Found: ' + w + g + i + g)
            else:
                print(w + '    [-]' + w + r + ' No Link Found' + r)
        except requests.exceptions.ConnectionError as e:
            print(w + '     [+] ' + w + r + 'Connection Error' + r)
    elif dork == 'X':
        print(w + '     [-] ' + w + r + 'KK bye.Exiting.' + r)
    else:
        print(w + "    [-] " + w + r + "I don't understand you!! Exiting" + r)
        sys.exit()
else:
    print(r + "    [-] I don't understand you!! Exiting" + r)
    sys.exit()
