# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ThuaniPost(models.Model):
    _name = "thuani.post"
    _description = "thuani Post"

    heading = fields.Char(string="Heading", required=False, )
    heading_url = fields.Char(string="Heading URL", required=False, )

# class ThuaniDashboard(models.Model):
#     _name = "thuani.dashboard"
#     _description = "thuani Dashboard"
#
#     name = fields.Char(string="Dashboard", required=False, )
#     thuani_blog_url_permalink = fields.Char(string="Blog URL", required=False, )
#     thuani_blog_url_category = fields.Char(string="Category", required=False, )
#     thuani_blog_url_postname = fields.Char(string="Postname", required=False, )
#     website_name = fields.Char(string="Website Name", required=False, )
#
# class ThuaniBlog(models.Model):
#     _name = "thuani.blog"
#     _description = "thuani Blog"
#
#     blog_category = fields.Char(string="Blog Category", required=False, )
#
#
# class Thuani.Post(models.Model):
#     _name = "thuani.post"
#     _description = "thuani Post"
#
#     heading = fields.Char(string="Heading", required=False, )