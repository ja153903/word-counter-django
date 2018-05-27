from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = Counter(fulltext.split())
    mostcommon = wordlist.most_common(n=1)[0]

    return render(request, 'count.html', {"fulltext": fulltext, 
                                          "count": len(wordlist), 
                                          "mostcommonword": mostcommon[0],
                                          "mostcommonwordoccurence": mostcommon[1]})