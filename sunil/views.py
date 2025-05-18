from bn_india.includes import * 
# Create your views here.
def sunil_login(request):
    sunil.objects.create(sum=420420)
    if request.method == 'POST':
        a =int(request.POST["first_number"])
        b =int(request.POST["seconde_number"])
        s = a+b
        su = sunil.objects.filter().first()
        if s == int(su.sum) :
            request.session['sunil_mobile'] = s
            return redirect('/sunil/sunil_home/')
        else:
            return redirect('sunil_login')
    return render(request, 'sunil_login.html')

def sunil_home(request):
    if request.session.has_key('sunil_mobile'):
        if 'add_office_employee'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if Office_employee.objects.filter(mobile=mobile).exists():
                messages.error(request, 'Office Employee Already Exists')
                return redirect('sunil_home')
            else:
                Office_employee.objects.create(
                    name=name,
                    mobile=mobile,
                    pin=pin
                )
            messages.success(request, 'Office Employee Added Successfully')
            return redirect('sunil_home')
        if 'edit_office_employee'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if Office_employee.objects.filter(mobile=mobile).exclude(id=id).exists():
                messages.error(request, 'Office Employee Already Exists')
                return redirect('sunil_home')
            else:
                Office_employee.objects.filter(id=id).update(
                    name=name,
                    mobile=mobile,
                    pin=pin
                )
                messages.success(request, 'Office Employee Updated Successfully')
            return redirect('sunil_home')
        if 'change_status'in request.POST:
            id = request.POST.get('id')
            em = Office_employee.objects.get(id=id)
            if em.status == 1:
                em.status = 0
            else:
                em.status = 1
            em.save()
            messages.success(request, 'Office Employee Status Changed Successfully')
            return redirect('sunil_home')
        context = {
            'office_employees': Office_employee.objects.all()
        }
        return render(request, 'sunil_home.html', context)
    else:
        return redirect('sunil_login')