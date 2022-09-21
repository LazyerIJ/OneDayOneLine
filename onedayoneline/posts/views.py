from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


# 제목리스트 -> 이 부분을 잘 고치면 달력모양이랑 합칠수 있지 않을까?
def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)

# 내용 상세 페이지
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})

# 새로운 글 등록 -> 이부분도 달력모양에서 되게끔 하면 안되나?
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = PostForm()
    
    return render(request, 'posts/create.html', {'form' : form})

# 글 수정
def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', post_id)
        
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update.html', {'form': form})

# 글 삭제  -> 우리한테는 이 기능 없애려고 했어서 선택 필요

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('index')
