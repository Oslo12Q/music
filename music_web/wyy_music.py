# -*- coding: utf-8 -*-
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
# 存储为文本

from .models import *
 
#def write2txt(data,path):
#    file = open(path,"w")#encoding='utf-8')
#    file.write(data)
#    file.close()

	
def song_all(id,uids):
    try:
        url = 'http://music.163.com/#/user/songs/rank?id=%s' % id
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options,executable_path='/usr/bin/chromedriver')#chrome浏览器的驱动

        driver.get("%s"%url)#需要抓取的用户链接，这里注意的是这里的id不是用户的id，而是用户听歌形成的所有时间排行的排行版的id
        # driver.find_element_by_id('')

        driver.switch_to.frame('g_iframe')  # 从windows切换到frame，切换到歌曲列表所在的frame
        # driver.switch_to_frame(driver.find_element_by_id('g_iframe'))
        data=''#用来保存数据 电脑上下微信
        try:
            wait = ui.WebDriverWait(driver, 15)
            #找到歌曲列表所在的父标签
            if wait.until(lambda driver: driver.find_element_by_class_name('g-bd')):
                time.sleep(5)
                a = driver.find_element_by_id('songsall').click()
                #print(a)

                #print('success!')
                data+=driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text+'\n'
                #print(data)#抓取用户听了多少首歌
                time.sleep(3)
                lists = driver.find_element_by_class_name('m-record').find_elements_by_tag_name('li')

                #print(len(lists))#网易只给出了前100首听的最频繁的歌
                for l in lists:
                    song_name = l.find_element_by_tag_name('b').text.replace("'","")
                    singer = l.find_element_by_class_name('s-fc8').text.replace('-','')
                    frequency = l.find_element_by_class_name('bg').get_attribute('style').replace(';','')
                    # 存db    
                    MUSIC.objects.create(song_name = song_name,singer = singer,frequency = frequency,mis_id = id,star_id = uids)
                    
                    #temp='歌曲名：'+l.find_element_by_tag_name('b').text+'歌手：'+l.find_element_by_class_name('s-fc8').text.replace('-','')+' 频率：'+l.find_element_by_class_name('bg').get_attribute('style')
                    #print(temp)#解析出歌名 歌手 频率   -555555555555555
                    #data+=temp+'\n'

        finally:
            driver.quit()
        return 'success'
    except Exception, err:
        print (err)
        return 'err'
    #write2txt(data,'%s-songsall.txt'%id)#保存文件中
	
def song_week (id,uids):
    try:
        url = 'http://music.163.com/#/user/songs/rank?id=%s' % id
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options, executable_path='d:\chromedriver.exe')  # c
        # driver = webdriver.Chrome(executable_path='d:\chromedriver.exe')#chrome浏览器的驱动，下载链接：https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip

        driver.get("%s"%url)#需要抓取的用户链接，这里注意的是这里的id不是用户的id，而是用户听歌形成的所有时间排行的排行版的id
        # driver.find_element_by_id('')

        driver.switch_to.frame('g_iframe')  # 从windows切换到frame，切换到歌曲列表所在的frame
        # driver.switch_to_frame(driver.find_element_by_id('g_iframe'))
        data=''#用来保存数据
        try:
            wait = ui.WebDriverWait(driver, 15)
            #找到歌曲列表所在的父标签
            if wait.until(lambda driver: driver.find_element_by_class_name('g-bd')):
                time.sleep(5)
                a = driver.find_element_by_id('songsweek').click()
                #print(a)

                #print('success!')
                data+=driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text+'\n'
                #print(data)#抓取用户听了多少首歌
                time.sleep(3)
                lists = driver.find_element_by_class_name('m-record').find_elements_by_tag_name('li')

                #print(len(lists))#网易只给出了前30首听的最频繁的歌
                for l in lists:
                    song_name = l.find_element_by_tag_name('b').text.replace("'","")
                    singer = l.find_element_by_class_name('s-fc8').text.replace('-','')
                    frequency = l.find_element_by_class_name('bg').get_attribute('style').replace(';','')
                    # 存db
                    MUSIC.objects.create(song_name = song_name,singer = singer,frequency = frequency,mis_id = id,star_id = uids)
                    
                #  temp='歌曲名：'+l.find_element_by_tag_name('b').text+' 歌手：'+l.find_element_by_class_name('s-fc8').text.replace('-','')+' 频率：'+l.find_element_by_class_name('bg').get_attribute('style')
                    #print(temp)#解析出歌名 歌手 频率  -5555
                #  data+=temp+'\n'
                    
        finally:
            driver.quit()
        return 'success'
    except Exception, err:
        return 'err'

    #write2txt(data,'%ssongsweek.txt'%id)#保存文件中
	


	

#331986378/286145176/95278744/67259702
if __name__ == '__main__':
	
    id = input('请输入要爬取的歌曲的id:')
	
    song_all(id)
    song_week(id)