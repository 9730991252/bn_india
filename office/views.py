from bn_india.includes import * 

# Create your views here.
def office_home(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            messages.success(request, 'Welcome to BN India!')
        else:
            return redirect('office_login')
        context={
            'e':e
        }
        return render(request, 'office/office_home.html', context)
    else:
        return redirect('office_login')
    
def add_member(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            pass
        else:
            return redirect('office_login')
        context={
            'e':e
        }
        return render(request, 'office/add_member.html', context)
    else:
        return redirect('office_login')
    
def add_group(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            pass
        else:
            return redirect('office_login')
        context={
            'e':e
        }
        return render(request, 'office/add_group.html', context)
    else:
        return redirect('office_login')
    
    
def add_office_employee(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        
        
        e = Office_employee.objects.filter(mobile=mobile).first()
        if e:
            if 'add_office_employee'in request.POST:
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                if Office_employee.objects.filter(mobile=mobile).exists():
                    messages.error(request, 'Office Employee Already Exists')
                    return redirect('add_office_employee')
                else:
                    Office_employee.objects.create(
                        name=name,
                        mobile=mobile,
                        pin=pin
                    )
                messages.success(request, 'Office Employee Added Successfully')
                return redirect('add_office_employee')
            if 'edit_office_employee'in request.POST:
                id = request.POST.get('id')
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                pin = request.POST.get('pin')
                if Office_employee.objects.filter(mobile=mobile).exclude(id=id).exists():
                    messages.error(request, 'Office Employee Already Exists')
                    return redirect('add_office_employee')
                else:
                    Office_employee.objects.filter(id=id).update(
                        name=name,
                        mobile=mobile,
                        pin=pin
                    )
                    if id == e.id:
                        s =  Session.objects.all()
                        for session in s:
                            data = session.get_decoded()
                            if data.get('office_mobile') == e.mobile:
                                Session.objects.filter(session_key=session.session_key).delete()
                    messages.success(request, 'Office Employee Updated Successfully')
                return redirect('add_office_employee')
            if 'change_status'in request.POST:
                id = request.POST.get('id')
                em = Office_employee.objects.get(id=id)
                if em.status == 1:
                    em.status = 0
                else:
                    em.status = 1
                em.save()
                messages.success(request, 'Office Employee Status Changed Successfully')
                return redirect('add_office_employee')
        else:
            return redirect('office_login')
        context={
            'e':e,
            'office_employees': Office_employee.objects.all()

        }
        return render(request, 'office/add_office_employee.html', context)
    else:
        return redirect('office_login')