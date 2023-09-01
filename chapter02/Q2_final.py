import random

name = input("名前をアルファベットで入力してください: ")

name_initial = name[0].upper()

while True:
    random_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    print(random_letter)

    if random_letter == name_initial:
        print("名前の頭文字が表示されました。プログラムを終了します。")
        break
