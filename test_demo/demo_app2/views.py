from django.shortcuts import render , redirect
from datetime import datetime
from demo_app2.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate ,login
#user name mubarak password Muba@123

from django.http import HttpResponse
# Create your views here.
def home(request):
    return render (request,"home.html")

def index(request):
    return render (request,"index.html")    

def about(request):
    return render(request,'about.html')

def service(request):
    return HttpResponse("hello service")

def bounding(request):
    return HttpResponse("hello contact")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been sent!!")
    return render(request,'contact.html')




def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check if user has entered correct credentials
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request ,user)
            return redirect("/file")
        else:
            return render(request,'login.html')
    return render(request,'login.html')


def logout(request):
    logout(request)
    return redirect('/login')



import PyPDF2
from django.http import FileResponse, Http404
import cv2 
from pytesseract import pytesseract
from pytesseract import Output
#from bounding_box import bound
from django.core.files.storage import FileSystemStorage



def pdf_get(request):
    # file=FileResponse(open("python-guide.pdf",'rb'), content_type='application/pdf')
   #a=PyPDF2.PdfFileReader(request.FILES["myfile"])
    
    a=PyPDF2.PdfFileReader("python-guide.pdf")
    #find the page numbers
    c=a.getNumPages()
    print(c)
    str1=''
    #pdf file extracting in to Text 
    for i in range(10,21):
        str1+=a.getPage(i).extractText()
        line=str1.splitlines()

    return render(request,"pdf_viewer.html",{'str1':line,'c':c})
    #return HttpResponse(str)
   

import fitz
def bound_box(request):
    filepath="sim_pdf.pdf"
    p=fitz.open(filepath)
    NumPages=p.pageCount
    patterns="you can"
    for i in range(0,NumPages):
        PageObj=p.load_page(i)
        r1=PageObj.search_for(patterns)
        for area in r1:
            if isinstance(area,fitz.fitz.Rect):
                annot=PageObj.addRectAnnot(area)
                annot.setColors(stroke=fitz.utils.getColor('red'))
        p.save("test_demo\static\super.pdf")
    return render(request,"bound.html")



def upload(request):
    context={}
    #requesting files from base.html
    if request.method=='POST':
        upload_file=request.FILES['document']
        #storing in Systemstorage
        fs=FileSystemStorage()
        name=fs.save(upload_file.name,upload_file)
        context['url']=fs.url(name)
        #print(upload_file.name)
        #print("filesize=",upload_file.size)
    return render(request,"upload.html",context)














'''

def bounding(request):
    
    pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    img = cv2.imread("sim_pdf-1.png")
    # image data in to dict object
    image_data = pytesseract.image_to_data(img, output_type=Output.DICT)

    # Printing each word
    # for word in image_data['text']:
    # 	print(word)

    for i, word in enumerate(image_data['text']):
	    if word != '':
		    x,y,w,h = image_data['left'][i],image_data['top'][i],image_data['width'][i],image_data['height'][i]
		    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
		    #cv2.putText(img,word,(x,y-16),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

    cv2.imshow("window", img)
    cv2.waitKey(0)
    #return render(request,"index.html")
bounding

'''