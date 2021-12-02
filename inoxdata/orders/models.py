from django.db import models
from django.urls import reverse


class Orders(models.Model):
    name_order = models.CharField(max_length=255, verbose_name='Заказ')  # номер заказа
    part = models.ForeignKey('Parts', on_delete=models.PROTECT, to_field='name_part', verbose_name='Деталь')  # ссылка на деталь
    need_qty = models.IntegerField(verbose_name='Количество', )  # требуемое количество деталей
    machine = models.ForeignKey('Machine', on_delete=models.PROTECT, verbose_name='Станок')  # станок для резки
    note = models.TextField(blank=True, verbose_name='Примечание')  # примечание (blank=True - значения может не быть)
    need_material = models.BooleanField(default=True, verbose_name='Материал в наличии')  # на будущее, есть ли материал
    date_for_ready = models.DateField(verbose_name='Дата выдачи заказчику')  # дата выдачи заказа клиенту
    otk = models.BooleanField(default=True, verbose_name='Одобрен')  # первая деталь в партии
    thickness = models.ForeignKey('Thickness', null=True, blank=True, verbose_name='Толщина', on_delete=models.PROTECT)
    priority = models.CharField(max_length=255, default=9, verbose_name='Приоритет')  # приоритет резки

    def __str__(self):
        return str(self.name_order)

    def get_absolute_url(self):
        return reverse('form_orders')

    def get_file_name(self):
        st = f'orders/media/{str(self.part)}.pdf'
        return st

    def get_machine_file_name(self):
        thickness = str(self.part.thickness)
        if '.' in str(self.part.thickness):
            thickness = thickness.replace('.', 'i')
        mfn = f'S{thickness} {str(self.part.material)} {str(self.part)}'
        return mfn

    def get_material(self):
        mtl = str(self.part.material)
        return mtl

    def get_thickness(self):
        thc = str(self.part.thickness)
        return thc

    def get_part_otk(self):
        potk = self.part.otk
        return potk

    def get_part_note(self):
        gpn = str(self.part.note)
        return gpn

    def get_required_material(self):
        grm = str(round((self.part.x_length * self.part.y_length / 1000000 * self.need_qty), 2))
        return grm

    def get_ready_qty(self):
        rqt = 0
        for i in self.readyorders_set.all():
            rqt = i.qty + rqt
            if rqt >= self.need_qty:
                self.priority = 0
                self.save()
        return str(rqt)

    def get_ready_time(self):
        rt = self.readyorders_set.order_by('date_time_ready').last()
        return rt.date_time_ready


class Parts(models.Model):
    name_part = models.CharField(max_length=255, unique=True, verbose_name='Деталь')  # название детали
    material = models.ForeignKey('Materials', verbose_name='Материал', on_delete=models.PROTECT)  # ссылка на материал
    thickness = models.ForeignKey('Thickness', verbose_name='Толщина', on_delete=models.PROTECT)  # толщина материала
    cut_length = models.IntegerField(verbose_name='Длина реза(мм)')  # длина реза
    cut_input = models.IntegerField(verbose_name='Количество входов')  # количество входов
    x_length = models.IntegerField(verbose_name='Длина')  # длина детали
    y_length = models.IntegerField(verbose_name='Ширина')  # ширина детали
    fill_factor = models.FloatField(default=1, verbose_name='Фактор площади')  # коэффициент заполнения на листе
    note = models.TextField(blank=True, verbose_name='Примечание')  # примечание (blank=True - значения может не быть)
    otk = models.BooleanField(default=False, verbose_name='Одобрен')  # отработана

    def __str__(self):
        return str(self.name_part)

    def get_absolute_url(self):
        return reverse('form_parts')


class Materials(models.Model):
    name_material = models.CharField(max_length=255, verbose_name='Материал')  # название материала

    def __str__(self):
        return str(self.name_material)

    def get_absolute_url(self):
        return reverse('form_materials')


class Thickness(models.Model):
    thickness = models.CharField(max_length=255, verbose_name='Толщина')  # название материала

    def __str__(self):
        return str(self.thickness)

    def get_absolute_url(self):
        return reverse('form_thickness')


class ReadyOrders(models.Model):
    qty = models.IntegerField(verbose_name='Количество')  # вырезанное количество
    date_time_ready = models.DateTimeField(auto_now_add=True)
    machine = models.ForeignKey('Machine', on_delete=models.PROTECT, verbose_name='Станок')
    ready_qty = models.ForeignKey('Orders', on_delete=models.PROTECT, default='', verbose_name='Готовые')

    def __str__(self):
        return str(self.qty)


class Storage(models.Model):
    name = models.CharField(max_length=255)  # обозначение куска для идентификации
    material = models.ForeignKey('Materials', on_delete=models.PROTECT, verbose_name='Материал')  # материала
    thickness = models.ForeignKey('Thickness', verbose_name='Толщина', on_delete=models.PROTECT)  # толщина материала
    square = models.FloatField()  # количество материала в мкв
    place = models.CharField(max_length=255)  # место где искать кусок


class Machine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Станок')  # станок

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('form_machine')

    def get_first_order(self):
        gfo = 1
        if self.orders_set.filter(priority__gte=1):
            gfo = str(self.orders_set.filter(priority__gte=1).order_by('priority')[0].id)
        return gfo


class CuttingSpeed(models.Model):
    material = models.ForeignKey('Materials', on_delete=models.PROTECT, verbose_name='Материал')  # материал
    thickness = models.ForeignKey('Thickness', on_delete=models.PROTECT, verbose_name='Толщина')  # толщина материала
    machine = models.ForeignKey('Machine', on_delete=models.PROTECT, verbose_name='Станок')  # станок для резки
    speed = models.IntegerField(verbose_name='Скорость')
    time_entrance = models.IntegerField(default=7, verbose_name='Время входа')

    def get_absolute_url(self):
        return reverse('form_cutting_speed')
