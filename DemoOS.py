from os.path import *
import glob
import os


# 풀패스(전체 경로)
print(abspath("demo.py"))
# 파일이름만
print(basename("c:\\work\\demo.py"))

fName = "C:\\Users\\student\\AppData\\Local\\Programs\\Python\\Python310\\pthon.exe"
if exists(fName):
    print("파일크기: {0}".format(getsize(fName)))
else:
    print("파일 없음")

result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)

print("운영체제이름:{0}".format(os.name))
print("환경변소:{0}".format(os.environ))

# os.system("notepad.exe")

os.chdir("..")
os.chdir("C:\\Users\\student\\AppData\\Local\\Programs\\Python\\Python310")
result=glob.glob("*.*")
print(result)