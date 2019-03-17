from rest_framework.response import Response
from rest_framework.views import APIView


class EmailDelivery(APIView):
    def post(self, request, *args, **kwargs):
        return Response(status=200, data="이메일 요청")
