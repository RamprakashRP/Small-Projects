from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import csv
import datetime

chromedriver_path = 'C:/Users/allpo/Desktop/Python/Projects/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('rp_py_test')
password = webdriver.find_element_by_name('password')
password.send_keys('Everypowerishere1.')

button_login = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

hashtag_list = ['likes', 'like', 'follow', 'likeforlikes', 'love', 'instagood', 'instagram', 'followforfollowback', 'followme', 'photooftheday', 'photography', 'bhfyp', 'instalike', 'l', 'instadaily', 'picoftheday', 'likeforfollow', 'fashion', 'beautiful', 'me', 'followers', 'smile', 'likeforlike', 'myself', 'followback', 'f', 'comment', 'followforfollow', 'likesforlikes', 'art', 'style', 'happy', 'photo', 'life', 'nature', 'insta', 'cute', 'viral', 'likesforlike', 'model', 'music', 'travel', 'memes', 'explorepage', 'liker', 'girl', 'explore', 'selfie', 'india', 'beauty', 'k', 'lfl', 'trending', 'following', 'likeback', 'loveyourself', 'lifestyle', 'tiktok', 'photoshoot', 'photographer']

prev_user_list = [] # if it's the first time you run it, use this line and comment the two below
with open("users_followed_list.csv") as f:
    data = csv.reader(f)
    for x in data:
        prev_user_list.append(x)
print(prev_user_list)
#prev_user_list = csv.read('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:, 1:2]  # useful to build a user log
#prev_user_list = list(prev_user_list[0])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(2.5)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(randint(1, 2))
    try:
        for x in range(1, 200):
            username = webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]').text

            if username not in prev_user_list:
                # If we already follow, do not unfollow
                if webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                    webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()

                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')

                    button_like.click()
                    likes += 1
                    sleep(randint(5, 8))

                    # Comments and tracker
                    comm_prob = randint(1, 10)
                    print('{}_{}: {}'.format(hashtag, x, comm_prob))
                    if comm_prob > 4:
                        comments += 1
                        webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]').click()
                        comment_box = webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')

                        if (comm_prob < 7):
                            comment_box.send_keys('Really cool! Do Follow @thuglife._.tamil')
                            sleep(1)
                        elif (comm_prob > 6) and (comm_prob < 9):
                            comment_box.send_keys('Nice work :) Do Follow @thuglife._.tamil')
                            sleep(1)
                        elif comm_prob == 9:
                            comment_box.send_keys('Nice gallery!! Do Follow @thuglife._.tamil')
                            sleep(1)
                        elif comm_prob == 10:
                            comment_box.send_keys('So cool! :) Do Follow @thuglife._.tamil')
                            sleep(1)
                        # Enter to post comment
                        post = webdriver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button')

                        post.click()
                        sleep(randint(12, 18))

                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(15, 19))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(10, 16))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for i in new_followed:
    l = [i, datetime.datetime.now().strftime("%d-%m-%y")]
    prev_user_list.append(l)

print(prev_user_list)

with open("users_followed_list.csv","w") as file:
    write = csv.writer(file)
    write.writerows(prev_user_list)

print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
