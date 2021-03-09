from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

def insert_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'insert.html',{'form':form})

def show_view(request):
    students=Student.objects.all()
    return render(request,'show.html',{'students':students})

def delete_view(request,id):
    students=Student.objects.get(id=id)
    students.delete()
    return redirect('/')

def update_view(request,id):
    students = Student.objects.get(id = id)
    form =StudentForm(request.POST,instance=students)
    if form.is_valid():
        form.save(commit=True)
        return redirect('/')
    return render(request,'update.html',{'students':students})