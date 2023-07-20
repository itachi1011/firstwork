
import logging
from  aiogram import Bot,Dispatcher,executor
from aiogram.types import *
from keyboards import *

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "6227937062:AAFKOeqJqVUH7_tW0yA-TUF5lpZ6eTA3TuE"

bot = Bot(token=BOT_TOKEN,parse_mode="html")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_bot(message:Message):
    btn = await cals_btn()
    await message.answer("0",reply_markup=btn)

@dp.callback_query_handler(text_contains = "num")
async def cals_num_callback(call : CallbackQuery):
    selected_num = call.data.split(":")[-1]
    now_num = call.message.text
    if now_num != "0" :
        new_num = now_num + selected_num
    else : 
        new_num =selected_num
    btn = call.message.reply_markup
    await call.message.edit_text(new_num,reply_markup=btn)    


@dp.callback_query_handler(text_contains='equ')
async def calc_equ_callback(call: CallbackQuery):
    selected_equ = call.data.split(":")[-1]
    equ_list = ['/', '*', '+', '-', '**', '%', '.']
    now_num = call.message.text
    if now_num[-1] in equ_list:
        await call.answer("❌", show_alert=True)
    else:
        new_num = now_num + selected_equ
        btn = call.message.reply_markup
        await call.message.edit_text(new_num, reply_markup=btn)



@dp.callback_query_handler(text="clear")
async def cals_clear_callback(call:CallbackQuery):
    now_num = call.message.text
    if now_num != "0":
        btn = call.message.reply_markup
        await call.message.edit_text("0", reply_markup=btn)



        


if name =="main":
    executor.start_polling(dp)

Asadbek, [20.07.2023 9:06]
from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton


async def cals_btn():
    btn = InlineKeyboardMarkup(row_width=4)
    btn.add(
        InlineKeyboardButton("©️",callback_data="clear"),
        InlineKeyboardButton("🔙",callback_data="back"),
        InlineKeyboardButton("%", callback_data="equ:%"),
        InlineKeyboardButton("➗", callback_data="equ:/"),
    )
    btn.add(
        InlineKeyboardButton("7️⃣",callback_data="num:7"),
        InlineKeyboardButton("8️⃣",callback_data="num:8"),
        InlineKeyboardButton("9️⃣", callback_data="num:9"),
        InlineKeyboardButton("✖️", callback_data="equ:*"),
    )
    btn.add(
        InlineKeyboardButton("4️⃣ ",callback_data="num:4"),
        InlineKeyboardButton("5️⃣",callback_data="num:5"),
        InlineKeyboardButton("6️⃣", callback_data="num:6"),
        InlineKeyboardButton("➖", callback_data="equ:-"),
    )
    btn.add(
        InlineKeyboardButton("1️⃣",callback_data="num:1"),
        InlineKeyboardButton("2️⃣",callback_data="num:2"),
        InlineKeyboardButton("3️⃣", callback_data="num:3"),
        InlineKeyboardButton("➕", callback_data="equ:+"),
    )
    btn.add(
        InlineKeyboardButton('.', callback_data='.'),
        InlineKeyboardButton('0️⃣', callback_data='num:0'),
        InlineKeyboardButton('', callback_data='equ:'),
        InlineKeyboardButton('🟰', callback_data='result')
    )
    return btn
\
