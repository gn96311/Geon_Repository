import sys

count = 0
for i in range(int(sys.stdin.readline())):
    word = str(sys.stdin.readline())
    if list(word) == sorted(word, key=word.find):
        count += 1
print(count)

#sorted에서 key=word.find 로 설정하면 "a"부터 순서대로 정렬되지 않고, word에서 찾아지는 문자 순서대로 정렬된다.
#ex) bacaabc 일때, 일반적인 sort를 실행하면 aaabbcc가 되지만, key=변수.find로 실행하면
#b가 제일 먼저 왔으니 b, 그리고 a, 그리고 c 순으로 정렬된다.
#그러므로 bbaaacc가 된다.