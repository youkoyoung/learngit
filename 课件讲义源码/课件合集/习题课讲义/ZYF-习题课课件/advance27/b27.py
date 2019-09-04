# 用协程的方式完成播放

movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
music_list = ['周杰伦.mp3', '五月天.mp3']
movie_format = ['mp4', 'avi']
music_format = ['mp3']

import asyncio
import time

# @asyncio.coroutine
async def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("now playing movie named {}".format(i))
            # yield time.sleep(3)
            await asyncio.sleep(3)
        elif i.split(".")[1] in music_format:
            print("now playing music named {}".format(i))
            # yield time.sleep(2)
            await asyncio.sleep(2)
        else:
            print("NO SUPPORTED")

loop = asyncio.get_event_loop()
task = [play(movie_list), play(music_list)]
loop.run_until_complete(asyncio.wait(task))
loop.close()