# by: t.me/Mikthon

import random
import requests

import telethon
from telethon.sync import functions
from user_agent import generate_user_agent
from help import *
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread
import threading
import asyncio
from telethon import events

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)
trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", s[0], "_", d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(a)
            f = [c[0], "_", s[0], "_", d[0]]
            username = ''.join(f)
        else:
            pass
    elif choice == "ثلاثي5":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+"_"+d+"_"+d
        f2 = c+"_"+d+"_"+c
        f3 = c+"_"+c+"_"+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f
    elif choice == "ثلاثي1":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(a)
        f = [c[0], "_", s[0], "_", d[0]]
        username = ''.join(f)
    elif choice == "ثلاثي2":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(b)
        f = [c[0], "_", s[0], "_", d[0]]
        username = ''.join(f)

    elif choice == "ثلاثي3":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(b)
        f = [c[0], "_", s[0], "_", d[0]]
        username = ''.join(f)

    elif choice == "ثلاثي4":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(a)
        f = [c[0], "_", s[0], "_", d[0]]
        username = ''.join(f)

    elif choice == "ثلاثي6":
        c = d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", s[0], "_", c[0]]
        username = ''.join(f)
        
    elif choice == "ثلاثي7":
        c = d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", s[0], "_", s[0]]    
        username = ''.join(f)
        
    elif choice == "ثلاثي8":
        c = d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", c[0], "_", s[0]]    
        username = ''.join(f)
    else:
        return "error"
    return username


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.الصيد"))
async def _(event):
    await event.edit(
        '''
**-- -- -- -- -- -- -- -- --
 الانواع :
 -- -- -- -- - 
 ثلاثي
 s_x_e - s_i_9 - s_7_q
{ ثلاثي عشوائي - كود فحص القديم }
×××××××××××××××××××××××
 ثلاثي1
 s_x_1 - s_j_9
{ ثلاثي رقم بلخير }
×××××××××××××××××××××××
 ثلاثي2
 s_6_c - s_3_m
 { ثلاثي رقم بلنص }
×××××××××××××××××××××××
 ثلاثي3
 s_8_9 - a_1_9
 { ثلاثي رقمين }
×××××××××××××××××××××××
 ثلاثي4
 a_i_e - a_m_o
 { ثلاثي حروف }
×××××××××××××××××××××××
 ثلاثي5
 s_x_s - s_s_m - x_a_a
 { مكرر عشوائي }
×××××××××××××××××××××××
 ثلاثي6
 s_x_s - s_3_s
 { ثلاثي مكرر تغير وسط }
×××××××××××××××××××××××
  ثلاثي7
 x_s_s - x_8_8
 { ثلاثي مكرر تغير بدايه }
×××××××××××××××××××××××
 ثلاثي8
 s_s_m - s_s_8
 { ثلاثي مكرر تغير بلخير }
×××××××××××××××××××××××
   طريقه الصيد هيه كالتالي
 - .صيد + نوع الصيد تكتب الاسم 
هوه ينشأ قناة تلقائي ويفحص بيها
 -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- 
مثال: .صيد ثلاثي
 ---------------------------------------------------------------------- — — — —
 الامر:  `.صيد` + النوع
 - يقوم بصيد معرفات عشوائية حسب النوع

 ٴ— — — — — — — — — —
 الامر:   `.حالة الصيد`
 • لمعرفة عدد المحاولات للصيد

@lllllj **

'''
    )

@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.صيد"))
async def hunterusername(event):
    msg = event.text.split()
    choice = str(msg[1])
    try:
        ch = str(msg[2])
        if "@" in ch:
            ch = ch.replace("@", "")
        await event.edit(f"جاري فحص نوع {choice} في @{ch} .")
    except:
        try:
            ch = await eighthon(
                functions.channels.CreateChannelRequest(
                    title="تم صيد يوزر ثلاثي",
                    about="تم الصيد معرف ثلاثي",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**تم انشاء القناة بنجاح .. سيتم صيد نوع {choice} !**")
        except Exception as e:
            await eighthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
            )
    isclaim.clear()
    isclaim.append("on")
    for i in range(19000000):
        username = gen_user(choice)
        if username == "error":
            await event.edit("** يرجى وضع النوع بشكل صحيح**.")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await eighthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"⌯ 𓆩 Source Max #1 🔔 !'𓆪\n⎱ User : ↣ (@{username}❳!\n⎱ Hunting type : {choice}\n⎱ Reminder : #x5",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await eighthon.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                else:
                    await eighthon.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")
    await event.client.send_message(event.chat_id, "انتهاء الفحص تم الصيد معرف ثلاثي")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت"))
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await eighthon(
                functions.channels.CreateChannelRequest(
                    title="صيد يوزرات ",
                    about="تم الصيد ",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await eighthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    for i in range(1000000000000):
        isav = check_user(username)
        if isav == True:
            try:
                await eighthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} !\n-  !\n- Hunting Log {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                break
            except telethon.errors.FloodError as e:
                await eighthon.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                break
            except Exception as eee:
                await eighthon.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                break
        else:
            pass
        trys2[0] += 1

        await asyncio.sleep(1.3)
    isclaim.clear()
    isclaim.append("off")
    await eighthon.send_message(event.chat_id, "**- تم الانتهاء من التثبيت بنجاح**")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
async def _(event):
    if "on" in isclaim:
        await event.edit(f"** الصيد وصل لـ({trys[0]}) من المحاولات**")
    elif "off" in isclaim:
        await event.edit("** الصيد  لا يعمل .**")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت"))
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.ت (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

            @eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة ت "))
            async def _(event):
                if "on" in isauto:
                    msg = await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
                elif "off" in isauto:
                    await event.edit("لايوجد تثبيت شغال !")
                else:
                    await event.edit("خطأ")
            for i in range(int(msg[0])):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await eighthon(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        await event.client.send_message(event.chat_id, f'''** 
𝙷𝚄𝙽𝚃𝙸𝙽𝙶 (@{username})
× ᴄʟɪᴄᴋs ↬  {trys}
lD: @Max985 / @P8_PP × @HFFHH **
    ''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:

                        await eighthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                trys += 1

                await asyncio.sleep(0.1)
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await eighthon.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await eighthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''**
𝙷𝚄𝙽𝚃𝙸𝙽𝙶 (@{username})
× ᴄʟɪᴄᴋs ↬  {trys}
-- -- -- -- -- -- -- -- -- -- -- -- -- **
    ''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await eighthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')

Threads=[] 
for t in range(100):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()
