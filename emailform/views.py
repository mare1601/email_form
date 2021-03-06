from django.shortcuts import render
from django.http import HttpResponse
from emailform.forms import PostForm
from django.utils import timezone
from emailform.models import Post
import json

# Create your views here.
def main_page(request):
  tmpl_vars = {
    'all_posts': Post.objects.all(),
    'form': PostForm()
  }
  return render(request, 'emailform/main_page.html', tmpl_vars)


def create_post(request):
    if request.method == 'POST':
        #I think something is wrong here possibly
        post_text = request.POST.get('try_this')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return JsonResponse(response_data)

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )