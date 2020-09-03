# -*- coding: utf-8 -*-
# from odoo import http


# class AagAttendancePayroll(http.Controller):
#     @http.route('/aag_attendance_payroll/aag_attendance_payroll/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aag_attendance_payroll/aag_attendance_payroll/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aag_attendance_payroll.listing', {
#             'root': '/aag_attendance_payroll/aag_attendance_payroll',
#             'objects': http.request.env['aag_attendance_payroll.aag_attendance_payroll'].search([]),
#         })

#     @http.route('/aag_attendance_payroll/aag_attendance_payroll/objects/<model("aag_attendance_payroll.aag_attendance_payroll"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aag_attendance_payroll.object', {
#             'object': obj
#         })
