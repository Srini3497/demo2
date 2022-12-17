from django.shortcuts import render, HttpResponse
from .models import FileForm
# Create your views here.
def home(req):
    if req.method == "GET":
        return render(req, 'index.html', {'form': FileForm()})
    elif req.method == "POST":
        frm = FileForm(req.POST, req.FILES)
        frm.save()
        return HttpResponse("Uploaded file")