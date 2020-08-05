from django.shortcuts import render

# Create your views here

html_base = """
    <h1 class="text-center">Dr. Teodoro Maldonado Carbo</h1>
    <ul>
        <li>   <a href="/">PORTADA</a>              </li>
        <li>   <a href="/asistencia/"> Asistencia </a>   </li>
        <li>   <a href="/notas/"> Notas </a>     </li>
        <li>   <a href="/personal/"> Personal </a>     </li>
        <li>   <a href="/estudiantes/"> Estudiantes </a>     </li>
        <li>   <a href="/materias/"> Materias </a>     </li>
    </ul>
"""


def home(request, template="home.html"):
    return render(request, template);

def asistencia(request, template="asistencias.html"):
    return render(request, template);

def notas(request, template="notas.html"):
    return render(request, template);

def personal(request, template="personal.html"):
    return render(request, template);


def estudiantes(request, template="estudiantes.html"):
    return render(request, template);


def materias(request, template="materias.html"):
    return render(request, template);


def cursos(request, template="cursos.html"):
    return render(request, template);


def login(request, template="login.html"):
    return render(request, template);


def Consultar(request, template="Consultar.html"):
    return render(request, template);


def enero(request, template="enero.html"):
    return render(request, template);


def febrero(request, template="febrero.html"):
    return render(request, template);


def marzo(request, template="marzo.html"):
    return render(request, template);


def abril(request, template="abril.html"):
    return render(request, template);


def mayo(request, template="mayo.html"):
    return render(request, template);


def junio(request, template="junio.html"):
    return render(request, template);


def julio(request, template="julio.html"):
    return render(request, template);


def agosto(request, template="agosto.html"):
    return render(request, template);


def septiembre(request, template="septiembre.html"):
    return render(request, template);


def octubre(request, template="octubre.html"):
    return render(request, template);


def noviembre(request, template="noviembre.html"):
    return render(request, template);


def diciembre(request, template="diciembre.html"):
    return render(request, template);
