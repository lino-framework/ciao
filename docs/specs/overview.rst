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


>>> print(analyzer.show_complexity_factors())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 30 plugins
- 41 models
- 4 user types
- 153 views
- 11 dialog actions
<BLANKLINE>




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


>>> rt.login('robin').show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- Contacts : Persons, Organizations, Partner Lists
- Calendar : My appointments, Overdue appointments, My unconfirmed appointments, My tasks, My guests, My presences, My overdue appointments, Calendar
- Office : My Upload files, My Excerpts, My Comments, Recent comments
- Configure :
  - System : Users, Site Parameters, Help Texts
  - Contacts : Organization types, Functions, List Types
  - Calendar : Calendars, Rooms, Recurring events, Guest roles, Calendar entry types, Recurrency policies, Remote Calendars, Planner rows
  - Topics : Topics
  - Office : Library volumes, Upload types, Excerpt Types, Comment Types
  - Places : Countries, Places
- Explorer :
  - System : Authorities, User types, User roles, All dashboard widgets, content types, Data checkers, Data problems
  - Contacts : Contact persons, Partners, List memberships
  - Calendar : Calendar entries, Tasks, Subscriptions, Entry states, Presence states, Task states, Planner columns, Access classes, Display colors
  - Topics : Interests
  - Office : Upload files, Upload areas, Excerpts, Comments, Mentions
- Site : About
