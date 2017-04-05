from django.shortcuts import render



def hello_view(request):
	context = {
		'content_title': 'It is sparta!!!!',
		'content_body': ' osdijf oisdj foisd hfoisdh foisdh foigsd oifhso'
	}

	return render(request, 'sparta/sparta.jinja2', context)
