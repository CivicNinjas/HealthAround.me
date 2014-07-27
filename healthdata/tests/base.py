import json

from django.test import TestCase as BaseTestCase
from rest_framework.test import APITestCase as BaseAPITestCase


class TestCaseCommonMixin(object):
    '''Common helpers for TestCase'''
    maxDiff = None

    def assertOrderedDictEqual(self, expected, calculated):
        '''
        Assert calculated is equal to the equivalent dict

        calculated includes OrderDicts, so it is serialized through
        JSON to turn them into plain dicts
        '''
        actual = json.loads(json.dumps(calculated))
        self.assertDictEqual(expected, actual)

    def score_text_no_data(self, name, feedback_url='#'):
        '''
        Construct the score_text when no data is available
        '''
        return {
            u'markdown': (
                u"We don't have data for {name} yet, but studies show it has"
                u" an impact on the health of a community. Do you know about"
                u" a data source? [Tell us about it]({feedback_url})."
            ).format(name=name, feedback_url=feedback_url),
            u'html': (
                u"<p>We don't have data for {name} yet, but studies show it"
                u" has an impact on the health of a community. Do you know"
                u" about a data source?"
                u" <a href=\"{feedback_url}\">Tell us about it</a>.</p>"
            ).format(name=name, feedback_url=feedback_url),
        }


class APITestCase(TestCaseCommonMixin, BaseAPITestCase):
    assertSerializerDataEqual = TestCaseCommonMixin.assertOrderedDictEqual

    def assertDataEqual(self, response, expected):
        '''
        assert Response data is equal to a dictionary

        Because data includes dict-like objects that aren't quite dicts, it
        passed through json encoding/decoding first, to get a plain old dict
        (with unicode strings)
        '''
        self.assertEqual(response.status_code, 200, response.content)
        self.assertOrderedDictEqual(expected, response.data)

class TestCase(TestCaseCommonMixin, BaseTestCase):
    assertScoreEqual = TestCaseCommonMixin.assertOrderedDictEqual
