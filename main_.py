import time, os, RPi.GPIO as GPIO

VIDEO_1 = "video_1.mp4"
VIDEO_2 = "video_2.mp4"
DIST

TRIG = 14
ECHO = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
    GPIO.output(TRIG, False)
    time.sleep(0.0002)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()
    
    while GPIO.input(ECHO) == 1:
        end = time.time()
    
    duration = end - start
    distance = duration * 34300 / 2 # in cm

    return distance

while True:
    time.sleep(DELAY)
    if distance() < DISTANCE_THRESHOLD_CM:
        os.system('killall -9 vlc')
        os.system(f'vlc --fullscreen --play-and-exit {VIDEO_1}')
    os.system(f'vlc --fullscreen --loop {VIDEO_2}')