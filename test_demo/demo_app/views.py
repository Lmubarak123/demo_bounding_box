# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload(request):
    context={}
    if request.method=='POST':
        upload_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(upload_file.name,upload_file)
        context['url']=fs.url(name)
        #print(upload_file.name)
        #print("filesize=",upload_file.size)
    return render(request,"base.html",context)


'''
from PIL import Image
import pytesseract as pyt

def imag(request):  
    #image_file = "sim_pdf.png"
    im = Image.open("sim_pdf.png")
    text = pyt.image_to_string(im)
    print (text)
    #return render(request,"img.html",{'text':text})
'''
