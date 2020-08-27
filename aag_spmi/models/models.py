# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"


    is_spmi = fields.Boolean('Anggota SPMI')
    spmi_med = fields.Selection( [("0","Tidak Dipotong"),("1","Lajang"),("2","Menikah")], string="Sumbangan SPMI")

