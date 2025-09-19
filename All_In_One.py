print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")

a = int(input())

i = 1

for i in range(a):
    print(i+1)

a = int(input("횟수를 입력하세요 : "))
b = input("문자열을 입력하세요 : ")

cnt = 0
add = 0

for i in range(a):
    if b[i] == 'O':
        cnt += 1
        add += cnt
        if b[i] == 'X' :
            cnt = 0
print(add)

a = int(input())
for i in range(1, a + 1):
    print("*" * i)

user = list(map(str, input().split()))

add = 0

if len(user) > 5 and len(user) <= 0:
    exit()  
else:
    for i in range(1, 11):
        add += int(user[i])

userOutput = add % 10
print(userOutput)


import sys
num = list(map(int, sys.stdin.read().split()))
temp = sum(x ** 2 for x in num) % 10
print(temp)

import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, 10):
    print(f"{n} * {i} = {n * i}")


import sys
input = sys.stdin.readline

n = int(input())
if n % 4 == 0 and n % 100 != 0:
    print("1")
else:
    print("0")




userScore = []
for i in range(5):
    score = int(input(f"{i+1}번째 점수를 입력하세요: "))
    userScore.append(score)

userScore.sort()
print(f"최대 점수는 {userScore[-1]}입니다.")
print(f"최소 점수는 {userScore[0]}입니다.")

userScore = [3, 9, 4, 2, 15, 99]

userScore.sort()
print(f"두번째로 큰 수는 {userScore[1]}입니다.")

scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]

scores.sort()

del scores[0]
del scores[-1]

print(scores)


userList = []
for i in range(5):
    userInput = input(f"{i+1}번째 문자열을 입력하세요: ")
    userList.append(userInput)

for i in range(-1, -6, -1):
    print(userList[i])


menu = 0
friends = ['홍길동', '박찬호', '손흥민']
while menu != 9:
    print("--------------")
    print("1. 친구리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    menu = int(input("메뉴를 입력하세요 : "))
    if menu == 1:
        print(friends)
    elif menu == 2:
        name = input("친구 이름을 입력하세요.")
        menu.append(name)
    elif menu == 3:
        del_name = input("삭제하고 싶은 친구의 이름을 입력하세요 : ")
        if del_name in menu:
            menu.remove(del_name)
        else:
            print("이름이 없음")
    elif menu == 4:
        old_name = input("변경하고 싶은 친구의 이름을 입력하세요 : ")
        if old_name in menu:
            index = menu.find(old_name)
            new_name = input("새로운 이름을 입력하세요 : ")
            menu.append(new_name)
        else:
            print("이름이 없음")
    
exit()


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[: : -2])

salaries = [200, 250, 300, 280, 500]

def modify(arr, temp):
    for i in range(5):
        arr[i] = arr[i] * temp
    return

print("인상전", salaries)

modify(salaries, 1.3)

print("인상후", salaries)
exit()


arr = []

for i in range(100):
    if i % 2 == 0 and i % 3 == 0:
        arr.append(i)

print(arr)

list1 = [10, 20, 30, 40, 50]
userOutput = 0
for i in range(5):
    userOutput += list1[i]

print(userOutput)

arrA = []
arrB = []
arrC =[]

for i in range(1, 31):
    arrA.append(i)

for i in range(1, 31):
    arrB.append(i)

for i in range(1, 31):
    arrC.append(i)

arrNew = []

for i in range(30):
    for j in range(30):
        for k in range(30):
            a = arrA[i]
            b = arrB[j]
            c = arrC[k]
            if a * a + b * b == c * c:
                print(f"{a}, {b}, {c}")


exit()
import sys
input = sys.stdin.readline

a = int(input())
for i in range(a + 1):
    b, c = map(int, input().split())
    print(b + c)


a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    print(b + c)


a = input()
print(ord(a))


import sys
input = sys.stdin.readline

a = input()
b = int(input())
print(a[b-1])




N = int(input())
num = input()
add = sum(int(digit) for digit in num)

print(add)

import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)


import sys
input = sys.stdin.readline


while(1):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        exit()
    else:
        print(a + b)
    

import sys
input = sys.stdin.readline

n = int(input())
nums = input()
total = 0
for i in range(n) :
    total += int(nums[i])
print(total)


import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()


print(int(a) + int(b) - int(c))
string = f"{a}{b}"
end = int(string) - int(c)
print(end)

import sys
input = sys.stdin.readline

N = int(input())

a = list(map(int, input().split()))
z = a.sort()
print(a[0], a[-1])


import sys
input = sys.stdin.readline

a = list(map(int, input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]
if a == ascending:
    print("ascending")
elif a == descending:
    print("descending")
else:
    print("mixed")


import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
H = a[0]
M = a[1]

lastM = M - 45

if lastM < 0:
    lastH = H - 1
    lastM += 60
    if lastH < 0:
        lastH += 24

print(lastH, lastM)


import sys
input = sys.stdin.readline
data = []
for i in range(9):
    data.append(int(input()))

max_data = max(data)
index_data = data.index(max_data) + 1
print(max_data)
print(index_data)

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

addOutput = str(a * b * c)

for i in range(10):
    print(addOutput.count(str(i)))


import sys
input = sys.stdin.readline


N, X = map(int, input().split())
nums = list(map(int, input().split()))

for i in nums:
    if i < X:
        print(i, end = " ")



import sys
input = sys.stdin.readline

S = input().strip()
for i in "abcdefghijklmnopqrstuvwxyz":
    print(S.find(i), end = " ")



import sys
input = sys.stdin.readline


nums = []
for i in range(10):
    nums.append(int(input()))

lastOutput = []

for i in nums:
    n = int(i) % 42
    if n not in lastOutput:
        lastOutput.append(n)
print(len(lastOutput))


import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    R, S = input().split()
    temp = ""
    for j in S:
        temp += str(j) * int(R)
    print(temp)

import sys
input = sys.stdin.readline

n = int(input())


for i in range(n):
    list1 = list(input())
    a = 0
    temp = 0

    for j in list1:
        if j == 'O':
            a += 1
            temp += a
        elif j == 'X':
            a = 0
print(temp)
