import requests
from bs4 import BeautifulSoup

"""
curl 'http://www.nepalstock.com/stockWisePrices' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Origin: http://www.nepalstock.com' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Referer: http://www.nepalstock.com/stockWisePrices' \
  -H 'Accept-Language: en-US,en;q=0.9,ne;q=0.8' \
  -H 'Cookie: ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2217f5894feaadfca1676427568e8cb8a7%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A12%3A%22202.79.47.32%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Linux%3B+Android+6.0%3B+Nexus+5+Build%2FMRA58N%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F92.0.4515.159+Mobil%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1630903898%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D1f845a861f7a191994926d5234ef7f32' \
  --data-raw 'startDate=&endDate=&stock-symbol=2915&_limit=500' \
  --compressed \
  --insecure
"""

if __name__ == '__main__':

    data = {
        'startDate': '',
        'endDate': '',
        'stock-symbol': '2915',
        '_limit': '500'
    }

    response = requests.post('http://www.nepalstock.com/stockWisePrices', data=data)
    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find('div', {'id': 'home-contents'})
    table = container.find('table')

    rows = table.findAll('tr')

    with open('data.csv', 'w') as f:
        for row in rows[1:len(rows)]:
            cells = row.findAll('td')
            if len(cells) == 8:
                f.write(f'{cells[1].text}, {cells[-1].text}\n')
                print(cells[1].text, cells[-1].text)