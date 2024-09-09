from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275531',
        'name': 'Muhammad Fadhil Nur Aziz',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)