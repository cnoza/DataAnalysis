## 1. The psql tool ##

/home/dq$ psql

## 2. Running SQL queries ##

/home/dq$ psql

	CREATE DATABASE dbName;

## 3. Special PostgreSQL commands ##

/home/dq$ psql

	\l -- list all available databases.
	\dt -- list all tables in the current database.
	\du -- list users.

## 4. Switching databases ##

/home/dq$ psql -d bank_accounts

## 5. Creating users ##

/home/dq$ psql
	
	CREATE ROLE userName WITH CREATEDB LOGIN PASSWORD 'password';

## 6. Adding permissions ##

/home/dq$ psql -d bank_accounts

	GRANT SELECT, INSERT, UPDATE, DELETE ON tableName TO userName;
	GRANT ALL PRIVILEGES ON tableName TO userName;
	\dp tableName
	
## 7. Removing permissions ##

/home/dq$ psql -d bank_accounts

	REVOKE SELECT, INSERT, UPDATE, DELETE ON tableName FROM userName;
	REVOKE ALL PRIVILEGES ON tableName FROM userName;

## 8. Superusers ##

/home/dq$ psql

	CREATE ROLE userName WITH LOGIN PASSWORD 'password' SUPERUSER;