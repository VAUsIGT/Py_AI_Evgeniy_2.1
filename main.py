import config
# запуск
print("------------------------------------------")
print(f"{config.VA_NAME} (v{config.VA_VER}) запускается..")
print("------------------------------------------")
from libraries import stt, tts #из папки библиотек (тех что нет в py)
from fuzzywuzzy import fuzz
from commands import execute_cmd


def va_respond(voice: str):
    print(voice)

    if voice.startswith(config.VA_ALIAS):
        # обращение к жене
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd']) # обращение к рукописной commands


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc

# приветствие
text = "Добрый  день, я Евгений, чем  могу быть  полезен?"
print("Евгений: " + text)
tts.va_speak(text)
print("----Попросите Женю рассказать о своих возможностях (командах)----")
# начать прослушивание команд
stt.va_listen(va_respond)
