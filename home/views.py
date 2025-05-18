from bn_india.includes import * 

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

@csrf_exempt
def office_login(request):
    if request.method == "POST":
        number=request.POST ['mobile']
        pin=request.POST ['pin']
        c= Office_employee.objects.filter(mobile=number,pin=pin,status=1)
        if c:
            request.session['office_mobile'] = request.POST["mobile"]
            return redirect('office_home')
        else:
            messages.error(request,f"Mobile Number or Secret Pin invalid.")
            return redirect('/office_login/')
    return render(request, 'home/office_login.html')