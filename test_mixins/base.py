"""
Base test runner.
"""
import os
import shutil
import tempfile

from django.conf import settings
from django.test import TestCase

from django_nose import NoseTestSuiteRunner


class AppTestRunner(NoseTestSuiteRunner):
    """
    If user uploads are tried in integration tests, they should not actually
    end up on the file system in the media root.  This subclass of the nose
    test runner will keep them in a temp directory
    """
    def setup_test_environment(self, **kwargs):
        super(AppTestRunner, self).setup_test_environment(**kwargs)

        self.backup = {
            'DEFAULT_FILE_STORAGE': settings.DEFAULT_FILE_STORAGE,
            'MEDIA_ROOT': settings.MEDIA_ROOT
        }
        settings.DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

        self.temp_media_root = tempfile.mkdtemp(prefix='app-tests-')
        settings.MEDIA_ROOT = self.temp_media_root

    def teardown_test_environment(self, **kwargs):
        super(AppTestRunner, self).teardown_test_environment(**kwargs)
        for name, value in self.backup.items():
            setattr(settings, name, value)

    def run_tests(self, test_labels, **kwargs):
        try:
            super(AppTestRunner, self).run_tests(test_labels, **kwargs)
        finally:
            shutil.rmtree(self.temp_media_root, ignore_errors=True)


class AppTestCase(TestCase):
    """
    Remove everything in the tmp storage directory.

    Inefficient? Yes. However, this workaround with the test runner is better
    than having files in your local ``MEDIA_ROOT``
    """
    for f in os.listdir(settings.MEDIA_ROOT):
        try:
            if os.path.isfile(f):
                os.unlink(f)
        except:
            pass
