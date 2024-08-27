from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)
class COELeadReport(models.Model):
    _name = 'crm.lead.coe_report'
    _description = 'Custom CRM Lead Report'

    # Add fields or methods if necessary
    def generate_report(self):
        _logger.info('********************* Starting generate_report method.')
        # Import your external script function here
        # from .crm_lead_report_generator import generate_crm_report
        
        # Call your function and handle any Odoo-specific logic
        # report_data = generate_crm_report()
        sample_data = [
            {'lead_name': 'Lead 1', 'team_name': 'Sales Team A', 'custom_data': 'Sample Data 1'},
            {'lead_name': 'Lead 2', 'team_name': 'Sales Team B', 'custom_data': 'Sample Data 2'},
            {'lead_name': 'Lead 3', 'team_name': 'Sales Team C', 'custom_data': 'Sample Data 3'},
        ]
        # Process and return the data as needed

        _logger.info('generate_report method is returning')

        return sample_data
        
    @api.model
    def _get_report_values(self, docids, data=None):
        _logger.warn("************************************ _get_report_values()")
        sample_data = self.generate_report()
        return {
            'doc_ids': docids,
            'doc_model': 'crm.lead.coe_report',
            'docs': sample_data,
        }
