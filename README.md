# Log Analysis Project

## Description
This project provides a reporting tool that gets data of a fictional web site and returns human readable report that answers questions: 
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

The project is done with Python script that uses the psycopg2 library to query PostgreSQL database.

## Script's design
### The script consists of 5 functions:
+ **helping function** establish connection, run query and close connection
+ **3 functions for 3 reports** set query, call helping function, print the result
+ **main function** condition when functions will be called; if it's true, calls other functons, prints report title

## Details about log_analysis.py functions
+ `run_query(query)` - establishes connection to database, runs query, closes db connection and returns result
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
7. Launch the VM with `vagrant up` command to download and install the Ubuntu-16.04, PostgreSQL, python, dependences, create database **"News"**. 
8. Run `vagrant ssh` to log in to the Ubuntu VM
9. Load data of **"News"**: navigate to vagrant directory and run `psql -d news -f newsdata.sql`
10. Run log analisis script `log_analysis.py` in the terminal with command `python /vagrant/log_analysis.py)`
11. Check the result 

## Expected result
![Screenshot with the result ont the console](/screenshot_report.jpg)
