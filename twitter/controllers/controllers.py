# -*- coding: utf-8 -*-
# from odoo import http


# class Twitter(http.Controller):
#     @http.route('/twitter/twitter', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/twitter/twitter/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('twitter.listing', {
#             'root': '/twitter/twitter',
#             'objects': http.request.env['twitter.twitter'].search([]),
#         })

#     @http.route('/twitter/twitter/objects/<model("twitter.twitter"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('twitter.object', {
#             'object': obj
#         })
