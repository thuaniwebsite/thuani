# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ThuaniCategoryCombine3(models.Model):
    _name = "thuani.category.combine3"
    _description = "thuani Category Combine3"
    _rec_name = "heading"

    heading = fields.Char(string="Heading", required=False, )  # Heading (Title) of the Post/Article
    url_heading = fields.Char(string="URL Heading", required=False, )  # URL of the post

    category1 = fields.Char(string="Cat1", required=False, )
    category2 = fields.Char(string="Cat2", required=False, )
    category3 = fields.Char(string="Cat3", required=False, )
    category4 = fields.Char(string="Cat4", required=False, )
    category5 = fields.Char(string="Cat5", required=False, )
    category6 = fields.Char(string="Cat6", required=False, )
    category7 = fields.Char(string="Cat7", required=False, )
    url_category1 = fields.Char(string="URL cat1", required=False, )
    url_category2 = fields.Char(string="URL cat2", required=False, )
    url_category3 = fields.Char(string="URL cat3", required=False, )
    url_category4 = fields.Char(string="URL cat4", required=False, )
    url_category5 = fields.Char(string="URL cat5", required=False, )
    url_category6 = fields.Char(string="URL cat6", required=False, )
    url_category7 = fields.Char(string="URL cat7", required=False, )

    url_combine = fields.Char(string="URL Combine", required=False, )

    # Making heading replace space with dash; make all heading lowercase. When heading is updated, the url is updated
    @api.onchange('heading')
    def set_url_heading(self):
        # at creation, check if == false, change to string
        if self.heading == False:
            self.url_heading = ""
        else:
            self.url_heading = str(self.heading).replace(' ', '-').lower()
        if self.category1 == False:
            self.url_category1 = ""
        else:
            self.url_category1 = str(self.category1).replace(' ', '-').lower()
        if self.url_combine == False:
            self.url_combine = ""
        # heading no data
        if self.heading == "":
            # heading no data; category1 no data; str(" heading no data, category no data a")
            if self.category1 == "":
                self.url_combine = str("")
            # heading no data; category has data; str("/" + self.url_category1 + " heading no data, category has data b")
            else:
                self.url_combine = str("/" + self.url_category1)
        # heading has data
        else:
            # heading has data, category1 no data; str("/" + self.url_heading + " heading has data, cat no data c")
            if self.category1 == "":
                self.url_combine = str("/" + self.url_heading)
            # Heading has data, category1 has data; str("/" + self.url_category1 + "/" + self.url_heading + " heading has data, cat has data d")
            else:
                self.url_combine = str("/" + self.url_category1 + "/" + self.url_heading)
        return

    # Making category1 replace space with dash; make all heading lowercase. When heading is updated, the url is updated
    @api.onchange('category1')
    def set_url_category1(self):
        if self.heading == False:
            self.url_heading = ""
        if self.category1 == False:
            self.url_category1 = ""
        if self.url_combine == False:
            self.url_combine = ""
        # if self.url_combine == False:
        #     self.url_combine = ""
        # replace space with dash; make everything lowercase .lower()
        self.url_category1 = str(self.category1).replace(' ', '-').lower()
        # if category1 has NO data
        if not self.category1:
            self.url_combine = str("/" + self.url_heading)
        # if category1 HAS data
        else:
            self.url_combine = str("/" + self.url_category1 + "/" + self.url_heading)
        return

    @api.onchange('url_combine')
    def set_url_combine(self):
        # at creation, check if = false, change to string
        if self.heading == False:
            self.url_heading = ""
        else:
            self.url_heading = str(self.heading).replace(' ', '-').lower()
        if self.category1 == False:
            self.url_category1 = ""
        else:
            self.url_category1 = str(self.category1).replace(' ', '-').lower()
        if self.url_combine == False:
            self.url_combine = ""
        return


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


class ThuaniCategory(models.Model):
    _name = "thuani.category"
    _description = "thuani Category"
    _rec_name = "category"

    # notation for string heading Category = String Cat; eg Cat1, Cat2 means category url rank 1, then rank 2 (Cat2)
    # Combined category url = /url_cat1/url_cat2/url_cat3/ etc
    # Category for the Post.
    # url is linked to Category for now. In future can be change to dynamic

    category = fields.Char(string="Cat", required=False, )
    url_category = fields.Char(string="URL Cat", required=False, )


class ThuaniCategoryCombine(models.Model):
    _name = "thuani.category.combine"
    _description = "thuani Category Combine"
    _rec_name = "category_combine"

    # category_combine = fields.Selection(string="Category1", selection=[('thuani.category')], required=False, )

    category_combine = fields.Many2one(comodel_name="thuani.category", string="Category Combine", required=False, )


class ThuaniCategoryCombine2(models.Model):
    _name = "thuani.category.combine2"
    _description = "thuani Category Combine2"
    _rec_name = "category_combine2"

    # category_combine = fields.Selection(string="Category1", selection=[('thuani.category')], required=False, )

    category_combine2 = fields.Many2one(comodel_name="thuani.category", string="Category Combine2", required=False, )

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


