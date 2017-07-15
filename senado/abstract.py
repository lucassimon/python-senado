# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Projeto(models.Model):

    nome = models.CharField(
        'Nome completo',
        max_length=255
    )

    descricao = models.TextField(
        'Descrição do projeto de lei',
    )

    pontuacao_acao = models.FloatField(
        'Pontuacao das ações'
    )

    posicionamento_contrarios = models.PositiveIntegerField(
        'Quantidade de posicionamentos contrarios'
    )

    posicionamento_neutro = models.PositiveIntegerField(
        'Quantidade de posicionamentos neutro'
    )

    posicionamento_favoravel = models.PositiveIntegerField(
        'Quantidade de posicionamentos favorável'
    )

    qtd_grupos = models.PositiveIntegerField(
        'Quantidade de Grupos Criados'
    )

    qtd_acompanhantes = models.PositiveIntegerField(
        'Quantidade de Usuários acompanhando'
    )

    qtd_comentarios = models.PositiveIntegerField(
        'Quantidade de comentarios somado todos os grupos'
    )

    is_removed = models.BooleanField(
        'is removed',
        default=False,
    )

    def __str__(self):
        return "%s" % self.nome

    class Meta:
        abstract = True
        ordering = ['nome']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projeto'


class Acao(models.Model):

    projeto = models.ForeignKey(
        Projeto
    )

    nome = models.CharField(
        'Nome completo',
        max_length=255
    )

    descricao = models.TextField(
        'Descrição',
    )

    creditos = models.FloatField(
        'Créditos',
        help_text='Pesos para gerar uma pontuação dos avanços'
    )

    is_removed = models.BooleanField(
        'is removed',
        default=False,
    )

    def __str__(self):
        return "%s" % self.nome

    class Meta:
        abstract = True
        ordering = ['nome']
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'


class Grupo(models.Model):
    """
    Grupos de cada projeto
    """

    projeto = models.ForeignKey(
        Projeto
    )

    nome = models.CharField(
        'Nome',
        max_length=255
    )

    is_removed = models.BooleanField(
        'is removed',
        default=False,
    )

    def __str__(self):
        return "%s" % self.nome

    class Meta:
        abstract = True
        ordering = ['nome']
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'


class Membro(models.Model):
    """
    Membros de um grupo
    """

    grupo = models.ForeignKey(
        Grupo
    )

    participante = models.ForeignKey(
        User
    )

    def __str__(self):
        return "%s - %S" % self.grupo - self.participante

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'


class Comentario(models.Model):

    grupo = models.ForeignKey(
        Grupo
    )

    usuario = models.ForeignKey(
        User,
        verbose_name='user',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    nome_usuario = models.CharField(
        "Nome do usuario",
        max_length=255,
        blank=True
    )

    email_usuario = models.EmailField(
        "Nome do endereço de email",
        max_length=254,
        blank=True
    )

    url_usuario = models.URLField(
        "Perfil do usuário",
        blank=True
    )

    comentario = models.TextField(
        'Comentário',
    )

    data_comentario = models.DateTimeField(
        'date/time submitted',
        default=None,
        db_index=True
    )

    ip_address = models.GenericIPAddressField(
        'IP address',
        unpack_ipv4=True,
        blank=True,
        null=True
    )

    likes_computados = models.PositiveIntegerField(
        'Votos a favor'
    )

    dislikes_computados = models.PositiveIntegerField(
        'Votos contra'
    )

    is_removed = models.BooleanField(
        'is removed',
        default=False,
    )

    def __str__(self):
        return "%s - %S" % self.nome_usuario - self.comentario[::20]

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'


class UsuarioVotaComentarios(models.Model):

    usuario = models.ForeignKey(
        User
    )

    comentario = models.ForeignKey(
        Comentario
    )

    likes = models.PositiveIntegerField(
        'Likes',
        default=0
    )

    dislikes = models.PositiveIntegerField(
        'Dislikes',
        default=0
    )

    votou = models.BooleanField(
        'Votou?',
        default=False
    )

    def __str__(self):
        return "%s - %s" % self.usuario - self.likes

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Usuario vota comentario'
        verbose_name_plural = 'Usuario vota comentarios'


class Posicionamento(models.Model):

    class Position:
        CONTRARIO = 1
        NEUTRO = 2
        FAVORAVEL = 3

    POSITION_CHOICES = (
        (Position.CONTRARIO, 'Contrário'),
        (Position.NEUTRO, 'Neutro'),
        (Position.FAVORAVEL, 'Favoravel'),
    )

    projeto = models.ForeignKey(
        Projeto
    )

    usuario = models.ForeignKey(
        User
    )

    posicionamento = models.PositiveSmallIntegerField(
        'Posicionamento',
        default=Position.NEUTRO,
        choices=POSITION_CHOICES
    )

    def __str__(self):
        return "%s - %s" % self.usuario - self.posicionamento

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Posicionamento'
        verbose_name_plural = 'Posicionamentos'


class Acompanhamento(models.Model):

    projeto = models.ForeignKey(
        Projeto
    )

    usuario = models.ForeignKey(
        User
    )

    def __str__(self):
        return "%s - %s" % self.projeto - self.usuario

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Acompanhamento'
        verbose_name_plural = 'Acompanhamentos'


class Notificacao(models.Model):

    usuario = models.ForeignKey(
        User,
        verbose_name=u'usuário',
    )

    app = models.BooleanField(
        default=False,
        verbose_name='aplicativo',
    )

    data_lembrete = models.DateTimeField(
        verbose_name=u'data do lembrete',
    )

    notificado = models.BooleanField(
        verbose_name=u'notificado',
    )

    lido = models.BooleanField(
        verbose_name=u'visualizada',
        default=False
    )

    descricao = models.TextField(
        verbose_name=u'observações',
    )

    rd_station = models.BooleanField(
        default=False,
        verbose_name=u'rd station',
    )

    url = models.URLField(
        blank=True,
        max_length=200,
        null=True,
        verbose_name='url',
    )

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
