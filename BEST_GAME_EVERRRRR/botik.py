from CONFIGI.config.load_all_data import LoadData
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Contact
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler,CallbackQueryHandler
class RunGameBot:
    def __init__(self):
        self.txt = ''
        self.dataloader = LoadData("BEST_GAME_EVERRRRR/CONFIGI/data/bot_data.json")
        self.token = self.dataloader.load_token()
        self.used_keyboard = []
        self.main_keyboard = [
            [InlineKeyboardButton("статистика", callback_data='info')],
            [InlineKeyboardButton("построить", callback_data='build')],
            [InlineKeyboardButton("🔼", callback_data='u')],
            [InlineKeyboardButton("◀️",callback_data="l"),
             InlineKeyboardButton("▶️",callback_data="r")],
            [InlineKeyboardButton("🔽", callback_data='d')],
            [InlineKeyboardButton("следующий ход",callback_data="next_move")],
            [InlineKeyboardButton("ЭТО МОДИФИКАЦИ АААААААААААААААААААА",callback_data='mod')]
        ]
        self.build_keyboard = [
            [InlineKeyboardButton("домик", callback_data='house_lvl_1')],
            [InlineKeyboardButton("гробик", callback_data='house_lvl_2')],
            [InlineKeyboardButton("домик-парилка", callback_data='house_lvl_3')],
            [InlineKeyboardButton("заводик", callback_data='factory')],
            [InlineKeyboardButton("банк", callback_data='bank')],
            [InlineKeyboardButton("назад", callback_data='main_page')]
        ]


    def play_game(self,update : Update,context:CallbackContext):
        reply_markup = InlineKeyboardMarkup(self.main_keyboard)
        update.message.reply_text(f"Чо делать будешь? \n {self.txt}",reply_markup=reply_markup)
    def move_button(self,update:Update,context:CallbackContext):
        query = update.callback_query
        query.answer()
        print(query.data)
        if query.data == 'mod':
            self.txt += ",".join(self.dataloader.load_player_id())
        if query.data == 'build':
            self.used_keyboard = self.build_keyboard
        if query.data == 'main_page':
            self.used_keyboard = self.main_keyboard
        if query.data == 'info':
            self.txt += 'papapepagemabodi'
        update.callback_query.message.edit_text(f"Чо делать будешь? \n {self.txt}",reply_markup=InlineKeyboardMarkup(self.used_keyboard))
        self.txt = ''