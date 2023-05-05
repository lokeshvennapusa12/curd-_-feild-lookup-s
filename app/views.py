from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from app.models import *

def Insert_Dept(request):
    deno=input('Enter dept name: ')
    dn=input('Enter dname: ')
    lo=input('Enter location: ')
    DO=Dept.objects.get_or_create(deptno=deno,dname=dn,loc=lo)[0]
    DO.save()
    return HttpResponse('Dept data updated')

def Display_Dept(request):
    LOD=Dept.objects.all()
    d={'dept':LOD}
    return render(request,'Display_Dept.html',context=d)



def Insert_Emp(request):
    enu=input('Enter empno: ')
    ena=input('Enter ename: ')
    j=input('Enter job: ')
    mg=input('Enter mgr: ')
    hd=input('Enter hire date: ')
    sa=input('Enter sal: ')
    com=input('Enter comm: ')
    deno=input('Enter deptno: ')
    dn=input('Enter dname: ')
    lo=input('Enter location: ')
    DO=Dept.objects.get_or_create(deptno=deno,dname=dn,loc=lo)[0]
    DO.save()
    EO=Emp.objects.get_or_create(empno=enu,ename=ena,job=j,mgr=mg,hiredate=hd,sal=sa,comm=com,deptno=DO)[0]
    EO.save()
    return HttpResponse('Employee data updated')

def display_emp(request):
    LOE=Emp.objects.all()

    # LOE=Emp.objects.get(hiredate__month='5')

    LOE=Emp.objects.exclude(hiredate__month='5')
    
    # Feeld lookups

    LOE=Emp.objects.filter(hiredate__gt='1981-02-11')
    LOE=Emp.objects.filter(hiredate__gte='1980-02-11')
    LOE=Emp.objects.filter(hiredate__lt='1981-02-11')
    LOE=Emp.objects.filter(hiredate__lte='1981-12-11')


    LOE=Emp.objects.filter(hiredate__year='1981')
    LOE=Emp.objects.filter(hiredate__month='9')
    LOE=Emp.objects.filter(hiredate__day='17')

    
    LOE=Emp.objects.filter(ename__startswith='a')
    LOE=Emp.objects.filter(ename__endswith='n')
    LOE=Emp.objects.filter(ename__contains='l')
    

    LOE=Emp.objects.filter(Q(hiredate__year__gt='1980') & Q(hiredate__month__gt='02'))
    LOE=Emp.objects.all()

    # Feeld Lookups

    LOE=Emp.objects.filter(ename='Ford').delete()
    LOE=Emp.objects.filter(ename='Ward').delete()
    LOE=Emp.objects.all()
     
    

    d={'employee':LOE}
    return render(request,'display_emp.html',context=d)

def update_emp(request):
    Emp.objects.all()
    Emp.objects.filter(ename='Allen').update(job='Sales')
    Emp.objects.filter(ename='Allen').update(hiredate='1986-09-28')
    Emp.objects.filter(job='clerk').update(sal=2000)
    Emp.objects.filter(ename='James').update(sal=1200)
    Emp.objects.filter(ename='Miller').update(comm=-200)
    Emp.objects.all().update(comm=0)
    Emp.objects.filter(ename='Allen').update(job='Salesman')
    Emp.objects.filter(job='manager').update(job='Manager')
    Emp.objects.filter(job='salesman').update(job='Salesman')
    Emp.objects.filter(job='clerk').update(job='Clerk')
    Emp.objects.filter(job='analyst').update(job='Analyst')
    Emp.objects.filter(job='president').update(job='President')
    Emp.objects.all()
    Emp.objects.update_or_create(empno=7935,defaults={'ename':'Siva'})
    Emp.objects.update_or_create(empno=7900,defaults={'ename':'Bhupal'})


    
    d={'employee':Emp.objects.all()} 

    return render(request,'display_emp.html',context=d)

def Delete_emp(request):
    Emp.objects.all()
    Emp.objects.filter(ename='Bhupal').delete()
    Emp.objects.filter(empno=7935).delete()
    Emp.objects.filter(empno=7867).delete()
    Emp.objects.filter(ename='Suresh').delete()

    d={'employee':Emp.objects.all()} 
    return render(request,'display_emp.html',context=d)



    