'''
"플랫폼 문제번호"를 입력하세요.
(BOJ, SWEA, PG, LTC)
ex) 1000, boj 1000, swea 1000

'''

import requests, re
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

while True:
    p_num = input('문제 번호를 입력하세요.\n> ')
    if p_num == '' or p_num == '0' :
        break

    url = f"https://www.acmicpc.net/problem/{p_num}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.find('span', {'id': 'problem_title'}).text.strip()

    # re라이브러리를 사용하여 파일명으로 불가능한것과 공백을 '_'로 바꿔줌(정규표현식)
    title = re.sub(r'[\\/*:?"<>| ]', '_', title)

    # [문제번호_제목].py 생성
    with open(f'{p_num}_{title}.py', 'w', encoding='utf-8') as f:
        f.write(f'# https://www.acmicpc.net/problem/{p_num}\n')
        f.write(f'# {p_num} {title}\n')
        f.write(f'import sys\nsys.stdin = open("input_{p_num}.txt", "r")\n')
    
    # input_[문제번호].txt 생성
    with open(f'input_{p_num}.txt', 'w', encoding='utf-8') as f:
        pass