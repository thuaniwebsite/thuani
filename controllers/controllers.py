# -*- coding: utf-8 -*-
from odoo import http

# class Thuani(http.Controller):
#     @http.route('/thuani/thuani/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/thuani/thuani/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('thuani.listing', {
#             'root': '/thuani/thuani',
#             'objects': http.request.env['thuani.thuani'].search([]),
#         })

#     @http.route('/thuani/thuani/objects/<model("thuani.thuani"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('thuani.object', {
#             'object': obj
#         })