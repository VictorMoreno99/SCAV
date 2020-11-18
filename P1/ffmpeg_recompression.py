import os

os.system('ffmpeg -i lena.png -vf scale=320:-1 lena_recompressed.png')  # We scale the image from 512x512 to 320x320
