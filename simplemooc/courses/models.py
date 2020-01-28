from django.db import models

class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter( 
            models.Q(title__icontains = query) |
            models.Q(description__icontains = query )
            )

class Course(models.Model):

    title = models.CharField('Nome', max_length= 100)
    slug = models.SlugField('Atalho',max_length=50)
    description = models.TextField('Descricao',blank = True)
    follows = models.IntegerField(default = 0)
    imagem = models.ImageField(upload_to = 'courses/images',verbose_name= 'Imagem', null=True, blank = True)
    created_at = models.DateTimeField('Criado em',auto_now_add = True )
    updated_at= models.DateTimeField( 'Atualizado em', auto_now = True )

    objects = CourseManager()
    
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['description']
        
        
        #def get_absolute_url(self):
        #from django.urls import reverse
        #return reverse('curso.html', args=[self.slug])