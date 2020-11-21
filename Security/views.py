from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def homepage(request):
	error = ""
	if request.method == 'POST':
		u = request.POST['username']
		p = request.POST['password']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error = "yes"
	d = {'error' : error}
	return render(request,'index.html',d)

def otp_page(request):
	return render(request,'otp_page.html')

def Logout(request):
	if not request.user.is_staff:
		return redirect('homepage')
	logout(request)
	return redirect('homepage')

def dashboard(request):
	return render(request,'dashboard.html')