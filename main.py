import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# User data storage
users = {}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in users:
        users[user_id] = {
            "balance": 100,
            "name": update.effective_user.first_name,
        }
    await update.message.reply_text(f"স্বাগতম, {users[user_id]['name']}!\nআপনার balance: ৳{users[user_id]['balance']}")

# Balance command
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    balance = users.get(user_id, {}).get("balance", 0)
    await update.message.reply_text(f"আপনার বর্তমান ব্যালেন্স: ৳{balance}")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "/start - শুরু করুন\n"
        "/balance - আপনার ব্যালেন্স দেখুন\n"
        "/deposit - টাকা জমা দিন\n"
        "/withdraw - টাকা তুলুন\n"
        "/profile - প্রোফাইল দেখুন\n"
        "/help - সাহায্য মেনু"
    )
    await update.message.reply_text(text)

# Run bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("help", help_command))
    print("Bot is running...")
    app.run_polling()
