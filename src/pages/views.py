from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
	return render(request, "home.html", {})

def contact(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about(request, *args, **kwargs):
	my_context = {
		'my_text': 'pete',
		'my_number': 42,
		'my_list': [76, 78, 21, 'abc', True],
		'my_html': '<h2>A Level 2 Heading Rendered Using the Safe Filter</h2>'
	}
	return render(request, "about.html", my_context)