from django.shortcuts import render, HttpResponse

from simplemooc.courses.models import Course

def homeDefault(request):
  last_courses = Course.objects.order_by('-pk')[0:3]
  most_follows = Course.objects.order_by('follows')[0:3]
  context ={
    'last_courses': last_courses,
    'most_follows': most_follows,
  }
  return render( request, 'simplemooc/home.html', context )


