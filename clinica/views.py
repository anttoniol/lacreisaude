from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from .models import Profissional, Consulta, Endereco, Contato
from .serializers import ConsultaSerializer, ProfissionalSerializer, EnderecoSerializer, ContatoSerializer


class ProfissionalListAPIView(generics.GenericAPIView):
    serializer_class = ProfissionalSerializer
    queryset = Profissional.objects.all()
    def get(self, request, *args, **kwargs):
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProfissionalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsultaListAPIView(generics.GenericAPIView):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()

    def get(self, request, *args, **kwargs):
        profissionais = Consulta.objects.all()
        serializer = ConsultaSerializer(profissionais, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ConsultaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnderecoListAPIView(generics.GenericAPIView):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()

    def get(self, request, *args, **kwargs):
        enderecos = Endereco.objects.all()
        serializer = EnderecoSerializer(enderecos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContatoListAPIView(generics.GenericAPIView):
    serializer_class = ContatoSerializer
    queryset = Contato.objects.all()

    def get(self, request, *args, **kwargs):
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(contatos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ContatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsultaProfissionalDetailAPIView(generics.GenericAPIView):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()

    def get(self, request, id_profissional, *args, **kwargs):

        consulta = Consulta.objects.filter(profissional = int(id_profissional))
        if not consulta:
            return Response(
                {"res": "There is no appointment with the professional ID provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ConsultaSerializer(consulta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConsultaDetailAPIView(generics.GenericAPIView):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()

    def get_object(self, id_consulta):
        try:
            return Consulta.objects.get(id=id_consulta)
        except Consulta.DoesNotExist:
            return None

    def get(self, request, id_consulta, *args, **kwargs):
        consulta = self.get_object(id_consulta)
        if not consulta:
            return Response(
                {"res": "There is no appointment with the ID provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id_consulta, *args, **kwargs):
        consulta = self.get_object(id_consulta)
        if not consulta:
            return Response(
                {"res": "There is no appointment with the ID provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'data': request.data.get('data'),
            'profissional': request.data.get('profissional'),
        }
        serializer = ConsultaSerializer(instance = consulta, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_consulta, *args, **kwargs):
        consulta = self.get_object(id_consulta)
        if not consulta:
            return Response(
                {"res": "There is no appointment with the ID provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        consulta.delete()
        return Response(
            {"res": "Appointment deleted successfully!"},
            status=status.HTTP_200_OK
        )


class ProfissionalDetailAPIView(generics.GenericAPIView):
    serializer_class = ProfissionalSerializer
    queryset = Profissional.objects.all()

    def get_object(self, id_profissional):
        try:
            return Profissional.objects.get(id=id_profissional)
        except Profissional.DoesNotExist:
            return None

    def get(self, request, id_profissional, *args, **kwargs):
        profissional = self.get_object(id_profissional)
        if not profissional:
            return Response(
                {"res": "There is no professional with the ID provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProfissionalSerializer(profissional)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id_profissional, *args, **kwargs):
        profissional = self.get_object(id_profissional)
        if not profissional:
            return Response(
                {"res": "There is no professional with the ID provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nome_completo': request.data.get('nome_completo'),
            'nome_social': request.data.get('nome_social'),
            'profissao': request.data.get('profissao'),
            'endereco': request.data.get('endereco'),
            'contato': request.data.get('contato')
        }

        serializer = ProfissionalSerializer(instance = profissional, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_profissional, *args, **kwargs):
        profissional = self.get_object(id_profissional)
        if not profissional:
            return Response(
                {"res": "There is no professional with the ID provided"},
                status=status.HTTP_400_BAD_REQUEST
            )
        profissional.delete()
        return Response(
            {"res": "Professional deleted successfully!"},
            status=status.HTTP_200_OK
        )