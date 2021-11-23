import pyaudio
import wave
import sys


def play():
    chunk = 1024 # 2014kb
    wf = wave.open(r"data/music/test1.wav", 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)

    data = wf.readframes(chunk)  # читать данные
    print(data)

    while True:
        data = wf.readframes(chunk)
        if data == "":
            break
        stream.write(data)

    stream.stop_stream()  # Остановить поток данных

    stream.close()
    p.terminate()  # Закрыть PyAudio
    print('Конец функции воспроизведения!')

if __name__ == '__main__':
    audio_file = 'data/music/portugal-the-man-feel-it-still.mp3'  # Укажите файл записи
    play()  # Воспроизвести файл записи