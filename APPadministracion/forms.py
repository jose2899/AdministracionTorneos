from django import forms
from APPadministracion.models import Persona, Torneo, Arbitro, Ticket, Equipo, Jugador, Implementos, Encuentro 

#creamos los formularios para cada una de las clases
class FormularioPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields=["nombre","apellido","correo","celular","cedula","user","contra"]

class FormularioTorneo(forms.ModelForm):
    class Meta:
        model = Torneo 
        fields=["nombre","alias","numeroEquipo","descripcion","fechaInicio","fechaFin","tipo_Tor"] 
class FormularioArbitro(forms.ModelForm):
    class Meta:
        model = Arbitro
        fields=["PropiedadTorneo","nombre","apellido","correo","celular","cedula"]

class FormularioImplementos(forms.ModelForm):
    class Meta:
        model = Implementos
        fields=["PropiedadTorneo","nombre","cantidad","descripcion","tipo_Im"]

class FormularioTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields=["PropiedadTorneo","nombre","apellido","correo","cedula","estado_Ticket"]

class FormularioEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields=["PropiedadTorneo","nombre","alias","frase","entrenador","cantidadJugador","estado_Equipo"]

class FormularioJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields=["PropiedadEquipo","nombre","apellido","correo","celular","cedula","posicion_Jugador"]

class FormularioEncuentro(forms.ModelForm):
    class Meta:
        model = Encuentro
        fields=["PropiedadTorneo","nombreA","nombreB","fechaPartido","hora","golesA","golesB","faltas","tarjetaRoja","tarjetaAmarilla"]