from player import Player
from .account import *


class Controller:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.play()
        self.strategy = self.get_strategy()

    def play(self):
        Generator(self.driver)
        self.get_started()
        self.round(no=10)

    def observe(self):
        return Player(Table(), self.strategy)

    def round(self, no, k=0):
        if self.listen_for_turn():
            player = self.observe()
            move = player.strategy.think()
            if move[0] == 'fold' and player.table.to_call != 0:
                return self.fold()
            elif (move[0] == 'fold' and player.table.to_call == 0) or move[0] == 'check':
                return self.check()
            elif move[0] == 'call':
                return self.call()
            elif move[0] == 'raise':
                amt = move[1]
                return self.raise_bet(amt)
        elif round_over:
            if no == k:
                break
            self.round(no, k + 1)
        elif out_of_cash:
            self.get_back()
            self.round(no, k + 1)

    def check(self):
        event = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tableBtnCheck")))
        event.click()

    def fold(self):
        event = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tableBtnFold")))
        event.click()

    def call(self):
        event = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tableBtnCall")))
        event.click()

    def raise_bet(self, amount):
        slider = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".action-slider-val-input")))
        slider.send_keys(amount)
        event = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tableBtnRaise")))
        event.click()

    def get_back(self):
        event = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tableBtnSitIn")))
        event.click()

    def get_strategy(self):
        strategy = input("What strategy do you want to play: ")
        return Strategy(strategy)

    def get_started(self):
        play_now = self.driver.find_element_by_xpath("//button[@id='carouselItem0 - playNow']")
        play_now.click()
        time.sleep(1)
        proceed = self.driver.find_element_by_xpath("//button[@id='modalBtnTXTWBCLI_COMMON_OK']")
        proceed.click()

    def listen(self):
        pass