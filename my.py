#!/usr/bin/env python
#https://ja.wikibooks.org/wiki/Python/変数と代入
print('Test Code')
a=5
b = a + 2
print(b)

hensuu = 6
iremono = hensuu + 4
print(iremono)

nedan = 800
kosuu = 3
syuppi = nedan * kosuu
print(syuppi)

a = -3
b = a + 4
print(b)

a = 5
b = "こんにちは。"
print(b)

a = 5
b = "ABCD"
print(b)

a = 5
b = "a"
print(b)

b = "こんにちわ。"
print("b")


a = 5
b = "a"
print("b")
print(b)

a = 5
b = "a"
print("b")
print(b)
print(a)

A = 1
a = 3
print("A=", A)
print("a=", a)

#https://ja.wikibooks.org/wiki/Python/数値入力と文字入力と出力表示
#print("文字を入力してみよう。")
#x = input()
#print(2 * x)


x = 123
print(f"数は{x} です")

x = 123
print(f"文字列{{x}} には {x} が代入されます")

#https://ja.wikibooks.org/wiki/Python/条件分岐と繰り返し
x = 3
if x == 2 :
    print("abcd")

x = 3
if x == 3 :
    print("abcd")

x = 3
if x == 2 :
    print("abcd")
print("ef")

x = 3
if x == 2 :
    print("abcd")
    print("ef")

x = 3
if x > 2 :
    print("xが2よりも大きいよ。")
print("プログラムが終了しました。")

x = 3

if x == 2 :
    print("xが2に等しいよ。")
else:
    print("xが2に等しくないよ。")
print("プログラムが終了しました。")

x = 3

if x == 2 :
    print("xが2に等しいよ。")
if x != 2 :
    print("xが2に等しくないよ。")
print("プログラムが終了しました。")


x = 3

if (x > 2) & (x < 5) :
    print("xが2より大きくて5より小さいよ。")
else:
    print("そうでない場合。")
print("プログラムが終了しました。")

x = 6

if (x > 2) & (x < 5) :
    print("xが2より大きくて5より小さいよ。")
else:
    print("そうでない場合。")
print("プログラムが終了しました。")
