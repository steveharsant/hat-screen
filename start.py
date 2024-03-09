import os
import time
from screen_lib import LCD_1inch69
from PIL import Image

def log(message, enabled=True):
    if enabled:
        print(message)

disp = LCD_1inch69()
disp.Init()
disp.bl_DutyCycle(100)

gifs_directory = './gifs'
file_names = os.listdir(gifs_directory)
duration = 30  # Maximum duration in seconds

while True:
    for file in file_names:
        disp.clear()
        start_time = time.time()
        gif = Image.open(f"{gifs_directory}/{file}")
        log(f"Opened file: {file} with {gif.n_frames} frames")

        while (time.time() - start_time) < duration:
            for i in range(0, gif.n_frames):
                gif.seek(i)
                image = gif.convert('RGBA').copy()
                disp.ShowImage(image)
                time.sleep(0.02)
