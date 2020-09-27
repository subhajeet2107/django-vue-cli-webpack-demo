from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def home(request):
	ctx = {
	}
	return render(request, 'mainsite/home.jinja', ctx)