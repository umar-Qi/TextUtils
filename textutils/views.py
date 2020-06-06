#I have created this file - Umer
from django.http import HttpResponse
from django.shortcuts import render
#code for display contents in another file

#def read_file(request):
#    f = open('/home/umer/Errors.txt', 'r')
#    file_contents = f.read()
#    f.close()
#    return HttpResponse(file_contents, content_type='text/plain')

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):

    #get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
#    charcount = request.GET.get('charcount', 'off')

    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''(){}[];:"<>/?!@#$%^&'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (fullcaps == "on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'change to Uppercase', 'analyzed_text': analyzed}
            djtext = analyzed
            #return render(request, 'analyze.html', params)
    if(newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
            params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
            djtext = analyzed
            #return render(request, 'analyze.html', params)
    if (extraspaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps!= "on" and newlineremover != "on" and extraspaceremove != "on"):
        return HttpResponse("Error")
        #return render(request, 'analyze.html', params)
  #  if (charcount == "on"):
  #      analyzed = djtext
  #       params = {'purpose': 'Count the Characters', 'analyzed_text': len(analyzed)}
 #       return render(request, 'analyze.html', params)
    #else:
     #   return HttpResponse("Error")
    return render(request, 'analyze.html', params)
