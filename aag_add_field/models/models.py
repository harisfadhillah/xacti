# -*- coding: utf-8 -*-

from odoo import models, fields, api


class employee(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    x_idno = fields.Integer(string='IDNO')
    x_empsts = fields.Char(string='Empl. Status')
    x_allcd = fields.Char(string='Code Golongan')
    x_spmi = fields.Boolean(string='SPMI')
    x_spmi_med = fields.Integer(string='SPMI Med')
    x_nokop = fields.Char(string='NO Koperasi')
    x_nobpjskes = fields.Char(string='NO BPJSKES')
    x_bpjskesadd = fields.Integer(string='Tambahan BPJS KES')
    x_nobpjstk = fields.Char(string='NO BPJSTK')
    x_nobpjspen = fields.Char(string='NO BPJS Pensiun')
    x_npwp = fields.Char(string='NPWP')

    idno = fields.Integer(string='IDNO')

    _sql_constraints = [
        ('x_idno_unique',
         'unique(x_idno)',
        'IDNO tidak boleh duplicate - must unique!'),
        ('x_nokop_unique',
         'unique(x_nokop)',
         'IDKOP tidak boleh duplicate - must unique!'),
        ('x_nobpjskes_unique',
         'unique(x_nobpjskes,x_idno)',
         'IDBPJSKES tidak boleh duplicate - must unique!'),
        ('x_bpjstk_unique',
         'unique(x_nobpjstk,x_idno)',
         'NOBPJSTK tidak boleh duplicate - must unique!'),
        ('x_nobpjspen_unique',
         'unique(x_nobpjspen,x_idno)',
         'IDNO tidak boleh duplicate - must unique!'),
        ('x_npwp_unique',
         'unique(x_npwp,x_idno)',
         'NPWP tidak boleh duplicate - must unique!'),
    ]




class contract(models.Model):
    _name = 'hr.contract'
    _inherit = 'hr.contract'
    x_tpk = fields.Integer(string='TPK')
    x_occup = fields.Integer(string='Tunj. Golongan')
    x_family = fields.Integer(string='Tunj. Keluarga')
    x_functional = fields.Integer(string='Tunj. Fungsional')
    x_trans = fields.Integer(string='Tunj. Transportasi')
    x_perform = fields.Integer(string='Tunj. Prestasi')
    x_other = fields.Integer(string='Lain-Lain')
    x_presence = fields.Integer(string='Tunj. Kehadiran')
    x_shift = fields.Integer(string='Tunj. Shift/Harian')
    x_ovtrate = fields.Integer(string='Rate Overtime/Jam')

class company(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'
    x_meal = fields.Integer(string='Uang makan/hari')