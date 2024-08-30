import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000 # 48000
speaker = 'aidar' # aidar, baya, kseniya, xenia, random   выбираем голос
put_accent = True #акцент (знаки препинания)
put_yo = True
device = torch.device('cpu') # cpu или gpu
text = "GIT"

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models', #откуда брать модель
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)


# воспроизводим
def va_speak(what: str):
    audio = model.apply_tts(text=what+"..", # настройки модели
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5) # сон на время воспроизведения (делим число массива numpy на дискретизацию
    sd.stop()

# sd.play(audio, sample_rate)
# time.sleep(len(audio) / sample_rate)
# sd.stop()