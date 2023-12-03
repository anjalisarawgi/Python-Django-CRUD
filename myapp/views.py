from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email = request.POST['email']
        # #if email already exists:
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, 'Email already exists. Please try again')
            # return redirect('index.html')
        phone=request.POST['phone']
        address=request.POST['address']
        gender=request.POST['gender']
        User.objects.create(name=name, email=email, phone=phone, address=address, gender=gender)
        back=request.META['HTTP_REFERER']
        messages.success(request, 'Signed in Successfully!')
        return redirect(back)
        # return HttpResponse('Success: Thankyou for signing in')
    else:
        # users = User.objects.all()
        # return HttpResponse(users.query)
        context={
            "UsersData": User.objects.order_by('-id')
        }
        return render(request, 'index.html', context )


def delete(request, id):
    users = User.objects.get(id=id)
    users.delete()
    messages.success(request,'User deleted successfully')
    return redirect('/')


# def edit(request, id):
#     if request.method == "POST":
#         pass
#     else:
#         context={
#             'users': User.objects.get(id=id)
#         }
#         return render(request, 'edit.html', context)

def edit(request, id):
    if request.method == "POST":
        users = User.objects.get(id=id)
        users.name = request.POST['name']
        users.email = request.POST['email']
        users.phone = request.POST['phone']
        users.address = request.POST['address']
        users.gender=request.POST['gender']
        users.save()
        # User.objects.update(name=users.name, email=users.email, phone=users.phone, address=users.address, gender=users.gender)
        messages.success(request, 'record updated successfully')
        # back=request.META['HTTP_REFERER']
        return redirect('/')
    else:
        context={
            'users': User.objects.get(id=id)
        }
        return render(request, 'edit.html', context)


