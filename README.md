<h2>Log Analysis Project</h2>

<h3>Description</h3>
Reporting tool for internal usage that gets data from database and helps analyze what web site articles and authors more popular, and on which page users experiences high rate of issues. 

<h3>Executable file log_analysis.py with functions</h3>
<ul>
<li><strong>before_query()</strong> - establishes connection to database, returns db connection and cursor</li>
<li><strong>after_query(query, db, cursor)</strong> - takes query, db and cursor as arguments, runs query and return result, closes db connection</li>
<li><strong>article()</strong> -  print titles and number of views of the most popular three articles of all time</li>
<li><strong>authors()</strong> - print authors and number of views of the most popular article authors of all time</li>
<li><strong>log_errors()</strong> - print days with more than 1% of requests lead to errors</li>
</ul>

<h3>Requirements to run log_analysis</h3>
<ol>
<li>Vagrant and VirtualBox</li>
<li>Start VM with <em>vigrant up</em> command</li>
<li>Log in to is with <em>vigrant ssh</em> command</li>
<li>Add log_analysis and newsdata.sql files into vigrant folder</li>
<li>Within vigrant run python log_analysis.py</li>
<ol>
