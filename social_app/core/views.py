from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import get_pages
from django.contrib.auth.models import User
import json

# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  return render(request, 'home.html')

def home2(request):
  return render(request, 'home2.html')

def getPages(request):
	#context = user.name
	user = request.user
	social = user.social_auth.get(provider='facebook')
	x = get_pages(social.extra_data['access_token'], social.extra_data['id'])
	context = {'pages': x["data"]}
	return render(request, 'pages.html', context)
