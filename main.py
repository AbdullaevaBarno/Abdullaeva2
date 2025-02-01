from aiogram import types,Bot,Dispatcher,executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from btns import summer_flowers_menu, evening_flowers_menu, spring_flowers_menu, holiday_flowers_menu
from btns import main_menu, catalog_menu, buy_menu, aksiya_menu
from db import add_user,show_users, add_review,close_db,create_tables



api='7051245348:AAGiwFpJ3sG9qrNRxo7jJORTJfVDIRkR_nE'
PROXY_URL = "http://proxy.server:3128/"
bot=Bot(api)
storage = MemoryStorage()
dp=Dispatcher(bot,storage=storage)

ADMIN_ID = 7772310913

class ReviewState(StatesGroup):
    waiting_for_review = State()

class RegState(StatesGroup):
    name = State()
    surname = State()
    phone = State()
    telegram_id = State()
    


@dp.message_handler(text='🔍Biz haqqimizda🔍')
async def send_about(sms: types.Message):
    await sms.answer(text='🏪"Golden Rose" guller dukani\n🌐Garezsizlik, Nukus, Qaraqalpaqstan Respublikasi\n✅Biz sizge en jaqsi gullerdi usinamiz!')

@dp.message_handler(text='📱Baylanis ushin📱')
async def send_com(sms: types.Message):
    await sms.answer(text='Telefon nomer: 991234567\nInsta:@GoldenRose')

@dp.message_handler(commands=['start'])
async def send_hi(sms: types.Message):
    await sms.answer(text='Assalawmu aleykum\n"Golden Rose" guller dukanina\nxosh kelibsiz😊!',reply_markup=main_menu)

@dp.message_handler(commands=['help'])
async def send_help(sms: types.Message):
    await sms.answer(text='Bot funksiyalari:\n/start-Salemlesiw\n/help-Jardem\n/catalog-Guller katologi\n/leave_review-Koomentariya qaldiriw')

@dp.message_handler(commands=['catalog'])
async def send_catalog(sms: types.Message):
    await sms.answer(text='Gullerdin tipin tanlan👇',reply_markup=catalog_menu)

@dp.message_handler(commands=['discounts'])
async def show_discounts(sms: types.Message):
    await sms.answer(text='Aksiyalar:\n1."🌹Qizil atirgul🌹" - 30% skidka\n2."🌷Lala🌷" - 20% skidka',reply_markup=aksiya_menu)

@dp.message_handler(commands=['leave_review'])
async def send_leave(sms: types.Message):
    await sms.answer(text='Kommentariya qaldirin✍')
    await ReviewState.waiting_for_review.set()

    

@dp.message_handler(state=ReviewState.waiting_for_review)
async def get_review(sms: types.Message, state):
    review_text = sms.text
    await add_review(sms.from_user.id,review_text)
    await bot.send_message(ADMIN_ID,
    f"Jana kommentariya:{review_text}\nPaydalaniwshi:@{sms.from_user.username}")
    await sms.answer('Kommentariya ushin raxmet!\nXabariniz jiberildi!')
    await state.finish()



