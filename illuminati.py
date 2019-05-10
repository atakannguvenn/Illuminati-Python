from subprocess import call
from random import choice, randint
import os, webbrowser, sys, codecs
import urllib.request
items = []
call('chcp 65001', shell=True)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

for i in range(0x30a1, 0x30ff + 1):
    items.append(str(chr(i)))
for i in range(0x4E00, 0x4E52):
    items.append(str(chr(i)))
for i in range(33, 48):
    items.append(chr(i))
for i in range(58, 127):
    items.append(chr(i))

def main(num = 6):
    urllib.request.urlretrieve("https://media.giphy.com/media/JtIRkbQdNfc1q/giphy.gif", "ehuehue.gif")
    urllib.request.urlretrieve("http://i.imgur.com/YsbKHg1.gif", "magic.gif")
    urllib.request.urlretrieve("http://www.picsymag.com/wp-content/uploads/2015/07/funny-gif17.gif", "wow.gif")
    while True:
        for color in ('a', 'b', 'c', 'd', 'e', 'f'):
            call('color ' + color, shell=True)
            if num == 30000:
                num = 6
            while (True):
                text = random_generator()
                print("".join(text))
                num += 1
                if num == 25000:
                    webbrowser.open("wow.gif")
                elif num == 15000:
                    webbrowser.open("ehuehue.gif")
                elif num == 5000:
                    webbrowser.open("magic.gif")
                if num == 30000:
                    os.system("taskkill /f /im Microsoft.Photos.exe")
                if num % 2000 == 0:
                    break

def random_generator():
    texttemp = []
    for x in range(20):
        texttemp.append("".join(choice(items) for _ in range(randint(1, 10)))
                        + randint(1, 10)*" ")
    return texttemp

main()