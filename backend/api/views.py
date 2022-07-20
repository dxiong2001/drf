import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):

    body = request.body

    data = {}
    try:
        data = json.loads(body) # string of JSON data -> python dict
    except:
        pass

    print(data)
    data['params'] = dict(request.GET)
    print(data['params']['url'][0])
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    return JsonResponse(data)