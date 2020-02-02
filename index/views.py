from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from .models import *
import random
import string

# Create your views here.
def home(request):
    print("Home")
    return render(request, 'index/index.html')

def user_login(request):
    print("User Authentication")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('user-home')
    else:
        return redirect('index-home')

def user_home(request):
    return render(request, 'index/home.html')

def claim_age(request):
    print("Claim Age")
    r_value = id_generator()
    print("R: ", r_value)
    u1 = user_veri(name=request.user.username, veri_code=r_value)
    u1.save()
    return render(request, 'index/claim_age.html', {'r_value' : r_value})

def claim_address(request):
    print("Claim Address")
    r_value = id_generator()
    print("R: ", r_value)
    u1 = user_veri(name=request.user.username, veri_code=r_value)
    u1.save()
    return render(request, 'index/claim_address.html', {'r_value' : r_value})

def claim_degree(request):
    print("Claim Degree")
    r_value = id_generator()
    print("R: ", r_value)
    u1 = user_veri(name=request.user.username, veri_code=r_value)
    u1.save()
    return render(request, 'index/claim_degree.html', {'r_value' : r_value})

def verify_age(request, info):
    print("Verify Age")
    print("Age Request ID: ", info)
    age_veri = user_veri.objects.filter(veri_code__exact=info)
    if age_veri:
        return render(request, 'index/verify_info.html',{'title' : 'Age Verification', 'title1' : 'His Age is 21 Years', 'id' : info})
    else:
        return render(request, 'index/verify_info.html',{'title' : 'Age Verification', 'title1' : 'Verification Failed', 'id' : info, 'icon' : 'cross'})

def verify_address(request, info):
    print("Verify Address")
    print("Address Request ID: ", info)
    add_veri = user_veri.objects.filter(veri_code__exact=info)
    if add_veri:
        return render(request, 'index/verify_info.html',{'title' : 'Address Verification', 'title1' : 'Address Verification Sucessful', 'id' : info})
    else:
        return render(request, 'index/verify_info.html',{'title' : 'Address Verification', 'title1' : 'Address Verification UnSucessful', 'id' : info, 'icon' : 'cross'})

def verify_degree(request, info):
    print("Verify Degree")
    print("Degree Request ID: ", info)
    deg_veri = user_veri.objects.filter(veri_code__exact=info)
    if deg_veri:
        return render(request, 'index/verify_info.html', {'title' : 'Degree Verification', 'title1' : 'Degree Verification Sucessful', 'id' : info, 'type': 'degree'})
    else:
        return render(request, 'index/verify_info.html', {'title' : 'Degree Verification', 'title1' : 'Degree Verification Failed', 'id' : info, 'icon' : 'cross'})

def add_documents(request):
    return render(request, 'index/add_documents.html')

def add_documents_confirm(request):
    print("Add documents confirm")
    if request.method == 'POST' and request.FILES['file_name']:
        myfile = request.FILES['file_name']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        u1 = user_data(name=request.user.username, file_name=filename, file_hash='qwerty')
        u1.save()
        return render(request, 'index/add_documents.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'index/add_documents.html')


def view_documents(request):
    return render(request, 'index/view_documents.html')

def id_generator(size=60, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def view_university(request):
    return render(request, 'index/university.html')