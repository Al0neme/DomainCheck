# -*-coding:utf-8-*-
import requests, warnings,socket
from bs4 import BeautifulSoup as bs

warnings.filterwarnings('ignore')
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    "Connection": "close"
}
proxies = {

}


def check_domain(domain):
    url = "http://" + domain
    location = ''
    end = 0
    while True:
        try:
            resp = requests.get(url=url, headers=headers, verify=False, timeout=10, allow_redirects=False)
            status_code = str(resp.status_code)
            if "30" in str(resp.status_code):
                # 请求跳转内容
                location = "Location: " + url + " "
                resp = requests.get(url=url, headers=headers, verify=False, timeout=10)
                resp.close()
            ip = socket.gethostbyname(domain)
            resp.encoding = resp.apparent_encoding  # 编码处理，避免乱码
            content = resp.text
            soup = bs(content, 'html.parser')
            title = soup.find("title").text
            # 返回结果
            return url + " [" + status_code + "] ip[ " + ip + " ] " + location + "title[ " + str(title).strip() + " ]"
        except Exception as e:
            # print(f"==========url[{url}] exception==========")
            # print(e)
            # print(f"==========url[{url}] exception==========")
            if end:
                return
            url = "https://" + domain
            end = 1
            continue


# print(check_domain("www.929g.com"))
