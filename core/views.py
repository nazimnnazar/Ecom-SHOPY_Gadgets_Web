from email import message
from .models import*
#cart
from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
#endcart
#Register
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#endregister
# Create your views here.
def home(request,c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = products.objects.filter(category=c_page, available=True)
    else:
        prodt = products.objects.all().filter(available=True)
    cat = categ.objects.all()
    return render(request,'index.html',{'pr': prodt, 'ct': cat})

def views(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'views.html',{'pr':prod})
#cart
def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def cartdetails(request, tot=0, count=0, c=0,c_item=None):
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        c_item = CartItems.objects.filter(cart=ct, active=True)
        for i in c_item:
            tot += (i.prod.price * i.quan)
            c = c + 1
        count = tot + 100
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', {'ci': c_item, 't': tot, 'cn': count, 'c': c})


def add_cart(request, product_id):
    pro = products.objects.get(id=product_id)
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        ct = CartList.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        ct_item = CartItems.objects.get(prod=pro, cart=ct)
        if ct_item.quan < ct_item.prod.stock:
            ct_item.quan += 1
        ct_item.save()
    except CartItems.DoesNotExist:
        ct_item = CartItems.objects.create(prod=pro, quan=1, cart=ct)
        ct_item.save()
    return redirect('cartDetails')


def min_cart(request, product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    pro = get_object_or_404(products, id=product_id)
    c_item = CartItems.objects.get(prod=pro, cart=ct)
    if c_item.quan > 1:
        c_item.quan -= 1
        c_item.save()
    else:
        c_item.delete()

    return redirect('cartDetails')

def remove(request,product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    pro = get_object_or_404(products, id=product_id)
    c_item = CartItems.objects.get(prod=pro, cart=ct)
    c_item.delete()
    return redirect('cartDetails')
#end cart
def contact(request):
    return render(request,'contact.html')

def checkout(request):
    return render(request,'checkout.html')

#Register
def register(request):
    form=CreateUserForm
    if request.method == 'POST':
         form=CreateUserForm(request.POST)
         if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Accounts was created for " +user)
            return redirect('login')
    context={'form':form}
    return render(request,'register.html',context)


def signin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password error')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request,'profile.html')

#end Register
def add(request):
    return render(request,'add.html')

# def cartsetails(request):
#     return render(request,'cart.html')