@dp.callback_query_handler()
async def send_callback(call: types.CallbackQuery):
    data = call.data
    if data == 'spring_flowers':#bahargi guller
        await call.message.edit_text('Bahargi guller turin tanlan👇:',reply_markup=spring_flowers_menu)
    elif data == 'lola':
        await call.answer('Suwret jiberilip atir')
        photo = open(file='lala.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Lala\nbahasi: 100,000 swm',reply_markup=buy_menu)
    elif data == 'nappi':
        await call.answer('Suwret jiberilip atir')
        photo = open(file='nargiza.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='🪷Nargiza🪷\nbahasi: 110,000 swm',reply_markup=buy_menu)
    elif data == 'violet':
        await call.answer('Suwret jiberilip atir')
        photo = open(file='violet.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='🪻Binafsha🪻\nbahasi: 150,000 swm',reply_markup=buy_menu)

    elif data == 'summer_flowers':#jazgi guller
        await call.message.edit_text('Jazgi guller turin tanlan👇:',reply_markup=summer_flowers_menu)
    elif data == 'red_rose':
        await call.answer('Suwret jiberilip atir')
        photo = open(file='red.roses.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Qizil atirgul\nbahasi: 300,000 swm',reply_markup=buy_menu)
    elif data == 'lily':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='liliya.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Liliya\nbahasi: 120,000 swm',reply_markup=buy_menu)
    elif data == 'peony':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='pion.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Pion\nbahasi: 300,000 swm',reply_markup=buy_menu)

    elif data == 'holiday_flowers':
        await call.message.edit_text('Bayram ushin ajayip guller👇:',reply_markup=holiday_flowers_menu)  
    elif data == 'bouqet':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='bayram.buketi.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Bayram buketi\nbahasi: 400,000 swm',reply_markup=buy_menu)
    elif data == 'love_bouqet':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='love.buketi.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Love buketi\nbahasi: 350,000 swm',reply_markup=buy_menu)
    elif data == 'perfect':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='arnalgan.buket.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Arnalgan buket\nbahasi: 250,000 swm',reply_markup=buy_menu)
    elif data == 'box_flowers':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='box.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Shishali gul\nbahasi: 500,000 swm',reply_markup=buy_menu)
    elif data == 'beautiful':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='moychechak.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Moychechak\nbahasi: 200,000 swm',reply_markup=buy_menu)
    elif data == 'black_rose':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='qara.atirgul.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Qara atirgul\nbahasi: 600,000 swm',reply_markup=buy_menu)

    elif data == 'evening_flowers':#keshki guller
        await call.message.edit_text('Keshki guller turin tanlan👇:', reply_markup=evening_flowers_menu)
    elif data == 'orchid':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='orxideya.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Orxideya\nbahasi: 150,000 swm',reply_markup=buy_menu)
    elif data == 'jasmine':
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='yasemin.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Yasemin\nbahasi: 80,000 swm',reply_markup=buy_menu)
    elif data =='zambak'and 'buy' :
        await call.answer(text='Suwret jiberilip atir')
        photo = open(file='zambak.flowers.jpg',mode='rb')
        await call.message.answer_photo(
            photo=photo,
            caption='Zambak\nbahasi: 130,000 swm',reply_markup=buy_menu)
        
    elif data == 'aksiya':
        await call.message.answer('Buyirtpaniz qabil qilindi.Raxmet!\nTez arada sizge jetkeriledi.')

    elif data == 'buy':
        await call.message.answer('Satip aliw ushin guller kataloginan gul turin tanlan👇')
        import time
        time.sleep(2)
        await call.message.answer('/catalog-Guller katalogi')
    elif data == 'leave_review':
        await call.message.answer('Kommentariya qaldiriw ushin /leave_review komandasin isletin')
    elif data == 'buying':
        await call.message.answer('Satip aliwinizdan aldin bizden registraciyadan otin!')
        import time
        time.sleep(3)
        await call.message.answer('Oziniz haqqinda magliwmat kiritin👇')
        await call.message.answer('Atinizdi kiritin:')
        await RegState.name.set()
    

@dp.message_handler(state=RegState.name)
async def save_name(sms:types.Message,state:FSMContext):
    async with state.proxy() as joni:
        joni['name']=sms.text
    await sms.answer(text='Bizge familiyanizdi jazin:')
    await RegState.surname.set()

@dp.message_handler(state=RegState.surname)
async def save_surname(sms:types.Message,state:FSMContext):
    async with state.proxy() as joni:
        joni['surname']=sms.text
    await sms.answer(text='Aqrigisi qaldi, bizge telefon nomerinzidi jazin:')
    await RegState.phone.set()

@dp.message_handler(state=RegState.phone)
async def save_phone(sms:types.Message,state:FSMContext):
    async with state.proxy() as joni:
        joni['phone']=sms.text
    await sms.answer(text='Siz registraciadan otiwdi juwmaqladiniz.')
    import time
    time.sleep(2)
    await sms.answer(text=f'''
Sizdin atiniz:{joni['name']},
Familiyaniz:{joni['surname']},
Telefon nomeriniz:{joni['phone']}
''')
    import time
    time.sleep(2)
    await sms.answer(text='Raxmet.Tez arada siz benen baylanisamiz!')
    await add_user(telegram_id=sms.from_user.id,
                    name=joni['name'],
                    surname=joni['surname'],
                    phone = joni['phone'])
    
    await state.finish()

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)

