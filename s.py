import os.path
import urllib.request
from urllib.request import Request, urlopen
import subprocess
import sys
import base64
import urllib.request
import ssl
import requests
import json
import pathlib
from termcolor import colored

def say(text):
    print(colored(text, 'green', attrs=['bold']))
def error(text):
    print(colored(text, 'red', attrs=['bold']))
ssl._create_default_https_context = ssl._create_unverified_context
ipAddressUrl = 'https://mcsimakyr-default-rtdb.europe-west1.firebasedatabase.app/ip-address.json'
def getAddress():
    req = urllib.request.Request(ipAddressUrl)
    with urllib.request.urlopen(req) as response:
       return json.loads(response.read().decode("utf-8"))
def decB64(i):
    base64_string = i
    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    return sample_string
configFile = "YmVkcm9jazoKICBhZGRyZXNzOiAwLjAuMC4wCiAgcG9ydDogMTkxMzIKICBjbG9uZS1yZW1vdGUtcG9ydDogZmFsc2UKICBtb3RkMTogIlBST1NUTyBTSU1BS1lSIgogIG1vdGQyOiAiU0lNQUtZUiBUWVQiCiAgc2VydmVyLW5hbWU6ICJUWVQgTkVUIFNJTUFLWVJBIgpyZW1vdGU6CiAgYWRkcmVzczogYXV0bwogIHBvcnQ6IDI1NTY1CiAgYXV0aC10eXBlOiBvZmZsaW5lCmNvbW1hbmQtc3VnZ2VzdGlvbnM6IHRydWUKcGFzc3Rocm91Z2gtbW90ZDogZmFsc2UKcGFzc3Rocm91Z2gtcHJvdG9jb2wtbmFtZTogZmFsc2UKcGFzc3Rocm91Z2gtcGxheWVyLWNvdW50czogdHJ1ZQpsZWdhY3ktcGluZy1wYXNzdGhyb3VnaDogZmFsc2UKcGluZy1wYXNzdGhyb3VnaC1pbnRlcnZhbDogMwptYXgtcGxheWVyczogOTk5CmRlYnVnLW1vZGU6IGZhbHNlCmdlbmVyYWwtdGhyZWFkLXBvb2w6IDMyCmFsbG93LXRoaXJkLXBhcnR5LWNhcGVzOiB0cnVlCmFsbG93LXRoaXJkLXBhcnR5LWVhcnM6IGZhbHNlCnNob3ctY29vbGRvd246IHRydWUKY2FjaGUtY2h1bmtzOiB0cnVlCmNhY2hlLWltYWdlczogMAphYm92ZS1iZWRyb2NrLW5ldGhlci1idWlsZGluZzogZmFsc2UKZm9yY2UtcmVzb3VyY2UtcGFja3M6IHRydWUKeGJveC1hY2hpZXZlbWVudHMtZW5hYmxlZDogZmFsc2UKbWV0cmljczoKICBlbmFibGVkOiBmYWxzZQogIHV1aWQ6IDg1Zjk2MzcwLWNlNGQtNDhkYi1iNjhlLWUzZTI2Y2RlNDg4ZgpzY29yZWJvYXJkLXBhY2tldC10aHJlc2hvbGQ6IDIwCmVuYWJsZS1wcm94eS1jb25uZWN0aW9uczogZmFsc2UKdXNlLWFkYXB0ZXJzOiB0cnVlCgpjb25maWctdmVyc2lvbjogNA=="
dbg = False

error("=============================================")
say("Программа по подключению к серверу Майнкрафт")
say("Создал:   SimaKyr.")
say("Сайт: https://simakyr.github.io/mcs/")
error("=============================================")

stPgFile = 'installed_yn'
def run_command(command):
    p = subprocess.Popen(command,
    stdout = subprocess.PIPE,
    stderr = subprocess.STDOUT)
    return iter(p.stdout.readline, b'')
if(len(sys.argv) == 2):
    if(sys.argv[1] == "h"):
        say("Привет! Что требуем:")
        say("1 - Сброс параметров")
        say("2 - Режим отладки")
        say("\n")
        i = str(input("Введите число:"))
        if(i == "1"):
            if(os.path.exists(stPgFile)):
              os.remove(stPgFile)
            say("Сбросено! Продолжаем обычное выполнение...")
        if(i == '2'):
            dbg = True
            say("Вкючили режим отладки! Продолжаем обычное выполнение...")
urlGC = 'https://ci.opencollab.dev/job/GeyserMC/job/Geyser/job/master/lastSuccessfulBuild/artifact/bootstrap/standalone/target/Geyser.jar'

stPg = False

