from rest_framework import serializers
from APPadministracion.models import *

class torneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = ['id','nombre','alias','numeroEquipo','descripcion','fechaInicio','fechaFin','tipo_Tor']
        extra_kwargs = {'id': {'required': False}}

class equipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id','PropiedadTorneo','nombre','alias','frase','entrenador','cantidadJugador','estado_Equipo']
        extra_kwargs = {'id': {'required': False}}
    
class jugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['id','PropiedadEquipo','nombre','apellido','correo','celular','cedula','posicion_Jugador']
        extra_kwargs = {'id': {'required': False}}

class arbitroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arbitro
        fields = ['id','PropiedadTorneo','nombre','apellido','correo','celular','cedula']
        extra_kwargs = {'id': {'required': False}}

class implementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implementos
        fields = ['id','PropiedadTorneo','nombre','cantidad','descripcion','tipo_Im']
        extra_kwargs = {'id': {'required': False}}
    
class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','PropiedadTorneo','nombre','apellido','correo','cedula','estado_Ticket']
        extra_kwargs = {'id': {'required': False}}

class encuentroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuentro
        fields = ['id','PropiedadTorneo','nombreA','nombreB','fechaPartido','hora','golesA','golesB','faltas','tarjetaRoja','tarjetaAmarilla']
        extra_kwargs = {'id': {'required': False}}