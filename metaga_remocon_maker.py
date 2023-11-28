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

    # カウンターリモコン作成
    jsontext = '{"saveDataTypeName":"CounterRemocon","saveData":[{},'
    jsontext = jsontext + '{"label":"[FP増加]","messageFormat":"{0} {1} {2} {4}",' \
                          '"modifyValue":"","counterName":"FP","operator":"plus"},' \
                          '{"label":"[HP増加]","messageFormat":"{0} {1} {2} {4}",' \
                          '"modifyValue":"","counterName":"HP","operator":"plus"},' \
                          '{"label":"[EN増加]","messageFormat":"{0} {1} {2} {4}",' \
                          '"modifyValue":"","counterName":"EN","operator":"plus"},' \
                          '{"label":"[FP減少]","messageFormat":"{0} {1} {2} {4}",' \
                          '"modifyValue":"","counterName":"FP","operator":"minus"},' \
                          '{"label":"[HP減少]","messageFormat":"{0} {1} {2} {4}",' \
                          '"modifyValue":"","counterName":"HP","operator":"minus"},' \
                          '{"label":"[EN減少]","messageFormat":"{0} {1} {2} {4}",' \
                          '"modifyValue":"","counterName":"EN","operator":"minus"}'

    # PC名
    character_name = ""
    try:
        element = driver.find_element_by_id("base.name")
        character_name = element.get_attribute("value")
        print(character_name)
    except:
        # メッセージボックス（情報）
        messagebox.showinfo("エラー", "URLが不正です")
        sys.exit()

    # 機体データ作成
    # 機体名
    element = driver.find_element_by_id("base.guardian.name")
    gd_name = element.get_attribute("value")
    print(gd_name)

    # 特技
    for i in metaga_util.NumList():
        skillcostid = "skills." + i + ".cost"
        print(skillcostid)
        try:
            element = driver.find_element_by_id(skillcostid)
            skillcost = element.get_attribute("value")
            ignoreflg = False

            costtype = ""
            costpoint = ""

            if "EN" in skillcost:
                costtype = "EN"
                costpoint = skillcost.replace("EN", "")
            elif "HP" in skillcost:
                costtype = "HP"
                costpoint = skillcost.replace("HP", "")
            elif "FP" in skillcost:
                costtype = "FP"
                costpoint = skillcost.replace("FP", "")
            else:
                ignoreflg = True

            skillnameid = "skills." + i + ".name"
            element = driver.find_element_by_id(skillnameid)
            skillname = element.get_attribute("value")

            # 代償が数値でなければ無視
            if not costpoint.isdecimal() and not ignoreflg:
                ignoreflg = True
                messagebox.showinfo("データエラー", skillname + "の代償が数値ではありません")

            if not ignoreflg:
                # JSON追加
                print(skillname + ", " + skillcost)
                jsontext = jsontext + ', {"label": "【' + skillname + '】", "messageFormat": "【' + skillname
                jsontext = jsontext + '】 {0} {1} {2} {4}", "modifyValue": "' + costpoint + '", '
                jsontext = jsontext + '"counterName": "' + costtype + '", "operator": "minus"}'

        except:
            break

    # 武装
    for i in metaga_util.WeaponList():
        weaponcostid = "outfits.total." + i + "strong"
        print(weaponcostid)

        element = driver.find_element_by_id(weaponcostid)
        weaponcost = element.get_attribute("value")
        ignoreflg = False

        costtype = ""
        costpoint = ""

        if "EN" in weaponcost:
            costtype = "EN"
            costpoint = weaponcost.replace("EN", "")
        elif "HP" in weaponcost:
            costtype = "HP"
            costpoint = weaponcost.replace("HP", "")
        elif "FP" in weaponcost:
            costtype = "FP"
            costpoint = weaponcost.replace("FP", "")
        else:
            ignoreflg = True

        weaponnameid = "outfits.total." + i + "name"
        element = driver.find_element_by_id(weaponnameid)
        weaponname = element.get_attribute("value")

        # 代償が数値でなければ無視
        if not costpoint.isdecimal() and not ignoreflg:
            ignoreflg = True
            messagebox.showinfo("データエラー", weaponname + "の代償が数値ではありません")

        if not ignoreflg:
            # JSON追加
            print(weaponname + ", " + weaponcost)
            jsontext = jsontext + ', {"label": "【' + weaponname + ' 代償】", "messageFormat": "【' + weaponname
            jsontext = jsontext + ' 代償】 {0} {1} {2} {4}", "modifyValue": "' + costpoint + '", '
            jsontext = jsontext + '"counterName": "' + costtype + '", "operator": "minus"}'

    # 末尾
    jsontext = jsontext + ']}'

    # "."を消去
    character_name = character_name.replace(".", "")
    gd_name = gd_name.replace(".", "")

    driver.quit()

    f = open(character_name + "_" + gd_name +'.json', 'w', encoding='utf-8')
    f.write(jsontext)
    f.close()

    # メッセージボックス（情報）
    messagebox.showinfo("カウンターリモコン生成完了", "カウンターリモコンの生成が完了しました")
    sys.exit()


#エントリー
EditBox = tkinter.Entry(width=50)
EditBox.pack()

#ボタン
Button = tkinter.Button(text=u'カウンターリモコン生成', width=50)
Button.bind("<Button-1>",SubmitEntryValue)
#左クリック（<Button-1>）されると，SubmitEntryValue関数を呼び出すようにバインド
Button.pack()

root.mainloop()

