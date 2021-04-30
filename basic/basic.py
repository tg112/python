x = 10  # int
y = "10"  # str
z = 10.0  # float

sum1 = x + x
# 型を合わせないとエラーになる。
# sum2 = x + y
sum3 = x + z

print(sum1, sum3)

# listはデータ型関係なく格納できるデータ構造
lis = [1, 10.0, "str"]
lis.append("hoge")  # [1, 10.0, 'str', 'hoge']
lis.index(10.0)  # 1
lis.remove(10.0)  # [1, 'str', 'hoge']
len(lis)  # 3
lis.clear()  # []

"abcdef"[:3]  # abc


# rangeを使うことで、自動的に数のリストを作ることができる。
nums = len(range(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

students_grade = [9.1, 4.6, 7.5]
# dir(__builtins__)でビルトインのファンクション一覧が見れる。
# 調べたメソッドは、help()で調べられる
mysum = sum(students_grade)
ave = mysum / len(students_grade)

# dictionaries
students_grade = {"Marry": 9.1, "Sim": 8.2, "Bob": 1.5}
total = sum(students_grade.values())
print(students_grade["Marry"])
print(total)

# turple
# immutableで()で囲む
temp = (1, 4, 5)
print(temp)

# function / if


def ave(mylist):
    if type(mylist) == list:
        ave = sum(mylist) / len(mylist)
        return ave
    else:
        return "hoge"


x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")


if x == 1 or y == 2:
    print("Yes")
else:
    print("No")

## user input 
user_input = input("Enter input")
str_format = f"Hello {user_input}"
str_format2 = "Hello %s" % user_input
print(str_format2)