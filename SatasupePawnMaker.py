#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

class SkillData():
    name = ""
    skill_class = ""
    level = ""
    timing = ""
    target = ""
    range = ""
    cost = ""
    memo = ""

class HeroData():
    character_name = ""
    player_name = ""

    crime = 0
    life = 0
    love = 0
    culture = 0
    combat = 0
    body = 0
    mind = 0
    emotion = 0
    power = 0
    initiative = 0
    attack = 0
    destroy = 0

    url = ""

    def input_data(self, driver, input_url):
        self.url = input_url
        self.character_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
        self.player_name = driver.find_element(by=By.ID, value="base.player").get_attribute("value")
        self.crime = driver.find_element(by=By.ID, value="base.abl.crime.value").get_attribute("value")
        self.life = driver.find_element(by=By.ID, value="base.abl.life.value").get_attribute("value")
        self.love = driver.find_element(by=By.ID, value="base.abl.love.value").get_attribute("value")
        self.culture = driver.find_element(by=By.ID, value="base.abl.culture.value").get_attribute("value")
        self.combat = driver.find_element(by=By.ID, value="base.abl.combat.value").get_attribute("value")
        self.body = driver.find_element(by=By.ID, value="base.gift.body.value").get_attribute("value")
        self.mind = driver.find_element(by=By.ID, value="base.gift.mind.value").get_attribute("value")
        self.emotion = driver.find_element(by=By.ID, value="base.emotion").get_attribute("value")
        self.power = driver.find_element(by=By.ID, value="base.power.total.value").get_attribute("value")
        self.initiative = driver.find_element(by=By.ID, value="base.power.initiative").get_attribute("value")
        self.attack = driver.find_element(by=By.ID, value="base.power.attack").get_attribute("value")
        self.destroy = driver.find_element(by=By.ID, value="base.power.destroy").get_attribute("value")

        print(self.character_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "PC:" + self.character_name +  \
                   "\nPL:" + self.player_name

        text = text + "\n【犯罪】" + str(self.crime) + \
                   "【生活】" + str(self.life) + \
                   "【恋愛】" + str(self.love) + \
                   "【教養】" + str(self.culture) + \
                   "【戦闘】" + str(self.combat) + \
                   "\n" + \
                   "【肉体】" + str(self.body) + \
                   "【精神】" + str(self.mind) + \
                   "【性業値】" + str(self.emotion) + \
                   "\n【戦闘力】" + str(self.power) + \
                   "【反応力】" + str(self.initiative) + \
                   "【攻撃力】" + str(self.attack) + \
                   "【破壊力】" + str(self.destroy)

        print(text)

        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_キャラクターテキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("キャラクターテキストデータを生成しました")
        self.output_porn(text)

    def output_porn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.character_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = int(self.initiative)
        jsontext["data"]["status"] = []

        i = 0

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "肉体"
        jsontext["data"]["status"][i]["value"] = self.body
        jsontext["data"]["status"][i]["max"] = self.body
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "精神"
        jsontext["data"]["status"][i]["value"] = self.mind
        jsontext["data"]["status"][i]["max"] = self.mind
        i = i + 1

        jsontext["data"]["params"] = []

        j = 0

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "犯罪"
        jsontext["data"]["params"][j]["value"] = self.crime
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "生活"
        jsontext["data"]["params"][j]["value"] = self.life
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "恋愛"
        jsontext["data"]["params"][j]["value"] = self.love
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "教養"
        jsontext["data"]["params"][j]["value"] = self.culture
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "戦闘"
        jsontext["data"]["params"][j]["value"] = self.combat
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "性業値"
        jsontext["data"]["params"][j]["value"] = self.emotion
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "戦闘力"
        jsontext["data"]["params"][j]["value"] = self.power
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "攻撃力"
        jsontext["data"]["params"][j]["value"] = self.attack
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "破壊力"
        jsontext["data"]["params"][j]["value"] = self.destroy
        j = j + 1

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        command = ("//行為判定 0に難易度と必要成功度を入れる\n{犯罪}r>=0[0]　犯罪判定\n{生活}r>=0[0]　生活判定\n{恋愛}r>=0[0]　恋愛判定\n"
                   "{教養}r>=0[0]　教養判定\n{戦闘}r>=0[0]　戦闘判定\n{攻撃力}r>=0[0]　攻撃力判定\n//一般判定\n2d6\n1d6")

        jsontext["data"]["commands"] = command
        jsontext["data"]["externalUrl"] = self.url
        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_キャラクター駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as file:  # 第二引数：writableオプションを指定
            json.dump(jsontext, file, ensure_ascii=False)

        print("キャラクター駒データを生成しました")


def get_data(value):

    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    akyo = HeroData()
    time.sleep(5)

    akyo.input_data(driver, url)
    akyo.output_text()

    driver.quit()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"サタスペRPG ココフォリア用駒データ作成ツール")
    root.geometry("400x150")


    frame1 = tkinter.Frame(root, width=400, height=50)  # Label
    frame2 = tkinter.Frame(root, width=400, height=50)  # Button, Entry
    frame3 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame4 = tkinter.Frame(root, width=200, height=50)  # Button, Entry

    frame1.propagate(False)
    frame2.propagate(False)
    frame3.propagate(False)
    frame4.propagate(False)

    # Frameを配置（grid）
    frame1.grid(row=0, column=0, columnspan=2)
    frame2.grid(row=1, column=0, columnspan=2)
    frame3.grid(row=2, column=0)
    frame4.grid(row=2, column=1)

    # ラベル
    Static1 = tkinter.Label(frame1,text=u'キャラクターシートURL\nhttps://character-sheets.appspot.com/satasupe/')
    Static1.pack()

    # エントリー
    EditBox = tkinter.Entry(frame2, width=50)
    EditBox.pack()

    Button1 = tkinter.Button(frame3, text=u'生成', command=lambda: [get_data(EditBox.get())])
    Button1.pack()

    # ボタン
    Button2 = tkinter.Button(frame4, text=u'終了', command=lambda: root.quit())
    Button2.pack()

    root.mainloop()