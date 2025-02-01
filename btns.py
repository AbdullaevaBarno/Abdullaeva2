from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
about = KeyboardButton(text='🔍Biz haqqimizda🔍')
communication = KeyboardButton(text='📱Baylanis ushin📱')
main_menu.add(about)
main_menu.add(communication)


catalog_menu = InlineKeyboardMarkup()
spring = InlineKeyboardButton(text='🌼Bahargi guller🌼', callback_data='spring_flowers')
summer = InlineKeyboardButton(text='🌷Jazgi guller🌷', callback_data='summer_flowers')
holiday = InlineKeyboardButton(text='💐Bayram gulleri💐', callback_data='holiday_flowers')
evening = InlineKeyboardButton(text='🌌Keshki guller🌌', callback_data='evening_flowers')
buy = InlineKeyboardButton(text='Satip aliw✅',callback_data='buy')
kommentari = InlineKeyboardButton(text='Kommentariya qaldiriw📝', callback_data='leave_review')
catalog_menu.add(spring,summer)
catalog_menu.add(holiday,evening)
catalog_menu.add(buy)
catalog_menu.add(kommentari)

spring_flowers_menu = InlineKeyboardMarkup()
lola = InlineKeyboardButton(text='🌷Lala🌷', callback_data='lola')
nappi = InlineKeyboardButton(text='🪷Nargiz🪷', callback_data='nappi')
violet = InlineKeyboardButton(text='🪻Binafsha🪻', callback_data='violet')
spring_flowers_menu.add(lola,nappi,violet)
spring_flowers_menu.add(buy)

summer_flowers_menu = InlineKeyboardMarkup()
red_rose = InlineKeyboardButton(text='🌹Qizil atirgul🌹', callback_data='red_rose')
lily = InlineKeyboardButton(text="🪷Liliya🪷", callback_data='lily')
peony = InlineKeyboardButton(text='🌸Pion🌸', callback_data='peony')
summer_flowers_menu.add(red_rose,lily,peony)
summer_flowers_menu.add(buy)

holiday_flowers_menu = InlineKeyboardMarkup()
bouqet = InlineKeyboardButton(text='💐Bayram💐', callback_data='bouqet')
love_bouqet = InlineKeyboardButton(text='💞Love💞', callback_data='love_bouqet')
perfect = InlineKeyboardButton(text='💝ForYou💝', callback_data='perfect')
box_flowers = InlineKeyboardButton(text='💎Shishali💎', callback_data='box_flowers')
beautiful = InlineKeyboardButton(text='🌼Moychechak🌼',callback_data='beautiful')
black_rose = InlineKeyboardButton(text='🖤QaraAtirgul🖤', callback_data='black_rose')
holiday_flowers_menu.add(bouqet,love_bouqet,perfect)
holiday_flowers_menu.add(box_flowers,beautiful,black_rose)
holiday_flowers_menu.add(buy)

evening_flowers_menu = InlineKeyboardMarkup()
orchid = InlineKeyboardButton(text='🪷Orxideya🪷', callback_data='orchid')
jasmine = InlineKeyboardButton(text='🌺Yasemin🌺', callback_data='jasmine')
zambak = InlineKeyboardButton(text='🪻Zambak🪻', callback_data='zambak')
evening_flowers_menu.add(orchid,jasmine,zambak)
evening_flowers_menu.add(buy)

buy_menu = InlineKeyboardMarkup()
buying = InlineKeyboardButton(text='Satip aliw✅',callback_data='buying')
buy_menu.add(buying)

aksiya_menu = InlineKeyboardMarkup()
aksiya = InlineKeyboardButton('Buyirtpa qiliw', callback_data='aksiya')
aksiya_menu.add(aksiya)
