a = 1

if a == 1:
    print('a = 1')
else:
    print('no match')

b = 3

if a > b:
    print('a > b')
elif a == b:
    print('a==b')
else:
    print('a < b')


match a:
    case 1:
        print('match 1')
    case 3:
        print('match 3')
    case _:
        print('no match')


# 先用變數 score 接受使用者輸入的分數，然後用 if-elif-else 判斷分數為
# 100 、 90~99 、 80~89 、 70~79 、 60~69 及 60 以下的區間，依序印出
# "Perfect!" 、 "Excellent!" 、 "Great!" 、 "Good!" 、 "Not Bad!" 、 "Bad!" 等訊息，
# 注意判斷數字區間可以用 and 連接 score < 100 及 score >= 90 或直接用 90 <= score < 100 ，
# 最後如果輸入的分數不在 0 到 100 的範圍就印出 "That's impossible!!"

score = 70

if score == 100:
    print('Perfect!')
elif 90 <= score < 100:
    print('Excellent!')
elif 80 <= score < 90:
    print('Great!')
elif 70 <= score < 80:
    print('Good!')
elif 60 <= score < 70:
    print('Not Bad!')
elif score < 60:
    print('Bad!')
else:
    print("That's impossible!!")
