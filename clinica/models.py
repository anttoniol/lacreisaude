from django.db import models


class Contato(models.Model):
    prefixo = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return f"({self.prefixo}){self.numero}"


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return f"({self.logradouro}), {self.cep}"


class Profissional(models.Model):
    nome_completo = models.CharField(max_length = 255)
    nome_social = models.CharField(max_length=255, null=True)
    profissao = models.CharField(max_length = 50)
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING)
    contato = models.ManyToManyField(Contato)

    def __str__(self):
        return self.nome_completo


class Consulta(models.Model):
    data = models.DateTimeField(auto_now = False)
    profissional = models.ForeignKey(Profissional, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.data}, {self.profissional}"
