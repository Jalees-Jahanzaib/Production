from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required

from .models import Files
from .forms import  CommentForm
def home(request):
    context={
        'Files': Files.objects.all()
    }
    
    
    return render(request,"blog/home.html",context)
class FileListView(ListView):
    model= Files
    template_name = 'blog/home.html'
    context_object_name= 'Files'
    ordering = ['-date_posted']
class FileDetailView(DetailView):
    model=Files

class FileCreateView(CreateView):
    model=Files
    fields=['title','summary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class FileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Files
    fields = ['title', 'summary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class FileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Files
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Files, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            form.instance.author = request.user
            if request.user.is_staff and request.user.is_superuser :
                form.instance.role = "Final"
                form.instance.final="True"
                print(form.instance.final,type(form.instance.final))
        
            elif  request.user.is_superuser:
                form.instance.role = "Phase 2"
                form.instance.stage3="True"

            elif request.user.is_staff  :
                form.instance.role = "Phase 1"
                form.instance.stage2="True"

        
            else :
                form.instance.role = "Scan"
                form.instance.stage1="True"


            comment.files = post
            comment.save()
            return redirect('file-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

       
def about(request): 
    return render(request,"blog/about.html")


