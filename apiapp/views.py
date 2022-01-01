
from rest_framework.response import Response
from .models import Employe
from .serializer import EmployeSerializer
from rest_framework.decorators import api_view



@api_view(['GET'])
def EmployeList(request):
    employes = Employe.objects.all()
    serializer = EmployeSerializer(employes, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def Employeadd(request):
    serializer = EmployeSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def Employeupdate(request, pk):
    employe = Employe.objects.get( id = pk )
    serializer = EmployeSerializer(instance = employe, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Employedelete(request,pk):
    employe = Employe.objects.get(id = pk)
    employe.delete()

    return Response("Employe deleted")
  
    