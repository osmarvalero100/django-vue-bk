from django.http import HttpResponse

# Create your views here.
def home_inicio(request):
    return HttpResponse("<h1>Hola Mundo desde Django</h1>")
