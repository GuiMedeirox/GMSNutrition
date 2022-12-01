from django.db import models

# Create your models here.

class nutricionistas(models.Model):
    nut_nome = models.CharField("Nome", max_length=255, blank=False, null=False)
    nut_crn = models.CharField("Crn", max_length=255, blank=False, null=False)
    def __str__(self):
        return self.nut_nome
    class Meta:
        verbose_name_plural = "nutricionistas"

class pacientes(models.Model):
    pac_nome = models.CharField("Nome", max_length=255, blank=False, null=False)
    pac_idade = models.IntegerField("Idade", default=1, blank=False, null=False)
    pac_meta = models.CharField("Meta", max_length=255, blank=False, null=False)
    pac_nut_nome = models.ForeignKey("nutricionistas", on_delete=models.CASCADE)
    def __str__(self):
        return self.pac_nome
    class Meta:
        verbose_name_plural = "pacientes"

class cardapios(models.Model):
    car_cardapio = models.TextField(blank=False, null=False)
    car_pac_nome = models.ForeignKey("pacientes", on_delete=models.CASCADE) 
    def __str__(self):
        return "Cardápio de {}".format(self.car_pac_nome)
    class Meta:
        verbose_name_plural = "cardapios dos pacientes"