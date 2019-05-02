# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ThuaniDashboard(models.Model):
    _name = "thuani.dashboard"
    _description = "thuani Dashboard"

    # Blog
    thuani.nam_blog_url = fields.Char(string="Blog URL", required=False, )




# class thuani(models.Model):
#     _name = 'thuani.thuani'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100