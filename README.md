<h2>Log Analysis Project</h2>

<h3>Description</h3>
Reporting tool for internal usage that gets data from database and helps analyze what web site articles and authors more popular, and on which page users experiences high rate of issues. 

<h3>Program's design</h3>
<p>The program consists of 5 functions:</p>
<ul>
<li><strong>before function</strong> - establish connection</li>
<li><strong>after function</strong> - run query and close connection</li>
<li><strong>3 functions for 3 reports</strong> call before function, set query, cal after function, print the result</li>
<li><strong>condition when functions will be called</strong> if it's true, calls other functons, prints report title</li>
</ul>

<h3>log_analysis.py functions</h3>
<ul>
<li><strong>before_query()</strong> - establishes connection to database, returns db connection and cursor</li>
<li><strong>after_query(query, db, cursor)</strong> - takes query, db and cursor as arguments, runs query and return result, closes db connection</li>
<li><strong>article()</strong> -  print titles and number of views of the most popular three articles of all time</li>
<li><strong>authors()</strong> - print authors and number of views of the most popular article authors of all time</li>
<li><strong>log_errors()</strong> - print days with more than 1% of requests lead to errors</li>
<li><strong>if __name__ == '__main__'</strong></li> - if this condition is true, call functions listed below
</ul>

<h3>Requirements to run log_analysis</h3>
<ol>
<li>Install Vagrant and VirtualBox</li>
<li>From the console start VM with <em>vigrant up</em> command</li>
<li>Log in to is with <em>vigrant ssh</em> command</li>
<li>Add log_analysis and newsdata.sql files into vigrant folder</li>
<li>Run python log_analysis.py within the VM (python /vagrant/log_analysis.py)</li>
<li>Check the result on the console</li>
<ol>
  
<h3>Expected result</h3>
<img src="https://github.com/mpaskal/log-analysis_project/blob/master/screenshot_report.jpg" alt="screenshot_report.jpg" style="max-width:100%">
<a target="_blank" href=:https://github.com/mpaskal/log-analysis_project/blob/master/screenshot_report.jpg'</a>
