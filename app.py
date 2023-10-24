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

# Use your Own chat ID - and group Title to limit the bot to your own group for privacy
def private_check(update):
    if str(update.message.chat.id) == "-123456789" and update.message.chat.type == "supergroup" and update.message.chat.title == "Group Title":
        return True
    else:
        update.message.reply_text('go play with your own bot , this is mine (: ')

def terraform_show():
    terraform_show_process = subprocess.run(['terraform', 'show', '-json'], stdout=subprocess.PIPE, text=True)
    terraform_show_output = terraform_show_process.stdout
    jq_process = subprocess.run(['jq', '.values.root_module.resources[] | " \(.values.name) \(.values.network[].ip) \(.values.server_type) \(.values.status)"'], input=terraform_show_output, stdout=subprocess.PIPE, text=True)
    output = jq_process.stdout.replace('"','')
    output = f"*Live Instances*: ```{output} ```"
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

            plan = subprocess.check_output(["terraform", "plan", "-var", f"instance_count={num}", "-no-color" ], text=True)

            plan_line = [line for line in plan.split('\n') if 'Plan:' in line]

            if plan_line:
                update.message.reply_text(plan_line[0])
            else:
                update.message.reply_text("No changes. Your infrastructure matches the configuration")
        except Exception as e:
            update.message.reply_text("give me a number after the command")


def apply(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id
    message_id = update.message.message_id
    
    if private_check(update):
        try:
            num = int(context.args[0])
            wait_message = update.message.reply_text("Please Wait..")

            apply = subprocess.check_output(["terraform", "apply", "-auto-approve", f"-var=instance_count={num}" ],text=True)
            apply_line = [line for line in apply.split('\n') if 'Apply' in line]
            
            res = terraform_show()
            context.bot.edit_message_text(text=apply_line[0], chat_id=chat_id, message_id=wait_message.message_id, parse_mode="MARKDOWN")
            update.message.reply_text(res,parse_mode="MARKDOWN")

        except Exception as e:
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
