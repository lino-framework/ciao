# -*- coding: UTF-8 -*-
# Copyright 2019-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
Base Django settings for Lino Ciao applications.

"""

from lino.projects.std.settings import *
from lino.api.ad import _
from lino_ciao import SETUP_INFO

class Site(Site):

    verbose_name = "Lino Ciao"
    version = SETUP_INFO['version']
    url = "http://ciao.lino-framework.org/"
    help_url = "http://ciao.lino-framework.org/user/index"

    demo_fixtures = ['std', 'demo', 'demo2']
    # project_model = 'tickets.Project'
    # project_model = 'deploy.Milestone'
    textfield_format = 'html'
    custom_layouts_module = 'lino_ciao.lib.ciao.custom_layouts'
    user_types_module = 'lino_ciao.lib.ciao.user_types'
    workflows_module = 'lino_ciao.lib.ciao.workflows'
    obj2text_template = "**{0}**"

    # default_build_method = 'appyodt'
    default_build_method = 'weasy2pdf'
    default_ui = 'lino_react.react'

    # experimental use of rest_framework:
    # root_urlconf = 'lino_book.projects.team.urls'

    # migration_class = 'lino_ciao.lib.ciao.migrate.Migrator'

    auto_configure_logger_names = "atelier django lino lino_xl lino_ciao"

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        # yield 'lino.modlib.extjs'
        # yield 'lino.modlib.bootstrap3'
        # yield 'lino.modlib.gfks'
        # yield 'lino.modlib.system'
        # yield 'lino.modlib.users'
        yield 'lino_ciao.lib.users'
        yield 'lino_ciao.lib.contacts'
        # yield 'lino_xl.lib.online.users'
        yield 'lino_xl.lib.cal'
        yield 'lino_xl.lib.calview'
        yield 'lino.modlib.publisher'
        # yield 'lino_xl.lib.sepa'
        # yield 'lino_xl.lib.extensible'
        # yield 'lino_xl.lib.addresses'
        # yield 'lino_xl.lib.phones'
        #yield 'lino_xl.lib.households'
        #yield 'lino_xl.lib.humanlinks'
        # yield 'lino_xl.lib.cv'
        # yield 'lino_noi.lib.courses'
        # yield 'lino_noi.lib.products'

        yield 'lino_ciao.lib.topics'
        # yield 'lino_xl.lib.votes'
        # yield 'lino_ciao.lib.tickets'
        # yield 'lino_xl.lib.skills'
        # yield 'lino_xl.lib.deploy'
        # yield 'lino_noi.lib.working'
        yield 'lino_xl.lib.lists'
        # yield 'lino_xl.lib.blogs'

        # yield 'lino.modlib.changes'
        # yield 'lino.modlib.notify'
        yield 'lino.modlib.uploads'
        # yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.excerpts'
        yield 'lino.modlib.export_excel'
        # yield 'lino.modlib.tinymce'
        # yield 'lino.modlib.smtpd'
        yield 'lino.modlib.weasyprint'
        yield 'lino_xl.lib.appypod'
        # yield 'lino.modlib.wkhtmltopdf'
        yield 'lino.modlib.comments'
        yield 'lino.modlib.dashboard'
        yield 'lino.modlib.checkdata'

        # yield 'lino.modlib.awesomeuploader'

        # yield 'lino_noi.lib.noi'
        yield 'lino_ciao.lib.ciao'
        # yield 'lino_xl.lib.inbox'
        # yield 'lino_xl.lib.mailbox'
        # yield 'lino_xl.lib.meetings'

    def get_plugin_configs(self):
        for i in super(Site, self).get_plugin_configs():
            yield i
        # yield ('addresses', 'partner_model', 'contacts.Person')
        yield ('cal', 'partner_model', 'contacts.Person')
        yield ('contacts', 'with_roles_history', True)

    # def setup_plugins(self):
    #     super(Site, self).setup_plugins()
    #     # self.plugins.comments.configure(
    #     #     commentable_model='tickets.Ticket')
    #     # self.plugins.skills.configure(
    #     #     demander_model='contacts.Person')
    #     self.plugins.addresses.configure(
    #         partner_model='contacts.Person')
    #     self.plugins.cal.configure(
    #         partner_model='contacts.Person')
    #     self.plugins.contacts.configure(
    #         with_roles_history=True)

        # self.plugins.skills.configure(
        #     demander_model='tickets.Ticket')
        # self.plugins.tickets.configure(
        #     site_model='cal.Room',
        #     milestone_model='courses.Course')

    def setup_quicklinks(self, user, tb):
        super(Site, self).setup_quicklinks(user, tb)
        tb.add_action(self.models.contacts.Persons)
        tb.add_action(self.models.contacts.Companies)

        a = self.models.users.MySettings.default_action
        tb.add_instance_action(
            user, action=a, label=_("My settings"))

        tb.add_action(
            self.models.cal.MyEntries.insert_action,
            label=_("New calendar entry"))


# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'

USE_TZ = True
# TIME_ZONE = 'Europe/Brussels'
# TIME_ZONE = 'Europe/Tallinn'
TIME_ZONE = 'UTC'
