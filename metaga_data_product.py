# coding: utf-8
from selenium import webdriver
from time import sleep
import tkinter
import sys
from tkinter import messagebox
import metaga_util


root = tkinter.Tk()
root.title("URLを入力してください")
root.geometry("400x100")

# 2文字に満たない文字列に0を追加
def AddZero(str):
    if len(str) < 2:
        str = "0" + str
    return str

#
# ボタンが押されるとここが呼び出される
#
def SubmitEntryValue(event):
    #エントリーの中身を削除
    url = EditBox.get()

    if url == "":
        # メッセージボックス（情報）
        messagebox.showinfo("エラー", "URLが入力されていません")
        sys.exit()

    try:
        driver = webdriver.Chrome()
    except:
        # メッセージボックス（情報）
        messagebox.showinfo("エラー", "chromedriver.exeが存在しません")
        sys.exit()

    try:
        driver.get(url)
    except:
        # メッセージボックス（情報）
        messagebox.showinfo("エラー", "URLが不正です")
        sys.exit()

    sleep(3);

    # キャラクターデータ作成
    text = "【キャラデータフォーマット】\n"

    # PC名
    try:
        element = driver.find_element_by_id("base.name")
        character_name = element.get_attribute("value")
        print(character_name)
        text = text + "PC：" + character_name + " "
    except:
        # メッセージボックス（情報）
        messagebox.showinfo("エラー", "URLが不正です")
        sys.exit()

    # PL名
    element = driver.find_element_by_id("base.player")
    player_name = element.get_attribute("value")
    print(player_name)
    text = text + "PL：" + player_name + "\n"

    #体力
    element = driver.find_element_by_id("abl.strong.disp")
    abl_strong_disp = AddZero(element.get_attribute("value"))
    print(abl_strong_disp)

    element = driver.find_element_by_id("abl.strong.dispbonus")
    abl_strong_dispbonus = element.get_attribute("value")
    print(abl_strong_dispbonus)

    text = text + "【体力】" + abl_strong_disp + "/+" + abl_strong_dispbonus

    # 反射
    element = driver.find_element_by_id("abl.reflex.disp")
    abl_reflex_disp = AddZero(element.get_attribute("value"))
    print(abl_reflex_disp)

    element = driver.find_element_by_id("abl.reflex.dispbonus")
    abl_reflex_dispbonus = element.get_attribute("value")
    print(abl_reflex_dispbonus)

    text = text + "【反射】" + abl_reflex_disp + "/+" + abl_reflex_dispbonus

    # 知覚
    element = driver.find_element_by_id("abl.sense.disp")
    abl_sense_disp = AddZero(element.get_attribute("value"))
    print(abl_sense_disp)

    element = driver.find_element_by_id("abl.sense.dispbonus")
    abl_sense_dispbonus = element.get_attribute("value")
    print(abl_sense_dispbonus)

    text = text + "【知覚】" + abl_sense_disp + "/+" + abl_sense_dispbonus + "\n"

    # 理知
    element = driver.find_element_by_id("abl.intellect.disp")
    abl_intellect_disp = AddZero(element.get_attribute("value"))
    print(abl_intellect_disp)

    element = driver.find_element_by_id("abl.intellect.dispbonus")
    abl_intellect_dispbonus = element.get_attribute("value")
    print(abl_intellect_dispbonus)

    text = text + "【理知】" + abl_intellect_disp + "/+" + abl_intellect_dispbonus

    # 意志
    element = driver.find_element_by_id("abl.will.disp")
    abl_will_disp = AddZero(element.get_attribute("value"))
    print(abl_will_disp)

    element = driver.find_element_by_id("abl.will.dispbonus")
    abl_will_dispbonus = element.get_attribute("value")
    print(abl_will_dispbonus)

    text = text + "【意志】" + abl_will_disp + "/+" + abl_will_dispbonus

    # 幸運
    element = driver.find_element_by_id("abl.bllesing.disp")
    abl_bllesing_disp = AddZero(element.get_attribute("value"))
    print(abl_bllesing_disp)

    element = driver.find_element_by_id("abl.bllesing.dispbonus")
    abl_bllesing_dispbonus = element.get_attribute("value")
    print(abl_bllesing_dispbonus)

    text = text + "【幸運】" + abl_bllesing_disp + "/+" + abl_bllesing_dispbonus + "\n"

    # 加護
    text = text + "加護："
    kagolist = ["0", "001", "002", "003"]
    for i in kagolist:
        spid = "specials." + i + ".name"
        try:
            element = driver.find_element_by_id(spid)
            special = element.get_attribute("value")
            if special != "":
                print(special)
                text = text + special + " 1/1 "

        except:
            break

    text = text + "\n"

    # 財産ポイント
    text = text + "財産ポイント："
    element = driver.find_element_by_id("addfortunepoint")
    money = element.get_attribute("value")
    text = text + money + "\n"

    # アイテム
    text = text + "アイテム："
    itemnumlist = metaga_util.NumList()

    # 無視アイテムリスト
    ignoreitemlist = metaga_util.IgnoreItemList()

    for i in itemnumlist:
        itemid = "items." + i + ".name"
        try:
            element = driver.find_element_by_id(itemid)
            item = element.get_attribute("value")
            ignoreflg = False
            for j in ignoreitemlist:
                if j == item:
                    ignoreflg = True

            if not ignoreflg:
                # 将来的に全アイテムの個数を取得できるようにする
                print(item)
                itempointid = "items." + i + ".point"
                element = driver.find_element_by_id(itempointid)
                itempoint = element.get_attribute("value")
                itemnokazu = "1"
                if itempoint.isdecimal():
                    itemnokazu = str(metaga_util.ItemNumCheck(item, int(itempoint)))

                text = text + item + " " + itemnokazu + "/" + itemnokazu + " "

        except:
            break


    text = text + "\n\n\n\n"

    # 機体データ作成
    # 機体名
    element = driver.find_element_by_id("base.guardian.name")
    gd_name = element.get_attribute("value")
    print(gd_name)
    text = text + gd_name + "\n"
    text = text + "【機体データフォーマット】\n"

    # PC
    text = text + "PC：" + character_name + " "
    text = character_name + "\n" + text

    # レベル
    element = driver.find_element_by_id("base.level")
    level = element.get_attribute("value")
    print(level)
    text = text + "レベル：" + level + " "

    # サイズ
    element = driver.find_element_by_id("base.guardian.size")
    size = element.get_attribute("value")
    print(size)
    text = text + "サイズ：" + size + "\n"

    # 各種機体ステータス
    # 命中
    element = driver.find_element_by_id("outfits.total.hit")
    hit = AddZero(element.get_attribute("value"))
    print(hit)
    text = text + "【命中】" + hit

    # 回避
    element = driver.find_element_by_id("outfits.total.dodge")
    dodge = AddZero(element.get_attribute("value"))
    print(dodge)
    text = text + "【回避】" + dodge

    # 砲撃
    element = driver.find_element_by_id("outfits.total.magic")
    magic = AddZero(element.get_attribute("value"))
    print(magic)
    text = text + "【砲撃】" + magic

    # 防壁
    element = driver.find_element_by_id("outfits.total.countermagic")
    countermagic = AddZero(element.get_attribute("value"))
    print(countermagic)
    text = text + "【防壁】" + countermagic

    # 行動
    element = driver.find_element_by_id("outfits.total.action")
    action = AddZero(element.get_attribute("value"))
    print(action)
    text = text + "【行動】" + action + "\n"

    # 力場
    element = driver.find_element_by_id("outfits.total.fp")
    fp = AddZero(element.get_attribute("value"))
    print(fp)
    text = text + "【力場】" + fp

    # 耐久
    element = driver.find_element_by_id("outfits.total.hp")
    hp = AddZero(element.get_attribute("value"))
    print(hp)
    text = text + "【耐久】" + hp

    # 感応
    element = driver.find_element_by_id("outfits.total.mp")
    mp = AddZero(element.get_attribute("value"))
    print(mp)
    text = text + "【感応】" + mp

    # 移動力
    element = driver.find_element_by_id("outfits.total.battlespeed.total")
    battlespeed = AddZero(element.get_attribute("value").replace("ﾏｽ", ""))
    print(battlespeed)
    text = text + "【移動力】" + battlespeed + "\n"

    # 主近名前
    element = driver.find_element_by_id("outfits.total.main_weapon_shortname")
    mws_name = element.get_attribute("value")
    print(mws_name)

    # 主近射程
    element = driver.find_element_by_id("outfits.total.main_weapon_shortrange")
    mws_range = element.get_attribute("value")
    print(mws_range)

    # 主近代償
    element = driver.find_element_by_id("outfits.total.main_weapon_shortstrong")
    mws_strong = element.get_attribute("value")
    if mws_strong == "":
        mws_strong = "なし"
    print(mws_strong)

    # 主近属性・ダメージ
    element = driver.find_element_by_id("outfits.total.main_weapon_shortattack")
    mws_attack = element.get_attribute("value")
    print(mws_attack)
    mws_attack_list = mws_attack.split("+")

    # 主近種類（白兵か射撃か）
    mws_type = "射撃"
    if mws_range == "0":
        mws_type = "白兵"

    # 主近対象
    mws_target = "単体"
    if "●" in mws_name:
        mws_target = "範囲1"

    # ちょっと面倒だが武器ごとの攻撃力を追加
    mws_list = []
    mws_num_list = []
    mws_base_attack = "00"
    for i in metaga_util.NumList():
        try:
            element = driver.find_element_by_id("outfits.main_weapon_short." + i + ".name")
            mws_list.append(element.get_attribute("value"))
            mws_num_list.append(i)
        except:
            break

    for i in range(len(mws_list)):
        if mws_list[i] == mws_name:
            element = driver.find_element_by_id("outfits.main_weapon_short." + mws_num_list[i] + ".attack")
            mws_base_attack = AddZero(element.get_attribute("value"))

    if mws_name != "":
        text = text + "[*]主近：" + mws_name + " 射程：" + mws_range + " 代償：" + mws_strong + "\n"
        text = text + "攻：〈" + mws_attack_list[0] + "〉" + "+" + AddZero(mws_attack_list[1]) + "/" + hit \
               + "(" + mws_type + ") 対：" + mws_target + "\n"

    # 副近名前
    element = driver.find_element_by_id("outfits.total.sub_weapon_shortname")
    sws_name = element.get_attribute("value")
    print(sws_name)

    # 副近射程
    element = driver.find_element_by_id("outfits.total.sub_weapon_shortrange")
    sws_range = element.get_attribute("value")
    print(sws_range)

    # 副近代償
    element = driver.find_element_by_id("outfits.total.sub_weapon_shortstrong")
    sws_strong = element.get_attribute("value")
    if sws_strong == "":
        sws_strong = "なし"
    print(sws_strong)

    # 副近属性・ダメージ
    element = driver.find_element_by_id("outfits.total.sub_weapon_shortattack")
    sws_attack = element.get_attribute("value")
    print(sws_attack)
    sws_attack_list = sws_attack.split("+")

    # 副近種類（白兵か射撃か）
    sws_type = "射撃"
    if sws_range == "0":
        sws_type = "白兵"

    # 副近対象
    sws_target = "単体"
    if "●" in sws_name:
        sws_target = "範囲1"

    # ちょっと面倒だが武器ごとの攻撃力を追加
    sws_list = []
    sws_num_list = []
    sws_base_attack = "00"
    for i in metaga_util.NumList():
        try:
            element = driver.find_element_by_id("outfits.sub_weapon_short." + i + ".name")
            sws_list.append(element.get_attribute("value"))
            sws_num_list.append(i)
        except:
            break

    for i in range(len(sws_list)):
        if sws_list[i] == sws_name:
            element = driver.find_element_by_id("outfits.sub_weapon_short." + sws_num_list[i] + ".attack")
            sws_base_attack = AddZero(element.get_attribute("value"))

    if sws_name != "":
        text = text + "[*]副近：" + sws_name + " 射程：" + sws_range + " 代償：" + sws_strong + "\n"
        text = text + "攻：〈" + sws_attack_list[0] + "〉" + "+" + AddZero(sws_attack_list[1]) + "/" + hit \
               + "(" + sws_type + ") 対：" + sws_target + "\n"

    # 主遠名前
    element = driver.find_element_by_id("outfits.total.main_weapon_longname")
    mwl_name = element.get_attribute("value")
    print(mwl_name)

    # 主遠射程
    element = driver.find_element_by_id("outfits.total.main_weapon_longrange")
    mwl_range = element.get_attribute("value")
    print(mwl_range)

    # 主遠代償
    element = driver.find_element_by_id("outfits.total.main_weapon_longstrong")
    mwl_strong = element.get_attribute("value")
    if mwl_strong == "":
        mwl_strong = "なし"
    print(mwl_strong)

    # 主遠属性・ダメージ
    element = driver.find_element_by_id("outfits.total.main_weapon_longattack")
    mwl_attack = element.get_attribute("value")
    print(mwl_attack)
    mwl_attack_list = mwl_attack.split("+")

    # 主遠種類（砲撃）
    mwl_type = "砲撃"

    # 主遠対象
    mwl_target = "単体"
    if "●" in mwl_name:
        mwl_target = "範囲1"

        # ちょっと面倒だが武器ごとの攻撃力を追加
    mwl_list = []
    mwl_num_list = []
    mwl_base_attack = "00"
    for i in metaga_util.NumList():
        try:
            element = driver.find_element_by_id("outfits.main_weapon_long." + i + ".name")
            mwl_list.append(element.get_attribute("value"))
            mwl_num_list.append(i)
        except:
            break

    for i in range(len(mwl_list)):
        if mwl_list[i] == mwl_name:
            element = driver.find_element_by_id("outfits.main_weapon_long." + mwl_num_list[i] + ".attack")
            mwl_base_attack = AddZero(element.get_attribute("value"))

    if mwl_name != "":
        text = text + "[*]主遠：" + mwl_name + " 射程：" + mwl_range + " 代償：" + mwl_strong + "\n"
        text = text + "攻：〈" + mwl_attack_list[0] + "〉" + "+" + AddZero(mwl_attack_list[1]) + "/" + magic \
               + "(" + mwl_type + ") 対：" + mwl_target + "\n"

     # 副遠名前
    element = driver.find_element_by_id("outfits.total.sub_weapon_longname")
    swl_name = element.get_attribute("value")
    print(swl_name)

    # 副遠射程
    element = driver.find_element_by_id("outfits.total.sub_weapon_longrange")
    swl_range = element.get_attribute("value")
    print(swl_range)

    # 副遠代償
    element = driver.find_element_by_id("outfits.total.sub_weapon_longstrong")
    swl_strong = element.get_attribute("value")
    if swl_strong == "":
        swl_strong = "なし"
    print(swl_strong)

    # 副遠属性・ダメージ
    element = driver.find_element_by_id("outfits.total.sub_weapon_longattack")
    swl_attack = element.get_attribute("value")
    print(swl_attack)
    swl_attack_list = swl_attack.split("+")

    # 副遠種類（砲撃）
    swl_type = "砲撃"

    # 副遠対象
    swl_target = "単体"
    if "●" in swl_name:
        swl_target = "範囲1"

    # ちょっと面倒だが武器ごとの攻撃力を追加
    swl_list = []
    swl_num_list = []
    swl_base_attack = "00"
    for i in metaga_util.NumList():
        try:
            element = driver.find_element_by_id("outfits.sub_weapon_long." + i + ".name")
            swl_list.append(element.get_attribute("value"))
            swl_num_list.append(i)
        except:
            break

    for i in range(len(swl_list)):
        if swl_list[i] == swl_name:
            element = driver.find_element_by_id("outfits.sub_weapon_long." + swl_num_list[i] + ".attack")
            swl_base_attack = AddZero(element.get_attribute("value"))

    if swl_name != "":
        text = text + "[*]副遠：" + swl_name + " 射程：" + swl_range + " 代償：" + swl_strong + "\n"
        text = text + "攻：〈" + swl_attack_list[0] + "〉" + "+" + AddZero(swl_attack_list[1]) + "/" + magic \
               + "(" + swl_type + ") 対：" + swl_target + "\n"

    # 防御修正
    # 斬
    element = driver.find_element_by_id("armourstotal.slash")
    armour_slash = AddZero(element.get_attribute("value"))
    print(armour_slash)

    # 刺
    element = driver.find_element_by_id("armourstotal.pierce")
    armour_pierce = AddZero(element.get_attribute("value"))
    print(armour_pierce)

    # 殴
    element = driver.find_element_by_id("armourstotal.crash")
    armour_crash = AddZero(element.get_attribute("value"))
    print(armour_crash)

    # 炎
    element = driver.find_element_by_id("armourstotal.fire")
    armour_fire = AddZero(element.get_attribute("value"))
    print(armour_fire)

    # 氷
    element = driver.find_element_by_id("armourstotal.ice")
    armour_ice = AddZero(element.get_attribute("value"))
    print(armour_ice)

    # 雷
    element = driver.find_element_by_id("armourstotal.thunder")
    armour_thunder = AddZero(element.get_attribute("value"))
    print(armour_thunder)

    # 光
    element = driver.find_element_by_id("armourstotal.light")
    armour_light = AddZero(element.get_attribute("value"))
    print(armour_light)

    # 闇
    element = driver.find_element_by_id("armourstotal.dark")
    armour_dark = AddZero(element.get_attribute("value"))
    print(armour_dark)

    text = text + "防：斬" + armour_slash + "/刺" + armour_pierce + "/殴" + armour_crash + "/炎" + armour_fire + "\n" \
           + "   /氷" + armour_ice + "/雷" + armour_thunder + "/光" + armour_light + "/闇" + armour_dark



    # input("Press ENTER to Close the automated browser")
    driver.quit()

    # "."を消去
    character_name = character_name.replace(".", "")
    gd_name = gd_name.replace(".", "")

    f = open(character_name + "_" + gd_name +'.txt', 'w', encoding='utf-8')
    f.write(text)
    f.close()

    # メッセージボックス（情報）
    messagebox.showinfo("データ生成完了", "データ生成が完了しました")
    sys.exit()


#エントリー
EditBox = tkinter.Entry(width=50)
EditBox.pack()

#ボタン
Button = tkinter.Button(text=u'データ生成', width=50)
Button.bind("<Button-1>",SubmitEntryValue)
#左クリック（<Button-1>）されると，SubmitEntryValue関数を呼び出すようにバインド
Button.pack()

root.mainloop()

