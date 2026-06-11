TRIG = 23
ECHO = 24

import time, os, vlc, RPi.GPIO as GPIO

DISTANCE_THRESHOLD_CM = 50
DELAY = 0.2
VIDEO_1 = "video_1.mp4"
VIDEO_2 = "video_2.mp4"

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    GPIO.output(TRIG, False)
    time.sleep(0.1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    
    while GPIO.input(ECHO) == 0:
        start = time.time()
    
    while GPIO.input(ECHO) == 1:
        end = time.time()
    
    duration = end - start
    distance = duration * 34300 / 2

    return distance

print(distance())


instance = vlc.Instance()
player = instance.media_player_new()

media = instance.media_new('video.mp4')
player.set_media(media)
player.set_fullscreen(True)

player.play()

time.sleep(2)

while True:
    time.sleep(DELAY)
    res = distance()
    if res < DISTANCE_THRESHOLD_CM:
        player.set_time(0)
    player.set_time(120000)