import os


def runBash(command):
    os.system(command)


def cut_video(input):
    output = "10sec_bbb.mp4"
    str = ("ffmpeg -i " + input + " -ss 00:00:00 -t 00:00:10 -c copy " + output)
    runBash(str)


def resize(input,scale1,scale2,output):
    str = "ffmpeg -i " + input + " -vf scale=" + scale1 + ":" + scale2 + " " + output
    runBash(str)


def change_codecs(input, scale1, scale2):
    strvp8 = "ffmpeg -i " + input + " -c:v libvpx -c:a libvorbis -vf scale=" + scale1 + "x" + scale2 + \
             " vp8.webm"
    strvp9 = "ffmpeg -i " + input + " -c:v libvpx-vp9 -c:a libvorbis -vf scale=" + scale1 + "x" + scale2 + \
             " vp9.webm"
    strh265 = "ffmpeg -i " + input + " -c:v libx265 -vf scale=" + scale1 + "x" + scale2 + \
              " h265.mp4"
    strav1 = "ffmpeg -i " + input + " -c:v libaom-av1 -vf scale=" + scale1 + "x" + scale2 + \
             " av1.mp4"

    runBash(strvp8)
    runBash(strvp9)
    runBash(strh265)
    runBash(strav1)


def montage(input1, input2, input3, input4):
    str = 'ffmpeg -i ' + input1 + ' -i ' + input2 + ' -i ' + input3 + ' -i ' + input4 + \
          ' -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]"' \
          ' -map "[v]" montage.mp4'
    runBash(str)


def stream():
    str = "ffmpeg -i bbb.mp4 -v 0 -vcodec mpeg4 -acodec copy -b:v 64k -f mpegts udp://127.0.0.1:1234"
    runBash(str)


def main():
    print("You want to change codecs(1) or stream the video(2)")
    ex = int(input())
    if ex == 1:
        print("In which sizes do you want do resize? \n")
        print("Size 1: ")
        scale1 = str(input())
        print("Size 2: ")
        scale2 = str(input())
        cut_video("bbb.mp4")
        resize("10sec_bbb.mp4", scale1, scale2, "resized.mp4")
        change_codecs("resized.mp4", scale1, scale2)
        montage("av1.mp4", "vp8.webm", "vp9.webm", "h265.mp4")
    if ex == 2:
        stream()


main()