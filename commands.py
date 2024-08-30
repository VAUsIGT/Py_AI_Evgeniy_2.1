import datetime, webbrowser, random, os, time
from libraries.num2t4ru import num2text #https://github.com/Yuego/num2t4ru
from libraries import stt, tts #из папки библиотек (тех что нет в py)
import sys
from libraries.Sound.sound import Sound #управление звуком ОС (временно выключено) https://github.com/Paradoxis/Windows-Sound-Manager
def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        print(
            "Я умею: произносить время, рассказывать анекдоты, включать музыку, делать заметки, могу рассказать о себе, рассказать о командах, хрюкать, выключать компьютер, могу сам выключаться, управлять громкостью и открывать браузер")
        text = "Я умею: ...."
        text += "произносить время ...."
        text += "рассказывать анекдоты ...."
        text += "включать музыку...."
        text += "делать заметки.."
        text += "могу рассказать о себе...."
        text += "рассказать о командах...."
        text += "хрюкать...."
        text += "выключать компьютер...."
        text += "могу сам выключаться...."
        text += "управлять громкостью...."
        text += "и открывать браузер"
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейч+ас " + num2text(now.hour) + " " + num2text(now.minute)
        print("Сейчас " + str(now.hour) + ":" + str(now.minute))
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']
        text = random.choice(jokes)
        print("Евгений: " + text)
        tts.va_speak(text)


    elif cmd == "hello":
        hello = ["Здраствуйте",
                 "Добрый день",
                 "Здравия желаю!",
                 "Аве!",
                 "Алоха!"]
        text = random.choice(hello)
        print("Евгений: " + text)
        tts.va_speak(text)

    elif cmd == "yandex":
        webbrowser.open("https://yandex.ru/search/")  # доработать {} ?text={}

    elif cmd == "ratio":
        text = "Включаю музыку"
        print("Евгений: " + text)
        tts.va_speak(text)
        os.system("C:/Users/XOMA/PycharmProjects/py_AI_Evgeniy_2.1/best.mp3")

    elif cmd == "stop":
        text = ("До новых встреч!")
        print("Евгений: " + text)
        tts.va_speak(text)
        sys.exit()

    elif cmd == "pig":
        text = ("Хрю-хрю!")
        print("Евгений: " + text)
        tts.va_speak(text)

    elif cmd == "history":
        text = (
            "Меня создал GIT / ГИТ, Я называюсь ЕВГЕНИЙ, то есть - единый виртуальный гениальный евро настраивающийся интелект йотирования, люблю печеньки и диван.")
        print("Евгений: " + text)
        tts.va_speak(text)

    elif cmd == "off":
        text = ("Чтобы выключить компьютер скажите: женя 46")
        text1 = ("Чтобы выключить компьютер скажите: женя, сорок шесть")
        print("Евгений: " + text)
        tts.va_speak(text1)

    elif cmd == "off-true":
        text = ("Выключение компьютера, не забудьте сохранить данные")
        print("Евгений: " + text)
        tts.va_speak(text)
        os.system('shutdown -s')

    elif cmd == "thanks":
        text = ("Всегда пожалуйста")
        print("Евгений: " + text)
        tts.va_speak(text)

    elif cmd == "IGT":
        os.startfile("C:/Program^ Files/obs-studio/bin/64bit/obs64.exe")

    elif cmd == "console":
        os.startfile("C:/WINDOWS/system32/cmd.exe")

    elif cmd == "-volume":
        Sound.volume_down()
    elif cmd == "+volume":
        Sound.volume_up()
    elif cmd == "off-volume":
        Sound.mute()
    elif cmd == "on-volume":
        Sound.volume_max()
    elif cmd == "min-volume":
        Sound.volume_set(10)
    elif cmd == "max-volume":
        Sound.volume_set(100)

    else:
        print("Вы что-то сказали? Я не расслышал...")