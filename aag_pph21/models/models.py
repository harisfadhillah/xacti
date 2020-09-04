# -*- coding: utf-8 -*-

from odoo import models, fields, api

class master_ptkp(models.Model):
    _name = 'aag_master_ptkp'

    name = fields.Char(string="Code PTKP")
    nominal = fields.Integer(string="nominal")

class master_pkp(models.Model):
    _name = 'aag_master_pkp'

    rate = fields.Float(string="Tarif")
    minimum = fields.Integer(string="Penghasilan Minimum")
    maximum = fields.Integer(string="Penghasilan Maximum")
    company_id = fields.Many2one(string="Company", comodel_name="res.company")

class employee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    ptkp_id = fields.Many2one(string='PTKP',comodel_name='aag_master_ptkp')

class company(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'
    pkp_ids = fields.One2many(string='PKP', comodel_name='aag_master_pkp', inverse_name='company_id')
