from django.shortcuts import render

def login(request):
	return render(request,"login.html")
def register(request):
	return render(request,'register.html')
def detail(request):
	return render(request,'detail.html')
def search(request):
	render(request,'search.html')
	#speech recognition
	import speech_recognition as sr
	import webbrowser as wb
	import bs4
	import lxml
	import requests

	chrome_path ="C:/Users/HP/AppData/Local/Google/Chrome/Application/chrome.exe"
	r= sr.Recognizer()

	with sr.Microphone() as source:

		print("say something\n")
		audio = r.record(source,duration =5)
	try:
	    text= r.recognize_google(audio)
	    print(text)
	    res = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + text+ '&callback=handleResponse')
	    soup = bs4.BeautifulSoup(res.text, 'lxml')
	    t = str(soup.select('body'))
	    f = open('C:/Users/HP/Desktop/sih_django/libauto/stport/templates/detail.html','w')
	    index =t.find('title')
	    while(t[index]!= ','):
	        if(t[index]!= '"'):
	            print(t[index], end="")
	            f.write(t[index])
	        index = index +1
	    f.write("</br>")    
	    index =t.find('author')
	    while(t[index]!= ','):
	        if(t[index]!= '"'):
	            print(t[index], end="")
	            f.write(t[index])
	        index = index +1    
	    f.close()   
	except Exception as e:
		print(e)
		
	return render(request,'detail.html')