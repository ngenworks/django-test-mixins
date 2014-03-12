"""
Assertion helpers
"""

class AssertStatusMixin(object):
    """
    Shortcuts to assert response codes.
    """
    def assert200(self, response):
        """
        Assert a 200 response
        """
        self.assertEquals(response.status_code, 200)
        return response

    def assert201(self, response):
        """
        Assert a 201 created response
        """
        self.assertEquals(response.status_code, 201)
        return response

    def assert202(self, response):
        """
        Assert a 202 response
        """
        self.assertEquals(response.status_code, 202)
        return response

    def assert400(self, response):
        """
        Assert a 400 response
        """
        self.assertEquals(response.status_code, 400)
        return response

    def assert401(self, response):
        """
        Assert a 401 response
        """
        self.assertEquals(response.status_code, 401)
        return response

    def assert403(self, response):
        """
        Assert a 403 response
        """
        self.assertEquals(response.status_code, 403)
        return response

    def assert404(self, response):
        """
        Assert a 404 response
        """
        self.assertEquals(response.status_code, 404)
        return response
