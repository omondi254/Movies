from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dataset/index.html')



def about(request):
    pass


def contact(request):
    pass


def Groups(request):
    pass