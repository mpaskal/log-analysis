# Log Analysis Project

## Description
Reporting tool for internal usage that gets data from database and helps analyze what web site articles and authors more popular, and on which page users experiences high rate of issues. 

## Program's design
### The program consists of 5 functions:
+ **before function** - establish connection
+ **after function** - run query and close connection
+ **3 functions for 3 reports** call before function, set query, cal after function, print the result
+ **condition when functions will be called** if it's true, calls other functons, prints report title


## log_analysis.py functions
+ `before_query()` - establishes connection to database, returns db connection and cursor
+ `after_query(query, db, cursor)` - takes query, db and cursor as arguments, runs query and return result, closes db connection
+ `article()` - has a quesry with subquery, prints titles and number of views of the most popular three articles of all time
+ `authors()` - has a quesry with subquery, prints authors and number of views of the most popular article authors of all time
+ `log_errors()` - has a quesry with subquery, prints days with more than 1% of requests lead to errors
+ `if __name__ == '__main__'` - if this condition is true, call functions listed below


## Requirements to run log_analysis
1. Install Vagrant and VirtualBox
2. From the console start VM with <em>vigrant up</em> command
3. Log in to is with <em>vigrant ssh</em> command
4. Add log_analysis and newsdata.sql files into vigrant folder
5. Run python log_analysis.py within the VM (python /vagrant/log_analysis.py)
6. Check the result on the console
## Expected result
![Screenshot with the result ont the console](/screenshot_report.jpg)
