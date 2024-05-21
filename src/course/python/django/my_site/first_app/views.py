from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

# Create your views here.

articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}

def news_view(request, topic):
    try:
        articles[topic]
        return HttpResponse(articles[topic]) # Template HTML file (JINJA) in the future
    except KeyError:
        # result = "No page for that topic!"
        # return HttpResponseNotFound(result)
        raise Http404("No page for that topic!")

def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))

def num_page_view(request, num_page):
    topic_list = list(articles.keys())
    try:
        topic = topic_list[num_page]
        return HttpResponseRedirect(topic)
    except IndexError as e:
        raise Http404("No page for that topic!") from e
