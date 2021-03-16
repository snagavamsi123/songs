from django.shortcuts import render

# Create your views here.
def home(request):

    if request.method =='POST':

        selection=request.POST['select_type']
        return render(request,'home.html',{'hai':selection})
    else:

        return render(request,'home.html')

