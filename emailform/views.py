from django.shortcuts import render
from django.http import HttpResponse
from emailform.forms import PostForm
from django.utils import timezone
from emailform.models import Post
import json

# Create your views here.
def main_page(request):
  posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
  return render(request, 'emailform/main_page.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['first'] = post.first
        response_data['last'] = post.last
        response_data['email'] = post.email
        response_data['created_date'] = post.created.strftime('%B %d, %Y %I:%M %p')

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )