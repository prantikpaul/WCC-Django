from django.urls import path
from .views import *
urlpatterns = [
path('',index, name='index'),
path('about_us/',about, name='aboutpp'),
path('service/',serive, name='service'),
path('mission/',mission, name='mission'),
path('contact/',contact, name='contact'),
path('faq/',faq, name='faq'),
path('feedback/',feedback, name='feedback'),
path('career/',career, name='career'),
path('request_free_consultation/',req, name='req'),
path('thank_you/',thank_u, name='thank_u'),
path('vision/',vision, name='vision'),
]
