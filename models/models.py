# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ThuaniPost(models.Model):
    _name = "thuani.post"
    _description = "thuani Post"

    # fields for Heading of the Post (article/blog). False bc for future templating. Check in future
    heading = fields.Char(string="Heading", required=False, )  # Heading (Title) of the Post/Article
    heading_url = fields.Char(string="Heading URL", required=False, )  # URL of the post

    base = fields.Char(string="Base", required=False, )
    base_url = fields.Char(string="Base URL", required=False, )

    # Combine URL
    combine_url = fields.Char(string="Combine URL", required=False, )

    @api.onchange('base')
    def set_base_url(self):
        # make base url same as base data; make everything lowercase .lower()
        self.base_url = str(self.base).lower()
        # check if theres data in combine url. If not, make it a string so return has no error bool false not string
        if self.combine_url == False:
            self.combine_url = 'string'
        # if have data, combine the url
        elif not self.base:
            # if base has no data, just use post heading
            self.combine_url = str("/" + self.heading_url)
        else:
            # if base has data, do normal combine all
            self.combine_url = str("/" + self.base_url + "/" + self.heading_url)
        return

    # Making heading replace space with dash; make all heading lowercase. When heading is updated, the url is updated
    @api.onchange('heading')
    def set_heading_url(self):
        # replace space with dash; make everything lowercase .lower()
        self.heading_url = str(self.heading).replace(' ', '-').lower()
        if not self.base:
            # if base has no data
            self.combine_url = str("/" + self.heading_url)
        else:
            # else combine as normal
            self.combine_url = str("/" + self.base_url + "/" + self.heading_url)
        return


class ThuaniBase(models.Model):
    _name = "thuani.base"
    _description = "thuani Base"
    _rec_name = "base"  # makes the name linked to the field you want to display for many2one. If datafield
    # has name = , then no need for rec_name as it's default is to datafield name

    base = fields.Char(string="Base", required=False, )
    base_url = fields.Char(string="Base URL", required=False, )


class ThuaniPost2(models.Model):
    _name = "thuani.post2"
    _description = "thuani Post2"

    # this takes data from thuani.base in field base (rec name is base)
    base_many = fields.Many2one(comodel_name="thuani.base", string="Base Many", required=False, )


# class ThuaniCategoryRank(models.Model):
#     _name = "thuani.category.rank"
#     _description = "thuani Category Rank"
#     _rec_name = "category_rank"
#
#     category_rank = fields.Char(string="Category Rank", required=False, )
#     odoofield


class ThuaniCategory(models.Model):
    _name = "thuani.category"
    _description = "thuani Category"
    _rec_name = "category"

    category = fields.Char(string="Category", required=False, )
    category_url = fields.Char(string="Category URL", required=False, )


class ThuaniCategoryCombine(models.Model):
    _name = "thuani.category.combine"
    _description = "thuani Category Combine"
    _rec_name = "category_combine"

    # category_combine = fields.Selection(string="Category1", selection=[('thuani.category')], required=False, )

    category_combine = fields.Many2one(comodel_name="thuani.category", string="Category Combine", required=False, )

    # @api.multi
    # def method_name(self):
    #     view_id = self.env.ref('thuani.category.tree_view_thuani_category').id
    #     context = self._context.copy()
    #     return {
    #         'name': 'form_name',
    #         'view_type': 'form',
    #         'view_mode': 'tree',
    #         'views': [(view_id, 'form')],
    #         'res_model': 'thuani.category',
    #         'view_id': view_id,
    #         'type': 'ir.actions.act_window',
    #         'res_id': self.id,
    #         'target': 'new',
    #         'context': context,
    #     }


# TODO: Check for unique url when all is combined. If not unique at serial number in postname

# Create new menu:
# models/models.py make new class >
# views/xmlname.xml create odooform; odootree; odooaction; menu >
# security/ir.model.access.csv add new line >
# access_thuani_category_combine,thuani.thuani,model_thuani_category_combine,,1,1,1,1
# access_uniqueNameOfClass; model_ is _name in your class


class ThuaniCheckbox(models.Model):
    _name = "thuani.checkbox"
    _description = "thuani Checkbox"

    blue = fields.Boolean('Blue')
    pink = fields.Boolean('Pink')
    yellow = fields.Boolean('Yellow')
