from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Sacar al perro",
    "february": "Bañar al gato",
    "march": "Aprender un framework nuevo",
    "april": "Sacar al perro",
    "may": "Bañar al gato",
    "june": "Aprender un framework nuevo",
    "july": "Sacar al perro",
    "august": "Bañar al gato",
    "september": "Aprender un framework nuevo",
    "october": "Sacar al perro",
    "november": "Bañar al gato",
    "december": "Aprender un framework nuevo"
}


def index(response):
    list_items = ""  # String para crear el html de la lista
    months = list(monthly_challenges.keys())  # Traemos la lista de las claves

    # For-loop para crear una cadena de elementos de lista html
    # cada elemento de la lista es un hipervinculo a cada mes
    # OJO: hacer uso de \ para las referencias a la cadena
    for m in months:
        capitalized_month = m.capitalize()
        month_path = reverse("month-challenge", args=[m])
        list_items += f"<li> <a href = \"{month_path}\">{capitalized_month}</a> </li>"

    data_response = f"<ul>{list_items}</ul>"
    return HttpResponse(data_response)


def monthly_challenges_number(request, month):
    # Lista de las claves del diccionario
    months = list(monthly_challenges.keys())
    try:
        # Obtener la clave de la lista en la posicion month (la dirección mandada como entero)
        month_redirect = months[month - 1]
        # Haciendo la ruta más dinámica
        # reverse(nombre definido en las rutas de la app, un array con un solo elemento(el resto de la url))
        redirect_path = reverse(
            "month-challenge", args=[month_redirect])  # /challenge/january
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month number doesn´t exist!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
