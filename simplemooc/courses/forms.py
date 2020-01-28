from django import forms     
# from django.core.mail import send_mail


class ContactCourses(forms.Form):

    name = forms.CharField(label='Nome' , max_length = 100)
    email = forms.EmailField(label = 'Email')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget = forms.Textarea
    )

    #def send_mail(self):
        # Na VIEW é apenas o que tem que ser exibido ou não.
     #   send_mail('Procuro um Emprego', 'Olá, estou procurando um emprego. Você pode me ajudar?',
      #  'nastarinabas@gmail.com', ['joxob33550@mailart.ws'], fail_silenty=False )
       # return True