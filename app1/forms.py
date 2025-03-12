from django import forms # type: ignore
from .models import Players,TeamStanding,BengaluruTeamPlayers,ChennaiTeamPlayers,EastBengalTeamPlayers,GoaTeamPlayers,HyderabadTeamPlayers,JamshedpurTeamPlayers,KeralaTeamPlayers,MohammedanTeamPlayers,MohunBaganTeamPlayers,MumbaiTeamPlayers,NorthEastTeamPlayers,OdishaTeamPlayers,PunjabTeamPlayers
from django.contrib.auth.models import User


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = '__all__'


class TeamStandingForm(forms.ModelForm):
    class Meta:
        model = TeamStanding
        fields = ['img','team_name', 'matches_played', 'wins', 'draws', 'loss','points']

class TeamPlayersForm(forms.ModelForm):
    class Meta:
        model = BengaluruTeamPlayers
        model = ChennaiTeamPlayers
        model = EastBengalTeamPlayers
        model = GoaTeamPlayers
        model = HyderabadTeamPlayers
        model = JamshedpurTeamPlayers
        model = KeralaTeamPlayers
        model = MohammedanTeamPlayers
        model = MohunBaganTeamPlayers
        model = MumbaiTeamPlayers
        model = NorthEastTeamPlayers
        model = OdishaTeamPlayers
        model = PunjabTeamPlayers

        fields = '__all__'



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
