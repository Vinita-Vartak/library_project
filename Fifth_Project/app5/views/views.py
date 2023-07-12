from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, redirect, render

from app5.models import Book

@login_required
def welcome_page(request):  
    return render(request, "welcome.html")

import datetime

@login_required
def show_all_books(request):
    books = Book.objects.filter(is_active=True)  
    return render(request, "showbooks.html", {"allbooks": books, "today": datetime.datetime.now()})

@login_required
def show_single_book(request, bid): 
    try:
        book_obj = Book.objects.get(id=bid) 
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist..!")
    return render(request=request, template_name="bookdetail.html", context={"book": book_obj})

def common_var(req):
    final_dict = req.POST
    book_name = final_dict.get("nm")
    book_price = final_dict.get("prc")
    book_qty = final_dict.get("qty")
    book_is_pub = final_dict.get("ispub")
    return book_name, book_price, book_qty, book_is_pub

@login_required # type: ignore
def add_single_book(request):
           
    if request.method == "POST":
        book_name, book_price, book_qty, book_is_pub = common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
        Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_published=is_pub)
        messages.success(request, f"Book has been added Suceesfully..!")
        return redirect("show_books")
    

    elif request.method == "GET":
                
        return render(request, "addbook.html")
    
    
    
    
@login_required
def edit_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    if request.method == "GET":
        return render(request, "bookedit.html", {"single_book": book_obj})
    elif request.method == "POST":
        book_name, book_price, book_qty, book_is_pub = common_var(request)
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
        # for updating the data of books
        book_obj.name = book_name
        book_obj.price = book_price
        book_obj.qty = book_qty
        book_obj.is_published = is_pub
        book_obj.save()
        messages.success(request, f"Book:{book_obj.name} has been Updated Suceesfully..!") 
        return redirect("show_books")

@login_required
def delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.delete()  # hard delete
    return redirect("show_books")

@login_required
def soft_delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.is_active = False   # soft delete
    book_obj.save()
    messages.info(request,"Book deleted Successfully..")
    return redirect("show_books")

@login_required
def show_inactive_books(request):
    books = Book.objects.filter(is_active=False)  
    return render(request, "showinactivebook.html", {"allbooks": books, "today": datetime.datetime.now()})

#********************************************************************************************************
from app5.forms import AddressForm, BookForm, GeeksForm

# def form_view(request):
#     context ={}
#     context['form']= GeeksForm()
#     return render(request, "form_test.html", {"form": GeeksForm})

# def form_view(request):
#     context ={}
#     context['form']= GeeksForm()
#     return render(request, "form_test.html", {"form": BookForm})

# def form_view(request):
#     context ={}
#     context['form']= GeeksForm()
#     return render(request, "form_test.html", {"form": AddressForm})

# def form_view(request):
#     if request.method == "POST":
#                 # pass
#         print("IN POST Request")
#         data = request.POST
#         print(data)    #It will return None
#         return HttpResponse("All is ok")
    
# After submitting form ,we will get output as below
#     IN POST Request
# <QueryDict: {'csrfmiddlewaretoken': ['N0YeQ7Qa8RMtqPDHfHVIFgOlyqUOShRbJTGQ2j0IMGfVONTQjYEvaNPQPPS5K6o2'],
# 'name': ['Book_14'], 'price': ['344'], 'qty': ['5'], 'is_published': ['on']}>


# After submitting form ,we will get output as below if "is_published" is unchecked

# IN POST Request
# <QueryDict: {'csrfmiddlewaretoken': ['InlA3hPx4G7w0g7u41rPXIivBnTd0sDsEg3cftZ5IvAYoenD8iaCsfj0SMRuShaj'], 
# 'name': ['Book_17'], 'price': ['76'], 'qty': ['4']}>

    # elif request.method == "GET":
    #     print("GET request")
    #     return render(request, "book_form_test.html", {"bookform": BookForm})
  
# for below program o/p will be same only it will chk wheather data valid or not.  
# def form_view(request):
#     if request.method == "POST":
#                 # pass
#         print("IN POST Request")
#         data = request.POST
#         form= BookForm(data)
#         if form.is_valid():
#             print("For If condition")
#         return HttpResponse("All is ok")
#     elif request.method == "GET":
#         print("GET request")
#         return render(request, "book_form_test.html", {"bookform": BookForm})
    
# to get data in mysql database as well as in show active books, so redirect used so that after entering 
# it will go to show_active books

def form_view(request):
    if request.method == "POST":
                # pass
        print("IN POST Request")
        data = request.POST
        form= BookForm(data)
        if form.is_valid():
            form.save()
        # return HttpResponse("All is ok")
        return redirect("show_books")
    elif request.method == "GET":
        print("GET request")
        return render(request, "book_form_test.html", {"bookform": BookForm})
    
    
#****************************************************************************
    

