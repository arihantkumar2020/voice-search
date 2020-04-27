from django.shortcuts import render
from django.http import HttpResponse, request
import speech_recognition as sr
import pyaudio
import webbrowser as wb
from .models import UserSearches
from operator import attrgetter
import datetime
from django.db import models, connection

# Create your views here.





#rdirecting to voicesearch home page
def home(request):
    
    return render(request, 'home.html', allDynamicContent())





#returning dynamic content to make the web page dynamic
def allDynamicContent():

    recent_var = []

    i = 0

    for str in sorted(UserSearches.objects.all(), key = attrgetter('search_datetime'), reverse=True):
        if i < 10 :
            recent_var.append(str.search_input)
        i += 1
    
    recent_searches = recent_var
    
    return {'recent_searches': recent_searches}






# to receive search query in the form of text
def text(request):

    search_string = request.POST['TextInput']

    textToWeb(search_string)

    return render(request, 'home.html', allDynamicContent())





#to receive audio and converting it into text
def speech(request):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        output = r.recognize_google(audio)
    except:
        pass

    '''except sr.UnknownValueError:
        output = 'Google speech recognition could not understand audio'
    except sr.RequestError as e:
        output = 'Could not request results from google speech recognition service; {0}'.format(e)'''
    
    textToWeb(output)

    return render(request, 'home.html', allDynamicContent())





#to open client's search query in a new tab
def textToWeb(output_str):

    updateDatabase(output_str)

    outputlist = list(output_str.split(' '))

    search_new_str = '+'.join(outputlist)

    searchquery = 'https://www.google.com/search?q='+search_new_str

    wb.get().open_new_tab(searchquery)

    return






#updating data when search query is passed
def updateDatabase(output_str):
    current_datetime = datetime.datetime.now()

    try:
        delete_existing_obj = UserSearches.objects.filter(search_input = output_str)
        delete_existing_obj.delete()
    except Exception:
        pass
    finally:
        new_obj = UserSearches(search_input = output_str, search_datetime = current_datetime)
        new_obj.save()
    
    return