from django.shortcuts import render, redirect, HttpResponse
from .models import Employee, Department, Role
from django.db.models import Q

# Create your views here.

# function for dashboard


def index(request):
    return render(request, 'index.html')


# for view all emp details
def allEmp(request):
    data = Employee.objects.all()
    context = {'data': data, 'tot': len(data)}
    return render(request, 'allEmp.html', context)


# find specific emp details
def findEmp(request):
    emps = Employee.objects.all()
    if request.method == 'POST':
        empFilters = request.POST['empid']
        # print(empFilters)

        try:
            empFilters = int(empFilters)
            print(type(empFilters))
            data = emps.filter(id=empFilters)
            context = {'data': data}
            # return render(request, 'findEmp.html', context)

        except:
            data = emps.filter(Q(firstName__icontains=empFilters) | Q(
                lastName__icontains=empFilters) | Q(dept__name__icontains=empFilters))
            context = {'data': data}
    else:
        context = {'data': emps}
    return render(request, 'findEmp.html', context)


# add emp details to db
def addEmp(request):
    if request.method == 'POST':
        firstname = (request.POST['first']).capitalize()
        lastname = (request.POST['last']).capitalize()
        phone = int(request.POST['phone'])
        jd = request.POST['date']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])

        # print(f"{firstname}\n{lastname}\n{phone}\n{jd}\n{salary}\n{bonus}\n{dept}\n{role}")
        newEmp = Employee(firstName=firstname, lastName=lastname, phone=phone,
                          salary=salary, bonus=bonus, hireDate=jd, dept=Department.objects.get(id=dept), role=Role.objects.get(id=role))
        newEmp.save()
        context = {'data': 1}
        return render(request, 'addEmp.html', context)

    return render(request, 'addEmp.html')


# remove emp details from db
def rmEmp(request):
    emps = Employee.objects.all()
    if request.method == 'POST':
        empFilters = request.POST['empid']
        # print(empFilters)

        try:
            empFilters = int(empFilters)
            print(type(empFilters))
            data = emps.filter(id=empFilters)
            context = {'data': data}
            # return render(request, 'findEmp.html', context)

        except:
            data = emps.filter(Q(firstName__icontains=empFilters) | Q(
                lastName__icontains=empFilters) | Q(dept__name__icontains=empFilters))
            context = {'data': data}
    else:
        context = {'data': emps}
    return render(request, 'rmEmp.html', context)


# for update data
def updEmp(request, pk, status):
    # print(f'key {pk}')
    # print(data.firstName)
    data = Employee.objects.get(id=pk)
    context = {}
    if status == 0:
        context = {'data': data}
    elif status == 1:
        context = {'data': data, 'status': status}
    else:
        pass
    return render(request, 'updateEmp.html', context)


# for delete datas
def delEmp(request, uid):
    print(uid)
    data = Employee.objects.get(id=uid)
    data.delete()
    return redirect(allEmp)


# for update data
def dataUpEmp(request, id):
    # print(id)
    if request.method == 'POST':
        data = Employee.objects.get(id=id)
        # print(data.firstName, data.lastName)
        firstName = (request.POST['first']).capitalize()
        lastName = (request.POST['last']).capitalize()
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])

        data.firstName = firstName
        data.lastName = lastName
        data.phone = phone
        data.salary = salary
        data.bonus = bonus
        data.dept = Department.objects.get(id=dept)
        data.role = Role.objects.get(id=role)

        data.save()
        # print(f'{firstName}\n{lastName}\n{phone}\n{salary}\n{bonus}\n{dept}\n{role}')
        return redirect(updEmp, pk=id, status=1)
    else:
        return redirect(updEmp, pk=id, status=0)
