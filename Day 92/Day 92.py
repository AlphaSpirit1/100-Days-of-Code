import csv
import time

from selenium import webdriver

WEB_DRIVER_PATH = "C:/Users/ASUS PC/Documents/chromedriver.exe"


band = input("which band would you like to get the data for?")

driver = webdriver.Chrome(executable_path=WEB_DRIVER_PATH)

driver.get(f"https://soundcloud.com/{band}/popular-tracks")
try:
    is_band = driver.find_element_by_class_name("errorTitle")
    print("There is no such band")
except:
    accept_cookies = driver.find_element_by_id("onetrust-accept-btn-handler")
    accept_cookies.click()
    time.sleep(5)
    likes_list = driver.find_elements_by_class_name("sc-button-like")
    names_list = driver.find_elements_by_class_name("soundTitle__title")
    plays_num_list = driver.find_elements_by_class_name("sc-visuallyhidden")
    band_name_list = driver.find_elements_by_class_name("soundTitle__usernameText")
    dict_list = []
    for x in range(len(names_list)):
        play_x = x+1
        new_dict = {"Band":band_name_list[x].text,"name": names_list[x].text, "plays": plays_num_list[3*play_x -2].text, "likes": likes_list[x].text}
        dict_list.append(new_dict)


    keys = dict_list[0].keys()

    a_file = open(f"{band}.csv", "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dict_list)
    a_file.close()
    print(f"A new file named {band}.csv has been created")
finally:
    driver.quit()