from odoo import models, fields


class Donante(models.Model):
    _name = 'cai.donante'
    _description = 'Donantes'

    nombre_donante = fields.Char(string='Nombre del Donante')
    correo_donante = fields.Char(string='Correo del Donante')
    lista_donaciones = fields.One2many('cai.donacion', 'donante_id', string='Donaciones')

    def realizar_donacion(self):
        # Lógica para realizar un pedido
        donacion = self.env['cai.pedido'].create({
            'donante_id': self.id,
            # Otros campos del pedido
        })
        # Realizar acciones adicionales relacionadas con el pedido
        return True

    def obtener_informacion_donacion(self):
        # Lógica para obtener información del pedido
        donacion = self.env['cai.donacion'].search([('donante_id', '=', self.id)], limit=1)
        if donacion:
            # Realizar acciones para obtener información del pedido
            informacion_donacion = donacion.nombre_donacion  # Ejemplo: Obtener el nombre del pedido
            return informacion_donacion
        else:
            return False
