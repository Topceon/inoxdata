from django.db import models
from django.urls import reverse


class Orders(models.Model):
    nameOrder = models.CharField(max_length=255, verbose_name='Заказ')  # номер заказа
    part = models.ForeignKey('Parts', on_delete=models.PROTECT, verbose_name='Деталь')  # ссылка на деталь
    ready_qty = models.IntegerField(default=0)  # количество готовых деталей
    need_qty = models.IntegerField(verbose_name='Количество')  # требуемое количество деталей
    priority = models.ForeignKey('Orders', blank=True, on_delete=models.PROTECT)  # споследовательность
    note = models.TextField(blank=True, verbose_name='Примечание')  # примечание (blank=True - значения может не быть)
    need_material = models.BooleanField(default=True, verbose_name='Материал в наличии')  # на будущее, есть ли материал
    date_for_ready = models.DateField(verbose_name='Дата выдачи заказчику')  # дата выдачи заказа клиенту
    otk = models.BooleanField(default=False, verbose_name='Одобрен')  # первая деталь в партии

    def get_absolute_url(self):
        return reverse('form_orders')


class Parts(models.Model):
    name_part = models.CharField(max_length=255, verbose_name='Деталь')  # название детали
    material = models.ForeignKey('Materials', verbose_name='Материал', on_delete=models.PROTECT)  # ссылка на материал
    x_length = models.IntegerField(verbose_name='Длина')  # длина детали
    y_length = models.IntegerField(verbose_name='Ширина')  # ширина детали
    fill_factor = models.FloatField(default=1, verbose_name='Фактор площади')  # коэффициент заполнения на листе
    cut_length = models.IntegerField(verbose_name='Длина реза(мм)')  # длина реза
    cut_input = models.IntegerField(verbose_name='Количество входов')  # количество входов
    otk = models.BooleanField(default=False, verbose_name='Одобрен')  # отработана

    def get_absolute_url(self):
        return reverse('form_parts')


class Materials(models.Model):
    name_material = models.CharField(max_length=255, verbose_name='Материал')  # название материала
    thickness_material = models.CharField(max_length=255, verbose_name='Толщина')  # толщина материала
    fiber_speed = models.FloatField(null=True, blank=True, verbose_name='Волокно')  # скорость резки на волокне
    yag_speed = models.FloatField(null=True, blank=True, verbose_name='Yag')  # скорость резки на твердотельном
    gidro_speed = models.FloatField(null=True, blank=True, verbose_name='Гидро')  # скорость резки на гидре

    def __str__(self):
        return str(self.name_material) + ' ' + str(self.thickness_material) + 'мм'

    def get_absolute_url(self):
        return reverse('forms')


class ReadyOrders(models.Model):
    nameOrder = models.CharField(max_length=255)  # номер заказа
    part = models.ForeignKey('Parts', on_delete=models.PROTECT)  # ссылка на деталь
    need_qty = models.IntegerField()  # требуемое количество деталей
    note = models.TextField(blank=True)  # примечание (blank=True - значение может быть пустым)
    date_time_ready = models.DateTimeField(auto_now_add=True)  # время готовности
    otk = models.CharField(max_length=255)  # кто утвердил партию

    def get_absolute_url(self):
        return reverse('ready')


class Storage(models.Model):
    name = models.CharField(max_length=255)  # обозначение куска для идентификации
    material = models.ForeignKey('Materials', on_delete=models.PROTECT)  # ссылка на характеристики материала
    square = models.FloatField()  # количество материала в мкв
    place = models.CharField(max_length=255)  # место где искать кусок
