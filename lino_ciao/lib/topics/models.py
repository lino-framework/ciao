# -*- coding: UTF-8 -*-
# Copyright 2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import dd, _

from lino_xl.lib.topics.models import *
from lino.modlib.comments.mixins import Commentable

class Topic(Topic, Commentable):
    pass

class TopicDetail(dd.DetailLayout):
    main = """
    id ref name #topic_group
    description
    topics.InterestsByTopic comments.CommentsByRFC
    """


# @dd.receiver(dd.post_analyze)
# def my_details(sender, **kw):
#     contacts = sender.models.contacts
#     contacts.Companies.set_detail_layout(contacts.CompanyDetail())

Topics.set_detail_layout(TopicDetail())
