from django.contrib import admin # type: ignore
from .models import Players,TeamStanding,BengaluruTeamPlayers,ChennaiTeamPlayers,EastBengalTeamPlayers,GoaTeamPlayers,HyderabadTeamPlayers,JamshedpurTeamPlayers,KeralaTeamPlayers,MohammedanTeamPlayers,MohunBaganTeamPlayers,MumbaiTeamPlayers,NorthEastTeamPlayers,OdishaTeamPlayers,PunjabTeamPlayers

# Register your models here.
class PlayersAdmin(admin.ModelAdmin):
    list_display='name','position','mathch','goal',
admin.site.register(Players,PlayersAdmin)

class StandingAdmin(admin.ModelAdmin):
    list_display= 'team_name', 'matches_played', 'wins', 'draws', 'loss'
admin.site.register(TeamStanding,StandingAdmin)

class TeamPlayersAdmin(admin.ModelAdmin):
    list_display='name','position','mathch','goal',
admin.site.register(BengaluruTeamPlayers,TeamPlayersAdmin)
admin.site.register(ChennaiTeamPlayers,TeamPlayersAdmin)
admin.site.register(EastBengalTeamPlayers,TeamPlayersAdmin)
admin.site.register(GoaTeamPlayers,TeamPlayersAdmin)
admin.site.register(HyderabadTeamPlayers,TeamPlayersAdmin)
admin.site.register(JamshedpurTeamPlayers,TeamPlayersAdmin)
admin.site.register(KeralaTeamPlayers,TeamPlayersAdmin)
admin.site.register(MohammedanTeamPlayers,TeamPlayersAdmin)
admin.site.register(MohunBaganTeamPlayers,TeamPlayersAdmin)
admin.site.register(MumbaiTeamPlayers,TeamPlayersAdmin)
admin.site.register(NorthEastTeamPlayers,TeamPlayersAdmin)
admin.site.register(OdishaTeamPlayers,TeamPlayersAdmin)
admin.site.register(PunjabTeamPlayers,TeamPlayersAdmin)





