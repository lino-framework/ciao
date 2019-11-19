# -*- coding: UTF-8 -*-
# Copyright 2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

# $ python setup.py test -s tests.PackagesTests.test_packages

SETUP_INFO = dict(
    name='lino-ciao',
    version='19.11.0',
    install_requires=['lino-xl', 'lino-react'],

    # tests_require=['pytest', 'mock'],
    # test_suite='tests',
    description=("A Lino application for managing meeting calendars"),
    long_description="""\

Lino Ciao is a customizable Lino application for managing meeting calendars and
inviting people to them.  It is currently a submarine project, used only by its
authors and therefore poorly documented.

- The central project homepage is http://ciao.lino-framework.org

- For *introductions* and *commercial information* about Lino ciao
  please see `www.saffre-rumma.net
  <http://www.saffre-rumma.net>`__.


""",
    author='Rumma & Ko Ltd',
    author_email='info@saffre-rumma.net',
    url="http://ciao.lino-framework.org",
    license='BSD-2-Clause',
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 1 - Alpha
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Intended Audience :: System Administrators
Intended Audience :: Information Technology
Intended Audience :: Customer Service
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Topic :: Communications :: Email :: Address Book
Topic :: Office/Business :: Groupware
""".splitlines())

SETUP_INFO.update(packages=[str(n) for n in """
lino_ciao
lino_ciao.lib
lino_ciao.lib.ciao
lino_ciao.lib.ciao.fixtures
lino_ciao.lib.contacts
lino_ciao.lib.contacts.fixtures
lino_ciao.lib.topics
lino_ciao.projects
lino_ciao.projects.ciao1
lino_ciao.projects.ciao1.settings
lino_ciao.projects.ciao1.settings.fixtures
lino_ciao.projects.ciao1.tests
lino_ciao.lib.users
lino_ciao.lib.users.fixtures
""".splitlines() if n])

SETUP_INFO.update(message_extractors={
    'lino_ciao': [
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**.js',                'javascript', None),
        ('**/config/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(include_package_data=True, zip_safe=False)
# SETUP_INFO.update(package_data=dict())


# def add_package_data(package, *patterns):
#     l = SETUP_INFO['package_data'].setdefault(package, [])
#     l.extend(patterns)
#     return l

# l = add_package_data('lino_noi.lib.noi')
# for lng in 'de fr'.split():
#     l.append('locale/%s/LC_MESSAGES/*.mo' % lng)
