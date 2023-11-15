# DB1.py

import sqlite3

# 메모리에 작업
# 연결객체 리턴 받기
con = sqlite3.connect(":memory:")
# 커서객체 리턴
cur = con.cursor()

# 테이블구조(자료구조 생성)
cur.execute("create table PhoneBook (name text, phoneNum text);")

# 1건 입력
cur.execute("insert into phoneBook values ('홍길동','010-222');")

# 입력 파라메터 처리
name = "전우치"
phoneNumber = "010-123"
cur.execute("insert into phoneBook values (?,?);",(name, phoneNumber))

# N건 입력
datalist = (("박문수","010-333"),("김길동","010-567"))
cur.executemany("insert into phoneBook values (?,?);",datalist)

# 검색
cur.execute("select * from PhoneBook;")
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())



