import time, os

with open("config.txt", "r") as f:
    content = f.read().splitlines()
    distance_threshold_cm = int(content[0])
    delay = float(content[1])
    video1 = content[2]
    video2 = content[3]

def distance():
    with open("distance.txt", "r") as f: return int(f.read())

while True:
    time.sleep(delay)
    if distance() < distance_threshold_cm:
        os.system('killall -9 vlc')
        os.system(f'vlc --fullscreen --play-and-exit {video1}')
    os.system(f'vlc --fullscreen --loop {video2}')