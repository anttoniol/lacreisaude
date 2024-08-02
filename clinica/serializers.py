from rest_framework import serializers
from .models import Contato, Endereco, Profissional, Consulta


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ["prefixo", "numero"]


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ["logradouro", "numero", "complemento",
                  "bairro", "cidade", "uf", "cep"]


class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ["nome_completo", "nome_social", "profissao",
                  "endereco", "contato"]

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ["data", "profissional"]