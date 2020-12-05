import os


def runBash(command):
    os.system(command)

def analysis(input, output):
    str = "ffmpeg -i " + input + " 2> " + output
    runBash(str)
    strings = ("Duration")
    file = open(output, 'r')
    for line in file:
        if strings in line:
            print(line)
            break

def changename(oldname1,newname1):
    str1 = os.getcwd() + "/" + oldname1
    str2 = os.getcwd() + "/" + newname1
    os.rename(str1, str2)

def resize(input,scale1,scale2,output):
    str = "ffmpeg -i " + input + " -vf scale=" + scale1 + ":" + scale2 + " " + output
    runBash(str)

def change(input, output, audiocodec, videocodec):
    str = "ffmpeg -i " + input + " -c:v " + videocodec + " -c:a " + audiocodec + " " + output
    runBash(str)


def main():
    print("Introduce un número de ejercicio del 1 al 4")
    ex = int(input())
    if ex == 1:
        print("Introduce the name of the video you want to analyze")
        name = str(input())
        analysis(name, "output.txt")
    if ex == 2:
        print("Introduce the name of the video you want to rename")
        oldname = str(input())
        print("Introduce the new name with its format")
        newname = str(input())
        changename(oldname, newname)
    if ex == 3:
        print("Introduce the name of the video you want to resize")
        name = str(input())
        print("Introduce the first size")
        firstsize = str(input())
        print("Introduce the second size")
        secondsize = str(input())
        print("Introduce the new video name with its format")
        output = str(input())
        resize(name, firstsize, secondsize, output)
    if ex == 4:
        print("Introduce the name of the video you want to change the codecs")
        name = str(input())
        print("Introduce the new audio codec")
        audiocodec = str(input())
        print("Introduce the new video codec")
        videocodec = str(input())
        print("Introduce the new video name with its final format")
        output = str(input())
        change(name, output, audiocodec, videocodec)

main()

