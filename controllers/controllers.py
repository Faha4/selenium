# -*- coding: utf-8 -*-
from odoo import http

# class LeadIdShow(http.Controller):
#     @http.route('/lead_id_show/lead_id_show/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lead_id_show/lead_id_show/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lead_id_show.listing', {
#             'root': '/lead_id_show/lead_id_show',
#             'objects': http.request.env['lead_id_show.lead_id_show'].search([]),
#         })

#     @http.route('/lead_id_show/lead_id_show/objects/<model("lead_id_show.lead_id_show"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lead_id_show.object', {
#             'object': obj
#         })