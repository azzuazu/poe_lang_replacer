import sys

##########################################################
# replaceするファイル名のパス全てを""の中に入力してね
##########################################################
filename = r"C:\Users\zeruc\Documents\My Games\Path of Exile\production_Config.ini"





























class TranslateTo:
    JP = "0"
    EN = "1"

# 今の言語を見つける
with open(filename, 'r', encoding="utf-8") as f:
    for i, line in enumerate(f):
        if line == "language=jp\n":
            now_lang = TranslateTo.EN
            break
        elif line == "language=en\n":
            now_lang = TranslateTo.JP
            break

# 変換と保存
if now_lang == TranslateTo.JP:
    print("translating en to jp!")
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            fileText = f.read()
            after = fileText.replace('language=en', 'language=jp')

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(after)
        print("finished! now: language=jp")
    except FileNotFoundError as e:
        print("err! plz check filename.")

elif now_lang == TranslateTo.EN:
    print("translating jp to en!")
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            fileText = f.read()
            after = fileText.replace('language=jp', 'language=en')

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(after)
        print("finished! now: language=en")
    except FileNotFoundError as e:
        print("err! plz check filename.")

else:
    print("error! plz ask azumi")