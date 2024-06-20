from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
# static demo data
# posts=[
#         {'id':1, 'title':'Post 1', 'content':'Content of Post 1'},
#         {'id':2,'title':'Post 2', 'content':'Content of Post 2'},
#         {'id':3,'title':'Post 3', 'content':'Content of Post 3'},
#         {'id':4,'title':'Post 4', 'content':'Content of Post 4'},
#     ]

def index(request):
    blog_title="Latest Posts"
    #getting data from post model
    all_posts= Post.objects.all()

    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'blog/index.html', {'blog_title' : blog_title, 'page_obj':page_obj})

def detail(request, post_id):
    # static data
    # post = next((item for item in posts if item['id'] == post_id), None)
    
    try:
    # getting data from model by post id
        post= Post.objects.get(pk=post_id)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post does not exist!")
   
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html', {'post': post, 'related_posts': related_posts})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url")) #redirect keyword to direct from one url to another

def new_url_view(request):
    return HttpResponse("New URL")

def contact_view(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            logger = logging.getLogger("TESTING")
            if form.is_valid():
                logger.debug(f'POST Data is {form.cleaned_data["name"]} {form.cleaned_data["email"]} {form.cleaned_data["message"]}')
                success_message="Your email has been sent!"
                return render(request,'blog/contact.html',{'form': form, 'success_message': success_message})

            else:
                logger.debug('Form validation failure')
            return render(request,'blog/contact.html',{'form': form, 'name': name, 'email': email, 'message': message})
        return render(request,'blog/contact.html')


def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request,'blog/about.html', {'about_content': about_content})