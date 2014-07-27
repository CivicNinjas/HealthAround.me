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

    def score_text_no_data(self, name):
        '''
        Construct the score_text when no data is available
        '''
        feedback_url = "http://healtharound.me/#/feedback"
        return {
            u'markdown': (
                u"We are still working on aggregating data for {name}. This"
                u" data will be made available as time and funding allows."
                u" Do you know of another data source we should be aware of?"
                u" [Tell us about it]({feedback_url})."
            ).format(name=name, feedback_url=feedback_url),
            u'html': (
                u"<p>We are still working on aggregating data for {name}."
                u" This data will be made available as time and funding"
                u" allows. Do you know of another data source we should be"
                u" aware of?"
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
