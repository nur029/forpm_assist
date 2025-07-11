from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "YOUR_REAL_BOT_TOKEN_HERE"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👷‍♂️ Hello! I am your PM Assistant Bot.\n"
        "Use /help to see what I can do."
    )

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n"
        "/area <length> <width> - Calculate area (m²)\n"
        "/volume <length> <width> <depth> - Calculate volume (m³)\n"
        "/foundationpit <length> <width> <depth> - Calculate foundation pit volume (m³)\n"
    )

# /area 10 20
async def area(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        length = float(context.args[0])
        width = float(context.args[1])
        result = length * width
        await update.message.reply_text(f"✅ Area: {result:.2f} m²")
    except (IndexError, ValueError):
        await update.message.reply_text(
            "Usage: /area <length> <width>\nExample: /area 10 20"
        )

# /volume 10 20 5
async def volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        length = float(context.args[0])
        width = float(context.args[1])
        depth = float(context.args[2])
        result = length * width * depth
        await update.message.reply_text(f"✅ Volume: {result:.2f} m³")
    except (IndexError, ValueError):
        await update.message.reply_text(
            "Usage: /volume <length> <width> <depth>\nExample: /volume 10 20 5"
        )

# /foundationpit 10 20 3
async def foundation_pit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        length = float(context.args[0])
        width = float(context.args[1])
        depth = float(context.args[2])
        volume = length * width * depth
        await update.message.reply_text(
            f"✅ Foundation Pit Volume: {volume:.2f} m³\n"
            f"(Length: {length} m, Width: {width} m, Depth: {depth} m)"
        )
    except (IndexError, ValueError):
        await update.message.reply_text(
            "Usage: /foundationpit <length> <width> <depth>\nExample: /foundationpit 10 20 3"
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("area", area))
    app.add_handler(CommandHandler("volume", volume))
    app.add_handler(CommandHandler("foundationpit", foundation_pit))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()
