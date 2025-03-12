from django.db import models # type: ignore

# Create your models here.

class Players(models.Model):
    
    img = models.ImageField(upload_to='players/', blank=True, null=True)    
    name = models.CharField(max_length=30) 

    club = models.ImageField(upload_to='club_img/', blank=True, null=True)

    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    # club = models.ImageField(upload_to='players/', null=True, blank=True)    
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class TeamStanding(models.Model):
    img = models.ImageField(upload_to='club_img/', blank=True, null=True)
    team_name = models.CharField(max_length=100, unique=True)
    matches_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    loss = models.PositiveIntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name
    


class BengaluruTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='beng_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class ChennaiTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='chen_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class EastBengalTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='eb_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class GoaTeamPlayers(models.Model):

    img = models.ImageField(upload_to='goa_pl/', blank=True, null=True)   
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class HyderabadTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='hyd_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name

class JamshedpurTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='jams_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class KeralaTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='ker_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class MohammedanTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='moha_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name

class MohunBaganTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='mohu_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name

class MumbaiTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='mum_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class NorthEastTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='ne_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class OdishaTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='odis_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    
class PunjabTeamPlayers(models.Model):
    
    img = models.ImageField(upload_to='punj_pl/', blank=True, null=True)    
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    mathch = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.name
    

