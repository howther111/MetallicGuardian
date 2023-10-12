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


class GuardianData():
    character_name = ""
    guardian_name = ""
    level = 0
    guardian_size = ""
    player_name = ""
    strong_total = 0
    strong_bonus = 0
    reflex_total = 0
    reflex_bonus = 0
    sense_total = 0
    sense_bonus = 0
    intellect_total = 0
    intellect_bonus = 0
    will_total = 0
    will_bonus = 0
    bllesing_total = 0
    bllesing_bonus = 0
    specials_000 = ""
    specials_001 = ""
    specials_002 = ""
    specials_003 = ""
    specials_004 = ""
    add_fortune_point = 0
    outfits_total_hit = 0
    outfits_total_dodge = 0
    outfits_total_magic = 0
    outfits_total_countermagic = 0
    outfits_total_action = 0
    outfits_total_fp = 0
    outfits_total_hp = 0
    outfits_total_mp = 0
    outfits_total_attack = 0
    outfits_total_battlespeed_total = ""

    outfits_main_weapon_shortname = ""
    outfits_main_weapon_shortattack = ""
    outfits_main_weapon_shortrange = ""
    outfits_main_weapon_shortstrong = ""

    outfits_sub_weapon_shortname = ""
    outfits_sub_weapon_shortattack = ""
    outfits_sub_weapon_shortrange = ""
    outfits_sub_weapon_shortstrong = ""

    outfits_main_weapon_longname = ""
    outfits_main_weapon_longattack = ""
    outfits_main_weapon_longrange = ""
    outfits_main_weapon_longstrong = ""

    outfits_sub_weapon_longname = ""
    outfits_sub_weapon_longattack = ""
    outfits_sub_weapon_longrange = ""
    outfits_sub_weapon_longstrong = ""

    armourstotal_slash = 0
    armourstotal_pierce = 0
    armourstotal_crash = 0
    armourstotal_fire = 0
    armourstotal_ice = 0
    armourstotal_thunder = 0
    armourstotal_light = 0
    armourstotal_dark = 0

    break_flg = 0

    url = ""

    def input_data(self, driver, input_url):
        self.url = input_url
        self.character_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
        self.guardian_name = driver.find_element(by=By.ID, value="base.guardian.name").get_attribute("value")
        self.level = driver.find_element(by=By.ID, value="base.level").get_attribute("value")
        self.guardian_size = driver.find_element(by=By.ID, value="base.guardian.size").get_attribute("value")
        self.player_name = driver.find_element(by=By.ID, value="base.player").get_attribute("value")
        self.strong_total = driver.find_element(by=By.ID, value="abl.strong.total").get_attribute("value")
        self.strong_bonus = driver.find_element(by=By.ID, value="abl.strong.bonus").get_attribute("value")
        self.reflex_total = driver.find_element(by=By.ID, value="abl.reflex.total").get_attribute("value")
        self.reflex_bonus = driver.find_element(by=By.ID, value="abl.reflex.bonus").get_attribute("value")
        self.sense_total = driver.find_element(by=By.ID, value="abl.sense.total").get_attribute("value")
        self.sense_bonus = driver.find_element(by=By.ID, value="abl.sense.bonus").get_attribute("value")
        self.intellect_total = driver.find_element(by=By.ID, value="abl.intellect.total").get_attribute("value")
        self.intellect_bonus = driver.find_element(by=By.ID, value="abl.intellect.bonus").get_attribute("value")
        self.will_total = driver.find_element(by=By.ID, value="abl.will.total").get_attribute("value")
        self.will_bonus = driver.find_element(by=By.ID, value="abl.will.bonus").get_attribute("value")
        self.bllesing_total = driver.find_element(by=By.ID, value="abl.bllesing.total").get_attribute("value")
        self.bllesing_bonus = driver.find_element(by=By.ID, value="abl.bllesing.bonus").get_attribute("value")
        self.specials_000 = driver.find_element(by=By.ID, value="specials.0.name").get_attribute("value")
        self.specials_001 = driver.find_element(by=By.ID, value="specials.001.name").get_attribute("value")
        self.specials_002 = driver.find_element(by=By.ID, value="specials.002.name").get_attribute("value")
        try:
            self.specials_003 = driver.find_element(by=By.ID, value="specials.003.name").get_attribute("value")

        except:
            pass

        try:
            self.specials_004 = driver.find_element(by=By.ID, value="specials.004.name").get_attribute("value")

        except:
            pass

        self.outfits_total_hit = driver.find_element(by=By.ID, value="outfits.total.hit").get_attribute("value")
        self.outfits_total_dodge = driver.find_element(by=By.ID, value="outfits.total.dodge").get_attribute("value")
        self.outfits_total_magic = driver.find_element(by=By.ID, value="outfits.total.magic").get_attribute("value")
        self.outfits_total_countermagic = driver.find_element(by=By.ID, value="outfits.total.countermagic").get_attribute("value")
        self.outfits_total_action = driver.find_element(by=By.ID, value="outfits.total.action").get_attribute("value")
        self.outfits_total_fp = driver.find_element(by=By.ID, value="outfits.total.fp").get_attribute("value")
        self.outfits_total_hp = driver.find_element(by=By.ID, value="outfits.total.hp").get_attribute("value")
        self.outfits_total_mp = driver.find_element(by=By.ID, value="outfits.total.mp").get_attribute("value")
        self.outfits_total_action = driver.find_element(by=By.ID, value="outfits.total.action").get_attribute("value")
        self.outfits_total_battlespeed_total = driver.find_element(by=By.ID, value="outfits.total.battlespeed.total").get_attribute("value")
        self.outfits_total_battlespeed_total = self.outfits_total_battlespeed_total.replace("ﾏｽ", "")

        self.add_fortune_point = driver.find_element(by=By.ID, value="addfortunepoint").get_attribute("value")

        self.outfits_main_weapon_shortname = driver.find_element(by=By.ID, value="outfits.total.main_weapon_shortname").get_attribute("value")
        self.outfits_main_weapon_shortattack = driver.find_element(by=By.ID, value="outfits.total.main_weapon_shortattack").get_attribute("value")
        self.outfits_main_weapon_shortrange = driver.find_element(by=By.ID, value="outfits.total.main_weapon_shortrange").get_attribute("value")
        self.outfits_main_weapon_shortstrong = driver.find_element(by=By.ID, value="outfits.total.main_weapon_shortstrong").get_attribute("value")

        self.outfits_sub_weapon_shortname = driver.find_element(by=By.ID, value="outfits.total.sub_weapon_shortname").get_attribute("value")
        self.outfits_sub_weapon_shortattack = driver.find_element(by=By.ID, value="outfits.total.sub_weapon_shortattack").get_attribute("value")
        self.outfits_sub_weapon_shortrange = driver.find_element(by=By.ID, value="outfits.total.sub_weapon_shortrange").get_attribute("value")
        self.outfits_sub_weapon_shortstrong = driver.find_element(by=By.ID, value="outfits.total.sub_weapon_shortstrong").get_attribute("value")

        self.outfits_main_weapon_longname = driver.find_element(by=By.ID,
                                                                value="outfits.total.main_weapon_longname").get_attribute(
            "value")
        self.outfits_main_weapon_longattack = driver.find_element(by=By.ID,
                                                                  value="outfits.total.main_weapon_longattack").get_attribute(
            "value")
        self.outfits_main_weapon_longrange = driver.find_element(by=By.ID,
                                                                 value="outfits.total.main_weapon_longrange").get_attribute(
            "value")
        self.outfits_main_weapon_longstrong = driver.find_element(by=By.ID,
                                                                  value="outfits.total.main_weapon_longstrong").get_attribute(
            "value")

        self.outfits_sub_weapon_longname = driver.find_element(by=By.ID,
                                                               value="outfits.total.sub_weapon_longname").get_attribute(
            "value")
        self.outfits_sub_weapon_longattack = driver.find_element(by=By.ID,
                                                                 value="outfits.total.sub_weapon_longattack").get_attribute(
            "value")
        self.outfits_sub_weapon_longrange = driver.find_element(by=By.ID,
                                                                value="outfits.total.sub_weapon_longrange").get_attribute(
            "value")
        self.outfits_sub_weapon_longstrong = driver.find_element(by=By.ID,
                                                                 value="outfits.total.sub_weapon_longstrong").get_attribute(
            "value")

        self.armourstotal_slash = driver.find_element(by=By.ID, value="armourstotal.slash").get_attribute("value")
        self.armourstotal_pierce = driver.find_element(by=By.ID, value="armourstotal.pierce").get_attribute("value")
        self.armourstotal_crash = driver.find_element(by=By.ID, value="armourstotal.crash").get_attribute("value")
        self.armourstotal_fire = driver.find_element(by=By.ID, value="armourstotal.fire").get_attribute("value")
        self.armourstotal_ice = driver.find_element(by=By.ID, value="armourstotal.ice").get_attribute("value")
        self.armourstotal_thunder = driver.find_element(by=By.ID, value="armourstotal.thunder").get_attribute("value")
        self.armourstotal_light = driver.find_element(by=By.ID, value="armourstotal.light").get_attribute("value")
        self.armourstotal_dark = driver.find_element(by=By.ID, value="armourstotal.dark").get_attribute("value")

        print(self.guardian_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "ガーディアン:" + self.guardian_name + "\n" + \
                   "PC:" + self.character_name +  \
                   " PL:" + self.player_name + "\n" + \
                   "レベル:" + self.level + \
                   " サイズ:" + self.guardian_size

        text = text + "\n財産ポイント:" + self.add_fortune_point

        text = text + "\n【命中】" + str(self.outfits_total_hit) + \
                   "【回避】" + str(self.outfits_total_dodge) + \
                   "【砲撃】" + str(self.outfits_total_magic) + \
                   "【防壁】" + str(self.outfits_total_countermagic) + \
                   "【行動】" + str(self.outfits_total_action) + \
                   "\n【力場】" + str(self.outfits_total_fp) + \
                   "【耐久】" + str(self.outfits_total_hp) + \
                   "【感応】" + str(self.outfits_total_hp) + \
                   "【移動力】" + str(self.outfits_total_battlespeed_total)

        text = text + "\n加護:" + self.specials_000 + "/" + self.specials_001 + "/" + self.specials_002

        if self.specials_003 != "":
            text = text + "/" + self.specials_003

        if self.specials_004 != "":
            text = text + "/" + self.specials_004

        text = text + "\n[*]主近:" + self.outfits_main_weapon_shortname + \
                " 射程:" + self.outfits_main_weapon_shortrange + \
                " 代償:" + self.outfits_main_weapon_shortstrong + \
                "\n攻撃力:" + self.outfits_main_weapon_shortattack

        text = text + "\n[*]副近:" + self.outfits_sub_weapon_shortname + \
                " 射程:" + self.outfits_sub_weapon_shortrange + \
                " 代償:" + self.outfits_sub_weapon_shortstrong + \
                "\n攻撃力:" + self.outfits_sub_weapon_shortattack

        text = text + "\n[*]主遠:" + self.outfits_main_weapon_longname + \
                   " 射程:" + self.outfits_main_weapon_longrange + \
                   " 代償:" + self.outfits_main_weapon_longstrong + \
                   "\n攻撃力:" + self.outfits_main_weapon_longattack

        text = text + "\n[*]副遠:" + self.outfits_sub_weapon_longname + \
                   " 射程:" + self.outfits_sub_weapon_longrange + \
                   " 代償:" + self.outfits_sub_weapon_longstrong + \
                   "\n攻撃力:" + self.outfits_sub_weapon_longattack

        text = text + "\n防御力:斬" + self.armourstotal_slash + \
                "/刺" + self.armourstotal_pierce + \
                "/殴" + self.armourstotal_crash + \
                "/炎" + self.armourstotal_fire + \
                "/氷" + self.armourstotal_ice + \
                "/雷" + self.armourstotal_thunder + \
                "/光" + self.armourstotal_light + \
                "/闇" + self.armourstotal_dark

        print(text)

        file_name = self.guardian_name + "_ガーディアンテキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("ガーディアンテキストデータを生成しました")
        self.output_porn(text)

    def output_porn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.guardian_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = int(self.outfits_total_action)
        jsontext["data"]["status"] = []

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][0]["label"] = "FP"
        jsontext["data"]["status"][0]["value"] = self.outfits_total_fp
        jsontext["data"]["status"][0]["max"] = self.outfits_total_fp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][1]["label"] = "HP"
        jsontext["data"]["status"][1]["value"] = self.outfits_total_hp
        jsontext["data"]["status"][1]["max"] = self.outfits_total_hp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][2]["label"] = "EN"
        jsontext["data"]["status"][2]["value"] = self.outfits_total_mp
        jsontext["data"]["status"][2]["max"] = self.outfits_total_mp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][3]["label"] = "財産ポイント"
        jsontext["data"]["status"][3]["value"] = self.add_fortune_point
        jsontext["data"]["status"][3]["max"] = self.add_fortune_point

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][4]["label"] = "ブレイク"
        jsontext["data"]["status"][4]["value"] = 1
        jsontext["data"]["status"][4]["max"] = 1

        i = 5
        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = self.specials_000
        jsontext["data"]["status"][i]["value"] = 1
        jsontext["data"]["status"][i]["max"] = 1
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = self.specials_001
        jsontext["data"]["status"][i]["value"] = 1
        jsontext["data"]["status"][i]["max"] = 1
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = self.specials_002
        jsontext["data"]["status"][i]["value"] = 1
        jsontext["data"]["status"][i]["max"] = 1
        i = i + 1

        if self.specials_003 != "":
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = self.specials_003
            jsontext["data"]["status"][i]["value"] = 1
            jsontext["data"]["status"][i]["max"] = 1
            i = i + 1

        if self.specials_004 != "":
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = self.specials_004
            jsontext["data"]["status"][i]["value"] = 1
            jsontext["data"]["status"][i]["max"] = 1
            i = i + 1

        jsontext["data"]["params"] = []
        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][0]["label"] = "体力"
        jsontext["data"]["params"][0]["value"] = self.strong_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][1]["label"] = "反射"
        jsontext["data"]["params"][1]["value"] = self.sense_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][2]["label"] = "知覚"
        jsontext["data"]["params"][2]["value"] = self.strong_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][3]["label"] = "理知"
        jsontext["data"]["params"][3]["value"] = self.intellect_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][4]["label"] = "意志"
        jsontext["data"]["params"][4]["value"] = self.will_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][5]["label"] = "幸運"
        jsontext["data"]["params"][5]["value"] = self.bllesing_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][6]["label"] = "命中"
        jsontext["data"]["params"][6]["value"] = self.outfits_total_hit

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][7]["label"] = "回避"
        jsontext["data"]["params"][7]["value"] = self.outfits_total_dodge

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][8]["label"] = "砲撃"
        jsontext["data"]["params"][8]["value"] = self.outfits_total_magic

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][9]["label"] = "防壁"
        jsontext["data"]["params"][9]["value"] = self.outfits_total_countermagic

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][10]["label"] = "行動"
        jsontext["data"]["params"][10]["value"] = self.outfits_total_action

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][11]["label"] = "移動力"
        jsontext["data"]["params"][11]["value"] = self.outfits_total_battlespeed_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][12]["label"] = "斬防御"
        jsontext["data"]["params"][12]["value"] = self.armourstotal_slash

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][13]["label"] = "刺防御"
        jsontext["data"]["params"][13]["value"] = self.armourstotal_pierce

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][14]["label"] = "殴防御"
        jsontext["data"]["params"][14]["value"] = self.armourstotal_crash

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][15]["label"] = "炎防御"
        jsontext["data"]["params"][15]["value"] = self.armourstotal_fire

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][16]["label"] = "氷防御"
        jsontext["data"]["params"][16]["value"] = self.armourstotal_ice

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][17]["label"] = "雷防御"
        jsontext["data"]["params"][17]["value"] = self.armourstotal_thunder

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][18]["label"] = "光防御"
        jsontext["data"]["params"][18]["value"] = self.armourstotal_light

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][19]["label"] = "闇防御"
        jsontext["data"]["params"][19]["value"] = self.armourstotal_dark

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        jsontext["data"]["commands"] = ""
        jsontext["data"]["externalUrl"] = self.url
        file_name = self.guardian_name + "_ガーディアン駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as file:  # 第二引数：writableオプションを指定
            json.dump(jsontext, file)

        print("ガーディアン駒データを生成しました")


