s = input().rstrip()
tmp = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
dic = {i:0 for i in tmp}
for i in s: dic[i] += 1
print(*dic.values())