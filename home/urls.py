from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, \
    LoansPageView, ElementPageView, NewsPageView, ClientsPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('clients.html', ClientsPageView.as_view(), name='clients'),
    path('news.html', NewsPageView.as_view(), name='news'),
    path('elements.html', ElementPageView.as_view(), name='elements'),
    path('loans.html', LoansPageView.as_view(), name='loans'),
    path('contact.html', ContactPageView.as_view(), name='contact'),
    path('index.html', HomePageView.as_view(), name='index'),
    path('about-us.html', AboutPageView.as_view(), name='about'),
]
