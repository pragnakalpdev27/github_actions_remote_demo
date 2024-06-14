from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world chaitali!")

def demo(request):
    return HttpResponse("Hello world pragnakalp!")
