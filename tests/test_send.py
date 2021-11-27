

import asyncio
import aiofiles


async def get_file():
    async with aiofiles.open('thisfile.txt', 'w') as thisfile_fl:
        await thisfile_fl.write(' dsfasdfsadfsadfdsafdsafdfdsfsdfdsffdsfdsfdsfsd'
                                'asdfsadfsdfsdfdsfdsfdasfdddddddddddddddddddddd'
                                'adsfffffffffffffffffffffffffffffffffffffffffff'
                                'asdfdsafsdafasdfsdafdfdfdsfsdafasdfsdafsdafsad')


asyncio.run(get_file())

with open('thisfile.txt', 'rb') as thisfile_fl:
    # while True:
    #     data = thisfile_fl.read(10)
    #     print(data)
    #
    #     if data == b'':
    #         break

    for i in thisfile_fl.read(10):
        print(i)