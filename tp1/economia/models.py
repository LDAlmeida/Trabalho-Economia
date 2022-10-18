from django.db import models
from economia import ml_model
from economia.ml_model import prever
class Person(models.Model):
    empregos = models.FloatField('Quantos empregos já teve?')
    certificacoes_tecnologia = models.FloatField('Quantos certificações tem na área de tecnologia?')
    certificacoes_gestao = models.FloatField('Quantos certificações tem na área de gestão?')
    certificacoes_seguranca = models.FloatField('Quantos certificações tem na área de segurança do trabalho?')
    horas_tecnologia = models.FloatField('Quantas horas de cursos tem na área de tecnologia?')
    horas_gestao = models.FloatField('Quantas horas de cursos tem na área de gestão?')
    horas_segurança = models.FloatField('Quantas horas de cursos tem na área de segurança do trabalho?')
    graduacoes = models.FloatField('Quantas graduações você tem?')
    demissoes = models.FloatField('Quantas vezes já foi mandado embora?')
    papeis = models.FloatField('Quantos papéis já publicou na área de tecnologia da informação?')
    discriminado = models.FloatField('Quantas vezes já se sentiu discriminado?')
    casado = models.FloatField('Quantas vezes já foi casado?')
    filhos = models.FloatField('Quantos filhos você tem?')
    receber = models.FloatField('Quanto você ou quer receber?')
    bolas = models.FloatField('Quantas bolas de tenis cabem em uma limosine?')
    previsao = models.CharField(max_length=50, blank=True)

    def prever_emprego(self):
        lista = [self.empregos,self.certificacoes_tecnologia,self.certificacoes_gestao,self.certificacoes_seguranca,self.horas_tecnologia,self.horas_gestao,self.horas_segurança,self.graduacoes, self.demissoes, self.papeis, self.discriminado, self.casado, self.filhos, self.receber, self.bolas]
        prev = prever(lista)
        self.previsao = prev
        self.save()