logo = "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#+=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@+++=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW+++++=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*+++++*=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=++++****=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#++++*****:=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@++++****+:::=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*+++****+:::::=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*+++****+:::::::=WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW=+++****+++::::::+WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#+++****+++++::::#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWW@+++****+++++++:*@WW*#WWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWW*+:+***++++++++#@@#+:+#WWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWW@=+::***+++++++*@@@*++:++@WWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWW@#+::+**+++++++#@@=++++:+++@WWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWW@:::+**++++++*@@@*+++++:++++@WWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWW@+:::**++++++#@@=+++++++:+++++WWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWW*:::+*+++++*@@#***++++++::++++*WWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWW=::::*+++++#@@@@**+++++++::+++++*WWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWW#::::+++++*@@@@@@@@*++++++:::+++++*WWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWW@:::::*+++#@@@@@@@@@@@*++++::::+++++=WWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWW+::::+***@@@@@@@@@@@@@W@*++:::+++++++=WWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWW*:::::**#WW@@@@@@@@@@WWWWWW=:::++++++++#WWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWW=:::::+=WWWWWWWW@@@WWWWWWWWWWW=:+++++++++#WWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWW@::::::@WWWWWWWWWWWWWWWW@@@@@@##@=+++++++++@WWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWW:::::::::::::::::::::::::+++=@WWWWW#*****+++@WWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWW+::::::::::::::::+++++++*#WWWWWWWWWWWW#****+++@WWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWW=::::::::++********+*=@WWWWWWWWWWWWWWWWWW#***+:+WWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWW#++***************#WWWWWWWWWWWWWWWWWWWWWWWWW#==*:+WWWWWWWWWWWWW\nWWWWWWWWWWWWWWWW=************=@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#==+*WWWWWWWWWWWW\nWWWWWWWWWWWWWWW=*********#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#=**WWWWWWWWWWW\nWWWWWWWWWWWWWW#*****=@WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW#==WWWWWWWWWW\nWWWWWWWWWWWWW@**#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW##WWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\nWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW\n"
def split_host_port(string):
    if not string.rsplit(':', 1)[-1].isdigit():
        return (string, None)

    string = string.rsplit(':', 1)

    host = string[0]  # 1st index is always host
    port = str(string[1])

    return (host, port)
def main():
    print(colored(logo, 'blue', attrs=['blink']))
    say("Приветствую вас!")
    if(dbg):
        say("Проверяем установлена ли данная программа...")
    #say("Введите адрес сервера MINECRAFT: JAVA EDITION.")
    #say("Он должен выглядить так *.tcp.ngrok.io:*****")
    #ip = str(input("Адрес сервера:"))
    ip = getAddress()
    if(dbg):
        say("Адрес сервера:" + ip)
    if(dbg):
        say("Запись новых параметров...")
    cfg = decB64(configFile)
    cfg = cfg.replace("auto", split_host_port(ip)[0]).replace("25565", split_host_port(ip)[1])

    f = open("config.yml", "w", encoding='utf-8')
    f.write(cfg)
    f.close()
    say('=====================================================================')
    say('Для подключения зайдите в MINECRAFT -> Играть -> Друзья -> TYT PROSTO')
    say('=====================================================================')
    say('Подробнее на сайте: https://simakyr.github.io/mcs/')
    if(dbg):
        say("Запуск...")
    try:
        prg = './geysermc.sh'
        # say(prg)
        #subprocess.call(['java', '-jar', str(pathlib.Path().absolute()) + '/geyser.jar'])
        subprocess.call(prg)
    except:
        error('Наверное это не Termux!')
        subprocess.call("java -jar geysermc.jar")
if(os.path.exists(stPgFile)):
    if(dbg):
        say("Программа уже установлена! Отлично!")
    stPg = True
    main()
else:
    if(dbg):
        error("Программа не установлена )-: Начинаем установку...")

    say("Начием скачивать установщик JAVA...")
    with urllib.request.urlopen('http://raw.githubusercontent.com/MasterDevX/java/master/installjava') as f:
        html = f.read().decode('utf-8')
        f = open("installjava", "w", encoding='utf-8')
        f.write(html)
        f.close()

        #st = os.stat('installjava')
        #os.chmod('installjava', st.st_mode | os.stat.S_IEXEC)

        say("JAVA установщик скачан. Устанавливаем JAVA...")
        try:
            os.chmod(str(pathlib.Path().absolute()) + "/installjava", 0o775)
            subprocess.call("./installjava")
        except:
            error('Неудача. Наверное это Windows.')
        say("Скачиваем сервер GeyserMC...")
        file_name = "geysermc.jar"
        with open(file_name, "wb") as f:
            response = requests.get(urlGC, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                    sys.stdout.flush()
        f.close()
        say("Скачивание успешно завершено!")

        say("Устанавливаем GeyserMC...")
        f = open("geyser.sh", "w", encoding='utf-8')
        f.write('#!/bin/bash\ntermux-chroot\njava -jar geysermc.jar')
        f.close()
        os.chmod(str(pathlib.Path().absolute()) + "/geyser.sh", 0o775)
        say("Установка GeyserMC завершена!")

        f = open(stPgFile, "a")
        f.write("Привет! Этот файл не удалять \(-:")
        f.close()
        say("Для повторного запуска используй:")
        error("./s")
        say("Перезапуск...")
        main()
