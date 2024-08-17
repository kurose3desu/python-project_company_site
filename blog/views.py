from django.views.generic import ListView, DetailView
from .models import Post

class Index(ListView):
    model = Post

class Detail(DetailView):
    model = Post
    
from django.views.generic.edit import CreateView

class Create(CreateView):
    model = Post
    
    # 編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]
    

from django.views.generic.edit import UpdateView

class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags"]
    
    
from django.views.generic.edit import DeleteView

class Delete(DeleteView):
    model = Post
    
    # 削除したあとに移動する先（トップページ）
    success_url = "/"