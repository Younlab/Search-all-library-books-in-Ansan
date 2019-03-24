from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.library_search import SearchBook


class Search(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        params = {
            "keyword": request.GET['keyword'],
            "page": request.GET['page'],
            "count": request.GET['count'],
            "lib_num": request.GET['lib_num'],
        }
        search_result = SearchBook().find_book(**params)
        if search_result is None:
            return Response(data="검색결과를 찾을 수 없습니다.", status=status.HTTP_404_NOT_FOUND)
        return Response(data=search_result, status=status.HTTP_200_OK)
