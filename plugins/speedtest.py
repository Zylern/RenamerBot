import pyrogram
from pyrogram import Client as zylern
from pyrogram import filters
from pyrogram.types import Message
from speedtest import Speedtest

@zylern.on_message(pyrogram.filters.command(['speedtest', 'speed']))
async def start(_, hola: Message):
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    await hola.reply(
        text=
           "**➩ Download:** "
           f"{speed_convert(result['download'])} \n"
           "**➩ Upload:** "
           f"{speed_convert(result['upload'])} \n"
          "**➩ Ping:** "
           f"{result['ping']} \n"
          "**➩ ISP** "
           f"{result['client']['isp']}")

def speed_convert(size):
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"
    
