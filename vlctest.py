import vlc, time

instance = vlc.Instance()
player = instance.media_player_new()

media = instance.media_new('video.mp4')
player.set_media(media)

player.play()

time.sleep(2) 

if player.is_playing():
    player.set_time(120000)

try:
    while player.is_playing():
        time.sleep(1)
except KeyboardInterrupt:
    player.stop()