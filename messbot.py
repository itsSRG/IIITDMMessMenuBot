#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from datetime import datetime, timedelta

import logging

from telegram import __version__ as TG_VER

import os
api_key = os.environ.get('TELEGRAM_BOT_KEY')

menu = {
0:{'Sunday':'''Sunday

Breakfast   
    Onion Uthappam
    Sambar, G Chutney
    Bbj, Sprouted Grains
    Seasonal Cut Fruits*
    Tea, Coffee, Milk, Sugar, Salt

Lunch   
    Phulka, Aloo Gobi Mattar (For Veg Only)
    Paneer Biryani, Raitha (For Veg)
    Chk Biryani, Pl. Gravy, Raitha
    Egg
    Juice

Snacks  
    Pancake(W Jam)
    Tea,Cofee,Milk,Sugar

Dinner  
    Idly , G Chutney, Podi, Ghee
    Rice, Sambar , Papad,Curd
    Red Ginger Pickle
    Badusha/Banana
''',    
'Monday':'''Monday   

Breakfast   
    Pesarattu,Upma  
    Sambar , Red Coconut Chutney    
    Bbj, Sprouted Grains    
    Omlette(1)/ Banana (1)  
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
    Chapatti , Peas Masala  
    Aloo Masala Wedges, 
    Rice,Sambar,Rasam, Curd,Fryums  
    Tomato Pickle   
    Sugar ,Salt ,Ghee,Podi  
    Salad   

Snacks  
    Onion Pakoda    
    Tea,Cofee,Milk,Sugar    

Dinner  
    Chapatti, Toor Dal , Veg Kurma  
    Rice, Rasam, Papad,Curd 
    Mango Pickle    
    Gulam Jamun(2)
''',
'Tuesday':'''Tuesday  

Breakfast   
    Poori   
    Potato Masala   
    Bbj, Sprouted Grains    
    Boiled Egg(1)/ Fruit*   
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
    Phulka, Veg Kurma   
    Beetroot Channa Poriyal 
    "Rice,Vathakolambu,Rasam, Curd,Papad"   
    Mango Pickle    
    Sugar ,Salt ,Ghee,Podi  
    Juice   

Snacks  
    Mirchi Bajji (2) / C Chutney    
    Tea,Cofee,Milk,Sugar    

Dinner  
    Phulka, Kadai Paneer,   
    Veg Biryani, Curd Rice  
    Pickle, Raita   
    Boost*  
''',            
'Wednesday':'''Wednesday    

Breakfast   
    Masala Dosa 
    Sambar,P Chutney    
    Bbj, Sprouted Grains    
    Omlette (1)/ Banana (1) 
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
    Chapatti, Mixed Dal 
    Brinjal Poriyal 
    Rice,Mix Veg Karakozhambu,Rasam, Curd,Fryums    
    Lemon Pickle    
    Sugar ,Salt ,Ghee,Podi  
    Salad   

Snacks  
    Sweet Corn  
    Tea,Cofee,Milk,Sugar    

Dinner      
    Special Dinner
''',
'Thursday':'''Thursday 

Breakfast
    Chow Chow Bath  
    Mysore Bonda (2) , C Chutney    
    Bbj, Sprouted Grains    
    Boiled Egg(1)/ Fruit*   
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
    Poori , Punjabi Aloo Mattar 
    Kovakai Fry *,  
    Rice,Andhra Tomato Dal,Rasam, Curd,Papad    
    Pulichakeerai Pickle    
    Sugar ,Salt ,Ghee,Podi  
    Juice   

Snacks  
    Aloo Samosa / Tomato Sauce  
    Tea,Cofee,Milk,Sugar    

Dinner  
    Dosa, C Chutney 
    Plain Rice,Mixed Dal    
    Aloo Peas Dry   
    Butter Milk, Crispy Bread Halwa
''',
'Friday':'''Friday   

Breakfast   
    Rava Idly,Vada (2)  
    Sambar,   P Chutny  
    Bbj, Sprouted Grains    
    Omlette (1)/ Banana (1) 
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
    Phulka, Mix Veg Matar   
    Lauki Chana Dal, Gobi 65*   
    Rice,Rasam, Curd,Fryums 
    Mixveg Pickle   
    Sugar ,Salt ,Ghee,Podi  
    Salad   

Snacks  
    Channa Chat 
    Tea,Cofee,Milk,Sugar    

Dinner  
    Phulka, Mix Veg Kurma   
    Mix Veg Fried Rice  
    Veg Ball Manchurian*,Banana(1)  
    Tomato,Chilly Sauce 
    Curd Rice       
''',            
        
'Saturday':'''Saturday 

Breakfast   
    Methi Paratha   
    Channa Masala, Curd 2cups, Pickle   
    Bbj, Sprouted Grains    
    Boiled Egg (1) / Cut Fruits (1) 
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
    Chapatti , Mix Veg Curry    
    Chilli Soya Bean Dry, Perugu Pachadi    
    Rice,Sambar,Rasam, Curd,Masala Papad    
    Mango Pickle    
    Sugar ,Salt ,Ghee,Podi  
    Juice   

Snacks
    Dahi Vada   
    Tea,Cofee,Milk,Sugar    

Dinner  
    Chappati, Channa Peas Palak 
    Dal Kichichadi, Curd Rice   
    Aloo 65, Tomato Pickle  
    Papad
'''},
1:{
    'Sunday':'''Sunday
    
Breakfast   
Rava Dosa   
    Sambar, C Chutney   
    Bbj, Sprouted Grains    
    Seasonal Cut Fruits*    
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
Phulka , Kadai Chk * ( For Nv)  
    Phulka , Paneer Butter Masala * ( For Veg)  
    Veg Biryani , Onion Raitha  
    Juice   

Snacks  
Aloo Samosa(1-150gm)/ Green Chutney 
    Tea,Cofee,Milk,Sugar    

Dinner  
Chapatti , Veg Curry    
    Rice,Dal,Rasam, Buttermilk,Fryums   
    Pickel,Ghee 
    Seasonal Cut Fruits*/Banana''',      
'Monday':'''  
Monday

Breakfast   
Pongal , Mysore Bonda (2)   
    Sambar, G Chutney   
    Bbj, Sprouted Grains    
    Omelette (1)/ Banana (1)    
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
Chapatti , Dal Makhani  
    Bhindi Fry With Peanut *    
    Rice,Sambar,Rasam, Curd,Papad   
    Lemon Pickle    
    Sugar ,Salt ,Ghee,Podi  
    Salad   

Snacks  
Onion Pakoda    
    Tea,Cofee,Milk,Sugar    

Dinner  
Chole Bature, Onion Mirch Salad 
    White Rice, Snake Gourd Kootu   
    Butter Milk 
    Banana''',  
        
'Tuesday':
'''Tuesday

Breakfast   
Onion Dosa  
    Sambar,C Chutney    
    Bbj, Sprouted Grains    
    Boiled Egg (1) / Fruit* 
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
Poori , Dum Aloo    
    Beans Carrot Poriyal    
    "Rice,Vathakolabmu,Rasam,Curd,Fryums"   
    ,Tomato Pickle  
    Sugar ,Salt ,Ghee,Podi  
    Juice   

Snacks
    Banana Bajji (2) / C Chutney    
    Tea,Cofee,Milk,Sugar    

Dinner
    Phulka, Meal Maker Curry*** 
    Veg Fried Rice, Veg Ball Manchurian (2) 
    Tomato,Chilli Sauce 
    Curd Rice , Sweet Boondi''',    
        
'Wednesday':'''Wednesday

Breakfast   
Idly,Vada (2)
    Samabr,G Chutney
    Bbj, Sprouted Grains
    Omlette (1)/ Banana (1)
    Tea, Coffee, Milk, Sugar, Salt

Lunch   
Chapatti , Panchratan Dal
    Onion Pakoda*, Perugu Pachadi
    "Rice,Brinjal Mochai Gravy, Rasam,Masala Papad"
    Mango Pickle
    Sugar ,Salt ,Ghee,Podi
    Salad

Snacks
    Dahi Vada
    Tea,Cofee,Milk,Sugar

Dinner  
Phulka, Palak Paneer* Or Andhra Chk*
    Veg Biryani , Raitha
    French Fries(120gm)*
    Banana''',
    
'Thursday':'''Thursday

Breakfast   
Poori
    Channa Masala
    Bbj, Sprouted Grains
    Boiled Egg (1) / Fruit*
    Tea, Coffee, Milk, Sugar, Salt

Lunch   
Phulka , Rajma Dal,
    Aloo Gobi Matar Dry
    "Rice,Masala Sambar,Rasam,Curd,Fryums"
    Mango Pickle
    Sugar ,Salt ,Ghee,Podi
    Juice

Snacks  
Sweet Corn (Half Piece-6cm)
    Tea,Cofee,Milk,Sugar

Dinner  
Kal Dosa,G Chutney
    Rice,Sambar, Aloo Podimas
    Papad, Buttermilk
    Gulab Jamun(2)''',
    
'Friday':'''Friday  

Breakfast   
Semiya Upma,Poha    
    Mysore Bonda(2), P Chutney  
    Bbj, Sprouted Grains    
    Omlette (1)/ Banana (1) 
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
Phulka, Pumpkin Kaala Chana 
    Rice, Beetroot Chana Poriyal    
    Rasam, Curd,Papad   
    Mix Veg Pickle, Vathakolambu    
    Sugar ,Salt ,Ghee,Podi  
    Salad   

Snacks  
Mix Veg Maggi (130 Gm ) / Tomato Sauce  
    Tea,Cofee,Milk,Sugar    

Dinner  
Lacha Paratha ,Veg Kofta*(2)    
    Rice, Rasam 
    Raita,Masala Papad  
    Badam Milk Hot*''',
'Saturday':'''Saturday    

Breakfast   
Aloo Paratha    
    Channa Masala, Raitha, Pickle   
    Bbj, Sprouted Grains    
    Boiled Egg (1) / Fruit* 
    Tea, Coffee, Milk, Sugar, Salt  

Lunch   
Chapatti , Corn Peas Masala 
    Sprouted Dal,   
    Rice,Rasam, Curd,Fryums 
    Mango Pickle, Beetroot Poriyal  
    Sugar ,Salt ,Ghee,Podi  
    Juice   

Snacks
    Millet Snack**  
    Tea,Cofee,Milk,Sugar    

Dinner  
Pulka, Paneer Butter Masala 
    Rice,Sambar, Buttermilk 
    Fryums, 
    Bread Halwa'''}
    }

defaultMessage = "\n\nNote: Always check for Mess Menu Changes in The Institute Email"

today = datetime.today()
adjusted_date = today - timedelta(days=1)
week_number = adjusted_date.isocalendar()[1] % 2
day_of_week = today.strftime('%A')

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf'''Hi {user.mention_html()}!

Send any message to this bot, the only reply you will get is the IIITDM Mess Menu for the day :)''',
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    # await update.message.reply_text(update.message.text)
    await update.message.reply_text(menu[week_number][day_of_week]+defaultMessage)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    logging.debug(api_key)
    application = Application.builder().token(api_key).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()