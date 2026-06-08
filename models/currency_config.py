from odoo import models, fields

class CurrencyApiConfig(models.Model):
    _name = 'currency.api.config'
    _description = 'ExchangeRate-API Configuration'

    name = fields.Char(string="Provider Name", default="ExchangeRate-API", required=True)
    api_key = fields.Char(string="API Key", required=True, password=True)