import json
from django.http import JsonResponse
from .parser import *

def api_home(request, *args, **kwargs):

    body = request.body

    data = {}
    try:
        data = json.loads(body) # string of JSON data -> python dict
    except:
        pass

    print(data)
    data['params'] = dict(request.GET)
    # url = data['params']['url'][0]
    url = 'https://www.popsci.com/science/omicron-coronavirus-variant/'
    page_content = get_html(url)
    processed_text = getArticleTextSections(page_content)
    article_section = processArticleSections(processed_text)

    quotes = getQuotes(processed_text)

    title, author, date, image = getArticleInfo(page_content)

    people, people_extended = getNamedEntities(processed_text)
    attributed_quotes = attribute_quote(people_extended, quotes)

    
    print(url)
    print(title, author,date,image)
    print(attributed_quotes)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    return JsonResponse(data)