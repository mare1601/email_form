from django.shortcuts import render
from django.http import HttpResponse
from emailform.forms import PostForm
from django.utils import timezone
from emailform.models import Post
import json

def main_page(request):
    tmpl_vars = {
    'all_posts': Post.objects.reverse(),
    'form': PostForm()
    }
    #return render(request, 'emailform/main_page.html', tmpl_vars)
    return render(request, 'email_form.html', tmpl_vars)


def create_post(request):
    if request.method == 'POST':
        #I think something is wrong here possibly
        post_text = request.POST.get('the_post')
        response_data = {}
        post_last = request.POST.get('last_name')
        post_email = request.POST.get('email_address')
        # We do not have an author object so it will error
        #post = Post(text=post_text, author=request.user)
        post = Post(text=post_text, last=post_last, email=post_email)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['last'] = post.last
        response_data['email'] = post.email
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        #response_data['author'] = post.author.username

        # This was not doing anything - but why?
        #return JsonResponse(response_data)

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
