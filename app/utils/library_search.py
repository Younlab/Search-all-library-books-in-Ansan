from bs4 import BeautifulSoup
import requests
import re


class SearchBook:
    default_url = "http://lib.ansan.go.kr/"
    search_url = f"{default_url}simpleDataSearchList.do?"
    status_url = f"{default_url}detailBookData.do?"
    book_detail_url = f"{default_url}simpleDataSearchP.do?"

    def __init__(self, key_word=None):
        self.key_word = key_word

    def search_book(self, site_no=1):
        """
        도서관 소장 목록 및 대출 여부
        """
        result_data = []
        params = {
            "sitekey": site_no,
            "srcWord": self.key_word,
            "page": 1
        }
        default_response = requests.get(self.search_url, params).text
        default_soup = BeautifulSoup(default_response, 'lxml')
        page = len(default_soup.select("div.pn.clear > a"))
        # 페이지네이션이 1 이상일 경우 해당 경로 넘버링
        page_no = (range(1, page + 2)) if page > 0 else tuple(0)

        for page in page_no:
            params["page"] = page
            response = requests.get(self.search_url, params).text
            soup = BeautifulSoup(response, 'lxml')
            search_list = tuple(soup.select("div.serach_list > dl"))
            search_object = []
            for book_object in search_list:
                book_title = book_object.select_one("dt > a")
                book_id = int(re.search("\d+", book_title["onclick"]).group())
                book_author = book_object.select_one("dd:nth-of-type(1)").get_text()
                book_publisher = book_object.select_one("dd:nth-of-type(2)").get_text()
                book_publication_date = int(book_object.select_one("dd:nth-of-type(3)").get_text())
                book_library = book_object.select_one("dd:nth-of-type(4)").get_text()
                book_reference_room = book_object.select_one("dd:nth-of-type(5)").get_text()
                # book_location = self.search_loan_status(book_id)["call_no"]
                # book_status = self.search_loan_status(book_id)["status"]
                search_object.append(
                    {
                        "id": book_id,
                        "title": book_title.get_text(),
                        "author": book_author,
                        "publisher": book_publisher,
                        "publication_date": book_publication_date,
                        "library": book_library,
                        "reference_room": book_reference_room,
                        # "location": book_location,
                        # "status": book_status
                    }
                )

            result_data += search_object
        result_count = len(result_data)
        result = {"data": result_data, "count": result_count}
        return result

    def search_loan_status(self, book_id):
        """
        책 대출여부 확인/청구기호 확인
        """
        params = {
            "skey": book_id
        }
        response = requests.get(self.status_url, params).json()
        result = {
            "call_no": response["modelAndView"]["model"]["callNo"],
            "status": True
        }
        if response["modelAndView"]["model"]["status"] != "비치":
            result["status"] = False
        return result

    def search_book_detail(self, book_id):
        """
        책 상세정보 조회
        """
        params = {
            "skey": book_id
        }
        response = requests.get(self.book_detail_url, params).text
        soup = BeautifulSoup(response, 'lxml')
        body = soup.select_one("ul.zine_lst")
        title = body.select_one("h2").get_text(strip=True)
        image = body.select_one("img.tmb")["src"]
        auther = body.select_one("ul.lst_type_bull.v2 > li:nth-of-type(1)").get_text(strip=True)
        publication_information = body.select_one("ul.lst_type_bull.v2 > li:nth-of-type(2)").get_text(strip=True)
        notes = body.select_one("ul.lst_type_bull.v2 > li:nth-of-type(3)").get_text(strip=True)
        number_and_price = body.select_one("ul.lst_type_bull.v2 > li:nth-of-type(4)").get_text(strip=True)
        description = body.select_one("div.summary:nth-of-type(1)").get_text(strip=True)
        index = body.select_one("div.summary:nth-of-type(2)")
        result = {
            "title": title,
            "image": image,
            "author": auther,
            "publication": publication_information,
            "notes": notes,
            "number_price": number_and_price,
            "description": description,
            "index": index
        }
        return result


if __name__ == "__main__":
    SearchBook("파이썬").search_book()
