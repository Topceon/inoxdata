from django.db import models


class Orders(models.Model):
    nameOrder = models.CharField(max_length=255)  # номер заказа
    part = models.ForeignKey('Parts', on_delete=models.PROTECT)  # ссылка на деталь
    ready_qty = models.IntegerField()  # количество готовых деталей
    need_qty = models.IntegerField()  # требуемое количество деталей
    priority = models.ForeignKey('Orders', on_delete=models.PROTECT)  # ссылка на предыдущий заказ для последовательн
    note = models.TextField(blank=True)  # примечание (blank=True - значение может быть пустым)
    need_material = models.BooleanField(default=True)  # на будущее, есть ли материал
    date_for_ready = models.DateField()


class Parts(models.Model):
    name_part = models.CharField(max_length=255, default=1)  # название детали
    material = models.ForeignKey('Materials', on_delete=models.PROTECT)  # ссылка на материал
    x_length = models.IntegerField(default=1)  # длина детали
    y_length = models.IntegerField(default=1)  # ширина детали
    fill_factor = models.FloatField(default=1)  # коэффициент заполнения на листе
    cut_length = models.IntegerField(default=1)  # длина реза
    cut_input = models.IntegerField(default=1)  # количество входов
    otk = models.BooleanField(default=False)  # отработана


class Materials(models.Model):
    name_material = models.CharField(max_length=255)  # название материала
    thickness_material = models.CharField(max_length=255)  # толщина материала
    fiber_speed = models.FloatField(default=None)  # скорость резки на волокне
    yag_speed = models.FloatField(default=None)  # скорость резки на твердотельном
    gidro_speed = models.FloatField(default=None)  # скорость резки на гидре


class ReadyOrders(models.Model):
    nameOrder = models.CharField(max_length=255)  # номер заказа
    part = models.ForeignKey('Parts', on_delete=models.PROTECT)  # ссылка на деталь
    need_qty = models.IntegerField()  # требуемое количество деталей
    note = models.TextField(blank=True)  # примечание (blank=True - значение может быть пустым)
    date_time_ready = models.DateTimeField(auto_now_add=True)  # время готовности


class Storage(models.Model):
    name = models.CharField(max_length=255)  # обозначение куска для идентификации
    material = models.ForeignKey('Materials', on_delete=models.PROTECT)  # ссылка на характеристики материала
    square = models.FloatField()  # количество материала в мкв
    place = models.CharField(max_length=255)  # место где искать кусок
