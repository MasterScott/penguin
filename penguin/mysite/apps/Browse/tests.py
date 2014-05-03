from django.test import TestCase
import unittest
import datetime
from django.utils import timezone
from django.test.client import RequestFactory
from .models import *

""" Attempt to test users borrowing tools from other users. """
class BorrowTransactionTestCase(TestCase):
		
	def setUp(self):
		parrot = User.create_new_user("Parrot", "password", "03545", "polly@python.org", "1234567890", "Pining for the fjords.")
		User.create_new_user('Penguin', 'password', '03545', 'penguin@python.org', '5555551234', 'It\'s on the telly.')
		Tool.create_new_tool("Rusty Nail", parrot.id, "Holding up a stuffed parrot", "nail", "Parrot", "Rip it out of the cage.")
		Tool.create_new_tool("Warhammer of Zillyhoo", parrot.id, "Its majesty makes you weep.", "hammer", "03545", "Some time travel required.")
		

	def test_create_new_borrow_transaction(self):
		return None;
			
#	def test_get_borrow_transaction(self):
#	def test_get_borrower_borrow_transactions(self):
#	def test_is_current(self):

class BorrowTransactionApiTestCase(TestCase):
	
	def setUp(self):
		# Set up a Request Factory
		self.factory = RequestFactory()
	
	@unittest.skip #not ready yet
	def test_requestBorrowTransaction(self):
		request = self.factory.post('/api/borrowTransaction')
	
	@unittest.skip #not ready yet
	def test_getUnresolvedBorrowTransactions(self):
		request = self.factory.get(
			path = '/api/borrowTransaction/requestPending'
			)
		
	@unittest.skip #not ready yet
	def test_resolveBorrowRequest(self):
		request = self.factory.post('/api/borrowTransaction/resolve')
	
	@unittest.skip #not ready yet
	def test_getRejectedRequests(self):
		request = self.factory.get(
			path = '/api/borrowTransaction/rejected/:id'
			)
	
	@unittest.skip #not ready yet
	def test_requestEndBorrowTransaction(self):
		request = self.factory.put('/api/borrowTransaction')
	
	@unittest.skip #not ready yet
	def test_getEndBorrowTransactionRequests(self):
		request = self.factory.get(
			path = '/api/borrowTransaction/endRequests'
			)
	
	@unittest.skip #not ready yet
	def test_resolveEndBorrowTransaction(self):
		request = self.factory.delete(
			path = '/api/borrowTransaction/:transactionId'
			)
	
	@unittest.skip #not ready yet
	def test_getToolsUserIsBorrowing(self):
		request = self.factory.put(
			path = '/api/borrowTransaction/borrowing/:userId'
			)
	
	@unittest.skip #not ready yet
	def test_getToolsUserIsLending(self):
		request = self.factory.get(
			path = '/api/borrowTransaction/borrowed/:userId'
			)
	
	@unittest.skip #not ready yet
	def test_getAllCommunityHistory(self):
		request = self.factory.get(
			path = '/api/borrowTransaction/community/:zip'
			)
	
	@unittest.skip #not ready yet
	def test_getAllReturnPendingBorrowTransactionsInCommunityShed(self):
		request = self.factory.get(
			path = '/api/borrowTransaction/pendingCommunity'
			)
	
