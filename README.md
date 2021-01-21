# Python Test by Ivan Wong
### Date: 1/20/2021

## Running the application
### Populate the database 
To change the Total number of records to populate the database using the command-line argument, 
python seed.py <total>
i.e. python seed.py 150

### Run the Flask app
python ./app.py

### Access the web application 
To change the number of record per page on the table view, use the URL query parameter "?per_page=<per_Page>"

This application is deployed to AWS with a default of 25 rows per page.  The application can be access using this URL: http://35.247.36.115:5000/?per_page=25

### Unit Test
To test the application, run the following unit test cases.

python test.app.py
    
## Summary
This application addressed all the requirements of the Python Test assignment.

* Create a script called seed.py that populates a SQLite database. The number of users to load can be customized using the total parameter.
* Create a Flask application with a view to show the info of all the users of the database in a table.
  * Profile avatar should be visible and clicking the username should send me to the GitHub profile.
  * Pagination is needed and by default it should be of size 25.
      * Make sure that the page is responsive even with a large amount of data (use any optimization).
      * Optional but desired*: arguments to change pagination size.
* Create Unit Test cases. 
    
A seed.py script is used to fetch the Github user data using the [Users GitHub API](https://docs.github.com/en/rest/reference/users) and insert the GitHub user records to the SQLite database, gituser.db.
    
I used the Flask web framework to build this [web application](http://35.247.36.115:5000/?per_page=25) to display the Github users available in the SQLite database.  Flask is a micro web frame.  Several libraries are used in this application to fetch the records from the database (sqlite3), display the view (render_template), and provide pagination of the view table (flask_paginate). 
