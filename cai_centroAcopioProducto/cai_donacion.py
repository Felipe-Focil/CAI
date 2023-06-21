from odoo import models, fields


class CentroDeAcopio(models.Model):
    _name = 'mi.modulo.centro.acopio'
    _description = 'Centros de Acopio'

    nombre_centro = fields.Char(string='Nombre del Centro')
    lista_productos = fields.One2many('mi.modulo.centro.acopio.producto', 'centro_acopio_id', string='Productos')
    ubicacion = fields.Char(string='Ubicación')
    logo = fields.Binary(string='Logo')
    descripcion_centro = fields.Text(string='Descripción')
    correo_centro = fields.Char(string='Correo')
    numero_centro = fields.Char(string='Número de Contacto')
