{
    'name': 'GIS CRM extensions',
    'version': '1.0',
    'category': 'GIS',
    'summary': 'GIS CRM Customizations',
    'description': 'Custom CRM and pipeline features',
    'author': 'Christopher Piggott',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'reports/custom_crm_lead_report.xml'
    ],
    'license': 'Other proprietary',
    'installable': True,
    'application': True,
}
