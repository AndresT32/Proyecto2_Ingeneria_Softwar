from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Resultado
import json

@method_decorator(csrf_exempt, name='dispatch')
class ResultadosView(View):

    def get(self, request, id_resultado=None):
        if id_resultado:
            resultados = list(Resultado.objects.filter(id_resultado=id_resultado).values())
            if len(resultados) > 0:
                datos = {"message": "Success", "resultado": resultados[0]}
            else:
                datos = {"message": "Resultado not found"}
        else:
            resultados = list(Resultado.objects.values())
            datos = {"message": "Success", "resultados": resultados}
        return JsonResponse(datos)

    def post(self, request):
        data = json.loads(request.body)
        Resultado.objects.create(
            cod_ingreso_id=data["cod_ingreso"],  # FK a Pacientes
            hdl=data["hdl"],
            ldl=data["ldl"],
            trigliceridos=data["trigliceridos"],
            cod_laboratorista_id=data["cod_laboratorista"]  # FK a Laboratoristas
        )
        return JsonResponse({"message": "Success"})

    def put(self, request, id_resultado):
        data = json.loads(request.body)
        resultado = Resultado.objects.filter(id_resultado=id_resultado)
        if resultado.exists():
            r = resultado.first()
            r.cod_ingreso_id = data["cod_ingreso"]
            r.hdl = data["hdl"]
            r.ldl = data["ldl"]
            r.trigliceridos = data["trigliceridos"]
            r.cod_laboratorista_id = data["cod_laboratorista"]
            r.save()
            return JsonResponse({"message": "Updated"})
        else:
            return JsonResponse({"message": "Resultado not found"})

    def delete(self, request, id_resultado):
        resultado = Resultado.objects.filter(id_resultado=id_resultado)
        if resultado.exists():
            resultado.delete()
            return JsonResponse({"message": "Deleted successfully"})
        else:
            return JsonResponse({"message": "Resultado not found"})
