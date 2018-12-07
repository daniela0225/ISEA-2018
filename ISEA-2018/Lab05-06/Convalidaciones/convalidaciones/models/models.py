# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class convalidaciones(models.Model):
#     _name = 'convalidaciones.convalidaciones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Alumno(models.Model):
     _name = 'convalidaciones.alumno'

     name = fields.Char(string="Nombres y Apellidos")
     edad = fields.Integer(string="Edad")
     localidad = fields.Char(String="Localidad")
     provincia = fields.Char(String="Provincia")
     email = fields.Char(String="Email")
     convalidacion_ids = fields.One2many('convalidaciones.convalidacion', 'alumno_id', string="Convalidaciones del Alumno")

class Modulo(models.Model):
     _name = 'convalidaciones.modulo'

     name = fields.Char(string="Nombre")
     description = fields.Text(string="Descripcion")
     ciclo_ids = fields.Many2many('convalidaciones.ciclo')


class Convalidacion(models.Model):
     _name = 'convalidaciones.convalidacion'

     name = fields.Char()
     fecha_convalidacion = fields.Date(string="Fecha de la Convalidación")
     modulo_id = fields.Many2one('convalidaciones.modulo', string="Modulo")
     alumno_id = fields.Many2one('convalidaciones.alumno', string="Alumno")

class Ciclo(models.Model):
     _name = 'convalidaciones.ciclo'

     name = fields.Char(string="Nombre")
     description = fields.Text(string="Descripcion")
     modulo_ids = fields.Many2many('convalidaciones.modulo')

