# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aag_koperasi(models.Model):
    _name = 'aag_koperasi.aag_koperasi'
    _description = 'aag_koperasi.aag_koperasi'

    name = fields.Char('NIK')
    
    potongan = fields.Float('Potongan')
    status = fields.Boolean('Status')
    month = fields.Integer('Month')
    year = fields.Integer('Year')