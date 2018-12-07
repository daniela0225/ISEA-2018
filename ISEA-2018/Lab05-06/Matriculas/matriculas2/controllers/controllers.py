# -*- coding: utf-8 -*-
from odoo import http

# class Matriculas2(http.Controller):
#     @http.route('/matriculas2/matriculas2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/matriculas2/matriculas2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('matriculas2.listing', {
#             'root': '/matriculas2/matriculas2',
#             'objects': http.request.env['matriculas2.matriculas2'].search([]),
#         })

#     @http.route('/matriculas2/matriculas2/objects/<model("matriculas2.matriculas2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('matriculas2.object', {
#             'object': obj
#         })