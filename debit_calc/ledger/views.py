from django.shortcuts import render

def index(request):
    context = {}
    if request.method == 'POST':
        money = float(request.POST.get('money'))
        percent = float(request.POST.get('percent'))
        dedlane = float(request.POST.get('dedlane'))
        capitalization = "capitalization" in request.POST
        print(capitalization)
        if capitalization:
            print(1)
            context['result'] = money + money * ((1 + percent / 100 / 12) ** dedlane - 1)
        else:
            print(2)
            context['result'] = money + money*(percent/100)*(dedlane/12)
        context['result'] = round(context['result'], 2)
    return render(request, "index.html", context)