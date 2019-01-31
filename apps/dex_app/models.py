from django.db import models



# Create your models here.
class Abilities(models.Model):
    name = models.CharField(max_length=25)
    effect = models.CharField(max_length=255)

class Types(models.Model):
    tipe = models.CharField(max_length=15)

class Damage_Relationships(models.Model):
    tipe = models.ForeignKey(Types, related_name='damage_relationship')
    double_from = models.ManyToManyField(Types, related_name='double_to')
    double_to = models.ManyToManyField(Types, related_name='double_from')
    half_from = models.ManyToManyField(Types, related_name='half_to')
    half_to = models.ManyToManyField(Types, related_name='half_from')
    none_from = models.ManyToManyField(Types, related_name='none_to')
    none_to = models.ManyToManyField(Types, related_name='nome_from')

class Damage_Types(models.Model):
    name = models.CharField(max_length=25)

class Moves(models.Model):
    name = models.CharField(max_length=25)
    tipe = models.ForeignKey(Types, related_name='moves')
    category = models.ForeignKey(Damage_Types, related_name='moves')
    pp = models.IntegerField()
    power = models.CharField(max_length=25)
    accuracy = models.CharField(max_length=25)
    description = models.CharField(max_length=255)

class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    types = models.ManyToManyField(Types, related_name='pokemon_of_type')
    abilities = models.ManyToManyField(Abilities, related_name='pokemon_with_ability')
    bst = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    
class Learn_Methods(models.Model):
    method = models.CharField(max_length=25)

class Generations(models.Model):
    gen = models.CharField(max_length=25)
    dex_to = models.IntegerField()
    abilities = models.ManyToManyField(Abilities, related_name='generation')
    moves = models.ManyToManyField(Moves, related_name='generation')
    types = models.ManyToManyField(Types, related_name='generation')

class Versions(models.Model):
    name = models.CharField(max_length=25)
    gen = models.ForeignKey(Generations, related_name='versions')

class Pokemon_Learns_Move_By_Method(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name='learns_move_by_method')
    move = models.ForeignKey(Moves, related_name='pokemon_learns_by_method')
    method = models.ForeignKey(Learn_Methods, related_name='pokemon_learns_move_by')
    meth_qual = models.IntegerField()
    version = models.ForeignKey(Versions, related_name='pokemon_learns_move_by_method')