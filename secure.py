from aiogram import types

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.delete()
    await message.answer(f"Welcome on board, {members}.")


@dp.message_handler(IsGroup(), content_types=types.ContentType.CONTACT)
async def contact_share(msg: types.Message):
    await msg.delete()
    await msg.answer("Iltimos shaxsiy kontaktlarni guruhda almashmang...")


# So'kish xabarlarni o'chirish uchun bads ga qo'shimcha so'zlar yozing...
@dp.message_handler(IsGroup(), content_types=types.ContentType.TEXT)
async def bad_msg(msg: types.Message):
<<<<<<< HEAD
    bads = ['pidaraz', 'pidoraz', 'suka', 'dalbayop', 'dalpayop', 'qanjiq', 'yiban', 'yban', 'chumo', 'cumo', 'сука',
            'долбаеб', 'пидораз', 'пидараз','Хароми','хароми','Харом','харом','Хроми','хроми','Онангни ами','онангни ами',
            'Опангни ами','Чичикок','чичикок','Осирок','осирок','Морда','морда','Сука','сука','Канжик','канжик','Чумо','чумо',
            'Блят','блят','Кот','кот','Котмисан','котмисан','Йо баний врот','Итдан таркаган','итдан таркаган','Ит башара',
            'ит башара','Конченый','конченый','Аминга','аминга','Негрники','негрники','Отни котоги','Отники','Жалап','жалап',
            'Жала','жала','Соска','соска','Котогимни йепсан','котогимни йепсан','Канжу','канжу','Бле','бле','Блин','блин','Аптинга','аптинга',
            'Котинга','котинга','Амга','амга','Йепсан','йепсан','Котогими йепсан','котогими йепсан',]
            # Ака булар яхши ишларга йозилди максид холис
=======
    bads = ['pidaraz','chmo','lata','ypoд','aptinga', 'xaromi','onangni','opangni','Xaromi','haromi','xaromi','harom','xarom','chichiqo','osiroq','mordanga',
             'pidoraz', 'suka', 'dalbayop', 'dalpayop','tvar','тварь', 'qanjiq', 'yiban', 'yban', 'chumo', 'cumo', 'сука',
            'долбаеб', 'пидораз', 'пидараз','kot','Kot','kotmsan','konchenni','Kochenni','itdan tarqagan','it bashara','chlen','otsosi','Otsosi','Maraz','Gandon',
            'kotinga sqi','kotnga skey ','aminga','amnga','Aminga',' qotog bosh','Ypa','ypa','yabalnik','kotnga ske ',
            'qotogimi yepsan','negrnki','jalap','Jalap','jala','Jala','soska','Soska','qanju','Qanju','sssuka ble','ble','Ble','Blya','blya','blin','Blin',]
   #aka faqat togri chunaz atak unaqa sokindgan bola masmiz bunaqa sokinishlarni optni bollardan topib qoidik bz bulani yaxshi niyatda yozdik       
>>>>>>> 84553851e9ec77bd650c0d7a292935b098ce02cd
    for bad_word in bads:
        if bad_word in msg.text.lower():
            await msg.delete()
            await msg.answer(f"{msg.from_user.get_mention(as_html=True)} so'kinmang bo'lmasam guruhdan chiqib ketasiz! 😡")


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.delete()
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} left the group!")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.delete()
        await message.answer(f"{message.left_chat_member.full_name} banned!"
                             f"Admin: {message.from_user.get_mention(as_html=True)}.")
        
