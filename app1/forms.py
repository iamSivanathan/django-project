from django import forms # type: ignore
from .models import Players,TeamStanding,BengaluruTeamPlayers,ChennaiTeamPlayers,EastBengalTeamPlayers,GoaTeamPlayers,HyderabadTeamPlayers,JamshedpurTeamPlayers,KeralaTeamPlayers,MohammedanTeamPlayers,MohunBaganTeamPlayers,MumbaiTeamPlayers,NorthEastTeamPlayers,OdishaTeamPlayers,PunjabTeamPlayers

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = '__all__'


class TeamStandingForm(forms.ModelForm):
    class Meta:
        model = TeamStanding
        fields = ['team_name', 'matches_played', 'wins', 'draws', 'loss','points']

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

