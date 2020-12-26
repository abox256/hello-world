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

for i in range(5):
    print(i)


i=2
print("ブロックよりも前のiは",i)
for i in range(5):
    print(i)
print("ブロックの外側のiは",i)

# i = "b"
# while i != "q":
#     print("入力した文字を3個、ならべるよ。（終了したい場合はqを入力）")
#     i = input()
#     print(3*i)

# https://ja.wikibooks.org/wiki/Python/リスト
matome = [10 ,"asdf" ,30]
print(matome)

matome = [10 ,"asdf" ,30]
print(matome[1])

matome = [10 ,"asdf" ,30]
matome[0] = 4
print (matome)

matome = [10 ,"asdf" ,30]
print(matome[0] + matome[2])

matome = ["aaa" ,"bb" ,"cccc"]
matome[0] = 4
print(matome)

# 人名リスト
jinmei = ["yamada" ,"sato" ,"inoue"] 

for i in jinmei:
    print(i)

matome = ["aaa" ,"bb" ,"cccc"]
matome.append("d")
print(matome)

matome = ["aaa" ,"bb" ,"cccc"]
matome.pop()
print(matome)

matome = ["aaa" ,"bb" ,"cccc"]
matome.pop()
matome.pop()
print(matome)

matome = [-7 , -2, 5]

print(matome)
# 絶対値をabsで得る
obje= list(map(abs, matome) )

print(obje)

matome = [-7 , -2, 5]

# +3するだけの処置
def kansu(a):
    return a+3

print(matome)
obje= list(map(kansu, matome) )
print(obje)

matome = [5 , 2, 8, 6, 1 ]

# 3以上の要素を抽出
obje= list(filter(lambda x:(x >= 3)  , matome) )

print(obje)

matome = [5 , 2, 8, 6, 1 ]

# 3以上の要素を抽出
obje= list(map(lambda x:x if x % 2 == 0 else "奇数です" , matome ))
print("x")
print(obje)

# https://ja.wikibooks.org/wiki/Python/ファイルの書き込みと読み込み