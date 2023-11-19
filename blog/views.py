from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from django.db import transaction
from .models import Activity, Player
from django.contrib import messages
from django.http import HttpResponseBadRequest


def play_list(request):
    player = Player.objects.all()

    activitys = Activity.objects.all()
    return render(request, 'blog/play_list.html', {'player': player, 'activitys' : activitys})


def play_detail(request, id_play):
    player = get_object_or_404(Player, id_play=id_play)

    previous_activity = get_object_or_404(Activity, id_activ = player.activity.id_activ)
    if request.method == 'POST':
        form = MoveForm(request.POST, instance=player)
        if form.is_valid():
            new_activity = form.cleaned_data['activity']

            if new_activity.disponibilite == 'occupé':
                return HttpResponseBadRequest("l'activité est occupée.")

           

            elif new_activity.id_activ =='Restaurant':
                if player.etat!='affamé':
                    return HttpResponseBadRequest("Le joueur n'a pas faim.")
                else:
                    player.etat = 'Repus' 
                    player.save()

            elif new_activity.id_activ=='Kinésithérapie': 
                if player.etat!='Courbaturé':
                    return HttpResponseBadRequest("Le joueur n'a pas besoin d'aller chez le kiné.")
                
                else:
                    
                    player.etat = 'relaxé' 
                    player.save()

            elif new_activity.id_activ=='Temps libre': 
                if player.etat!='relaxé':
                    return HttpResponseBadRequest("Le joueur n'a pas besoin de profiter de temps libre.")
                
                else:
                    
                    player.etat = 'affamé' 
                    player.save()

            elif new_activity.id_activ == 'Entraînement':
                if player.etat != 'En forme':
                    return HttpResponseBadRequest("Le joueur ne peut pas s'entrainer")
                else:
               
                    player.etat = 'Courbaturé'
                    player.save()


            elif new_activity.id_activ == 'Séance de dédicace':
                if player.etat != 'Repus':
                    return HttpResponseBadRequest("Le joueur doit manger avant de faire des dédicaces.")
                else :
                    player.etat = 'Fatigué'
                    player.save()

            elif new_activity.id_activ == 'Sieste':
                if player.etat != 'Fatigué':
                    return HttpResponseBadRequest("Le joueur n'a pas besoin de dormir.")
                else:
                    player.etat = 'En forme'
                    player.save()

            with transaction.atomic():

                previous_activity.disponibilite = 'libre'
                previous_activity.save()
                player.activity.save()
                new_activity.disponibilite = 'occupé'
                new_activity.save()
                player.activity = new_activity
                player.save()


        return redirect('play_list')

    else:
        form = MoveForm(instance=player)

    return render(request, 'blog/play_detail.html', {'form': form, 'player': player})



 
