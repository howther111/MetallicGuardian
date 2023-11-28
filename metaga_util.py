# coding: utf-8
# itemはstr, pointはint, 返り値はint
def ItemNumCheck(item, point):
    ret = 0
    if "予備弾倉" in item or "嗜好品" in item :
        ret = point
    elif "中和剤" == item or "戦闘サプリメント" == item or "マルチツール" == item:
        ret = point / 2
    elif "GPS" == item:
        ret = point / 5
    elif "賦活剤" == item or "粒子コンデンサ" == item:
        ret = point / 10
    elif "エネルギーパック" == item:
        ret = point / 20
    elif "強化賦活剤" == item or "強化粒子コンデンサ" == item or "浄化活性ジェル" == item:
        ret = point / 30
    elif "神経加速剤" == item or "ハイエネルギーパック" == item or "脳機能活性剤" == item:
        ret = point / 50
    elif "大型粒子コンデンサ" == item or "超強化賦活剤" == item:
        ret = point / 70
    elif "メガエネルギーパック" == item:
        ret = point / 100
    else:
        ret = 1

    return int(ret)


def NumList():
    ret= ["0"]
    for i in range(999):
        num = i + 1
        numstr = ""
        if num < 10:
            numstr = "00" + str(num)
        elif num < 100:
            numstr = "0" + str(num)
        else:
            numstr = str(num)
        ret.append(numstr)

    return ret


def WeaponList():
    return ["main_weapon_short", "sub_weapon_short", "main_weapon_long", "sub_weapon_long"]


def IgnoreItemList():
    ret = ["", "貧乏", "風来坊", "中流家庭", "臨時収入", "組織の構成員", "組織の幹部", "当主", "富豪", "エグゼクティブ", "大富豪",
           "宿泊施設", "廃屋", "一般住宅", "個室", "隠れ家", "小型施設", "大型施設", "豪邸",
           "特別囚人", "レジスタンス", "配当生活", "騎士", "貴族", "騎士／貴族",
           "機内泊", "野営装備", "町工場", "キャンピングカー", "大型工廠", "研究施設",
           "学生服", "伝統衣装", "改造服", "DLSスーツ", "軍服", "軍服コート", "パイロットスーツ", "ボディアーマー", "神官服", "甲冑",
           "携帯端末", "フォーチュン徽章", "自動脱出装置", "エキストラ", "装飾品",
           "●拳銃", "素手", "ダガー", "ナイフ", "ダガー／ナイフ", "竹刀", "レイピア", "ロングソード", "棍",
           "日本刀", "投げナイフ", "マグナム", "ライアットガン", "●サブマシンガン", "●アサルトライフル", "サンダーバレット",
           "スナイパーライフル", "対戦車ライフル", "●手榴弾", "●アイシクルストーム", "●ロケットランチャー",
           "携帯電話", "パラシュート", "サバイバルキット", "衣服", "エンブレム", "専用カラー", "自動二輪", "自動車",
           "部隊証", "パルテア環境維持服", "ライフジャケット", "船外活動宇宙服",
           "タクティカルグローブ", "ウィップ", "クナイ", "トンファー", "レーザーソード", "●レーザーガン",
           "●バーニングハンド", "●フリーザーフォッグ", "オートスナイパーライフル", "レーザーライフル（P）",
           "●ファイアボール", "●分隊支援火器", "ライトニングボルト", "レムリアメダリオン"]

    return ret