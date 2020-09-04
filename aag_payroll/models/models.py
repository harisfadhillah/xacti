# -*- coding: utf-8 -*-

from datetime import date, datetime, time, timedelta

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, tools, _, SUPERUSER_ID
import pdb
import dateutil.parser
from pytz import timezone

import logging
_logger = logging.getLogger(__name__)

class hr_payslip(models.Model):
    _name = 'hr.payslip'
    _inherit = 'hr.payslip'

    @api.model
    def get_worked_day_lines(self, contracts, date_from, date_to):
        res = super(hr_payslip, self).get_worked_day_lines(contracts, date_from, date_to)
        _logger.info('------ res = %s', res )
        """
        [  { 'name':'Normal Working Days paid at 100%',
             'code':'WORK100',
             'number_of_days':21
             ........
            } 
        ]
        """

        presence = self.get_presence()
        absences = self.get_absences(res,presence)

        res.append({
            'name': 'Presences', 
            'sequence': 20, 
            'code': 'PRES', 
            'number_of_days': presence, 
            'number_of_hours': 0.0, 
            'contract_id': self.contract_id.id })


        res.append({
            'name': 'Absences', 
            'sequence': 30, 
            'code': 'ABS', 
            'number_of_days': absences,
            'number_of_hours': 0.0, 
            'contract_id': self.contract_id.id })

        return res 
        

    def get_presence(self):
        """cari jumlah kehadiran employee self.employee_id"""

        sql = """
            select count(*)
            from hr_attendance 
            where employee_id=%s
            and check_in between %s and %s
        """

        cr = self.env.cr 
        cr.execute(sql, (self.employee_id.id, self.date_from, self.date_to ))
        res = cr.fetchone()

        return res[0]

    def get_absences(self, res, presence):
        """cari jumlah ke tidakhadiran employee self.employee_id"""
        """jumlah hari kerja dikurang jumlah kehadiran adalah absense"""
        if res:
            number_of_days=res[0]['number_of_days']
        else:
            number_of_days=0
        return number_of_days-presence


# class aag_payroll(models.Model):
#     _name = 'aag_payroll.aag_payroll'
#     _description = 'aag_payroll.aag_payroll'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
