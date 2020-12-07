import os
import subprocess


class Container:

    def __init__(self, file):
        self.file = file

    def runBash(self, command):
        os.system(command)

    def cut_video(self):
        input = self.file
        output = "1min_video.mp4"
        str = ("ffmpeg -i " + input + " -ss 00:00:00 -t 00:01:00 -c copy " + output)
        self.runBash(str)
        self.cut = output

    def subtitles(self):
        input = self.cut
        output = "subtitled.mp4"
        self.sub = "subtitles.srt"
        str = "ffmpeg -i " + input + " -vf subtitles=" + self.sub + " " + output
        self.runBash(str)

    def video_export(self):
        input = self.cut
        output = "exported_video.mp4"
        str = "ffmpeg -i " + input + " -ss 00:00:00 -t 00:01:00 -map 0:v:0 -c:v copy " + output
        self.runBash(str)
        self.video = output

    def mono_audio(self):
        input = self.cut
        output = "mono_audio.mp4"
        str = "ffmpeg -i " + input + " -ss 00:00:00 -t 00:01:00 -map 0:a:0 -ac 1 " + output
        self.runBash(str)
        self.mono = output

    def lowrate_audio(self):
        input = self.cut
        output = "lowrate_audio.mp4"
        str = "ffmpeg -i " + input + " -ss 00:00:00 -t 00:01:00 -map 0:a:0 -b:a 24k " + output
        self.runBash(str)
        self.lowrate = output

    def createContainer(self):
        self.cut_video()
        self.subtitles()
        self.mono_audio()
        self.lowrate_audio()
        self.video_export()
        output = "container.mp4"
        str = "ffmpeg -i " + self.mono + " -i " + self.lowrate + " -i " + self.cut + " -i " \
              + self.sub + " -ss 00:00:00 -t 00:01:00 -map 0:a:0 -map 1:a:0 -map 2:v:0 " \
                           "-c:v copy -map 3:s:0 -c:s mov_text " + output
        self.runBash(str)
        self.container = output

    def compatibility(self, input):
        com = "ffprobe -v error -select_streams v:0 -show_entries stream=codec_name " \
              "-of default=noprint_wrappers=1:nokey=1 " + input
        os.chdir("/home/worca/PycharmProjects/SCAV/P3")
        video_codec = subprocess.check_output(com, shell=True)
        video_codec = video_codec.decode("utf-8")
        com = "ffprobe -v error -select_streams a:0 -show_entries stream=codec_name " \
              "-of default=noprint_wrappers=1:nokey=1 " + input
        audio_codec = subprocess.check_output(com, shell=True)
        audio_codec = audio_codec.decode("utf-8")
        video_codec = video_codec[:len(video_codec) - 1]
        audio_codec = audio_codec[:len(audio_codec) - 1]

        if (video_codec == "mpeg2") or (video_codec == "h264"):
            if audio_codec == "aac":
                print("Your container is compatible with DVB,ISDB and DTMB")
            if audio_codec == "ac3":
                print("Your container is compatible with DVB,ATSC and DTMB")
            if audio_codec == "mp3":
                print("Your container is compatible with DVB and DTMB")
        elif (video_codec == "avs") or (video_codec == "avs+"):
            if ((audio_codec == "dra") or (audio_codec == "aac")
                    or (audio_codec == "ac3") or (audio_codec == "mp2") or (audio_codec == "mp3")):
                print("Your container is compatible with DTMB")
        else:
            print("ERROR: NO COMPATIBILITY")


def main():
    cont = Container("bbb.mp4")
    cont.createContainer()
    cont.compatibility("container.mp4")


main()
