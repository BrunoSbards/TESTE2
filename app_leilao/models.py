from django.db import models

class estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    sigla_estado = models.CharField(max_length=5)

    def __str__(self):
        return self.sigla_estado


class leiloeiro(models.Model):
    id_leiloeiro = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    site = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    

class matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_estado = models.ForeignKey(estado, on_delete=models.CASCADE, null=False, blank=False)
    id_leiloeiro = models.ForeignKey(leiloeiro, on_delete=models.CASCADE, null=False, blank=False)
    numero_matricula = models.CharField(max_length=10)
    
    def __str__(self):
        return self.numero_matricula
    

class anexo(models.Model):
    id_anexo = models.AutoField(primary_key=True)
    id_leiloeiro = models.ForeignKey(leiloeiro, on_delete=models.CASCADE, null=False, blank=False)
    arquivo = models.CharField(max_length=255)

    def __str__(self):
        return self.arquivo
