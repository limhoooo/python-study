import re

# 네자리 문자열
# 네자리 문자열인데 ca?e 만 기억남
# ? 에 A~Z 까지 검색 해야함

# . : 하나의 문자를 의미
p1 = re.compile("ca.e")  # ex : care, cafe

# ^ : 문자열의 시작
p2 = re.compile("^de")  # ex : desk, destinaion

# $ : 문자열의 끝나는것
p3 = re.compile("se$")  # ex : case, base


def print_match(m):
    if m:
        print("m.group() : ", m.group())  # 일치하는 문자열 반환
        print("m.string : ", m.string)  # 일치하는 문자열
        print("m.start() : ", m.start())  # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())  # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())  # 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음")


# match : 주어진 문자열의 처음부터 일치하는지 확인
m = p1.match("caseaaaaa")
# search : 주어진 문자열 중에 일치하는게 있는지 확인
m = p1.search("good care")

print_match(m)

# findall : 일치하는 모든 것을 리스트 형태로 반환
lst = p1.findall("good care cafe")
print(lst)


# 정리

# 1. p = re.compile("원하는 형태의 정규식")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. m = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환
# . : 하나의 문자를 의미
# ^ : 문자열의 시작
# $ : 문자열의 끝나는것
