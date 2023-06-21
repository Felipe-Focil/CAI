from odoo import models, fields


class Producto(models.Model):
    _name = 'mi.modulo.producto'
    _description = 'Productos'

    donacion_id = fields.Many2one('mi.modulo.donacion', string='Donación')
    nombre = fields.Char(string='Nombre del Producto')
    cantidad = fields.Integer(string='Cantidad')
    estatus_entrega = fields.Selection([
        ('recibido', 'Recibido'),
        ('clasificacion', 'En Clasificación'),
        ('almacenamiento', 'En Almacenamiento'),
        ('camino', 'En Camino'),
        ('entregado', 'Entregado'),
        ('perdido', 'Perdido'),
    ], string='Estatus de Entrega')
    talla = fields.Char(string='Talla')
    genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('unisex', 'Unisex'),
    ], string='Género')
    estado_ropa = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
    ], string='Estado de la Ropa')
    peso = fields.Float(string='Peso')
    tipo = fields.Selection([
        ('perecedero', 'Perecedero'),
        ('no_perecedero', 'No Perecedero'),
    ], string='Tipo')
