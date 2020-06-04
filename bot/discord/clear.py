import threading
import datetime

def clear():
    check = open("서버 종류.txt", 'r', encoding="utf-8")
    check_list = check.readlines()
    server = []
    print("Start Clearing : "+str(datetime.datetime.now())+"\n")
    for i in check_list:
        server.append(i.split("\n")[0])
        cls = open("출첵_" + i.split("\n")[0] + ".txt", 'w')
        cls.write("")
        cls.close()
        print("clear the file : "+i)
    threading.Timer(86400, clear).start()


if __name__ == "__main__":
    clear()