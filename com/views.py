
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature, Features
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
       feature1=Feature()
       feature1.id= 10
       feature1.name= "Nuparam ---> Fast"
       feature1.is_true= True 
       feature1.details="Nuparam is a good person for helping the others"

       feature2=Feature()
       feature2.id= 20
       feature2.name= "Rajendra Prasad --> Reliable"
       feature2.is_true= True 
       feature2.details="Rajendra Prasad is a good person for helping the others. And he is very short temperred person"

       feature3=Feature()
       feature3.id= 30
       feature3.name= "Daulat Singh   --> Affordable"
       feature3.is_true= False
       feature3.details="Daula Singh is a good person for helping the others. He is very gentle person"

       feature4=Feature()
       feature4.id= 40
       feature4.name= "Gulab Singh   ---> Very Colstly"
       feature4.is_true= True 
       feature4.details="Gulab Singh is not a good person. He is very selfish in nature and always fight to other"

       feature5=Feature()
       feature5.id= 50
       feature5.name= "Dhyan Singh   ---> Trust Worthy"
       feature4.is_true= True 
       feature5.details="Dhyan Singh is very a very nice person. He is very kind and helpfull in nature and always try to solve the others problem"
       # this is for the for loop in the HTML index file 
       feature6 = [feature1, feature2, feature3, feature4, feature5]

       # this is for database connectivities call for features
       feature7 = Features.objects.all()

      # return render(request,'index.html',{'features': features})

       return render(request,'index.html',{'feature1': feature1,'feature2': feature2,'feature3': feature3,'feature4': feature4,'feature7': feature7,'feature6' : feature6})


def index1(request): 
       return render(request,'index1.html')  

def register(request) :
      if request.method == 'POST' :
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          password1 = request.POST['password1']
          
          if password == password1 :
              if User.objects.filter(email = email).exists() :
                  messages.info(request, 'Email already exists')
                  return redirect('register')
              
              elif User.objects.filter(username = username).exists() :
                  messages.info(request, 'Username already exists')
                  return redirect('register')
              else:
                  user = User.objects.create_user(username = username, email = email, password = password)
                  user.save()
                  return redirect('login')
          else:
             messages.info(request,'password do not match')
             return redirect('register')
      else:
        return render(request,'register.html')
      
      
def login(request):
     if request.method == 'POST' :
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(username = username, password = password)
          
          if user is not None :
              auth.login(request, user)
              return redirect('/')
          else:
              messages.info(request, " Credential is Invalid")
              return redirect('login')
     else:
            return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk) :
    return render(request, 'post.html', {'pk' : pk})


def counter(request):
    posts = [ 1, 2, 3, 4, 5, 'tim', 'tom', 'johan']
    return render(request, 'counter.html', {'posts': posts})