class ThuaniCategory1(models.Model):
    _name = "thuani.category1"
    _description = "thuani Category1"
    _rec_name = "category1"

    # notation for string heading Category = String Cat; eg Cat1, Cat2 means category url rank 1, then rank 2 (Cat2)
    # Combined category url = /url_cat1/url_cat2/url_cat3/ etc
    # Category for the Post.
    # url is linked to Category for now. In future can be change to dynamic

    category1 = fields.Char(string="Cat1", required=False, )
    url_category1 = fields.Char(string="URL Cat1", required=False, )


class ThuaniCategory2(models.Model):
    _name = "thuani.category2"
    _description = "thuani Category2"
    _rec_name = "category2"

    category2 = fields.Char(string="Cat2", required=False, )
    url_category2 = fields.Char(string="URL Cat2", required=False, )


class ThuaniCategory3(models.Model):
    _name = "thuani.category3"
    _description = "thuani Category3"
    _rec_name = "category3"

    category3 = fields.Char(string="Cat3", required=False, )
    url_category3 = fields.Char(string="URL Cat3", required=False, )


class ThuaniCategory4(models.Model):
    _name = "thuani.category4"
    _description = "thuani Category4"
    _rec_name = "category4"

    category4 = fields.Char(string="Cat4", required=False, )
    url_category4 = fields.Char(string="URL Cat4", required=False, )


class ThuaniCategory5(models.Model):
    _name = "thuani.category5"
    _description = "thuani Category5"
    _rec_name = "category5"

    category5 = fields.Char(string="Cat5", required=False, )
    url_category5 = fields.Char(string="URL Cat5", required=False, )


class ThuaniCategory6(models.Model):
    _name = "thuani.category6"
    _description = "thuani Category6"
    _rec_name = "category6"

    category6 = fields.Char(string="Cat6", required=False, )
    url_category6 = fields.Char(string="URL Cat6", required=False, )


class ThuaniCategory7(models.Model):
    _name = "thuani.category7"
    _description = "thuani Category7"
    _rec_name = "category7"

    category7 = fields.Char(string="Cat7", required=False, )
    url_category7 = fields.Char(string="URL Cat7", required=False, )


class ThuaniCategory8(models.Model):
    _name = "thuani.category8"
    _description = "thuani Category8"
    _rec_name = "category8"

    category8 = fields.Char(string="Cat8", required=False, )
    url_category8 = fields.Char(string="URL Cat8", required=False, )


class ThuaniCategoryCombine3(models.Model):
    _name = "thuani.category.combine3"
    _description = "thuani Category Combine3"
    _rec_name = "heading"

    heading = fields.Char(string="Heading", required=False, )  # Heading (Title) of the Post/Article
    url_heading = fields.Char(string="URL Heading", required=False, )  # URL of the post

    category1 = fields.Char(string="Cat1", required=False, )
    category2 = fields.Char(string="Cat2", required=False, )
    category3 = fields.Char(string="Cat3", required=False, )
    category4 = fields.Char(string="Cat4", required=False, )
    category5 = fields.Char(string="Cat5", required=False, )
    category6 = fields.Char(string="Cat6", required=False, )
    category7 = fields.Char(string="Cat7", required=False, )
    url_category1 = fields.Char(string="URL cat1", required=False, )
    url_category2 = fields.Char(string="URL cat2", required=False, )
    url_category3 = fields.Char(string="URL cat3", required=False, )
    url_category4 = fields.Char(string="URL cat4", required=False, )
    url_category5 = fields.Char(string="URL cat5", required=False, )
    url_category6 = fields.Char(string="URL cat6", required=False, )
    url_category7 = fields.Char(string="URL cat7", required=False, )

    url_combine = fields.Char(string="URL Combine", required=False, )

    # Making heading replace space with dash; make all heading lowercase. When heading is updated, the url is updated
    @api.onchange('heading')
    def set_url_heading(self):
        # at creation, check if == false, change to string
        if self.heading == False:
            self.url_heading = ""
        else:
            self.url_heading = str(self.heading).replace(' ', '-').lower()
        if self.category1 == False:
            self.url_category1 = ""
        else:
            self.url_category1 = str(self.category1).replace(' ', '-').lower()
        if self.url_combine == False:
            self.url_combine = ""
        # heading no data
        if self.heading == "":
            # heading no data; category1 no data; str(" heading no data, category no data a")
            if self.category1 == "":
                self.url_combine = str("")
            # heading no data; category has data; str("/" + self.url_category1 + " heading no data, category has data b")
            else:
                self.url_combine = str("/" + self.url_category1)
        # heading has data
        else:
            # heading has data, category1 no data; str("/" + self.url_heading + " heading has data, cat no data c")
            if self.category1 == "":
                self.url_combine = str("/" + self.url_heading)
            # Heading has data, category1 has data; str("/" + self.url_category1 + "/" + self.url_heading + " heading has data, cat has data d")
            else:
                self.url_combine = str("/" + self.url_category1 + "/" + self.url_heading)
        return

    # Making category1 replace space with dash; make all heading lowercase. When heading is updated, the url is updated
    @api.onchange('category1')
    def set_url_category1(self):
        if self.heading == False:
            self.url_heading = ""
        if self.category1 == False:
            self.url_category1 = ""
        if self.url_combine == False:
            self.url_combine = ""
        # if self.url_combine == False:
        #     self.url_combine = ""
        # replace space with dash; make everything lowercase .lower()
        self.url_category1 = str(self.category1).replace(' ', '-').lower()
        # if category1 has NO data
        if not self.category1:
            self.url_combine = str("/" + self.url_heading)
        # if category1 HAS data
        else:
            self.url_combine = str("/" + self.url_category1 + "/" + self.url_heading)
        return

    @api.onchange('url_combine')
    def set_url_combine(self):
        # at creation, check if = false, change to string
        if self.heading == False:
            self.url_heading = ""
        else:
            self.url_heading = str(self.heading).replace(' ', '-').lower()
        if self.category1 == False:
            self.url_category1 = ""
        else:
            self.url_category1 = str(self.category1).replace(' ', '-').lower()
        if self.url_combine == False:
            self.url_combine = ""
        return


