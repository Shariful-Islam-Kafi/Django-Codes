from django.http import HttpResponse

def home(request):
      return HttpResponse("This is HomePage")


def kafi(request):
      return HttpResponse("Hello Shariful Islam Kafi")
def contact(request):
      return HttpResponse("This is Contact Page")
