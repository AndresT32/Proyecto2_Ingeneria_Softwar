from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Login
import json

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):

    def get(self, request, id=None):
        if id:
            users = list(Login.objects.filter(id=id).values())
            if len(users) > 0:
                datos = {"message": "Success", "user": users[0]}
            else:
                datos = {"message": "User not found"}
        else:
            users = list(Login.objects.values())
            datos = {"message": "Success", "users": users}
        return JsonResponse(datos)

    def post(self, request):
        data = json.loads(request.body)
        Login.objects.create(
            username=data["username"],
            password=data["password"]
        )
        return JsonResponse({"message": "User created"})

    def put(self, request, id):
        data = json.loads(request.body)
        user = Login.objects.filter(id=id)
        if user.exists():
            u = user.first()
            u.username = data["username"]
            u.password = data["password"]
            u.save()
            return JsonResponse({"message": "User updated"})
        else:
            return JsonResponse({"message": "User not found"})

    def delete(self, request, id):
        user = Login.objects.filter(id=id)
        if user.exists():
            user.delete()
            return JsonResponse({"message": "Deleted successfully"})
        else:
            return JsonResponse({"message": "User not found"})

