# Test for one implementation of the interface
from lexicon.providers.henet import Provider
from integration_tests import IntegrationTests
from unittest import TestCase
import pytest

# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests
class FooProviderTests(TestCase, IntegrationTests):

    Provider = Provider
    provider_name = 'henet'
    domain = 'lexicontest.com'
    def _filter_post_data_parameters(self):
        return ['email', 'pass']

    def _filter_headers(self):
        return ['Authorization', 'Cookie']

    def _filter_query_parameters(self):
        return ['pass']
