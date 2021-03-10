#i have created this file
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
    #return HttpResponse( '''Hello <a href "https://www.youtube.com">YOUTUBE</a>''')
def index(request):
   return render(request, 'index.html')
    #return HttpResponse( "Home")
def analyze(request):
    #get the text and analyze the text
    djtext= request.GET.get('text', 'default')
    removepunc= request.GET.get('removepunc', 'off')
    fullcaps= request.GET.get('fullcaps', 'off')
    newlineremover= request.GET.get('newlineremover', 'off')
    extraspaceremover= request.GET.get('extraspaceremover', 'off')
    charcounter= request.GET.get('charcounter', 'off')




   
    if removepunc == "on":
   # analyzed = djtext
        punctuations =  '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Changed to UPPER CASE','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed+ char
        params={'purpose':'Removed New Line','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    elif(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1]== " "):
                analyzed = analyzed + char
        params={'purpose':'Removed Extra Space','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    elif(charcounter=="on"):
        analyzed=""
        analyzed= len(djtext)
        params={'purpose':'Character Counted','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)



    else:
        return HttpResponse("error")