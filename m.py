from operator import contains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
import time 
import telebot


	
#Open  FB 

driver= webdriver.Chrome(
    executable_path='/home/gagik/Documents/projects/FbBirthdays/chromedriver_linux64/chromedriver'
) 
wait = WebDriverWait(driver, 10)
driver.get("https://facebook.com")
userid="<username>"
pwd="<password>"
time.sleep(2)

# 
# 
# 
# 




# Login To FB
emailelement= driver.find_element(By.XPATH,'//*[@id="email"]')
emailelement.send_keys(userid)
time.sleep(1.5)
passwordfield= driver.find_element(By.XPATH,'//*[@id="pass"]')
passwordfield.send_keys(pwd)
time.sleep(1.5)
button= driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
button.click()
time.sleep(2)




usernames = []
driver.get("https://www.facebook.com/events/birthdays/")
time.sleep(5)
birthdays= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]")
# print(len(birthdays))
flag = True
k = 1
usernames = []
dates = []
while flag:
    
        try:
            if k<4:
                container = birthdays.find_elements(By.CSS_SELECTOR, f'div.mfycix9x:nth-child({k})')
                usertext = container[0].text
                new_usertext = usertext.split()
                username = new_usertext[0] + ' ' + new_usertext[1]
                date = new_usertext[2] + ' ' + new_usertext[3]
                usernames.append(str(username))
                dates.append(date)

                k+=1
            else:
                selector = '.imjq5d63 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4)'
                if selector[-2] == str(k):
                    container = birthdays.find_elements(By.CSS_SELECTOR,f'.imjq5d63 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child({k})')
                    usertext = container[0].text
                    new_usertext = usertext.split()
                    username = new_usertext[0] + ' ' + new_usertext[1]
                    date = new_usertext[2] + ' ' + new_usertext[3]
                    usernames.append(str(username))
                    dates.append(date)
                    k+=1
                else:
                    flag = False
        except Exception as ex:
            print(ex)
            flag = False


title = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/div/div/h2/span').text
print(title)
driver.close()



bot = telebot.TeleBot('5501940180:AAH4c1li_8nLBlgfqAfSWMGrXsxURQuL01k')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,f'<b>{title} </b>',parse_mode = 'html')
    for element1 ,element2 in zip(usernames, dates):

        bot.send_message(message.chat.id,f'{element1} {element2}',parse_mode = 'html')


bot.polling(none_stop = True)

