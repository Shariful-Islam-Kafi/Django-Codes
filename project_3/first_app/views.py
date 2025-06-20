from django.shortcuts import render

# Create your views here.

def home(request):
      d = {'author' : 'Kafi', 'age' : 24, 'courses': [
            {
            'id' : 1,
            'course_name' : 'Python',
            'course_fee' : 5000
            },
            {
            'id' : 2,
            'course_name' : 'Django',
            'course_fee' : 10000
            },
            {
            'id' : 3,
            'course_name' : 'GO',
            'course_fee' : 20000
            },

      ]}
      return render(request, 'home.html', d)