from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourses

def Cursos(request):
    courses = Course.objects.all()
    template_cursos = 'cursos.html'
    context = {
        'courses': courses,
    }
    return render(request, template_cursos, context)


def details(request, slug):
    curso = get_object_or_404(Course, slug = slug)
    template_curso = 'curso.html'
    context = {}
    if request.method == 'POST':
        form = ContactCourses(request.POST)
        if (form.is_valid()):
            #form.send_mail
            context['is_valid'] = True
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['message'])
            form = ContactCourses()

    else:
        form = ContactCourses()
    context['curso'] = curso
    context['form'] = form
    return render(request, template_curso, context)