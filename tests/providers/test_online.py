# Test for one implementation of the interface
from lexicon.providers.online import Provider
from integration_tests import IntegrationTests
from unittest import TestCase
import pytest

# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests
class OnlineProviderTests(TestCase, IntegrationTests):

	Provider = Provider
	provider_name = 'online'
	domain = 'capsulecd.com'

	def _filter_headers(self):
		return ['Authorization', 'x-recruitment']

	def _test_engine_overrides(self):
		overrides = super(OnlineProviderTests, self)._test_engine_overrides()
		overrides['fallbackFn'] = (lambda x: 'placeholder_' + x if x != 'priority' else '')
		return overrides

	@pytest.mark.skip(reason="manipulating records by id is not supported")
	def test_Provider_when_calling_delete_record_by_identifier_should_remove_record(self):
		return
