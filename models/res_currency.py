import requests
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    @api.model
    def action_sync_egp_rates(self):
        api_key = "YOUR_FREE_API_KEY_HERE" 
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EGP"
        target_currencies = ['USD', 'EUR', 'SAR']
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get('result') == 'success':
                rates = data.get('conversion_rates', {})
                today_date = fields.Date.today()
                current_company_id = self.env.company.id
                
                for currency_code in target_currencies:
                    if currency_code in rates:
                        currency = self.search([('name', '=', currency_code), ('active', '=', True)], limit=1)
                        
                        if currency:
                            new_rate = rates[currency_code]
                            
                            existing_rate = self.env['res.currency.rate'].search([
                                ('currency_id', '=', currency.id),
                                ('name', '=', today_date),
                                ('company_id', '=', current_company_id)
                            ], limit=1)
                            
                            if existing_rate:
                                existing_rate.write({'rate': new_rate})
                                _logger.info(f"Updated rate for {currency_code} to {new_rate}")
                            else:
                                self.env['res.currency.rate'].create({
                                    'currency_id': currency.id,
                                    'rate': new_rate,
                                    'name': today_date,
                                    'company_id': current_company_id
                                })
                                _logger.info(f"Created new rate for {currency_code} to {new_rate}")
            else:
                _logger.error(f"ExchangeRate-API Error: {data.get('error-type')}")
        except Exception as e:
            _logger.error(f"Currency Sync Exception: {str(e)}")
