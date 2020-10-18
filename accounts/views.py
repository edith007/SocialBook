from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from .form import UserLoginForm, UserRegistrationForm, User
from post.models import Post
from comments.models import Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse





def login_view(request):
    form = UserLoginForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("posts:index")
    title = "Login"
    context = {
        'form' : form,
        'title' : title
    }
    return render(request, "account/forms.html", context)


def logout_view(request):
    logout(request)
    return redirect("posts:index")


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        user = form.save(commit=False)
        password = from.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("posts:index")
    title = "Register"
    context = {
        'form': form,
        'title' : title
    }
    return render(request, "account/forms.html", context)


def search_username(request):
    queryset_list = User.objects.all().order_by('username')
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(username__icontains=query)

    context = {
        "title": "Friends",
        "query": queryset_list
    }
    print('hey')
    return render(request, "accounts/friendSearch.html", context)


#
# Friend request
#
