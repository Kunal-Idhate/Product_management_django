from django.shortcuts import render,redirect
from home.models import Product,User
from django.http import JsonResponse
# Create your views here.

def index (request):
   search_query = request.POST.get('search')
   if search_query:
      recommended_products = Product.objects.filter(shape__startswith=search_query)
      context={
      "product":recommended_products,
      }
      return render(request,'product.html',context) 
     
   else:
      product = Product.objects.all()
      context={
           "product":product,
      }
      return render(request,'product.html',context)

def AddProduct(request):
 if request.method =='POST':
    shape=request.POST.get('shape')
    size=request.POST.get('size')
    location=request.POST.get('location')
    price=request.POST.get('price')
    product = Product(
       shape=shape,
       size=size,
       location=location,
       price =price,
    )
    product.save()
 return redirect("home")


def UpdateProduct(request,id):
   if request.method =='POST':
    shape=request.POST.get('shape')
    size=request.POST.get('size')
    location=request.POST.get('location')
    price=request.POST.get('price')
    product = Product(
       id=id,
       shape=shape,
       size=size,
       location=location,
       price =price,
    )
    product.save()
   return redirect("home")


def DeleteProduct (request,id):
    product = Product.objects.filter(id=id)
    product.delete()
    return redirect("home")

# USer CRUD
def Users(request):
    user = User.objects.all()
    context={
        "user":user,
    }
    return render(request,'users.html',context)


def AddUser(request):
 if request.method =='POST':
    name=request.POST.get('name')
    age=request.POST.get('age')
    address=request.POST.get('address')
    
    user = User(
       name=name,
       age=age,
       address=address,
    )
    user.save()
 return redirect("users")

def UpdateUser(request,id):
   if request.method =='POST':
    name=request.POST.get('name')
    age=request.POST.get('age')
    address=request.POST.get('address')
    user = User(
       id=id,
       name=name,
       age=age,
       address=address,
    )
    user.save()
   return redirect("users")

def DeleteUser(request,id):
   user = User.objects.filter(id=id)
   user.delete()
   return redirect("users")
   

# Searching product

# def RecommandedProduct(request):
#    return

# def SearchResult (request):
#    payload=[]
#    if request.method =='GET':
#       search_query = request.GET.get('search')
#       recommended_products = Product.objects.filter(shape__startswith=search_query)
#    context={
#       "product":recommended_products,
#    }
#    return render(request,'product.html',context)
def SearchProduct (request):
   search_query = request.GET.get('search')
   payload=[]
   if search_query:
      recommended_products = Product.objects.filter(shape__startswith=search_query)
      for obj in recommended_products:
         payload.append({
            "id": obj.id,
            "shape": obj.shape,
            "size": obj.size,
            "location": obj.location,
            "price": obj.price,
         })
      
   
   return JsonResponse(
      {
         "status": True,
         "payload": payload
      }
   )

