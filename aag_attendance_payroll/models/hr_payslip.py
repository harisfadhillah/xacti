from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class hr_payslip(models.Model):
    _name = 'hr.payslip'
    _inherit = 'hr.payslip'


    @api.model
    def get_worked_day_lines(self, contracts, date_from, date_to):
        res = super(hr_payslip, self).get_worked_day_lines( contracts, date_from, date_to )
        _logger.info('----- get_worked_day_lines = %s', res )
        return res 
