PROJECT

Create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

The tool reports on the following numbers for a newspaper website - 
1. Most popular three articles of all time
2. Most popular article authors of all time
3. Days on which more than 1% of requests led to errors

SET UP INSTRUCTIONS
1. Install and configure Virtual Machine
2. Start VM and SSH into it
3. Download newsdata.sql
4. cd into vagrant directory
5. Execute psql -d news -f newsdata.sql. This will set up the database "news" and connect to it. The database includes three tables:
	- The authors table includes information about the authors of articles.
	- The articles table includes the articles themselves.
	- The log table includes one entry for each time a user has accessed the site.
6. Use this CL window to study the database
7. In a new CL window, start VM, SSH into it and cd into vagrant. Use this to execute the python file you create.

PROGRAM EXECUTION
1. Place the attached report.py file in vagrant directory
2. Execute python newsdata.py from the command line window of step 7 above