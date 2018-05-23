# Log Analysis Tool
Source code for a log analysis reporting tool.

This reporting tool is a Python program using the psycopg2 module to connect to the database. Running this code prints out reports (in plain text) based on the data in a database called "news", and presumes the user has the "news" database on their machine.

The report answers in the following questions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 


### Prerequesites
Ensure that Python 3 and git are installed:
```
python3 --version
git --version
```


### Installing

From the Terminal, clone this repo onto your computer with:

```
git clone https://github.com/lewisisgood/logs-analysis
```

Move into the new directory:

```
cd logs-analysis/
```

Install required libraries:

```
sudo pip3 install -r requirements.txt
```

Run the loganalysis.py to generate the report:

```
python loganalysis.py
```

This will output a formatted version of my query results in the Terminal.


## Built With

* Python 3.5.2
* git 2.14.1

## Authors

* **Lewis King** - [Github](https://github.com/lewisisgood)

## Acknowledgments

* Thanks to Udacity for the Ubuntu VM and database creation file, which helped me make this project!