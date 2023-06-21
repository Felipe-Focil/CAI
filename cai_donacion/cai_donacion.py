from odoo import models, fields


class Donacion(models.Model):
    _name = 'mi.modulo.donacion'
    _description = 'Donaciones'

    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripción')

    id_pedido = fields.Many2one('mi.modulo.donacion', string='ID de la donacion')
    fecha_recepcion = fields.Date(string='Fecha de Recepción')
    fecha_entrega = fields.Date(string='Fecha de Entrega')
    lista_productos = fields.One2many('mi.modulo.donacion', 'donacion_id', string='Productos')
