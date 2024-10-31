from django.shortcuts import render
from contact_us.models import Footer,Message
from resume_app.models import Project



def home(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        sub = request.POST['sub']
        body = request.POST['body']
        Message.objects.create(fname=fname, email=email, subject=sub, body=body)

    projects = Project.objects.all()
    footer = Footer.objects.all().last()
    return render(request,'index.html',context={'projects':projects,'footer':footer})
