from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.shortcuts import render, HttpResponseRedirect
from .models import Book
from .forms import NewBookForm
def helloo(request):
    return HttpResponse('<h1>Hello kasem</h1>')

def listbook(request):
    context={}
    books=Book.objects.all()
    context['books']=books
    return render(request,'list.html', context={'books':books})

def book_details(request,id):
    book=Book.objects.filter(id=id).first()
    return render(request,'details.html',context={'book':book})

# def add(request):
#     print(request.method)
#     context={'form':Addbook}
#     # books=Book.objects.all()
#     # context['books']=books
#     Book.objects.create(title=request.POST['title'],
#     #  auther=Author.getauthorbyid(request.POST['auther_id']),
#      version=request.POST['version'],)
#     return render(request,'add.html', context)

def book_delete(request,id):
    Book.objects.filter(id=id).delete()
    return redirect('listbook')

def book_add(request):
    context = {}
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            version = form.cleaned_data['version']
            image = form.cleaned_data['image']
            author_id = form.cleaned_data['author']
            author = Author.objects.get(id=author_id)
            book = Book.objects.create(title=title, version=version, image=image, author=author)
            return HttpResponseRedirect('show/')
    else:
        form = NewBookForm()  # Create a new form instance for GET requests

    context['form'] = form
    return render(request, 'add.html', context)
    
def book_update(request,title):
    # return HttpResponse('<h1>update</h1')
    context={}
    form=NewBookFormModel(instance=Book.objects.filter(title=title).first())
    if(request.method=='POST'):
        form = NewBookFormModel(instance=Book.objects.filter(title=title).first(),data=request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('show')
    context['form']=form

    return render(request, 'update.html', context)
