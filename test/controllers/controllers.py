# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response



class Test(http.Controller):

    @http.route('/test',type='json', methods=['POST'], auth='public', sitemap=False)
    def index(self, **kw):
        # """ {
        #      "params": {
        #          "name":name,
        #          "price":0.0
        #
        #      }}"""
        if kw.get('name', False):
            product=request.env['product.template'].sudo().search([('name','=',kw.get('name', False))])
            if product:
                if kw.get('price', 0) == product.list_price:
                    return False
                else:
                    return True
            else:
                return "not Found"




