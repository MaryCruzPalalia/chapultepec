# -*- coding: utf-8 -*-

# from odoo import api
# from odoo import fields
# from odoo import models
# from odoo.exceptions import UserError
# from odoo.exceptions import ValidationError

# class FacturaParcial(models.Model):
#     _inherit = 'account.invoice'

#     x_student = fields.char(string='hola')


#     @api.depends('partner_id')
#     def _compute_depends(self):
#         print(self.id)
#         print(self.name)
#         print(self)
#         print(self.type)
#         #id_x= self.env['op.student'].search([('invoice_ids', '=', self.id)])
#         self.x_student="hola" #id_x.name
#        # print(self.x_student)
#        # return self.x_student

