from django.shortcuts import render

def home(request):
	return render(request,'home.html')

def reverse(request):
	text=request.GET['text_zone']
	text_words=len(text.split(' '))
	text_reverse=text[::-1]
	return render(request,'reverse.html',{'text_reverse':text_reverse,
		'text_words':text_words,'text':text})

