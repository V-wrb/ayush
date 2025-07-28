from telegram import Update
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

TOKEN = "8039094661:AAHyQcOEXnTl6aXGCAd-KghOJyosKbMrs0U"  # Aapka diya hua token

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.chat_join_request.from_user.id

    # Join request approve karna
    await update.chat_join_request.approve()

    # Greeting image aur text bhejna
    greeting_text = """Aap Bhi Kama Sake Ho Bilkul Meri Tarah With My Help, Don't Waste Time, Register & Add Funds Aur Daily Jackpot Udao🥳🔥 Jiskpe Paas Dimag Hai Woh Khud Aa Jayega🤪🤪

Register Fast ⏩ 
https://cooe02.in/#/register?r_code=5TRY4508

Join Telegram Channel 👇🤑
https://t.me/+9w2le62MKeI0YjRl
https://t.me/+9w2le62MKeI0YjRl
"""
    image_file = "welcome.jpg"  # Apne photo ka naam yahan likhein

    try:
        with open(image_file, "rb") as photo:
            await context.bot.send_photo(chat_id=user_id, photo=photo, caption=greeting_text)
    except Exception as e:
        print(f"Greeting image send nahi ho paya: {e}")

app = Application.builder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve))

print("Bot started... waiting for join requests!")
app.run_polling()