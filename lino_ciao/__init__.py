# -*- coding: UTF-8 -*-
# Copyright 2019-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""This is the main Python package of Lino Ciao.

.. autosummary::
   :toctree:

   lib


"""

from .setup_info import SETUP_INFO

__version__ = SETUP_INFO['version']

intersphinx_urls = dict(docs="http://ciao.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/ciao/blob/master/%s'
doc_trees = ['docs']
