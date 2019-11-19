# -*- coding: UTF-8 -*-
# Copyright 2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""This is the main Python package of Lino Ciao.

.. autosummary::
   :toctree:

   lib


"""

from os.path import join, dirname
fn = join(dirname(__file__), 'setup_info.py')
exec(compile(open(fn, "rb").read(), fn, 'exec'))

__version__ = SETUP_INFO['version']

intersphinx_urls = dict(docs="http://ciao.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/ciao/blob/master/%s'
doc_trees = ['docs']
