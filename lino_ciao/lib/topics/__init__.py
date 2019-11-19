# Copyright 2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""
Lino Ciao extension of :mod:`lino_xl.lib.topics`.

"""

from lino_xl.lib.topics import Plugin


class Plugin(Plugin):

    extends_models = ['Topic']
