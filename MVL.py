import os
import sys
import time
import configparser  # импортируем библиотеку

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("servers.ini")  # читаем конфиг

flag = True
endc = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magneto = '\033[36m'
os.system("clear")

while True:
    print(yellow + "█▄░▄█ ▀ █▄░█ █▀▀ ▄▀ █▀▀▄ ▄▀▄ █▀ ▀█")
    print(yellow + "█░█░█ █ █░▀█ █▀▀ █░ █▐█▀ █▀█ █▀ ░█░")
    print(yellow + "▀░░░▀ ▀ ▀░░▀ ▀▀▀ ░▀ ▀░▀▀ ▀░▀ ▀░ ░▀░")
    print(yellow + "▐▌░▐▌ █░░ ▄▀▄ █▄░█     █░░ ▄▀▄ █░█ █▄░█ ▄▀ █░░ █▀▀ █▀▀▄")
    print(yellow + "░▀▄▀░ █░▄ █▀█ █░▀█     █░▄ █▀█ █░█ █░▀█ █░ █▀▄ █▀▀ █▐█▀")
    print(yellow + "░░▀░░ ▀▀▀ ▀░▀ ▀░░▀     ▀▀▀ ▀░▀ ░▀░ ▀░░▀ ░▀ ▀░▀ ▀▀▀ ▀░▀▀ ")
    print(green + "Minecraft Virtual Local Area Network Launcher")
    print(green + "Minecraft виртульное локальное соединение лаунчер")
    print(red + "by kulisworm")

    print(magneto + "[" + yellow + "1" + magneto + "]" + green + "Подключится к серверам MVL")
    print(magneto + "[" + yellow + "2" + magneto + "]" + green + "Выйти")

    usercmd = input("MVL>")
    if usercmd == "1":
        print("Вы хотите установить\обновить ПО для подключения (рекомендуется)")
        usercmd = input("MVL>(y/n)")
        if usercmd == "y":
            os.system("apt update -y")
            os.system("apt install openvpn -y")
            print(yellow + "+")
            print(green + "Возврат в меню через 5 секунд")
            time.sleep(5)
        elif usercmd == "n":
            print("Загрузка серверов...")
            time.sleep(1)
            print(blue + "MVL cервера:")
            print(config["MVLservers"]["servers"])
            print(green + "Пользовательские сервера:")
            print(config["CustomUserServer"]["servers"])
            print("К каким серверам вы будете подключатся?")
            print(magneto + "[" + yellow + "1" + magneto + "]" + green + "К серверам MVL")
            print(magneto + "[" + yellow + "2" + magneto + "]" + green + "К пользовательским серверам")
            usercmd = input("MVL>")
            if usercmd == "1":
                print(yellow + "Выберите сервер:")
                print("Необходимо написать название файла конфигурации с расширением \n Например: Moscow.ovpn")
                print(config["MVLservers"]["servers"])
                usercmd = input("MVL>")
                os.system("openvpn --config " + usercmd)
                print('Произошла ошибка при подключении и\или процесс был прерван')
            elif usercmd == "2":
                print(yellow + "Выберите сервер:")
                print("Необходимо написать название файла конфигурации с расширением \n Например: Moscow.ovpn")
                print(config["CustomUserServer"]["servers"])
                usercmd = input("MVL>")
                os.system("openvpn --config " + usercmd)
                print('Произошла ошибка при подключении и\или процесс был прерван')
    elif usercmd == "2":
        sys.exit()
