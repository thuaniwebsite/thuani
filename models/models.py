# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ThuaniPost(models.Model):
    _name = "thuani.post"
    _description = "thuani Post"

    # fields for Heading of the Post (article/blog)
    heading = fields.Char(string="Heading", required=True, )  # Heading (Title) of the Post/Article
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

    base = fields.Char(string="Base", required=False, )
    base_url = fields.Char(string="Base URL", required=False, )

# working
    # @api.onchange('base')
    # def set_base_url(self):
    #     # replace space with dash; make everything lowercase .lower()
    #     self.base_url = str(self.base)
    #     # check if theres data in combine url. If not, make it a string so return has no error bool false not string
    #     if self.combine_url == False:
    #         self.combine_url = 'string'
    #     # if have data, combine the url
    #     else:
    #         self.combine_url = str("/" + self.base_url + "/" + self.heading_url)
    #     return
    #
    # # Making heading replace space with dash; make all heading lowercase. When heading is updated, the url is updated
    # @api.onchange('heading')
    # def set_heading_url(self):
    #     # replace space with dash; make everything lowercase .lower()
    #     self.heading_url = str(self.heading).replace(' ', '-').lower()
    #     self.combine_url = str("/" + self.base_url + "/" + self.heading_url)
    #     return




    # base url. When base is updated
    # @api.onchange('base')
    # def set_lower(self):
    #     # replace space with dash; make everything lowercase .lower()
    #     self.base_url = str(self.base).lower()
    #     return

    # # combine url. When base is updated; or heading is updated
    # @api.onchange('base_url')
    # def set_lower(self):
    #     # replace space with dash; make everything lowercase .lower()
    #     self.combine_url = str(self.base_url+self.heading).lower()
    #     return
    # @api.onchange('heading_url')
    # def set_lower(self):
    #     # replace space with dash; make everything lowercase .lower()
    #     self.combine_url = str(self.base_url+self.heading).lower()
    #     return

# TODO: Check for unique url when all is combined. If not unique at serial number in postname


# @api.onchange('heading')
# def set_upper(self):
#     self.heading = str(self.heading).upper()
#     return


# @api.onchange('heading')
# def onchange_case(self, default_code):
#     result = {'value': {
#         'default_code': str(default_code).lower()
#         }
#     }
#     return result

# heading = fields.Char(string="Heading", required=False, )
# heading_url_lower_copy = fields.Char(string="Heading URL Lower Copy", related='heading')
# heading_url = fields.Char(string="Heading URL Lower Copy", related='heading_url_lower_copy')
# heading_url[1] = heading_url[1].lower()

# @api.onchange('heading')
# def set_code(self, heading_url):
#     if not heading_url:
#         return False
#     return heading_url.lower()


# @api.onchange('heading')
# def set_code(self):
#     if not heading:
#         self.heading_url = self.heading.lower()
#     return self

# def _sanitize_email(self, email):
#     """ Sanitize and standardize blacklist entries: all emails should be
#     only real email extracted from strings (A <a@a> -> a@a)  and should be
#     lower case. """
#     emails = tools.email_split(email)
#     if not emails or len(emails) != 1:
#         return False
#     return emails[0].lower()

# @api.onchange('heading')
# def set_code(self):
#     self.heading_url = self.heading.lower()

# if heading_url_lower_copy is not None:
#     heading_url_lower = str(heading_url_lower_copy).lower()
# return heading_url_lower_copy

# url_text = fields.Text()
# url_text = heading_url_lower_copy
# if heading_url_lower_copy is not None:
#     heading_url_lower = heading_url_lower_copy(string="Heading URL Lower")

# heading_url = fields.Char(string="Heading URL", required=False, )


# makes heading_url = heading field
# heading_url = heading_url.lower()

# when heading is changed, this gets done. Makes heading url same as heading, and lower case
# has problems when creating new heading
# @api.onchange('heading')
# def set_code(self):
#     self.heading_url = self.heading.lower()


# heading_url = heading

# get heading and turn it into url
# fox.lower()       # all lower cases

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
