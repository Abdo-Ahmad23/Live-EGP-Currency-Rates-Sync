import requests
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    @api.model
    def action_sync_egp_rates(self):
        config = self.env['currency.api.config'].search([], limit=1)

        if not config or not config.api_key:
            _logger.error("Currency Sync Failed: No API Key found in Configuration menu!")
            return

        if not config.target_currency_code:
            _logger.error("Currency Sync Failed: No Target Country/Currency configured!")
            return

        api_key = config.api_key
        base_currency_code = config.target_currency_code


        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency_code}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get('result') == 'success':
                rates = data.get('conversion_rates', {})
                today_date = fields.Date.today()
                current_company_id = self.env.company.id

                active_currencies = self.search([('active', '=', True)])

                for currency in active_currencies:
                    currency_code = currency.name


                    if currency_code == base_currency_code:
                        continue

                    if currency_code in rates:
                        new_rate = rates[currency_code]

                        existing_rate = self.env['res.currency.rate'].search([
                            ('currency_id', '=', currency.id),
                            ('name', '=', today_date),
                            ('company_id', '=', current_company_id)
                        ], limit=1)

                        if existing_rate:
                            existing_rate.write({'rate': new_rate})
                            _logger.info(f"Updated rate for {currency_code} to {new_rate} against {base_currency_code}")
                        else:
                            self.env['res.currency.rate'].create({
                                'currency_id': currency.id,
                                'rate': new_rate,
                                'name': today_date,
                                'company_id': current_company_id
                            })
                            _logger.info(
                                f"Created new rate for {currency_code} to {new_rate} against {base_currency_code}")
            else:
                _logger.error(f"ExchangeRate-API Error: {data.get('error-type')}")
        except Exception as e:
            _logger.error(f"Currency Sync Exception: {str(e)}")