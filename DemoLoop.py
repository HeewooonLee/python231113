# DemoLoop.py

# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade : "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

value = 5
while value > 0:
    print(value)
    value -= 1

lst = ["문자열",100,3.14]
print(len(lst))
for item in lst :
    print(item)

# 딕셔너리
d = {"apple":100, "orange":200, "kiwi":300}
for item in d.items():
    print(item)

lst = list(range(1,11))
printi(lst)

years = list(range(2000,2024))
print(years)

days = list(range(1,32))
prit(days)

print("---수동으로 반복---")
for i in range(10):
    print(i)

print("---break구문---")
for i in lst:
    print("item:{0}", format(i))

print("---contiue구문---")
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}", format(i))

print("---리스트함축---")
print([i**2 for i in lst if i>5])
tp = ("apple","orange")
print([len(i) for i in tp])

print("---필터링함수---")
itemL = filter(None, lst)
for i in itemL:
    print(i)

# 함수 정의
def getBiggerThan20(i):
    return i>20

print("---필터링함수---")
itemL = filter(getBiggerTahn20, lst)
for i in itemL:
    print(i)

print("---람다함수---")
itemL = fILTER(lambda a:a>20, lst)
for i in itemL:
    print(i)
    