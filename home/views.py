from django.shortcuts import render
from django.views.generic import View, ListView
from django.http import HttpResponse
from .models import Clients
# Create your views here.


class ClientsPageView(ListView):
    model = Clients
    template_name = 'clients.html'
    context_object_name = 'all_clients_list'


class HomePageView(View):
    model = Clients

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        html = "<html><body><h1>I'am working!</h1>"
        html += "<a>User filled the form:</a><br>"
        for key, value in request.POST.items():
            html += f"Field - {key}, value - {value}<br>"
        html += '</body></html>'
        return HttpResponse(html)


class AboutPageView(View):
    def get(self, request):
        return render(request, 'about-us.html')

    def post(self, request):
        html = "<html><body><h1>I'am working!</h1>"
        html += "<a>User filled the form:</a><br>"
        for key, value in request.POST.items():
            html += f"Field - {key}, value - {value}<br>"
        html += '</body></html>'
        return HttpResponse(html)


class ContactPageView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        html = "<html><body><h1>I'am working!</h1>"
        html += "<a>User filled the form:</a><br>"
        for key, value in request.POST.items():
            html += f"Field - {key}, value - {value}<br>"
        html += '</body></html>'
        return HttpResponse(html)


class LoansPageView(View):
    def get(self, request):
        return render(request, 'loans.html')

    def post(self, request):
        html = "<html><body><h1>I'am working!</h1>"
        html += "<a>User filled the form:</a><br>"
        for key, value in request.POST.items():
            html += f"Field - {key}, value - {value}<br>"
        html += '</body></html>'
        return HttpResponse(html)


class ElementPageView(View):
    def get(self, request):
        return render(request, 'elements.html')

    def post(self, request):
        html = "<html><body><h1>I'am working!</h1>"
        html += "<a>User filled the form:</a><br>"
        for key, value in request.POST.items():
            html += f"Field - {key}, value - {value}<br>"
        html += '</body></html>'
        return HttpResponse(html)


class NewsPageView(View):
    def get(self, request):
        return render(request, 'news.html')

    def post(self, request):
        html = "<html><body><h1>I'am working!</h1>"
        html += "<a>User filled the form:</a><br>"
        for key, value in request.POST.items():
            html += f"Field - {key}, value - {value}<br>"
        html += '</body></html>'
        return HttpResponse(html)
