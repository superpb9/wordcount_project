import operator

from django.http import HttpResponse
from django.shortcuts import render


def home_page_test(request):
    return HttpResponse('Hello')

def home_page(request):
    return render(request, 'home.html', {'key':'Value is me'})

def count_page(request):
    #### This is how to pull the parametres from URL Request ...
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    word_count_dic = {}
    for word in wordlist:
        if word in word_count_dic:
            # Increase
            word_count_dic[word] += 1
        else:
            # add to the dictionary
            word_count_dic[word] = 1
    
    sortedwords = sorted(word_count_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count_page.html',
        {
        'fulltext':fulltext,
        'count_':len(wordlist), 
        'sortedwords':sortedwords
        }
    )


def about_page(request):
    return render(request, 'about.html')
