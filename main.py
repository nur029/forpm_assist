import json
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8179817126:AAH4Ctzrpwg3DknMg7_dSMxdoBRFI26aIfM"  # <<< PUT YOUR BOT TOKEN HERE

LANG_FILE = "languages.json"

# Load languages from file or create new
if os.path.exists(LANG_FILE):
    with open(LANG_FILE, "r") as f:
        user_languages = json.load(f)
else:
    user_languages = {}

def save_languages():
    with open(LANG_FILE, "w") as f:
        json.dump(user_languages, f)

def get_lang(user_id):
    return user_languages.get(str(user_id), "eng")

# All bot texts
TEXTS = {
    "start": {
        "eng": "👷‍♂️ Hello! I am your PM Assistant Bot.\nUse /help to see what I can do.",
        "kaz": "👷‍♂️ Сәлем! Мен сіздің құрылыс көмекшіңізмін.\nНе істей алатынымды көру үшін /help қолданыңыз.",
        "rus": "👷‍♂️ Привет! Я ваш помощник строителя.\nИспользуйте /help, чтобы узнать, что я умею."
    },
    "help": {
        "eng": "Available commands:\n/area <length> <width> - Calculate area\n/volume <length> <width> <depth> - Calculate volume\n/foundationpit <length> <width> <depth> - Foundation pit\n/lang <eng|kaz|rus> - Change language",
        "kaz": "Қол жетімді командалар:\n/area <ұзындығы> <ені> - Ауданды есептеу\n/volume <ұзындығы> <ені> <тереңдігі> - Көлемін есептеу\n/foundationpit <ұзындығы> <ені> <тереңдігі> - Қазаншұңқыр көлемі\n/lang <eng|kaz|rus> - Тілді өзгерту",
        "rus": "Доступные команды:\n/area <длина> <ширина> - Вычислить площадь\n/volume <длина> <ширина> <глубина> - Вычислить объем\n/foundationpit <длина> <ширина> <глубина> - Котлован\n/lang <eng|kaz|rus> - Сменить язык"
    },
    "lang_set": {
        "eng": "✅ Language set to English.",
        "kaz": "✅ Тіл Қазақ тіліне ауыстырылды.",
        "rus": "✅ Язык изменен на Русский."
    },
    "lang_invalid": {
        "eng": "❌ Unknown language. Use: eng, kaz, rus.",
        "kaz": "❌ Белгісіз тіл. Қолданыңыз: eng, kaz, rus.",
        "rus": "❌ Неизвестный язык. Используйте: eng, kaz, rus."
    },
    "area_result": {
        "eng": "✅ Area: {:.2f} m²",
        "kaz": "✅ Ауданы: {:.2f} м²",
        "rus": "✅ Площадь: {:.2f} м²"
    },
    "area_usage": {
        "eng": "Usage: /area <length> <width>",
        "kaz": "Қолданылуы: /area <ұзындығы> <ені>",
        "rus": "Использование: /area <длина> <ширина>"
    },
    "volume_result": {
        "eng": "✅ Volume: {:.2f} m³",
        "kaz": "✅ Көлемі: {:.2f} м³",
        "rus": "✅ Объем: {:.2f} м³"
    },
    "volume_usage": {
        "eng": "Usage: /volume <length> <width> <depth>",
        "kaz": "Қолданылуы: /volume <ұзындығы> <ені> <тереңдігі>",
        "rus": "Использование: /volume <длина> <ширина> <глубина>"
    },
    "pit_result": {
        "eng": "✅ Foundation Pit Volume: {:.2f} m³",
        "kaz": "✅ Қазаншұңқыр көлемі: {:.2f} м³",
        "rus": "✅ Объем котлована: {:.2f} м³"
    },
    "pit_usage": {
        "eng": "Usage: /foundationpit <length> <width> <depth>",
        "kaz": "Қолданылуы: /foundationpit <ұзындығы> <ені> <тереңдігі>",
        "rus": "Использование: /foundationpit <длина> <ширина> <глубина>"
    },
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(update.effective_user.id)
    await update.message.reply_text(TEXTS["start"][lang])

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(update.effective_user.id)
    await update.message.reply_text(TEXTS["help"][lang])

async def set_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    current_lang = get_lang(user_id)

    if not context.args:
        await update.message.reply_text(TEXTS["lang_invalid"][current_lang])
        return

    new_lang = context.args[0].lower()
    if new_lang in ["eng", "kaz", "rus"]:
        user_languages[user_id] = new_lang
        save_languages()
        await update.message.reply_text(TEXTS["lang_set"][new_lang])
    else:
        await update.message.reply_text(TEXTS["lang_invalid"][current_lang])

async def area(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(update.effective_user.id)
    try:
        length = float(context.args[0])
        width = float(context.args[1])
        result = length * width
        await update.message.reply_text(TEXTS["area_result"][lang].format(result))
    except:
        await update.message.reply_text(TEXTS["area_usage"][lang])

async def volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(update.effective_user.id)
    try:
        l = float(context.args[0])
        w = float(context.args[1])
        d = float(context.args[2])
        v = l * w * d
        await update.message.reply_text(TEXTS["volume_result"][lang].format(v))
    except:
        await update.message.reply_text(TEXTS["volume_usage"][lang])

async def foundation_pit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(update.effective_user.id)
    try:
        l = float(context.args[0])
        w = float(context.args[1])
        d = float(context.args[2])
        pit = l * w * d
        await update.message.reply_text(TEXTS["pit_result"][lang].format(pit))
    except:
        await update.message.reply_text(TEXTS["pit_usage"][lang])

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("lang", set_lang))
    app.add_handler(CommandHandler("area", area))
    app.add_handler(CommandHandler("volume", volume))
    app.add_handler(CommandHandler("foundationpit", foundation_pit))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()