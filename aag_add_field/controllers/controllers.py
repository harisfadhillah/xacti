# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/addons/aagAddField(http.Controller):
#     @http.route('/custom/addons/aag_add_field/custom/addons/aag_add_field/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/addons/aag_add_field/custom/addons/aag_add_field/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/addons/aag_add_field.listing', {
#             'root': '/custom/addons/aag_add_field/custom/addons/aag_add_field',
#             'objects': http.request.env['custom/addons/aag_add_field.custom/addons/aag_add_field'].search([]),
#         })

#     @http.route('/custom/addons/aag_add_field/custom/addons/aag_add_field/objects/<model("custom/addons/aag_add_field.custom/addons/aag_add_field"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/addons/aag_add_field.object', {
#             'object': obj
#         })
