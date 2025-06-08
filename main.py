import telebot
from telebot.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN, ADDRESSES

bot = telebot.TeleBot(TOKEN)

@bot.inline_handler(lambda query: True)
def inline_query(query):
    developer = InlineKeyboardButton("Хочу такого бота", url="https://t.me/TheAnotherOneUsername")
    if len(query.query) == 0:
        markup = InlineKeyboardMarkup()
        tonkeeper = InlineKeyboardButton("TonKeeper", url=f"https://app.tonkeeper.com/transfer/{ADDRESSES[0]}")
        mytonwallet = InlineKeyboardButton("MyTonWallet", url=f"https://my.tt/transfer/{ADDRESSES[0]}")
        tonhup = InlineKeyboardButton("TonHub", f"https://tonhub.com/transfer/{ADDRESSES[0]}")
        others = InlineKeyboardButton("Другие", url=f"ton://transfer/{ADDRESSES[0]}")
        markup.add(tonkeeper, mytonwallet)
        markup.add(tonhup, others)
        markup.add(developer)

        if len(ADDRESSES) > 1:
            text = f"Мои адреса:\n\n1) `{ADDRESSES[0]}`\n2) `{ADDRESSES[1]}`\n\nТакже можете отправить деньги быстро через кнопку ниже:"
        else:
            text = f"Мои адреса:\n\n`{ADDRESSES[0]}`\n\nТакже можете отправить деньги быстро через кнопку ниже:"

        result1 = InlineQueryResultArticle(
            id="1",
            title="Отправить адрес",
            description=f"Отправить адрес",
            input_message_content=InputTextMessageContent(
                text,
                parse_mode="Markdown"),
            reply_markup=markup
        )
        bot.answer_inline_query(query.id, [result1], cache_time=1)
    else:
        try:
            amnt = float(query.query)
            if amnt != 0:
                amount = int(amnt*1000000000)
                amount2 = int(amount*102/100)

                markup1 = InlineKeyboardMarkup()
                tonkeeper = InlineKeyboardButton("TonKeeper", url=f"https://app.tonkeeper.com/transfer/{ADDRESSES[0]}?amount={amount}")
                mytonwallet = InlineKeyboardButton("MyTonWallet", url=f"https://my.tt/transfer/{ADDRESSES[0]}?amount={amount}")
                tonhup = InlineKeyboardButton("TonHub", f"https://tonhub.com/transfer/{ADDRESSES[0]}?amount={amount}")
                others = InlineKeyboardButton("Другие", url=f"ton://transfer/{ADDRESSES[0]}?amount={amount}")
                markup1.add(tonkeeper, mytonwallet)
                markup1.add(tonhup, others)
                markup1.add(developer)

                markup2 = InlineKeyboardMarkup()
                tonkeeper = InlineKeyboardButton("TonKeeper", url=f"https://app.tonkeeper.com/transfer/{ADDRESSES[0]}?amount={amount2}")
                mytonwallet = InlineKeyboardButton("MyTonWallet", url=f"https://my.tt/transfer/{ADDRESSES[0]}?amount={amount2}")
                tonhup = InlineKeyboardButton("TonHub", f"https://tonhub.com/transfer/{ADDRESSES[0]}?amount={amount2}")
                others = InlineKeyboardButton("Другие", url=f"ton://transfer/{ADDRESSES[0]}?amount={amount2}")
                markup2.add(tonkeeper, mytonwallet)
                markup2.add(tonhup, others)
                markup2.add(developer)

                if len(ADDRESSES) > 1:
                    text = f"Мои адреса:\n\n1) `{ADDRESSES[0]}`\n2) `{ADDRESSES[1]}`\n\nТакже можете отправить деньги быстро через кнопку ниже:"
                else:
                    text = f"Мои адреса:\n\n`{ADDRESSES[0]}`\n\nТакже можете отправить деньги быстро через кнопку ниже:"

                result1 = InlineQueryResultArticle(
                    id="1",
                    title="Отправить адрес +0%",
                    description=f"Отправить адрес и сумму +0%",
                    input_message_content=InputTextMessageContent(
                        f"Сумма: `{amnt}` TON\n\n{text}",
                        parse_mode="Markdown"),
                    reply_markup=markup1
                )

                result2 = InlineQueryResultArticle(
                    id="2",
                    title="Отправить адрес +2%",
                    description=f"Отправить адрес и сумму +2%",
                    input_message_content=InputTextMessageContent(
                        f"Сумма: `{amnt*102/100}` TON\n\n{text}",
                        parse_mode="Markdown"),
                    reply_markup=markup2
                )
                bot.answer_inline_query(query.id, [result1, result2], cache_time=1)
        except: pass

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()
    developer = InlineKeyboardButton("Хочу такого бота", url="https://t.me/TheAnotherOneUsername")
    markup.add(developer)
    bot.reply_to(message, "Бот работает в инлайн режиме", reply_markup=markup)


bot.infinity_polling()
