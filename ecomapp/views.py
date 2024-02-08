from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from math import ceil
# Create your views here.
def index(request):
    allProds = []
    #      -1-    knowing the categories available
    # getting the category ,id values for all the objects and storing them as a list of dicts
    catprods = Product.objects.values('category', 'id')
    #taking the categories 
    cats = {item['category'] for item in catprods}
    # taking all thee objects "row" based on all categories we've known now
    for cat in cats:                
        prod= Product.objects.filter(category=cat)
        n=len(prod)
        nslides =n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nslides), nslides])
    params={'allProds' : allProds}
    return render(request,'index.html',params)


def about(request):
    return render(request,'about.html')

#@login_required
def contact(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        phone=request.POST['phone']
        contact_obj=Contact(name=name,email=email,desc=desc,phone_number=phone)
        contact_obj.save()
        messages.info(request,'recived feedback')
    return render(request,'contact.html')

#@login_required
def blog(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    
    if request.method=="POST":
        userX=request.user
        print(userX)
        comment = request.POST.get('comment', '')
        print(comment)
        postx=Post(content=comment,author=userX)
        postx.save()
        
    objs=Post.objects.all()
    print(objs)
    context={'objs':objs}
    return render(request,'blog.html',context)

#@login_required
from django.shortcuts import render

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/auth/login')

    current_user = request.user.username
    items = Orders.objects.filter(email=current_user)
    return render(request, 'profile.html', {'orders': items, 'username': current_user})



#@login_required
def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True



    return render(request,'checkout.html')