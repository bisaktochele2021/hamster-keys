from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from config import games
from api_client import login_client, register_event, create_code
import requests
import time

# Mapping user input to the corresponding game key in the games dictionary
GAME_CHOICES = {name: key for key, game in games.items() for name in game['names']}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user

    # Dynamically create the keyboard buttons from the games dictionary
    keyboard = [
        [KeyboardButton(name) for name in GAME_CHOICES.keys()]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Please choose a game:",
        reply_markup=reply_markup,
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the user's game choice and generate a promo code."""
    game_choice = update.message.text

    if game_choice in GAME_CHOICES:
        game_key = GAME_CHOICES[game_choice]

        try:
            await update.message.reply_text('Generating promo code...')
            token = await login_client(games[game_key])
            await update.message.reply_text("Wait 1-3 minutes...")
            register_event(games[game_key], token)
            await update.message.reply_text("Your promo code is ready!")
            time.sleep(5)
            code_response = await create_code(games[game_key], token)
            await update.message.reply_text("Your promo code is: ")
            await update.message.reply_text(f"{code_response['promoCode']}")
        except requests.HTTPError as e:
            await context.bot.send_message(chat_id="1263252996", text=f"HTTP error occurred: {e}")
        except Exception as e:
            await context.bot.send_message(chat_id="1263252996", text=f"An error occurred: {e}")
    else:
        await update.message.reply_text("Please choose a valid game option.")