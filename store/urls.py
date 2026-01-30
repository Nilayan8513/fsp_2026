from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='store_index'),
    path('test', views.test, name='test'),

    path('text', views.text, name='text'),
    path('fibo', views.fibo, name='fibo'),
    path('cal', views.cal, name='cal'),
    path('calculate', views.calculate, name='calculate'),
    path('ins', views.ins, name='ins'),
    path('insert', views.insert, name='insert'),
    path('student', views.student_view, name='student'),
    path('insstud', views.insstud, name='store_insstud'),
    path('show', views.show, name='show'),
    path('dele/<int:id>', views.dele, name='store_dele'),
    path('edit/<int:id>', views.edit, name='store_edit'),
    path('update/<int:id>', views.update, name='store_update'),

]