

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

# async with aiofiles.open('temp/message_send_' + chat_name + '.txt', 'w', encoding='utf-8') as message_fl:
#     await message_fl.write(message)
#
# async with aiofiles.open('temp/message_send_' + chat_name + '.txt', 'rb') as message_fl:
#     while True:
#         data = await message_fl.read(1024)
#
#         if data == b'':
#             break
#
#         await self.loop.sock_sendall(self, self.get_structure(data))
#
#     os.remove('temp/messages_send_' + chat_name + '.txt')