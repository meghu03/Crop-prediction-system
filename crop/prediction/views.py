from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from .models import cropdata

# Create your views here.
def index(request):
    return render(request,"index.html") 

def about(request):
    return render(request,"about.html")
    
def register(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist !!')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already exist !!')
                return render(request,'register.html')
            else:

                #save data in db
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('user created ')
                return redirect('login')

        else:
            messages.info(request, 'Invalid Credentials !!')
            return render(request,'register.html')
        return redirect('/')
    else:
        return render(request, 'register.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'crop.html')
        else:
            messages.info(request,'Invalid credentials !!')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def crop(request):
    return render(request,"crop.html")  

def predict(request):
    if request.method=="POST":
        p=int(request.POST["phos"])
        n=int(request.POST["nitro"])
        k=int(request.POST["potas"])
        t=float(request.POST["temp"])
        h=float(request.POST["humid"])
        ph=float(request.POST["ph"])
        r=float(request.POST["rain"]) 
        import pandas as pd 
        df=pd.read_csv(r"static/crop.csv")
        print(df.dropna(inplace=True))
        X_train=df[["N","P","K","temperature","humidity","ph","rainfall"]]
        y_train=df["label"]
        from sklearn.linear_model import LogisticRegression
        log=LogisticRegression()
        log.fit(X_train,y_train)
        pred=log.predict([[p,n,k,t,h,ph,r]])
        from .models import cropdata
        c=cropdata.objects.create(N=n,P=p,K=k,temperature=t,humidity=h,ph=ph,rainfall=r,label=pred)
        c.save()
    return render(request,"predict.html",{"p":p,"n":n,"k":k,"t":t,"h":h,"ph":ph,"r":r,"pred":pred})

def team(request):
    return render(request,"team.html")

def contact(request):
    return render(request,"contact.html")
