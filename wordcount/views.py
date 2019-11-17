

from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    wordcountdict = {}

    for word in wordlist:
        if word in wordcountdict:
            #Increase the value associated with the words
            wordcountdict[word] += 1
        else:
            #add word to wordcountdict and set value to 1
            wordcountdict[word] = 1

        sortedwordcountlist = sorted(wordcountdict.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwordcountlist})
