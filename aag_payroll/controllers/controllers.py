# -*- coding: utf-8 -*-
# from odoo import http


# class AagPayroll(http.Controller):
#     @http.route('/aag_payroll/aag_payroll/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aag_payroll/aag_payroll/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aag_payroll.listing', {
#             'root': '/aag_payroll/aag_payroll',
#             'objects': http.request.env['aag_payroll.aag_payroll'].search([]),
#         })

#     @http.route('/aag_payroll/aag_payroll/objects/<model("aag_payroll.aag_payroll"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aag_payroll.object', {
#             'object': obj
#         })
