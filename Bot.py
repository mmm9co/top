#biblioteki


import telebot
from telebot import types


TOKEN= "960381775:AAH1CGoG0Ddb1r7MdpvhKtX7dS6q45hS7Z8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','go'])
def welcome(message):

    bot.send_photo(message.chat.id, photo='https://sun9-12.userapi.com/c855232/v855232864/246539/f7ErJmLo22A.jpg')


    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("кальяны 💨")
    item2 = types.KeyboardButton("табак 🔥")
    item3 = types.KeyboardButton("контакты 📞")
    item4 = types.KeyboardButton("аренда 🏡")

    markup.add(item1, item2)
    markup.add(item3,item4)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> бот,созданный чтобы помочь вам с выбором табака и кальянов, а также предоставляю данные и контакты организации.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'кальяны 💨':

            bot.send_message(message.chat.id, " В заведении «Podkova» Вы можете покурить наши кальяны. \nКальяны доступны для аренды.  ")
            keybord_kal = types.InlineKeyboardMarkup()

            kal1 = types.InlineKeyboardButton('Easy Blow', callback_data='kal1')
            keybord_kal.add(kal1)
            kal2 = types.InlineKeyboardButton(' Alpha Hookah', callback_data='kal2')
            keybord_kal.add(kal2)
            kal3 = types.InlineKeyboardButton(' Cloud Hookah', callback_data='kal3')
            keybord_kal.add(kal3)
            kal4 = types.InlineKeyboardButton('  Sunrise', callback_data='kal4')
            keybord_kal.add(kal4)
            bot.send_message(message.chat.id, 'кальяны 💨', reply_markup=keybord_kal)
        elif message.text == 'табак 🔥':
            bot.send_message(message.chat.id, 'Покурить можно в заведении «Podkova» или приобрести у кальянщика')
            keybord = types.InlineKeyboardMarkup()

            key_1 = types.InlineKeyboardButton('Serbetli', callback_data='tab1')
            keybord.add(key_1)


            key_2 = types.InlineKeyboardButton('Paradox', callback_data='tab2')
            keybord.add(key_2)

            key_3 = types.InlineKeyboardButton('Honey', callback_data='tab3')
            keybord.add(key_3)

            key_4 = types.InlineKeyboardButton('Basio', callback_data='tab4')
            keybord.add(key_4)


            key_5 = types.InlineKeyboardButton('Daly', callback_data='tab5')
            keybord.add(key_5)

            key_6 = types.InlineKeyboardButton('Smoky Bull', callback_data='tab6')
            keybord.add(key_6)

            key_7 = types.InlineKeyboardButton('DO YOU', callback_data='tab7')
            keybord.add(key_7)


            bot.send_message(message.chat.id, 'табак 🔥', reply_markup=keybord)


        elif message.text == 'контакты 📞':

            markup = types.InlineKeyboardMarkup()
            url_buton = types.InlineKeyboardButton("instagram 📸",
                                                   url='https://www.instagram.com/royal_dym/?igshid=19w7iw8ixerfq')
            item2 = types.InlineKeyboardButton("телефон📲", callback_data='tel')
            item3 = types.InlineKeyboardButton("где нас найти?📍", callback_data='lokal')
            markup.add(url_buton, item2)
            markup.add(item3)

            bot.send_message(message.chat.id, 'контакты 📞', reply_markup=markup)
        elif message.text =="аренда 🏡":
            bot.send_message(message.chat.id ,"🔻ТАБАК НА ВЫБОР :\n"
                    "SERBETLI 8️⃣0️⃣грн (50g)\n"
                    "PARADOX  8️⃣0️⃣грн (50g)\n"
                    "HONEY BADGER 1️⃣6️⃣0️⃣грн (100g)\n"
                    "SMOKY BULL 1️⃣3️⃣0️⃣грн (100g)\n"
                    "BASIO 1️⃣5️⃣0️⃣грн (100g)\n"
                    "DO YOU (табак или табачная смесь) 1️⃣0️⃣0️⃣грн (50g)\n"
                    "DALY CODE 1️⃣0️⃣0️⃣грн (50g)\n"
                    "\n"
                    "🔻УГЛИ( 1 шт. - 3 грн) :\n"
                    "CocoLoco 1️⃣3️⃣0️⃣грн (1кг)\n"
                    "Phoenix 1️⃣1️⃣0️⃣грн (1кг)\n"
                    "Panda 1️⃣3️⃣0️⃣грн (1кг)\n"
                           "\n"
                    "🔻ПОЛУЧЕНИЕ\n"
                    "Самовывоз или доставка на такси\n" 
                    "———————————————————\n"
                    "При отметки нас в сторис -10% скидка\n"
                    "———————————————————\n"
                    "\n"
                    "🔘Стоимость Кальяна НА 1 СУТКИ 1️⃣6️⃣0️⃣ грн ,\n"
                    "ПОСЛЕДУЮЩИЕ ДНИ - 5️⃣0️⃣ грн (кроме чт,пт,сб,вс)\n"
                    "\n"
                    "‼️С  ЧЕТВЕРГА ПО ВОСКРЕСЕНЬЕ (включительно) последующие \n"
                    "дни аренды - 1️⃣6️⃣0️⃣ грн‼️\n"
                    "\n"
                    "🔘Фото документа подтверждения личности ОБЯЗАТЕЛЬНО!!!\n")



        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "inst":
                bot.send_message(call.message.chat.id, "https://instagram.com/royal_dym?igshid=19w7iw8ixerfq")
            elif call.data == "tel":
                bot.send_contact(call.message.chat.id, +380950774295, 'Иван')
                bot.send_contact(call.message.chat.id, +380730974258, 'Владислав')
                bot.send_contact(call.message.chat.id, +380950430349, 'Артем')

            elif call.data == "lokal":
                bot.send_location(call.message.chat.id,46.671599,32.617764)
            elif call.data == "tab1":
                bot.send_photo(call.message.chat.id, photo="https://dontabak.com.ua/5057-thickbox_default/tabak-serbetli-klubnika-banan-strawberry-banana-50-gramm.jpg")
                bot.send_message(call.message.chat.id,
                                 "Щербетли делается на основе мёда, что придает ему немного сладковатый натуральный вкус. Основным отличием от табаков других производителей является жаростойкость и высокое влагосодержание, что позволяет дольше наслаждаться вкусом и нагревать табак для большей дымности, при этом табак совсем не горчит.")

            elif call.data == "tab2":
                bot.send_photo(call.message.chat.id, photo="https://besplatka.ua/aws/746x-/83/81/51/66/tabak-dlya-kalyana-paradox-1-kg-photo-b3d5.jpg")
                bot.send_message(call.message.chat.id,"Paradox (Парадокс) – необычный, яркий, многослойный аромат лимонада «Тархун» с ноткой душистого базилика и мультифруктовым послевкусием. Бодрящий микс Paradox, в котором доминантом выступает мятно-анисовый эстрагон, особенно эффектно раскрывается в комбинациях с апельсином, лимоном и другими пряностями.")
            elif call.data == "tab3":
                bot.send_photo(call.message.chat.id, photo="https://cdn.c4.r-99.com/sites/default/files/imagecache/copyright/user-images/1042410/1PWLOfSbkQIvjKw5OsBJZw.jpeg")
                bot.send_message(call.message.chat.id,"Табачный лист не моется, что позволяет сохранить его богатый и благородный вкус. Во время курения раскрываются дополнительные цветочно-медовые ноты. Пропитывается лист в сахарном сиропе. Продукт обладает низким процентным содержанием никотина. Это хороший выбор для легкого курения и ежедневного пользования. Отличный выбор для начинающих курильщиков.")
            elif call.data == "tab4":
                bot.send_photo(call.message.chat.id, photo="https://shishastore.com.ua/image/catalog/Tabacco2/Basio/basio_cholate_tabak_dlya_kaliyan.jpg")
                bot.send_message(call.message.chat.id,"Табак удобно забивать в чашу, он не липнет к рукам и хорошо укладывается благодаря мелкой нарезке. Во время тяги Вы полностью насыщаетесь дымом,наполняясь приятными впечатлениями от легкости дымных облаков. Табак Basio обладает хорошей жаростойкостью, благодаря чему комфортно будет куриться на 3х угольках, размером кубика 25х25х25.")
            elif call.data == "tab5":
                bot.send_photo(call.message.chat.id, photo="https://shishamag.ru/tabak/dali/dali-img-2.jpg")
                bot.send_message(call.message.chat.id,"Табак относится к новшествам производителей и выпускается на основе чая(чай практически не чувствуется).При этом в чайные листья добавляется никотин. Смесь абсолютно не содержит табачных листьев и условно называется «Дали табак».Отличается от конкурентов наличием безвредных ароматизаторов.Мелкая нарезка обеспечивает глубокое раскрытие вкуса.")
            elif call.data == "tab6":
                bot.send_photo(call.message.chat.id, photo="https://kalyan.in.ua/media/catalog/product/cache/7/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/1/4/14tabak-dlya-kalyana-smoky-bull-medium-line-mango-100-gramm.jpg")
                bot.send_message(call.message.chat.id,"Благодаря высококачественному составу этот микс придется по душе курильщикам, предпочитающим крепкий и насыщенный вкус. Эффект полного расслабления и ощущения легкой эйфории гарантирован.Выбрав табак для кальяна Смоки Булл,как следует ощущаешь крепость вкуса и аромат взрывного микса для курения.")
            elif call.data == "tab7":
                bot.send_photo(call.message.chat.id, photo="https://lounge-room.ru/wp-content/uploads/2019/07/do-you-kalyannaya-chajnaya-smes-i-tabak-dlya-kalyana-iz-sankt-peterburga-1024x683.jpg")
                bot.send_message(call.message.chat.id,"Бленд Do You проработан так, чтобы максимально приблизить вкусовые ощущения к курению настоящего табака. Обладает ярким вкусом и густой дымностью.")

            elif call.data == "kal1":
                bot.send_photo(call.message.chat.id, photo="https://dumok.com.ua/files/products/kalyan-doubletoke-easyblow-craft-tr-5.1200x960.jpg?978353a351ab645272d6593ec3283fe7")
                bot.send_message(call.message.chat.id,"Шахта кальяна изготовлена из нержавеющей стали диаметром 15 мм, а её внешняя отделка выполнена из высококачественного пластика. Так же изделие имеет восьмиклапанную продувку. Благодаря легкой тяге, Easy Blow позволит Вам расслабиться и в полной мере насладиться не только ароматом,но и приятным послевкусием дыма в процессе курения.")
            elif call.data == "kal2":
                bot.send_photo(call.message.chat.id, photo="https://i8.rozetka.ua/goods/16584214/178453724_images_16584214018.jpg")
                bot.send_message(call.message.chat.id,"В 2018 году был выпущен один из самых лучших мини-кальянов этого года с нереально крутой продувкой – дым выходит из отверстий внизу изделия и красиво расползается по блюдцу. Кальян Alpha Х имеет компактные размеры – высота всего 40 см (длина шахты).")
            elif call.data == "kal3":
                bot.send_photo(call.message.chat.id, photo="https://ireland.apollo.olxcdn.com/v1/files/31261ancimsi1-UA/image;s=1000x700")
                bot.send_message(call.message.chat.id,"Кальян, а точнее все видимые его части распечатаны на 3Д принтере!Кальян хорошо протестирован и отлично курится. У него отличное блюдце красивой формы. Части шахты взаимозаменяемы, их можно легко менять,тем самым обновляя дизайн уже купленного Вами кальяна по желанию.Внутренняя часть кальяна из нержавеющей стали, благодаря чему он опять же долговечен и не поддается коррозии.")
            elif call.data == "kal4":
                bot.send_photo(call.message.chat.id, photo="https://vacuum.net.ua/wp-content/uploads/2019/07/IMG_6579-600x800.jpg")
                bot.send_message(call.message.chat.id,"Новинка на рынке – шахты для кальянов Украинского производства . Кальяны данного производителя изготавливаются из нержавеющей стали, основание из облегченного материала полиацеталь. Накладка шахты выполена из стабилизированного Дуба и Ясеня. Шахта имеет скрытую систему продува.Устройство шахты – наборное. На основание из нержавеющей стали одеваются 4 елемента декора и блюдце.Соединение шахты и колбы – посредством силиконового уплотнителя стандартного диаметра. К шахте Sunrise hookah подойдет практически любая колба.")



            # remove inline buttons


            # show alert





    except Exception as e:
        print(repr(e))

# RUN
bot.polling(none_stop=True)