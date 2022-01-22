from django.shortcuts import render

def movie_list(reqest):
	context = {}
	return render(reqest, profiles/movie_list.html)