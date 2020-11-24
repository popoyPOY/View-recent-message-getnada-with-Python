import requests
import json
from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#=======================================#+=============================================#
def getURL(username,email):
    URL = f'https://getnada.com/api/v1/inboxes/{username}@{email}.com'
    r = requests.get(URL).json()
    #getting the latest message
    try:

        uid = r['msgs'][1]['uid']
        mes = requests.get(f'https://getnada.com/api/v1/messages/html/{uid}')
        mes1 = BeautifulSoup(mes.content,'html.parser')
        finalmes = mes1.find('div').getText()
        print(f"Email Message: {bcolors.OKGREEN}{finalmes}{bcolors.ENDC}")
    except IndexError:
        print("Your Email doesn't have a new message")


email_list = ['getnada','abyssmail','boxmail','clrmail','dropjar','getairmail','inboxbear','robot-mail','tafmail','vomoto'
,'zetmail'
]
print("LIST OF EMAIL:")
for number, email in enumerate(email_list):
    print(f"[{number}]:{email}")

while True:
    try:

        userInput = input("Name of your email: ")
        userEmail = int(input("Your Desired Email: "))
        checkEmail = email_list[userEmail]
        getURL(userInput,checkEmail)
    except:
        print("Can't interpret email message!")