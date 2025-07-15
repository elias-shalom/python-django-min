from django.shortcuts import render

def home(request):
    resultado = None
    a = b = ''
    if request.method == 'POST':
        a = request.POST.get('a', '')
        b = request.POST.get('b', '')
        try:
            resultado = int(a) + int(b)
        except (ValueError, TypeError):
            resultado = 'Por favor ingresa números válidos.'
    return render(request, 'home.html', {'resultado': resultado, 'a': a, 'b': b})