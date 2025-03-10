from django.db import models # type: ignore

# Create your models here.

class Players(models.Model):
    # image = models.ImageField(upload_to='players/', null=True, blank=True)
    name = models.CharField(max_length=30)    
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
    team_name = models.CharField(max_length=100, unique=True)
    matches_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    loss = models.PositiveIntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name
    


class BengaluruTeamPlayers(models.Model):
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
    

