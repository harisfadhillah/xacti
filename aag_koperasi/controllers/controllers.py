# -*- coding: utf-8 -*-
# from odoo import http


# class AagKoperasi(http.Controller):
#     @http.route('/aag_koperasi/aag_koperasi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aag_koperasi/aag_koperasi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aag_koperasi.listing', {
#             'root': '/aag_koperasi/aag_koperasi',
#             'objects': http.request.env['aag_koperasi.aag_koperasi'].search([]),
#         })

#     @http.route('/aag_koperasi/aag_koperasi/objects/<model("aag_koperasi.aag_koperasi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aag_koperasi.object', {
#             'object': obj
#         })
