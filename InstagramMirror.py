from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Log import LogFile


class InstaMirror(object):
    """Main class"""

    def __init__(self, name='USERNAME', password='PASSWORD', copied_profile='PROFILE_ID', file_name='Log.txt'):  # TODO FIX CLASS INIT
        self.name = name  # Variables declaration
        self.password = password
        self.copied_profile = copied_profile
        self.file_name = file_name

        log = LogFile(file_name).terminal_to_file('Text')

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

    def delete_following(self):
        """Open following list after login"""
        profile = self.driver.find_element_by_css_selector(
            "a._soakw._vbtk2.coreSpriteDesktopNavProfile")
        profile.click()
        self.wait(3, "Openning following")

        following = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[3]/a')
        count_following = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/header/div[2]/ul/li[3]/a/span').text

        print("Following : " + count_following)
        following.click()
        self.wait(2)

        found = 1

        def scroll_down(self, count, max):
            """Scroll to END of screen"""
            pass

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

        following_range = range(int(count_following))
        self.wait(3, 'Deleting : ', False)

        for i in following_range:  # TODO Instagram guard?!
            profile_li = i + 1
            link = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[{}]/div/div[2]/span/button'.format(profile_li))
            link.click()

            sleep(2)

            nick = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[{}]/div/div[1]/div/div[1]/a'.format(profile_li)).text
            name = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div/div[2]/ul/li[{}]/div/div[1]/div/div[2]'.format(profile_li)).text
           #remaining = count_following - i
            print('Unfollowed : ({} / {}) remaining : '.format(name, nick))

        print('Deleted, copying profile follows of : ' + self.copied_profile)

    def wait(self, wait_time, message='Waiting', output=True):
        """Print waiting time"""
        print(message)
        if output:
            for i in range(wait_time):
                sleep(1)
                percent = '%.1f' % (((i + 1) / wait_time) * 100)
                print("{} %".format(percent))
        print("")


if __name__ == "__main__":
    mirror = InstaMirror()
    mirror.login()
    mirror.delete_following()
