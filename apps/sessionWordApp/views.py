from django.shortcuts import render,redirect
from time import gmtime, strftime

# Create your views here.
def index(request):

    return render(request,"sessionWordApp/index.html")
def new(request):
    if 'words' not in request.session:
        request.session['words'] = []
    if request.method == "POST":
        request.session['word']=request.POST['word']
        request.session['color']=request.POST['color']
    if 'font' not in request.POST:
        font = 'small'
    else:
        font = 'big'
    templist = request.session['words']
    templist.append({
        'word': request.POST['word'],
        'color': request.POST['color'],
        'font':font,
        'time': strftime("%I:%M:%S %p, %B %d %Y", gmtime())
    })
    request.session['words'] = templist
    return redirect("/")
