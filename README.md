# NoSql-Python

##Python - Flask:
```
	sudo pip install Flask gunicorn 
```
## CouchBase

1. Install cli 
	```
	sudo pip install couchbase
	```
2. If you face issue with this, in Mac
	try this
		```
		brew install libcouchbase
		```
	once it is done, try 
		```
		sudo pip install couchbase
		```
##Mongo db
1. Installation in mac
	```
		brew install mongodb
	```
	linux and Windows:
		http://docs.mongodb.org/manual/administration/install-on-linux/
2. Create data directory
	```
		sudo mkdir -p /data/db
	```
3. Run mango
	```
		mongod
	```
	Enable User interface and rest browsable
	```
		sudo mongod --httpinterface --rest
	```