class CharacterData():
    url = ""
    character_name = ""
    player_name = ""
    strong_total = 0
    strong_bonus = 0
    reflex_total = 0
    reflex_bonus = 0
    sense_total = 0
    sense_bonus = 0
    intellect_total = 0
    intellect_bonus = 0
    will_total = 0
    will_bonus = 0
    bllesing_total = 0
    bllesing_bonus = 0
    specials_000 = ""
    specials_001 = ""
    specials_002 = ""
    specials_003 = ""
    specials_004 = ""
    add_fortune_point = 0
    battlesubtotal_hit = 0
    battlesubtotal_dodge = 0
    battlesubtotal_magic = 0
    battlesubtotal_countermagic = 0
    battlesubtotal_action = 0
    battlesubtotal_fp = 0
    battlesubtotal_hp = 0
    battlesubtotal_mp = 0
    battlesubtotal_attack = 0

    def input_data(self, driver, input_url):
        self.url = input_url
        self.character_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
        self.player_name = driver.find_element(by=By.ID, value="base.player").get_attribute("value")
        self.strong_total = driver.find_element(by=By.ID, value="abl.strong.total").get_attribute("value")
        self.strong_bonus = driver.find_element(by=By.ID, value="abl.strong.bonus").get_attribute("value")
        self.reflex_total = driver.find_element(by=By.ID, value="abl.reflex.total").get_attribute("value")
        self.reflex_bonus = driver.find_element(by=By.ID, value="abl.reflex.bonus").get_attribute("value")
        self.sense_total = driver.find_element(by=By.ID, value="abl.sense.total").get_attribute("value")
        self.sense_bonus = driver.find_element(by=By.ID, value="abl.sense.bonus").get_attribute("value")
        self.intellect_total = driver.find_element(by=By.ID, value="abl.intellect.total").get_attribute("value")
        self.intellect_bonus = driver.find_element(by=By.ID, value="abl.intellect.bonus").get_attribute("value")
        self.will_total = driver.find_element(by=By.ID, value="abl.will.total").get_attribute("value")
        self.will_bonus = driver.find_element(by=By.ID, value="abl.will.bonus").get_attribute("value")
        self.bllesing_total = driver.find_element(by=By.ID, value="abl.bllesing.total").get_attribute("value")
        self.bllesing_bonus = driver.find_element(by=By.ID, value="abl.bllesing.bonus").get_attribute("value")
        self.specials_000 = driver.find_element(by=By.ID, value="specials.0.name").get_attribute("value")
        self.specials_001 = driver.find_element(by=By.ID, value="specials.001.name").get_attribute("value")
        self.specials_002 = driver.find_element(by=By.ID, value="specials.002.name").get_attribute("value")
        self.battlesubtotal_hit = driver.find_element(by=By.ID, value="battlesubtotal.hit").get_attribute("value")
        self.battlesubtotal_dodge = driver.find_element(by=By.ID, value="battlesubtotal.dodge").get_attribute("value")
        self.battlesubtotal_magic = driver.find_element(by=By.ID, value="battlesubtotal.magic").get_attribute("value")
        self.battlesubtotal_countermagic = driver.find_element(by=By.ID, value="battlesubtotal.countermagic").get_attribute("value")
        self.battlesubtotal_action = driver.find_element(by=By.ID, value="battlesubtotal.action").get_attribute("value")
        self.battlesubtotal_fp = driver.find_element(by=By.ID, value="battlesubtotal.fp").get_attribute("value")
        self.battlesubtotal_hp = driver.find_element(by=By.ID, value="battlesubtotal.hp").get_attribute("value")
        self.battlesubtotal_mp = driver.find_element(by=By.ID, value="battlesubtotal.mp").get_attribute("value")
        self.battlesubtotal_attack = driver.find_element(by=By.ID, value="battlesubtotal.attack").get_attribute("value")

        try:
            self.specials_003 = driver.find_element(by=By.ID, value="specials.003.name").get_attribute("value")

        except:
            pass

        try:
            self.specials_004 = driver.find_element(by=By.ID, value="specials.004.name").get_attribute("value")

        except:
            pass

        self.add_fortune_point = driver.find_element(by=By.ID, value="addfortunepoint").get_attribute("value")
        print(self.character_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "PC:" + self.character_name + \
               " PL:" + self.player_name + "\n"

        text = text + "【体力】" + str(self.strong_total) + "/+" + str(self.strong_bonus) + \
               "【反射】" + str(self.reflex_total) + "/+" + str(self.reflex_bonus) + \
               "【知覚】" + str(self.sense_total) + "/+" + str(self.sense_bonus) + \
               "\n【理知】" + str(self.intellect_total) + "/+" + str(self.intellect_bonus) + \
               "【意志】" + str(self.will_total) + "/+" + str(self.will_bonus) + \
               "【幸運】" + str(self.bllesing_total) + "/+" + str(self.bllesing_bonus) + "\n"

        text = text + "加護:" + self.specials_000 + "/" + self.specials_001 + "/" + self.specials_002

        if self.specials_003 != "":
            text = text + "/" + self.specials_003

        if self.specials_004 != "":
            text = text + "/" + self.specials_004

        text = text + "\n財産ポイント:" + self.add_fortune_point

        print(text)

        file_name = self.character_name + "_キャラクターテキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("キャラクターテキストデータを生成しました")
        self.output_porn(text)
        #tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    def output_porn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.character_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = int(self.battlesubtotal_action)
        jsontext["data"]["status"] = []

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][0]["label"] = "FP"
        jsontext["data"]["status"][0]["value"] = self.battlesubtotal_fp
        jsontext["data"]["status"][0]["max"] = self.battlesubtotal_fp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][1]["label"] = "HP"
        jsontext["data"]["status"][1]["value"] = self.battlesubtotal_hp
        jsontext["data"]["status"][1]["max"] = self.battlesubtotal_hp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][2]["label"] = "EN"
        jsontext["data"]["status"][2]["value"] = self.battlesubtotal_mp
        jsontext["data"]["status"][2]["max"] = self.battlesubtotal_mp

        jsontext["data"]["params"] = []
        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][0]["label"] = "体力"
        jsontext["data"]["params"][0]["value"] = self.strong_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][1]["label"] = "反射"
        jsontext["data"]["params"][1]["value"] = self.sense_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][2]["label"] = "知覚"
        jsontext["data"]["params"][2]["value"] = self.strong_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][3]["label"] = "理知"
        jsontext["data"]["params"][3]["value"] = self.intellect_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][4]["label"] = "意志"
        jsontext["data"]["params"][4]["value"] = self.will_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][5]["label"] = "幸運"
        jsontext["data"]["params"][5]["value"] = self.bllesing_bonus

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        jsontext["data"]["externalUrl"] = self.url
        jsontext["data"]["commands"] = ""
        file_name = self.character_name + "_キャラクター駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as file:  # 第二引数：writableオプションを指定
            json.dump(jsontext, file)

        print("キャラクター駒データを生成しました")


def get_data(value):
    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    character = CharacterData()
    time.sleep(5)

    character.input_data(driver, url)
    character.output_text()

    driver.quit()

    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    guardian = GuardianData()
    time.sleep(5)

    guardian.input_data(driver, url)
    guardian.output_text()

    driver.quit()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"メタリックガーディアンRPG ココフォリア用駒データ作成ツール")
    root.geometry("400x150")

    # ラベル
    Static1 = tkinter.Label(text=u'キャラクターシートURL\nhttps://character-sheets.appspot.com/mgr/')
    Static1.pack()

    # エントリー
    EditBox = tkinter.Entry()
    EditBox.pack()

    Button1 = tkinter.Button(text=u'生成', command=lambda: [get_data(EditBox.get())])
    Button1.pack()

    # ボタン
    Button2 = tkinter.Button(text=u'終了', command=lambda: root.quit())
    Button2.pack()

    root.mainloop()