from bs4 import BeautifulSoup
import requests

# 062040 산일
# 049950 미래컴퍼니
# 196170 알테오젠
# 310210 보로노이
# 000250 삼천당제약
# 363250 진시스템


def stockPrice(stock_code):
    res = requests.get(
        f'https://finance.naver.com/item/main.naver?code={stock_code}')
    res.raise_for_status()  # Check for request errors

    soup = BeautifulSoup(res.text, 'html.parser')
    stock_name = soup.select(
        '#middle > div.h_company > div.wrap_company > h2 > a')
    stock_price = soup.select(
        '#rate_info_nxt > div > p.no_today > em > span.blind')

    return [stock_name[0].text.strip(), stock_price[0].text.strip()]


while True:
    stock_code = input('Enter stock code (or "q" to quit): ')
    if stock_code.lower() == 'q':
        break
    try:
        name, price = stockPrice(stock_code)
        print(f'The current price of {name} is: {price}')
    except Exception as e:
        # naver 주식에서 가격이 없는 경우가 있어 에러 발생. html이 페이지마다 일정하지 않음(일 안하네?)
        print(f'Error fetching data for {stock_code}: {e}')
