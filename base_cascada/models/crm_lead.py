from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    work_address = fields.Char(string='Dirección de la obra')
    property_type = fields.Selection([
        ('flat', 'Piso'),
        ('house', 'Casa'),
        ('premises', 'Local'),
        ('office', 'Oficina'),
        ('other', 'Otros'),
    ], string='Tipo de inmueble')
    work_surface = fields.Float(string='Superficie, m²', digits=(16, 2))
    work_type = fields.Selection([
        ('full_renovation', 'Reforma integral'),
        ('partial_renovation', 'Reforma parcial'),
        ('new_build', 'Obra nueva'),
        ('interior_design', 'Interiorismo'),
    ], string='Tipo de trabajo')
    estimated_budget = fields.Monetary(string='Presupuesto estimado', currency_field='company_currency')
    planned_start_date = fields.Date(string='Fecha prevista de inicio')
    architect_id = fields.Many2one('res.partner', string='Arquitecto / Diseñador')
    lead_origin = fields.Selection([
        ('web', 'Página web'),
        ('referral', 'Recomendación'),
        ('social', 'Redes sociales'),
        ('architect', 'Arquitecto / Diseñador'),
        ('advertising', 'Publicidad'),
        ('phone', 'Llamada telefónica'),
        ('other', 'Otros'),
    ], string='Origen del lead')
