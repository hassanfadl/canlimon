# -*- coding: utf-8 -*-
from odoo import http


class Test(http.Controller):

    @http.route('/test', auth='public')
    def index(self, **kw):
        # """ {
        #      "params": {
        #          "name":name,
        #          "price":0.0
        #
        #      }}"""
        if kw.get('name', False):
            product=self.env['product.product'].sudo().search([('name','=',kw.get('name', False))])
            if kw.get('price', 0) == product.list_price:
                return False
            else:
                return True




