# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    idno = fields.Integer(string='IDNO')
    _sql_constraints = [
        ('idno_unique',
        'unique(idno)',
        'IDNO tidak boleh duplicate - must unique!')
    ]