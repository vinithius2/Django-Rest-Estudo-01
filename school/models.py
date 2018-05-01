from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=150)
    birth = models.DateField()
    adress = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)


class Student(Person):
    schooling = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'STUDENT'
        ordering = ('name',)


class Teacher(Person):
    matter = models.CharField(max_length=150)
    FK_TEACHER_STUDENT = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TEACHER'
        ordering = ('name',)
