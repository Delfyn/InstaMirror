from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Log import LogFile

import datetime


class InstaMirror(object):
    """Main class"""

    def __init__(self, username, password, copied_profile, file_name='Log.txt'):  # TODO FIX CLASS INIT
        self.username = username  # Variables declaration
        self.password = password
        self.copied_profile = copied_profile
        self.file_name = file_name

       # self.login()
       # self.delete_following()
        self.get_remote_follows()

    chrome_options = Options()
    chrome_options.add_argument("--dns-prefetch-disable")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--lang=en-US")

    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)
    except FileNotFoundError:
        print("chromedriver.exe not found")

    def login(self):
        """Login to IG """
        self.driver.get("https://www.instagram.com")
        login_button = self.driver.find_element_by_class_name("_fcn8k")
        login_button.click()
        username_field = self.driver.find_element_by_class_name("_qy55y")
        username_field.send_keys(self.name)
        self.wait(2, "Password")
        password_field = self.driver.find_element_by_class_name("_1mdqd")
        password_field.send_keys(self.password)
        login_click = self.driver.find_element_by_class_name("_84y62")
        login_click.click()
        self.wait(5, "Load full page")  # TODO if successful

    def get_following(self, profile):
        """Open following list after login"""
        self.driver.get("https://instagram.com/{}".format(profile))
        self.wait(3, "Openning following")

        following = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[3]/a')
        count_following = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[3]/a/span').text

        print("Following : " + count_following)
        following.click()
        self.wait(2)

        found = 1

        while (found < int(count_following)):
            following_scroll = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[{}]'.format(found))

            following_list = self.driver.find_elements_by_class_name(
                '_cx1ua')
            found = len(following_list)
            sleep(1)  # TODO

            ActionChains(self.driver).key_down(
                Keys.END).click(following_scroll).key_up(Keys.END).perform()  # TODO
            self.wait(0, "Loaded : {}".format(found), False)
        return count_following

    def delete_following(self):
            following_range = range(int(get_following(self.username))
            self.wait(3, 'Deleting : ', False)
            LogFile().write_to_file("Unfollowed : ")

            for i in following_range:  # TODO Instagram guard?!
                profile_li=i + 1
                link=self.driver.find_element_by_xpath(
                    '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[{}]/div/div[2]/span/button'.format(profile_li))
                link.click()

                sleep(2)

                nick=self.driver.find_element_by_xpath(
                    '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[{}]/div/div[1]/div/div[1]/a'.format(profile_li)).text

                name=self.driver.find_element_by_xpath(
                    '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[{}]/div/div[1]/div/div[2]'.format(profile_li)).text
                remaining=count_following - i  # TODO ?
                print('Unfollowed : ({} / {}) remaining : {}'.format(name,
                                                                    nick, str(remaining)))
                LogFile().write_to_file(str(nick) + str(name))

    def get_remote_follows(self):
        """Copy following from REMOTE_PROFILE"""
        self.get_following(self.copied_profile)

    def remote_follow(self):
        print("Following : ")



    def wait(self, wait_time, message='Waiting', output=True):
        """Print waiting time"""
        print(message)
        if output:
            for i in range(wait_time):
                sleep(1)
                percent='%.1f' % (((i + 1) / wait_time) * 100)
                print("{} %".format(percent))
        print("")


if __name__ == "__main__":
    mirror=InstaMirror("USERNAME", "PASSWORD", "REMOTE_PROFILE")
