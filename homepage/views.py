from django.shortcuts import render
from django.http import HttpResponse, request
import speech_recognition as sr
import pyaudio
import webbrowser as wb
from .models import UserSearches

# Create your views here.






def home(request):
    
    return render(request, 'home.html', allDynamicContent())





def allDynamicContent():

    recent_searches = UserSearches.objects.all()

    popular_searches = UserSearches.objects.all()
    
    return {'recent_searches': recent_searches, 'popular_searches': popular_searches}





def textWeb(request):

    search_string = request.POST['TextInput']

    outputlist = list(search_string.split(' '))

    search_new_str = '+'.join(outputlist)

    searchquery = 'https://www.google.com/search?q='+search_new_str

    wb.get().open_new_tab(searchquery)

    return render(request, 'home.html', allDynamicContent())






def speech(request):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        output = r.recognize_google(audio)
    except sr.UnknownValueError:
        output = 'Google speech recognition could not understand audio'
    except sr.RequestError as e:
        output = 'Could not request results from google speech recognition service; {0}'.format(e)
    
    outputlist = list(output.split(' '))

    speech2text = '+'.join(outputlist)

    searchquery = 'https://www.google.com/search?q='+speech2text

    wb.get().open_new_tab(searchquery)

    return render(request, 'home.html', allDynamicContent())
