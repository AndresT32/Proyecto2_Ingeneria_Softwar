from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Laboratoristas
import json

@method_decorator(csrf_exempt, name='dispatch')
class LaboratoristasView(View):

    def get(self, request, cod_laboratorista=None):
        if cod_laboratorista:
            lab = list(Laboratoristas.objects.filter(cod_laboratorista=cod_laboratorista).values())
            if len(lab) > 0:
                datos = {"message": "Success", "laboratorista": lab[0]}
            else:
                datos = {"message": "Laboratorista not found"}
        else:
            labs = list(Laboratoristas.objects.values())
            datos = {"message": "Success", "laboratoristas": labs}
        return JsonResponse(datos)

    def post(self, request):
        data = json.loads(request.body)
        Laboratoristas.objects.create(
            cod_laboratorista=data["cod_laboratorista"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            telefono=data["telefono"],
            profesion=data["profesion"]
        )
        return JsonResponse({"message": "Success"})

    def put(self, request, cod_laboratorista):
        data = json.loads(request.body)
        lab = Laboratoristas.objects.filter(cod_laboratorista=cod_laboratorista)
        if lab.exists():
            lab = lab.first()
            lab.nombre = data["nombre"]
            lab.apellido = data["apellido"]
            lab.telefono = data["telefono"]
            lab.profesion = data["profesion"]
            lab.save()
            return JsonResponse({"message": "Success"})
        else:
            return JsonResponse({"message": "Laboratorista not found"})

    def delete(self, request, cod_laboratorista):
        lab = Laboratoristas.objects.filter(cod_laboratorista=cod_laboratorista)
        if lab.exists():
            lab.delete()
            return JsonResponse({"message": "Deleted successfully"})
        else:
            return JsonResponse({"message": "Laboratorista not found"})


