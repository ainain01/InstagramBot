from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import tkinter as tk
from tkinter import filedialog

class Bot:
    comments = ['Great post!', 'Awesome!']

    def __init__(self, bot_account, actions):
        self.bot_account = bot_account
        self.actions = actions
        self.driver = None

    def login(self):
        chrome_path = r'C:/Users/Muhammad AinAin Khan/OneDrive/Desktop/youtube-master/chromedriver-win64/chromedriver-win64/chromedriver.exe'
        service = webdriver.chrome.service.Service(executable_path=chrome_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://instagram.com/')

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(
                self.bot_account['username'])
            self.driver.find_element(By.NAME, 'password').send_keys(self.bot_account['password'], Keys.RETURN)

            not_now_buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )

            for not_now_button in not_now_buttons:
                not_now_button.click()
                sleep(2)

        except Exception as e:
            print(f"Exception during login: {e}")

    def follow_view_like_comment_profile(self, target_accounts):
        try:
            for target_account in target_accounts:
                self.driver.get(f'https://www.instagram.com/{target_account}/')

                if 'follow' in self.actions:
                    follow_button = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH,
                                                        """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div""")))
                    follow_button.click()
                    sleep(3)

                if 'story' in self.actions:
                    try:
                        story_button = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH,
                                                            """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/div/div/span/img""")))
                        story_button.click()
                        sleep(3)
                    except:
                        pass

                if 'like_comment_follow' in self.actions:
                    self.like_comment_follow_latest_posts()

                print(f"Actions performed on {target_account}")

        except Exception as e:
            print(f"Exception during follow_view_like_comment_profile: {e}")

    def like_comment_follow_latest_posts(self):
        try:
            posts = self.driver.find_elements(By.XPATH, '//article//a[contains(@href, "/p/")]')

            for post in posts:
                post_link = post.get_attribute('href')
                self.driver.get(post_link)
                sleep(3)

                like_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[3]/div[1]/div[1]/span[1]/div""")))
                like_button.click()
                sleep(5)

                comment_input = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea""")))
                ActionChains(self.driver).move_to_element(comment_input).click().send_keys(
                    self.comments[0]).perform()
                sleep(1)

                post_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/div[2]/div""")))
                post_button.click()
                sleep(3)

                self.driver.get(f'https://www.instagram.com/{self.target_account}/')
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//article//a[contains(@href, "/p/")]')))

            print(f"Like, comment, and follow latest posts on {self.target_account}")

        except Exception as e:
            print(f"Exception during like_comment_follow_latest_posts: {e}")

    def send_message_to_account(self, target_account, message):
        try:
            self.driver.get(f'https://www.instagram.com/{target_account}/')

            message_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/direct/inbox/']")))
            message_button.click()
            sleep(3)

            try:
                not_now_button = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
                not_now_button.click()
                sleep(2)
            except:
                pass

            new_message_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div""")))
            new_message_button.click()
            sleep(3)

            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     """/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input""")))
            search_input.send_keys(target_account)
            sleep(2)

            account_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     f"""/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input""")))
            account_link.click()
            sleep(2)

            chat_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, """/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div""")))
            chat_button.click()
            sleep(2)

            message_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p""")))
            message_input.send_keys(message)
            message_input.send_keys(Keys.RETURN)
            sleep(3)

            print(f"Message sent to {target_account}")

        except Exception as e:
            print(f"Exception during send_message_to_account: {e}")

    def process_account(self, target_accounts):
        try:
            self.login()
            self.follow_view_like_comment_profile(target_accounts)
            if 'message' in self.actions:
                for target_account in target_accounts:
                    self.send_message_to_account(target_account, 'HEY! Follow @manifiestamgmt')
        except Exception as e:
            print(f"Exception during process_account: {e}")
        finally:
            if self.driver:
                self.driver.quit()

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def run_bot_callback(bot_account_entry, target_account_entry, actions_var):
    bot_account_file = bot_account_entry.get()
    target_account_file = target_account_entry.get()
    actions = [action for action in actions_var]

    with open(bot_account_file, 'r') as file:
        bot_accounts = [{'username': line.split(',')[0], 'password': line.split(',')[1]} for line in file]

    with open(target_account_file, 'r') as file:
        target_accounts = file.read().splitlines()

    for bot_account in bot_accounts:
        user_bot = Bot(bot_account, actions)
        user_bot.process_account(target_accounts)

def main_interface():
    root = tk.Tk()
    root.title("Instagram Bot Interface")

    # Bot Account Entry
    bot_account_label = tk.Label(root, text="Bot Account File:")
    bot_account_label.pack()

    bot_account_entry = tk.Entry(root)
    bot_account_entry.pack()

    browse_bot_account_button = tk.Button(root, text="Browse", command=lambda: browse_file(bot_account_entry))
    browse_bot_account_button.pack()

    # Target Account Entry
    target_account_label = tk.Label(root, text="Target Account File:")
    target_account_label.pack()

    target_account_entry = tk.Entry(root)
    target_account_entry.pack()

    browse_target_account_button = tk.Button(root, text="Browse", command=lambda: browse_file(target_account_entry))
    browse_target_account_button.pack()

    # Action Selection
    actions_var = []

    def on_checkbox_change(checkbox_value):
        if checkbox_value not in actions_var:
            actions_var.append(checkbox_value)
        else:
            actions_var.remove(checkbox_value)

    follow_checkbox = tk.Checkbutton(root, text="Follow", variable=tk.StringVar(), onvalue="follow",
                                     command=lambda: on_checkbox_change("follow"))
    like_checkbox = tk.Checkbutton(root, text="Like/Comment", variable=tk.StringVar(),
                                   onvalue="like_comment_follow", command=lambda: on_checkbox_change("like_comment_follow"))
    message_checkbox = tk.Checkbutton(root, text="Message", variable=tk.StringVar(),
                                      onvalue="message", command=lambda: on_checkbox_change("message"))
    story_checkbox = tk.Checkbutton(root, text="Story View", variable=tk.StringVar(),
                                    onvalue="story", command=lambda: on_checkbox_change("story"))

    follow_checkbox.pack()
    like_checkbox.pack()
    message_checkbox.pack()
    story_checkbox.pack()

    # Run Button
    run_button = tk.Button(root, text="Run Bot",
                           command=lambda: run_bot_callback(bot_account_entry, target_account_entry, actions_var))
    run_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main_interface()