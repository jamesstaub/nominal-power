from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class Installation(APIView):
    renderer_classes = (JSONRenderer, )
    def post(self, request):
        return Response({'some': 'data'})
