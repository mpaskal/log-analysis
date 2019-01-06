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

## Installation
1. Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [Vagrant](https://www.vagrantup.com/) for your OS
2. Launch your terminal. Everyting belown will be done in it.
3. Check that Vagrant was installed: run `vagrant --version`. You should see something like this
`C:\Users\Administrator>vagrant --version
Vagrant 2.2.2`
4. To get the project with test data and VM clone this [repo](https://github.com/mpaskal/log-analysis_project.git)
5. Navigate to the project directory
6. Unzip database file newsdata in the project directory
7. Launch the VM with `vigrant up` command to download and install the Ubuntu-16.04, PostgreSQL, python, dependences, create database **"News"**. 
8. Run `vagrant ssh` to log in to the Ubuntu VM
9. Load data of **"News"**: navigate to vagrant directory and run `psql -d news -f newsdata.sql`
10. Run log analisis script `log_analysis.py` in the terminal with command `python /vagrant/log_analysis.py)`
11. Check the result 

## Expected result
![Screenshot with the result ont the console](/screenshot_report.jpg)
