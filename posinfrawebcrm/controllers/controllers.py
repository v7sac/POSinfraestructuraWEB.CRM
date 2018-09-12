# -*- coding: utf-8 -*-
from openerp import http

# class Infrasan(http.Controller):
#     @http.route('/infrasan/infrasan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infrasan/infrasan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infrasan.listing', {
#             'root': '/infrasan/infrasan',
#             'objects': http.request.env['infrasan.infrasan'].search([]),
#         })

#     @http.route('/infrasan/infrasan/objects/<model("infrasan.infrasan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infrasan.object', {
#             'object': obj
#         })