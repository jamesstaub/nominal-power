# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from installations.methods import GeoResponse
import json

@csrf_exempt
def installation(request):
    serialized = json.loads(request.body.decode())
    response = GeoResponse(serialized['installation'])
    return JsonResponse(response.json)


 # NOTE: attempted to use django rest framework for nice api endpoint with ember, but got bogged down on
 # this error
 # rest_framework.exceptions.UnsupportedMediaType: Unsupported media type "application/json" in request.

#
# class Installation(APIView):
#     renderer_classes = (JSONRenderer, )
#
#     @csrf_exempt
#     def post(self, request):
#         print('---------------')
#         import ipdb; ipdb.set_trace()
#         print(request.data)
#         print('---------------')
#         return Response({'some': 'data'})
