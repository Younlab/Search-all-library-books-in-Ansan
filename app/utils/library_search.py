from bs4 import BeautifulSoup
import requests
import re


# default_url = "http://lib.ansan.go.kr/"
# search_url = f"{default_url}simpleDataSearchList.do?"
# status_url = f"{default_url}detailBookData.do?"
# book_detail_url = f"{default_url}simpleDataSearchP.do?"


class SearchBook:
    """
    라이브러리 색인
    """
    site_url = "http://lib.ansan.go.kr/"
    search_url = f"{site_url}detailDataSearchList.do?"

    def find_book(self, **kwargs):
        params = {
            "page": kwargs.get("page", 1),
            "search_vp": kwargs.get("count", 15),
            "srcWord": kwargs.get("keyword"),
            "sitekey2": kwargs.get("lib_num", 1),
        }
        html = requests.post(self.search_url, params).text
        soup = BeautifulSoup(html, "lxml")
        search_list = soup.select("div.serach_list > dl") if soup.select("div.serach_list > dl") != [] else None

        # 검색 결과가 없을 경우 None
        if search_list is None:
            return None
        last_page = int(soup.select_one("div.pn.clear").get_text().split()[-1])
        list_count = int(re.search("\d+", soup.select_one("div.result_area.t_left").get_text()).group())
        lib_name = re.search("\w+", soup.select_one("div.result_area.t_left > span:nth-of-type(1)").get_text()).group()

        data = [
            {
                "id": int(re.search("\d+", data.select_one("dt>a")["onclick"]).group()),
                "title": data.select_one("dt>a").get_text(),
                "author": data.select_one("dd:nth-of-type(1)").get_text(),
                "publisher": data.select_one("dd:nth-of-type(2)").get_text(),
                "publication_date": int(data.select_one("dd:nth-of-type(3)").get_text()),
                "lib": data.select_one("dd:nth-of-type(4)").get_text(),
                "reference_room": data.select_one("dd:nth-of-type(5)").get_text()
            } for data in search_list
        ]
        result = {
            "lib_name": lib_name,
            "lib_num": kwargs.get("lib_name"),
            "count": list_count,
            "current_page": int(kwargs.get("page")),
            "last_page": last_page,
            "keyword": kwargs.get("keyword"),
            "data": data
        }
        return result


if __name__ == "__main__":
    print(SearchBook().find_book(keyword="파이썬"))
