from django.shortcuts import render,redirect
from django.contrib import auth,messages
from .models import(
    Details
)
from .froms import(
    DetailsForm
)
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/')
def dash(request):
    details1=0
    details1 =  Details.objects.filter(user=request.user)[0].agreement
    print('Dett   ',details1)




    details = Details.objects.get(user=request.user)
    detailsForm = DetailsForm(instance=details)  

    if request.method == 'POST':
        form = DetailsForm(request.POST, instance=details)
        if form.is_valid():
            form1 = form.save(commit = False)
            form1.agreement = True
            form1.save()
            print(form.instance)
            return redirect('/review/')
    
    return render(request,"dash.html",{'form':detailsForm})

@login_required(login_url='/')
def review(request):
    details =  Details.objects.filter(user=request.user)[0]
    
    if request.method == "POST":
        auth.logout(request)
        return redirect ('/')
    
    if details.agreement == 0:
        
        text = 'Something wrong :( contact team ASAP!'
    else:
        text = 'Verified Succesfully ;)'
    
        
    context= {
        'name':details.name,
        'regis':details.regis,
        'email':request.user.username,
        'phone':details.phone,
        'block':details.block,
        'agree':text
    }
    return render(request,'review.html',context)

def home(request):
    
    if request.method == "POST":
        
        username = request.POST['email']
        password =  request.POST['password']

        print(password)
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            try:
                details = Details.objects.filter(user=request.user)[0].agreement
                print(details)
                if details == 1:
                    print("LOGIN SUCCESS")
                    return redirect('review/')
                else:
                    print('Dash')
                    return redirect('dash/')
            except:
                pass
                
        else:
            messages.success(request, "Wrong Credentials")
            return redirect('/')
    return render(request,'index.html')

