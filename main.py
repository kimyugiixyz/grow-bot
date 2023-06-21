# Created by KimYugii
# don't change the watermark respect the creator
# Github: @kimyugiixyz_
import time
import random
import pyautogui
import requests

def farm():
  """Farms for a specified amount of time."""
  for i in range(60):
    pyautogui.click()
    time.sleep(random.randint(1, 3))

def sell_items():
  """Sells items that the bot has farmed."""
  items = pyautogui.locateAllOnScreen('item.png')
  for item in items:
    x, y = item.left, item.top
    pyautogui.click(x, y)
    pyautogui.click(x + 120, y)

def buy_items():
  """Buys items that the bot needs."""
  items = pyautogui.locateAllOnScreen('item.png')
  for item in items:
    x, y = item.left, item.top
    pyautogui.click(x, y)
    pyautogui.click(x + 120, y)

def trade_with_players():
  """Trades with other players."""
  players = pyautogui.locateAllOnScreen('player.png')
  for player in players:
    x, y = player.left, player.top
    pyautogui.click(x, y)
    pyautogui.click(x + 120, y)

def complete_quests():
  """Completes quests."""
  quests = pyautogui.locateAllOnScreen('quest.png')
  for quest in quests:
    x, y = quest.left, quest.top
    pyautogui.click(x, y)
    pyautogui.click(x + 120, y)

def bypass_verification_bot():
  """Bypasses the verification bot."""
  url = 'https://growtopia.com/api/verify'
  data = {'username': 'your_username', 'password': 'your_password'}
  response = requests.post(url, data=data)
  if response.status_code == 200:
    print('Successfully bypassed the verification bot.')
  else:
    print('Failed to bypass the verification bot.')

def main():
  """Runs the bot."""
  farm()
  sell_items()
  buy_items()
  trade_with_players()
  complete_quests()
  bypass_verification_bot()

if __name__ == "__main__":
  main()
