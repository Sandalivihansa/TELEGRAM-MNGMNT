from RUKA import dp, OWNER_ID
from RUKA.helpers.errors import capture_error

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode

from RUKA.modules.disable import disablecommandhandler


@capture_error
async def ishikki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user_id = update.effective_user.id
    bot = context.bot
    await message.reply_text("I'm Alive")
    await bot.send_message(OWNER_ID, text=f"hello, {user_id}")


dp.add_handler(disablecommandhandler("ishikki", ishikki))
