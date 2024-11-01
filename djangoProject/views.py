from django.shortcuts import render
from contact_us.models import Footer,Message
from resume_app.models import Project, RequestedProject


def home(request):
    if request.method == 'POST' and 'fname' in request.POST:
        fname = request.POST['fname']
        email = request.POST['email']
        sub = request.POST['sub']
        body = request.POST['body']
        Message.objects.create(fname=fname, email=email, subject=sub, body=body)
    elif request.method == 'POST' and 'name' in request.POST :
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['topic']
        body = request.POST['body']
        RequestedProject.objects.create(name=name, email=email, description=description, body=body)

    projects = Project.objects.all()
    footer = Footer.objects.all().last()
    return render(request,'index.html',context={'projects':projects,'footer':footer})
