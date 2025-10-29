from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Pacientes

@method_decorator(csrf_exempt, name='dispatch')
class PacientesView(View):

    def get(self, request, cod_ingreso=None):
        if cod_ingreso:
            pacientes = list(Pacientes.objects.filter(cod_ingreso=cod_ingreso).values())
            if pacientes:
                datos = {"Message": "Success", "paciente": pacientes[0]}
            else:
                datos = {"Message": "Paciente no encontrado"}
        else:
            pacientes = list(Pacientes.objects.values())
            if pacientes:
                datos = {"Message": "Success", "pacientes": pacientes}
            else:
                datos = {"Message": "No hay pacientes registrados"}
        return JsonResponse(datos)
    
    def post(self, request):
        data = json.loads(request.body)
        Pacientes.objects.create(
            cod_ingreso=data["cod_ingreso"],
            documento=data["documento"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            direccion=data["direccion"],
            telefono=data["telefono"]
        )
        return JsonResponse({"Message": "Paciente creado exitosamente"})
    
    def put(self, request, cod_ingreso):
        data = json.loads(request.body)
        try:
            paciente = Pacientes.objects.get(cod_ingreso=cod_ingreso)
            paciente.documento = data["documento"]
            paciente.nombre = data["nombre"]
            paciente.apellido = data["apellido"]
            paciente.direccion = data["direccion"]
            paciente.telefono = data["telefono"]
            paciente.save()
            return JsonResponse({"Message": "Paciente actualizado"})
        except Pacientes.DoesNotExist:
            return JsonResponse({"Message": "Paciente no encontrado"})
    
    def delete(self, request, cod_ingreso):
        count, _ = Pacientes.objects.filter(cod_ingreso=cod_ingreso).delete()
        if count:
            return JsonResponse({"Message": "Paciente eliminado"})
        else:
            return JsonResponse({"Message": "Paciente no encontrado"})

