import os


def runBash(command):
    os.system(command)


def crop(start, end, input, output):
    str = "ffmpeg -i " + input + " -ss  " + start + " -to " + end + " -c copy " + output
    runBash(str)


def yuv_histogram(input):
    str = "ffplay " + input + " -vf \"split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay\""
    runBash(str)


def resize(input):
    str720 = "ffmpeg -i " + input + " -vf scale=1280:720 10sec720.mp4"
    str480 = "ffmpeg -i " + input + " -vf scale=640:480 10sec480.mp4"
    str360 = "ffmpeg -i " + input + " -vf scale=360:240 10sec360.mp4"
    str160 = "ffmpeg -i " + input + " -vf scale=160:120 10sec160.mp4"

    runBash(str720)
    runBash(str480)
    runBash(str360)
    runBash(str160)


def change(input, output, codec):
    str = "ffmpeg -i " + input + " -vcodec copy -acodec " + codec + " " + codec + "video.mp4"
    runBash(str)
    str2 = "ffmpeg -i " + codec + "video.mp4 -ac 1 " + output
    runBash(str2)


def main():
    print("Introduce un número de ejercicio del 1 al 4")
    ex = int(input())
    if ex == 1:
        crop("00:05:00", "00:05:10", "BBB.mp4", "10sec.mp4")
    if ex == 2:
        yuv_histogram("10sec.mp4")
    if ex == 3:
        resize("10sec.mp4")
    if ex == 4:
        change("10sec.mp4", "10secmono.mp4", "mp3")


main()
