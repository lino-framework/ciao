.. doctest docs/specs/overview.rst
.. _ciao.specs.overview:

===================
Lino Ciao Overview
===================


.. contents::
   :local:
   :depth: 2

>>> from lino import startup
>>> startup('lino_ciao.projects.ciao1.settings.demo')
>>> from lino.api.doctest import *


>>> rt.show(users.UserTypes)
======= =========== ===============
 value   name        text
------- ----------- ---------------
 000     anonymous   Anonymous
 100     user        User
 800     staff       Staff
 900     admin       Administrator
======= =========== ===============
<BLANKLINE>
