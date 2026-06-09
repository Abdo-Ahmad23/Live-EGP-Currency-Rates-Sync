from odoo import models, fields, api


class CurrencyApiConfig(models.Model):
    _name = 'currency.api.config'
    _description = 'Currency API Configuration'

    name = fields.Char(string="Name", required=True)
    api_key = fields.Char(string="API Key", required=True)

    target_country_id = fields.Many2one(
        'res.country',
        string="Target Country",
        required=True,
        help="Select the country to automatically fetch its currency code"
    )

    target_currency_code = fields.Char(
        string="Currency Code",
        compute="_compute_target_currency_code",
        store=True
    )

    @api.depends('target_country_id')
    def _compute_target_currency_code(self):
        for record in self:
            if record.target_country_id and record.target_country_id.currency_id:
                record.target_currency_code = record.target_country_id.currency_id.name
            else:
                record.target_currency_code = False

    @api.model
    def get_views(self, views, options=None):
        res = super(CurrencyApiConfig, self).get_views(views, options=options)
        if self.search_count([]) > 0:
            for view_data in res.get('views', {}).values():
                import xml.etree.ElementTree as ET
                root = ET.fromstring(view_data['arch'])
                root.set('create', 'false')
                view_data['arch'] = ET.tostring(root, encoding='utf-8').decode('utf-8')
        return res