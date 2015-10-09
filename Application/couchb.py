from flask import Flask, Blueprint
from couchbase.bucket import Bucket

couchb = Blueprint('couchb', __name__ )

@couchb.route("/")
def hello():
	try:
		from couchbase import Couchbase
		cb = Couchbase.connect(bucket='test_ZIZ')
		print cb
		c = Bucket('couchbase://localhost/test_ZIZ')

		resultset = c.query("dev_account", "all")
		print "------"
		print resultset
		print "------"

		# for row in resultset: print row.key
		return "Hello World!"
	except Exception as e:
		print "--------"
		print e
		print "--------"