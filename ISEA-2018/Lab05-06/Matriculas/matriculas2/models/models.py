# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class matriculas2(models.Model):
#     _name = 'matriculas2.matriculas2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Alumno(models.Model):
     _name = 'matriculas2.alumno'

     name = fields.Char(string="Nombres y Apellidos")
     edad = fields.Integer(string="Edad")
     telefono = fields.Char(String="Teléfono")
     direccion = fields.Char(String="Dirección")
     email = fields.Char(String="Email")
     matricula_id = fields.One2many('matriculas2.matricula', 'alumno_id', string="Matriculas del Alumno")


class Area(models.Model):
     _name = 'matriculas2.area'

     name = fields.Char(string="Área")
     description = fields.Char(string="Descripción")
     curso_ids = fields.One2many('matriculas2.curso', 'area_id', string="Cursos del Area")

class Curso(models.Model):
     _name = 'matriculas2.curso'

     name = fields.Char(string="Curso")
     description = fields.Char(string="Descripción")
     fec_ini = fields.Datetime(string="Fecha de Inicio")
     fec_fin = fields.Datetime(string="Fecha de Finalización")
     area_id = fields.Many2one('matriculas2.area', string="Área")

class Matricula(models.Model):
     _name = 'matriculas2.matricula'

     fecha = fields.Datetime(string="Fecha")
     alumno_id = fields.Many2one('matriculas2.alumno', string="Datos del Alumno")
     curso_id = fields.Many2one('matriculas2.curso', string="Curso")
     

     







