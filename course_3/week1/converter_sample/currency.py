from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    def get_cur(cur, soup):
        if cur == "RUR":
            return Decimal('1.0000'), Decimal('1')
        soup = soup.find("CharCode", string=cur)
        value = soup.parent.Value.string.replace(',','.')
        nominal = soup.parent.Nominal.string.replace(',','.')

        return Decimal(value), Decimal(nominal)

    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp',
                    params = {
                            "date_req": date
                        })  # Использовать переданный requests
    # print(response.text)
    soup = BeautifulSoup(response.content, "xml")
    from_cur = get_cur(cur_from, soup)
    # rur_cur = get_cur("RUR", soup)
    to_cur = get_cur(cur_to, soup)
    
    res = (amount * (from_cur[0] / from_cur[1])) / (to_cur[0] / to_cur[1])
    result = res.quantize(Decimal('0.0001'))
    return result  # не забыть про округление до 4х знаков после запятой


if __name__ == "__main__":
    import requests
    res = convert(Decimal("1000.1000"), 'EUR', 'JPY', "17/02/2005", requests)
    print(res)