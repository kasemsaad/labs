{
    'name': 'HMS',
    'author': 'kasem',
    'website': 'https://iti.gov.eg/home',
    'description': 'System for hms',
    'version': '3.0.1',
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/hmsviews.xml',
        'views/doctorsviews.xml',
        'views/departmentsviews.xml',
        'reports/hms_patient_template.xml',
        'reports/reports.xml',
        'views/inherit.xml'
    ],
    'depends': ['base', 'crm'],
    # 'installable': True
}
