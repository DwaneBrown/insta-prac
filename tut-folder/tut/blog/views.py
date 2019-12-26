from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse,Http404, HttpResponseRedirect
import datetime as dt
from .models import Pics

def home(request):
 
    pics = Pics.todays_pics()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()

            send_welcome_email(name,email)

            HttpResponseRedirect('home')
    else:
        form = NewsLetterForm()
    return render(request, 'blog/home.html', {"pics":pics,"letterForm":form})

class PicsListView(ListView):
    model = Pics
    template_name = 'blog/home.html'
    context_object_name = 'pics'
    ordering = ['-date_posted']

class PicsDetailView(DetailView):
    model = Pics

class PicsCreateView(LoginRequiredMixin, CreateView):
    model = Pics
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PicsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pics
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        pics = self.get_object()
        if self.request.user == pics.author:
            return True
        return False

class PicsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pics
    success_url = '/'
    def test_func(self):
        pics = self.get_object()
        if self.request.user == pics.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# search results
def search_results(request):
    if 'pics' in request.GET and request.GET["pics"]:
        search_term = request.GET.get("pics")
        searched_pics = Pics.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'folder/search.html',{"message":message,"pics":searched_pics,"search_term":search_term, "category": "search" })
    else:
        message = "You haven't searched for any term"
        return render(request, 'blog/search.html',{"message":message, "category": "search"})

# get by single pics
def pics(request, pics_id):
    try:
        pics = Pics.objects.get(id = pics_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "blog/pics.html", {"pics":pics})