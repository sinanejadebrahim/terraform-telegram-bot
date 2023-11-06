from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
import telegram
import subprocess
import logging

logging.basicConfig(
    filename='botlog.txt',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

# Use your Own chat ID - and group Title to limit the bot to your own group for privacy
def private_check(update):
    if str(update.message.chat.id) == "-123456789" and update.message.chat.type == "supergroup" and update.message.chat.title == "Group Title":
        return True
    else:
        update.message.reply_text('go play with your own bot , this is mine (: ')


def terraform_show():
    terraform_show = subprocess.run("terraform show -json | jq -r \'.values.root_module.resources[] | \" \(.values.name) \(.values.network[].ip) \(.values.server_type) \(.values.status)\"'", shell=True, text=True, capture_output=True, check=True)
    output = f"*Live Instances*: ```{terraform_show.stdout} ```"
    return output


def start(update: Update, context: CallbackContext):
    if private_check(update):
        update.message.reply_text('start')


def show_instances(update: Update, context: CallbackContext):
    if private_check(update):
        res = terraform_show()
        update.message.reply_text(res,parse_mode="MARKDOWN")


def plan(update: Update, context: CallbackContext):
    if private_check(update):
        try:
            num = int(context.args[0])
            plan = subprocess.run(f"terraform plan -var instance_count={num} -no-color | grep Plan: ", shell=True, text=True, capture_output=True, check=True )
            update.message.reply_text(f"🔄 {plan.stdout}")

        except IndexError as e:
            update.message.reply_text("give me a number after the command")


def apply(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    if private_check(update):
        try:
            num = int(context.args[0])
            wait_message = update.message.reply_text("Please Wait..")

            try:
                apply = subprocess.run(f"terraform apply -no-color -auto-approve -var=instance_count={num} | grep Apply", shell=True, text=True, capture_output=True, check=True)
                context.bot.edit_message_text(text=f"✅ {apply.stdout}", chat_id=chat_id, message_id=wait_message.message_id)
                update.message.reply_text(text=terraform_show(), parse_mode="MARKDOWN")

            except subprocess.CalledProcessError as e:
                logger.info("Terraform apply command failed with an error:")
                logger.info(e.stderr)
                context.bot.edit_message_text("*Terraform Error* ❌", parse_mode="MARKDOWN", chat_id=chat_id, message_id=wait_message.message_id)
                update.message.reply_text(e.stderr)

        except IndexError as e:
            logger.info(e)
            update.message.reply_text("give me a number after the command")

# Replace with your own Token
updater = Updater(token='<< TELEGRAM-BOT-TOKEN >>', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
show_handler = CommandHandler('show', show_instances)
apply_handler = CommandHandler('apply', apply)
plan_handler = CommandHandler('plan', plan)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(apply_handler)
dispatcher.add_handler(plan_handler)

updater.start_polling()
updater.idle()
