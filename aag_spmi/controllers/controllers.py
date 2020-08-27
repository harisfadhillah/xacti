# -*- coding: utf-8 -*-
# from odoo import http


# class AagSpmi(http.Controller):
#     @http.route('/aag_spmi/aag_spmi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aag_spmi/aag_spmi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aag_spmi.listing', {
#             'root': '/aag_spmi/aag_spmi',
#             'objects': http.request.env['aag_spmi.aag_spmi'].search([]),
#         })

#     @http.route('/aag_spmi/aag_spmi/objects/<model("aag_spmi.aag_spmi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aag_spmi.object', {
#             'object': obj
#         })