class ThuaniCategoryCombine4(models.Model):
    _name = "thuani.category.combine4"
    _description = "thuani Category Combine4"
    _rec_name = "heading"

    heading = fields.Char(string="Heading", required=False, )  # Heading (Title) of the Post/Article
    url_heading = fields.Char(string="URL Heading", required=False, )  # URL of the post

    category1 = fields.Char(string="Cat1", required=False, )
    category2 = fields.Char(string="Cat2", required=False, )
    category3 = fields.Char(string="Cat3", required=False, )
    category4 = fields.Char(string="Cat4", required=False, )
    category5 = fields.Char(string="Cat5", required=False, )
    category6 = fields.Char(string="Cat6", required=False, )
    category7 = fields.Char(string="Cat7", required=False, )
    url_category1 = fields.Char(string="URL cat1", required=False, )
    url_category2 = fields.Char(string="URL cat2", required=False, )
    url_category3 = fields.Char(string="URL cat3", required=False, )
    url_category4 = fields.Char(string="URL cat4", required=False, )
    url_category5 = fields.Char(string="URL cat5", required=False, )
    url_category6 = fields.Char(string="URL cat6", required=False, )
    url_category7 = fields.Char(string="URL cat7", required=False, )

    url_combine = fields.Char(string="URL Combine", required=False, )

    # Making heading replace space with dash; make all heading lowercase. When heading is updated, the url is updated
    @api.onchange('heading')
    def set_url_heading(self):
        # at creation, check if == false, change to string
        if self.heading == False:
            self.url_heading = ""
        else:
            self.url_heading = str(self.heading).replace(' ', '-').lower()
        if self.category1 == False:
            self.url_category1 = ""
        else:
            self.url_category1 = str(self.category1).replace(' ', '-').lower()
        if self.url_combine == False:
            self.url_combine = ""
        # heading no data
        if self.heading == "":
            # heading no data; category1 no data; str(" heading no data, category no data a")
            if self.category1 == "":
                self.url_combine = str("")
            # heading no data; category has data; str("/" + self.url_category1 + " heading no data, category has data b")
            else:
                self.url_combine = str("/" + self.url_category1)
        # heading has data
        else:
            # heading has data, category1 no data; str("/" + self.url_heading + " heading has data, cat no data c")
            if self.category1 == "":
                self.url_combine = str("/" + self.url_heading)
            # Heading has data, category1 has data; str("/" + self.url_category1 + "/" + self.url_heading + " heading has data, cat has data d")
            else:
                self.url_combine = str("/" + self.url_category1 + "/" + self.url_heading)
        return

    # Making category1 replace space with dash; make all heading lowercase. When heading is updated, the url is updated
    @api.onchange('category1')
    def set_url_category1(self):
        if self.heading == False:
            self.url_heading = ""
        if self.category1 == False:
            self.url_category1 = ""
        if self.url_combine == False:
            self.url_combine = ""
        # if self.url_combine == False:
        #     self.url_combine = ""
        # replace space with dash; make everything lowercase .lower()
        self.url_category1 = str(self.category1).replace(' ', '-').lower()
        # if category1 has NO data
        if not self.category1:
            self.url_combine = str("/" + self.url_heading)
        # if category1 HAS data
        else:
            self.url_combine = str("/" + self.url_category1 + "/" + self.url_heading)
        return

    @api.onchange('url_combine')
    def set_url_combine(self):
        # at creation, check if = false, change to string
        if self.heading == False:
            self.url_heading = ""
        else:
            self.url_heading = str(self.heading).replace(' ', '-').lower()
        if self.category1 == False:
            self.url_category1 = ""
        else:
            self.url_category1 = str(self.category1).replace(' ', '-').lower()
        if self.url_combine == False:
            self.url_combine = ""
        return
