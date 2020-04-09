from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    text = str(request.POST['fulltext'])
    word_num = len(text.split())
    dict = {}
    for word in text.lower().split():
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    sortedwords = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'word_num': word_num, 'text': text, 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')