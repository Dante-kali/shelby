from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    date = {
    'nombre_propietario': 'Jazmin',
    'telefono_propietario': '2254423719',
    'correo_propietario': 'jazminporco@gmail.com',
    'nombre_perro': 'Shelby',
    'raza_perro': 'Pitbull 3ra gen',
    'color_perro': 'negrito',
    'edad_perro': '3 años',
    'otras_caracteristicas': 'Es un pitbull gordito, es negrito y muy jugueton, si lo encuentra cerca por favor contacteme',
    'qr_code_url': 'https://scontent.xx.fbcdn.net/v/t1.15752-9/434711600_420045013974939_9119020785026248081_n.jpg?stp=dst-jpg_p403x403&_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_ohc=NnN6HKdV3UMAb4hBI95&_nc_oc=AdiJ-SItq0QzIQcOLl2tiHbxAbsg6bu4oqbIJpgfc-AookHwIvFNk65DBkCLSC3rHvB0LLCsSD9dPxr0nuZTPhzL&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdWAyLUyiSlmLZ3wjZthjBOkRUapEFP9zMXIyxm97q0C7A&oe=6641FC97',
    'dog_image_url' : 'https://scontent.xx.fbcdn.net/v/t1.15752-9/434656958_1794307041068649_3882096287514660206_n.jpg?stp=dst-jpg_p370x247&_nc_cat=110&ccb=1-7&_nc_sid=5f2048&_nc_ohc=DOKm-Hkt0U4Ab4dUyyb&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_Q7cD1QFKjFH-H3MyVBQGDWhXf1ZvaRyKlJ42JvSMCNm84p0RSw&oe=66420A6B'
}
    return render(request, 'home.html', date)

def contact(request):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    date = {
    'nombre_propietario': 'Jazmin',
    'telefono_propietario': '2254423719',
    'correo_propietario': 'jazminporco@gmail.com',
    'nombre_perro': 'Shelby',
    'raza_perro': 'Pitbull 3ra gen',
    'color_perro': 'negrito',
    'edad_perro': '3 años',
    'otras_caracteristicas': 'Es un pitbull gordito, es negrito y muy jugueton, si lo encuentra cerca por favor contacteme'
    }
    return render(request, 'contact.html', date)

def about(request):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    date = {
    'nombre_propietario': 'Jazmin',
    'telefono_propietario': '2254423719',
    'correo_propietario': 'jazminporco@gmail.com',
    'nombre_perro': 'Shelby',
    'raza_perro': 'Pitbull 3ra gen',
    'color_perro': 'negrito',
    'edad_perro': '3 años',
    'otras_caracteristicas': 'Es un pitbull gordito, es negrito y muy jugueton, si lo encuentra cerca por favor contacteme'
    }
    return render(request, 'about.html', date)

def process_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('contactName')
        email = request.POST.get('contactEmail')
        message = request.POST.get('contactMessage')

        date = {
            'name': name,
            'email' :email,
            'message' : message
        }
        return render(request, 'formulario.html', date)
    
    else:
        return HttpResponse('<h2>Error: Solo se permiten solicitudes POST.</h2>')