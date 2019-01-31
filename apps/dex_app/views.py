from django.shortcuts import render, redirect
from .models import *
import pokebase as pb




# Create your views here.
def dex_page(request, gen, id):
    newdexstr=""
    dexstr = str(id)
    while len(newdexstr) < (3-len(dexstr)):
        newdexstr += "0"
    newdexstr = "/static/dex_app/imgs/"+newdexstr+dexstr+".png"
    why = Generations.objects.get(gen=gen)
    pokemon = Pokemon.objects.get(id=id)

    versions = Versions.objects.filter(gen=why)

    movesingen = Pokemon_Learns_Move_By_Method.objects.filter(pokemon=pokemon)
    
    moveslist = []
    for version in versions:
        moveslist.append(movesingen.filter(version=version).order_by('meth_qual'))
    print(Learn_Methods.objects.all().values())
    context = {
        'gen': gen,
        'versions': versions,
        'pokemon': pokemon,
        'picnum': newdexstr,
        'moveslist': moveslist
    }
    return render(request, 'dex_app/pokedexshow.html', context)

def pokedex(request, gen):
    dex_to = Generations.objects.get(gen=gen)
    dex_to = dex_to.dex_to
    
    print(gen)
    if dex_to < 802:
        context = {
            'all_pokemon': Pokemon.objects.all()[0:dex_to],
            'gen': gen
        }
    else:
        context = {
            'all_pokemon': Pokemon.objects.all(),
            'gen': gen
        }
    
    return render(request,'dex_app/pokedex.html', context)

def moveshow(request, move, gen):
    monwholearn=[]
    mv = Moves.objects.get(name=move)
    movinmeth = Pokemon_Learns_Move_By_Method.objects.filter(move=Moves.objects.get(name=move.lower()))
    for version in Versions.objects.filter(gen=Generations.objects.get(gen=gen)):
        for mov in movinmeth:
            if mov.version.name == version.name:
                monwholearn.append(mov.pokemon)
    context = {
        'move': mv,
        'all_pokemon': monwholearn,
        'gen': gen
    }
    return render(request, 'dex_app/moveshow.html', context)

def moves(request, gen):
    
    context = {
        'all_moves': Moves.objects.all(),
        'gen': gen
    }

    return render(request, 'dex_app/moves.html', context)

def types(request):

    context = {
        'all_types': Types.objects.all(),
        'damage_rels': Damage_Relationships.objects.all()
    }

    return render(request, 'dex_app/types.html', context)

def showtypes(request, type):
    t = type

    context = {
        'type': Types.objects.get(tipe=t),
        'all_types': Types.objects.all(),
        'damage_rels': Damage_Relationships.objects.get(tipe=Types.objects.get(tipe=t))
    }

    return render(request, 'dex_app/typeshow.html', context)

# def setFighting(request):
#     pokedex = []
#     fighting = [56, 57, 62, 66, 67, 68, 106, 107, 214, 236, 237, 256, 257, 286, 296, 297, 307, 308, 391, 392, 447, 448, 453, 454, 475, 499, 500, 532, 533, 534, 538, 539, 559, 560, 619, 620, 638, 639, 640, 647, 652, 674, 675, 701, 739, 740, 759, 760, 766, 783, 784, 794, 795, 802]
#     for i in range(1, len(fighting)+1, 1):
#         mon = Pokemon.objects.filter(id=fighting[i-1])
#         mon.update(types=None)
        
#         # pokemon = []
#         pkmn = pb.pokemon(fighting[i-1])
#         # name = pkmn.name
#         # name = name.replace('-', ' ')
#         # pokemon.append(name.title())
#         typs=[]
#         # pkmn.types
#         for tp in pkmn.types:
#             # types.append(tp.type.name)
#             typ = tp.type.name.title()
#             # typs.append(Types.objects.get(tipe=typ).id)
#             mon.types.add(Types.objects.get(tipe=typ).id)
#         # if len(types) > 1:
#         #     temp = typs[1]
#         #     typs[1]=typs[0]
#         #     typs[0]=temp
#         # print(Pokemon.objects.get(id=fighting[i-1]))
#         # abil = pkmn.abilities
#         # a = []
#         # for ability in abil:
#         #     nm = ability.ability.name
#         #     nm = nm.replace('-', ' ')
#         #     a.append(Abilities.objects.get(name=nm.title()))
#         # bst = 0
#         # for stat in pkmn.stats:
#         #     bst += stat.base_stat
#         #     pokemon.append(stat.base_stat)
#         # pokemon.append(bst)
#         # print(pokemon)
#         # Pokemon.objects.create(name=pokemon[0], bst=pokemon[7], hp=pokemon[6], attack=pokemon[5], defense=pokemon[4], sp_attack=pokemon[3], sp_defense=pokemon[2], speed=pokemon[1])
#         # for ability in a:
#         #     Pokemon.objects.last().abilities.add(ability)
#         # for t in types:

#     return redirect('/')