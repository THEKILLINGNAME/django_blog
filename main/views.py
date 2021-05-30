from django.shortcuts import render

def index(request):
  data = {
    'title': 'Главная главная страница',
    'values': ['Hello', '123', 'Pararam'],
    'obj': {
      'car': 'BMW',
      'age': 10,
      'hobby': 'Basketball'
    }
  }

  return render(request, 'main/index.html', data)

def about(request):
  return render(request, 'main/about.html')

def contact(request):
  return render(request, 'main/contact.html')
