from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import discord
import time
import threading

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    now = time.localtime()

    check_server = []
    check = open("서버 종류.txt", 'a', encoding="utf-8")
    check_r = open("서버 종류.txt", 'r', encoding="utf-8")

    lines = check_r.readlines()
    for i in lines:
        check_server.append(i.split("\n")[0])

    if message.guild.name not in check_server:
        check.write(message.guild.name+"\n")

    f = open("명령어.txt", 'r', encoding="utf-8")
    g = open("명령어.txt", 'a', encoding="utf-8")
    h = open("명령어-관리자.txt", 'a', encoding="utf-8")
    m = open("명령어-관리자.txt", 'r', encoding="utf-8")
    k = open("출첵_"+message.guild.name+".txt", 'a', encoding="utf-8")
    l = open("출첵_"+message.guild.name+".txt", 'r', encoding="utf-8")
    q = open("주접.txt", 'r', encoding="utf-8")
    u = open("주접글.txt", 'r', encoding="utf-8")
    v = open("주접글.txt", 'a', encoding="utf-8")
    ACC_R = open("attentioncheckcommand.txt", 'r', encoding="utf-8")
    ACC_A = open("attentioncheckcommand.txt", 'a', encoding="utf-8")
    #ACC_W = open("attentioncheckcommand.txt", 'w', encoding="utf-8")
    command_dic = {"server":message.guild.name, "호밀구두":"", "sender":"sender : "+str(message.author), "message":message, "channel":"channel : "+str(message.channel.name), "현재시간":"현재 시간은 %02d시 %02d분입니다."%(now.tm_hour, now.tm_min)}
    attentioncheckcommand = {}
    cut = []
    cute = {}
    command_user = {}
    command_mas_user = {}
    command_mas_dic = {}
    attendance_list = []

    attentioncheckcommand_db = ACC_R.readlines()
    for i in attentioncheckcommand_db:
        attentioncheckcommand[i.split(" : ")[0]] = i.split(" : ")[1].split("\n")[0]

    cut_db = u.readlines()
    for i in cut_db:
        cut.append(i.split("\n")[0])

    cute_db = q.readlines()
    for i in cute_db:
        cute[i.split(" : ")[0]] = i.split(" : ")[1].split("\n")[0]
    cute_keys = cute.keys()

    command_mas_db = m.readlines()
    for i in command_mas_db:
        command_mas_dic[i.split(" : ")[0]] = i.split(" : ")[1].split(" - ")[0]
        command_mas_user[i.split(" : ")[0]] = i.split(" : ")[1].split(" - ")[1].split("\n")[0]
    command_mas_keys = command_mas_dic.keys()
    m.close()

    #명령어 목록 받아오기
    command_db = f.readlines()
    for i in command_db:
        command_dic[i.split(" : ")[0]] = i.split(" : ")[1].split(" - ")[0]
        command_user[i.split(" : ")[0]] = i.split(" : ")[1].split(" - ")[1].split("\n")[0]
    command_keys = command_dic.keys()
    f.close()

    #"$명령어 목록" 명령어 설정
    command_dic["명령어 목록"] = "명령어 목록입니다.\n"+"\n".join(list(command_keys))
    command_keys = command_dic.keys()

    #출석 현황 받아오기
    attendance_db = l.readlines()
    for i in attendance_db:
        attendance_list.append(i.split("\n")[0])
    l.close()

    msg = message.content


    #여기부터 반응 시작
    if message.guild.name in list(attentioncheckcommand.keys()):
        if msg == attentioncheckcommand[message.guild.name]:
            if str(message.author) in attendance_list:
                await message.channel.send(str(message.author)+"님은 이미 출석하셨습니다.")
                return
            else:
                k.write(str(message.author)+"\n")
                await message.channel.send(str(message.author) + "님의 출석이 인증되었습니다.")
                await message.channel.send("해당 서버에서의 " + str(len(attendance_list)+1) + "번째 출석입니다.")
                l.close()
                return
    else:
        if msg == "출첵":
            if str(message.author) in attendance_list:
                await message.channel.send(str(message.author)+"님은 이미 출석하셨습니다.")
                return
            else:
                k.write(str(message.author)+"\n")
                await message.channel.send(str(message.author) + "님의 출석이 인증되었습니다.")
                await message.channel.send("해당 서버에서의 " + str(len(attendance_list)+1) + "번째 출석입니다.")
                l.close()
                return

    if msg == "-메-":
        await message.channel.send("메이플 스토리~~~~\nM~~~")

    if msg[0] == "$":
        msg = msg[1:]






        if msg[:2] == "주접":
            if msg == "주접":
                ran = random.randint(0, len(cut)-1)
                await message.channel.send(cut[ran])
                return

            if msg.split("#")[0] == "주접추가":
                v.write(msg.split("#")[1] + "\n")
                await message.channel.send("추가 완료")
                return

            if len(msg.split("#"))>1:
                if msg[:4] == "주접설정":
                    t = open("주접.txt", 'w', encoding="utf-8")
                    cute[str(message.author)] = int(msg.split("#")[1])
                    cute_re = ""
                    for i in cute_keys:
                        cute_re += str(str(i) + " : " + str(cute[i]) + "\n")
                    t.write(cute_re)
                    print(cute_re)
                    t.close()
                    await message.channel.send("업로드 완료")
                    return
                elif msg[:4] == "주접농도":
                    target = "#".join(msg.split("#")[1:])
                    if target in cute_keys:
                        await message.channel.send(target+"의 현재 혈중 주접농도 : "+cute[target])
                        return
                    else:
                        await message.channel.send("그런 사람 없는디...")
                        return
            else:
                if msg == "주접농도":
                    print(cute, str(message.author))
                    await message.channel.send(str(message.author) + "님의 현재 혈중 주접농도 : " + cute[str(message.author)])
                    return



        if msg == "주사위":
            await message.channel.send("주사위를 굴립니다......\n"+str(random.randint(1, 6))+"이 나왔어요!!!")
            return

        if msg == "출석자":
            if len(attendance_list) > 0:
                await message.channel.send("\n".join(attendance_list))
                return
            else:
                await message.channel.send("출석자가 없습니다.")
                return

        if msg.split("#")[0] == "추가":
            command = msg.split("#")[1]
            responce = msg.split("#")[2]
            if command in command_keys:
                await message.channel.send("이미 존재하는 명령어 입니다.")
                return
            else:
                g.write(command + " : " + responce + " - " + message.author.name+"\n")
                h.write(command + " : " + responce + " - " + str(message.author)+"\n")
                await message.channel.send("『"+command+"』에 대한 반응으로 『"+responce+"』가 추가되었습니다.")
                g.close()
                h.close()
                return

        if msg.split("#")[0] == "상태":
            if str(message.author) == "justchatting#1231":
                state = msg.split("#")[1]

                if state == "온라인":
                    act = msg.split("#")[2]
                    if act == "game":
                        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.Game(name=msg.split("#")[3])))
                        await message.channel.send("상태가 변경되었습니다.")
                        return
                    if act == "streaming":
                        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.Streaming(name="JustChatting")))
                        await message.channel.send("상태가 변경되었습니다.")
                        return
                    if act == "listening":
                        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=msg.split("#")[3]))
                        await message.channel.send("상태가 변경되었습니다.")
                        return
                    if act == "watching":
                        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=msg.split("#")[3]))
                        await message.channel.send("상태가 변경되었습니다.")
                        return
                if state == "자리비움":
                    await client.change_presence(status=discord.Status.idle)
                    await message.channel.send("상태가 변경되었습니다.")
                    return
                if state == "다른용무":
                    await client.change_presence(status=discord.Status.do_not_disturb)
                    await message.channel.send("상태가 변경되었습니다.")
                    return
                if state == "오프라인":
                    await client.change_presence(status=discord.Status.offline)
                    await message.channel.send("상태가 변경되었습니다.")
                    return

        if msg in command_keys:
            await message.channel.send(command_dic[msg])
            return

        if msg.split("#")[0] == "제거":
            if msg.split("#")[1] in command_keys:
                a = open("명령어.txt", 'w', encoding="utf-8")
                b = open("명령어-관리자.txt", 'w', encoding="utf-8")
                del command_dic[msg.split("#")[1]]
                del command_user[msg.split("#")[1]]
                del command_mas_dic[msg.split("#")[1]]
                del command_mas_user[msg.split("#")[1]]
                command_mas_keys = list(command_mas_user.keys())
                command_keys = list(command_user.keys())
                command_remove = ""
                command_mas_remove = ""
                for i in command_keys:
                    command_remove += str(i+" : "+command_dic[i]+" - "+command_user[i]+"\n")
                for i in command_mas_keys:
                    command_mas_remove += str(i + " : " + command_mas_dic[i] + " - " + command_mas_user[i] + "\n")
                a.write(command_remove)
                b.write(command_mas_remove)
                await message.channel.send("명령어가 제거되었습니다.")
                a.close()
                b.close()
                return
            else:
                await message.channel.send("그런 명령어는 존재하지 않습니다.")
                return
        else:
            await message.channel.send("그런 명령어는 읍서")


client.run('NzE1MTQ3Mzg5NjE4MzU2MzE2.Xtcwhg.K20W-kWA1Uo3ReZ8eesBNdlMyj8')