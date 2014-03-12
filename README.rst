==================
Django test mixins
==================

The following are mixins we find ourselves using over and over again.

---------------
Assertion mixin
---------------

::

    from test_mixins.assertions import AssertStatusMixin

    class SomeTestClass(AssertStatusMixin, TestCase):
        def some_test(self):
            response = self.client.get('some-url')
            self.assert403(response)

            # login
            response = self.client.get('some-url')
            self.assert200(response)


The following status codes are accounted for, ``200``, ``201``, ``202``, ``400``,
``401``, ``403``, ``404``


------------
Nose Plugins
------------

Used in conjunction with nose/django-nose, ``test_mixins.nose_plugins.SuppressSouth``
lowers the South logging level to ``logging.ERROR``, so error output on
failing tests is more readable.

Usage
~~~~~

In ``settings.py``, add the following.

::

    NOSE_PLUGINS = ['test_mixins.nose_plugins.SuppressSouth']


