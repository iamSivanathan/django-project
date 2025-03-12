from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse
from .models import Players,TeamStanding,BengaluruTeamPlayers,ChennaiTeamPlayers,EastBengalTeamPlayers,GoaTeamPlayers,HyderabadTeamPlayers,JamshedpurTeamPlayers,KeralaTeamPlayers,MohammedanTeamPlayers,MohunBaganTeamPlayers,MumbaiTeamPlayers,NorthEastTeamPlayers,OdishaTeamPlayers,PunjabTeamPlayers

from .forms import PlayerForm, TeamStandingForm

from django.contrib.auth import authenticate, login, logout   #login
from django.contrib import messages

from django.contrib.auth.models import User  #register
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')


# teams
def team(request):
    return render(request,'team.html')

# clubs
def beng(request):
    pl = BengaluruTeamPlayers.objects.all()
    return render(request,'clubs/beng.html',{'pl':pl})

def chen(request):
    pl = ChennaiTeamPlayers.objects.all()
    return render(request,'clubs/chen.html',{'pl':pl})

def e_beng(request):
    pl = EastBengalTeamPlayers.objects.all()
    return render(request,'clubs/eastbeng.html',{'pl':pl})

def goa(request):
    pl = GoaTeamPlayers.objects.all()
    return render(request,'clubs/goa.html',{'pl':pl})

def hyd(request):
    pl = HyderabadTeamPlayers.objects.all()
    return render(request,'clubs/hyd.html',{'pl':pl})

def jams(request):
    pl = JamshedpurTeamPlayers.objects.all()
    return render(request,'clubs/jams.html',{'pl':pl})

def kerala(request):
    pl = KeralaTeamPlayers.objects.all()
    return render(request,'clubs/kerala.html',{'pl':pl})

def moham(request):
    pl = MohammedanTeamPlayers.objects.all()
    return render(request,'clubs/moham.html',{'pl':pl})


def mohun(request):
    pl = MohunBaganTeamPlayers.objects.all()
    return render(request,'clubs/mohun.html',{'pl':pl})

def mumbai(request):
    pl = MumbaiTeamPlayers.objects.all()
    return render(request,'clubs/mumbai.html',{'pl':pl})

def NE(request):
    pl = NorthEastTeamPlayers.objects.all()
    return render(request,'clubs/NE.html',{'pl':pl})

def odis(request):
    pl = OdishaTeamPlayers.objects.all()
    return render(request,'clubs/odis.html',{'pl':pl})

def punj(request):
    pl = PunjabTeamPlayers.objects.all()
    return render(request,'clubs/punj.html',{'pl':pl})

# standing
def standing(request):  
    ts = TeamStanding.objects.all()
    return render(request, 'standing.html', {'ts': ts})


# adds new team in standing table
def standadd(request):
    sform = TeamStandingForm()
    if request.method == 'POST':
        sform = TeamStandingForm(request.POST, request.FILES)
        if sform.is_valid():
            sform.save()
            return redirect('standing')
        else:
            sform = TeamStandingForm()        
    return render(request,'standadd.html',{'sform':sform})

# update team in standing table
def standform(request, pk):
    team = TeamStanding.objects.get(id=pk)
    sform = TeamStandingForm(instance=team)
    if request.method == "POST":
        sform = TeamStandingForm(request.POST, instance=team)
        if sform.is_valid():
            sform.save()
            return redirect('standing')
        return render(request,'standform.html',{'sform':sform})
    
    else:
        sform = TeamStandingForm(instance=team)  
    return render(request, 'standform.html', {'sform': sform})


# players

def player(request):
    pl=Players.objects.all()
    return render(request,'player.html',{'pl':pl})

def add(request):
    pform = PlayerForm()

    if request.method == 'POST':
        pform = PlayerForm(request.POST)
        if pform.is_valid():
            pform.save()
            return redirect('player')   
        else:
            pform = PlayerForm()     
    return render(request,'add.html',{'pform':pform})

def update(request,pk):
    upd= Players.objects.get(id=pk)
    pform = PlayerForm(instance=upd)
    if request.method == 'POST':
        pform = PlayerForm(request.POST,instance=upd)    
        if pform.is_valid():
            pform.save()
            return redirect('player')
    return render(request,'update.html',{"pform":pform})    

    # else:
    #     pform = PlayerForm(instance=upd)
    # return render(request,'update.html',{'pform':pform})


def remove(request,pk):
    upd = Players.objects.get(id=pk)
    if request.method == 'POST':
        upd.delete()
        return redirect('player')
    return render(request,'remove.html',{'upd':upd})


def contact(request):
    return render(request,'contact.html')


# login
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to homepage or dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

# register

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  # Redirect to your login page
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})