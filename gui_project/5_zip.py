kor=["사과","바나나","오렌지"]
eng=["apple","banana","orange"]

example = zip(kor,eng) # 인덱스의 세로로 합쳐줌

print(list(example))

####################
mixed =[('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

example2 = zip(*mixed)

print(list(example2))

mixed2 =[('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

kor2, eng2 = zip(*mixed2)

print(kor2)
print(eng2)