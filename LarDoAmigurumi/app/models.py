from django.db import models

class Tipo_linha(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome")
        def __str__(self):
            return f"{self.nome}"
        class Meta:
            verbose_name = "Tipo_linha"
            verbose_name_plural = "Tipo_linhas"
class Tipo_agulha(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome")
        def __str__(self):
            return f"{self.nome}"
        class Meta:
            verbose_name = "Tipo_agulha"
            verbose_name_plural = "Tipo_agulhas"
class Marca_linha(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome")
        def __str__(self):
            return f"{self.nome}"
        class Meta:
            verbose_name = "Marca_linha"
            verbose_name_plural = "Marca_linhas"
class Cor(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome")
        def __str__(self):
            return f"{self.nome}"
        class Meta:
            verbose_name = "Cor"
            verbose_name_plural = "Cores"                                                

class Agulha(models.Model):
        numero = models.IntegerField(verbose_name="Numero da agulha")
        tipo_agulha = models.ForeignKey('Tipo_agulha', on_delete=models.CASCADE, verbose_name="Tipo_agulha")
        def __str__(self):
            return self.tipo_agulha.nome
        class Meta:
            verbose_name = "Agulha"
            verbose_name_plural = "Agulhas"

class Linha(models.Model):
        tamanho = models.IntegerField(verbose_name="Tamanho")
        quantidade = models.IntegerField(verbose_name="Quantidade")
        tipo_linha = models.ForeignKey('Tipo_linha', on_delete=models.CASCADE, verbose_name="Tipo_linha")
        marca = models.ForeignKey('Marca_linha', on_delete=models.CASCADE, verbose_name="Marca")
        cor = models.ForeignKey('Cor', on_delete=models.CASCADE, verbose_name="Cor")
        def __str__(self):
           return f"{self.tipo_linha.nome}"

        class Meta:
            verbose_name = "Linha"
            verbose_name_plural = "Linhas"
class Enchimento(models.Model):
        nome = models.CharField(max_length=100, verbose_name="Nome")
        def __str__(self):
            return f"{self.nome}"

        class Meta:
            verbose_name = "Enchimento"
            verbose_name_plural = "Enchimentos"   

class Materiais(models.Model):
        linha = models.ForeignKey('Linha', on_delete=models.CASCADE, verbose_name="Linha")
        agulha = models.ForeignKey('Agulha', on_delete=models.CASCADE, verbose_name="Agulha",related_name="materiais_relacionados")
        enchimento = models.ForeignKey('Enchimento', on_delete=models.CASCADE, verbose_name="Enchimento")

        def __str__(self):
            return f"Linha: {self.linha.tipo_linha.nome}, Agulha: {self.agulha.tipo_agulha.nome}, Enchimento: {self.enchimento.nome}"

        
        class Meta:
            verbose_name = "Materiais"
            verbose_name_plural = "Materiais"
            
class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Receita(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    materiais = models.ForeignKey('Materiais', on_delete=models.CASCADE, verbose_name="Materiais")
    quantidade_linha = models.IntegerField(verbose_name="Quantidade de Linha")
    passos = models.TextField(verbose_name="Passos")
    dificuldade = models.CharField(max_length=50, verbose_name="Dificuldade")
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"




