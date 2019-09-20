from django.shortcuts import render
import requests
from django.http import HttpResponse
from django import forms
import main_site.objclass as objclass





class UserForm(forms.Form):
    player_name = forms.CharField(required=True, min_length=1, max_length=30)


def api_qry(request, name):
    qc_url = 'https://stats.quake.com/api/v2/Player/Stats?name='
    full_url = qc_url + name
    response = requests.get(full_url)
    player_data = response.json()
    return player_data


def index(request):
    if request.method == "POST":
        name = request.POST.get("player_name")
        player_data = api_qry(request, name)
        if "code" in player_data:
            return render(request, 'notfound.html')
        else:

            play_data = objclass.PlayerStats(player_data)

            #play_data = objclass.to_class(player_data)
            return render(request, 'responce.html', {
                'name': play_data.name,
                'rating': play_data.duel_rating,
                'games_count': play_data.duel_rating_games_count,
                'player_lvl': play_data.player_level,
                'player_exp': play_data.player_exp
            })
        #return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})