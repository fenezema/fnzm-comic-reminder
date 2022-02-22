# FNZM Comic Reminder (WIP)

## **Hola**
Fnzm Comic Reminder is a personal project to cater the author laziness on keeping notes of the author's favorite comics chapters. This project base idea is a daily reminder or message broadcaster of user subscribed comics by sending information (via messaging app) of title, latest chapter, last read chapter, and a flagger that indicates whether user has already read the latest chapter or not.

## **Project's Tech Stack**
This project is built using [Ariadne](https://ariadnegraphql.org/) (GraphQL Schema-first package for Python) on top of [Flask](https://flask.palletsprojects.com/en/2.0.x/).

The data saving itself is using JSON Read/Write that operates as a simple database. 
Note that for this matter, there are a few concerns that will raise. Based on this, here are a few assumptions on why the database is using a simple JSON Read/Write mechanism.
1. This is a personal project that basically will not save any personal/sensitive informations. The intended use is for personal project only and for Crash Course project. So the scope of this app will only cater personal needs.
2. Due to **Point 1**, currently, concern on multiple single file access will be eliminated.

## **How to Run**
Prerequisite (as of now):
1. Python3 with pip3. Check out the official page for [Python3](https://www.python.org/)
2. Flask. Check out the official page for [Flask](https://flask.palletsprojects.com/en/2.0.x/)
3. Ariadne. Check out the official page for [Ariadne](https://ariadnegraphql.org/)

**It it recommended to to run this project on a Unix/Unix-like(Fedora, Ubuntu, Debian, MacOC, etc) system for the ease of development.**

For **Point 2** and **Point 3**, these packages can be installed via command on the terminal<br>
`pip3 install flask` and `pip3 install ariadne`

Once installed, we need to tell flask where the app can be run via this command on the terminal<br>
`export FLASK_APP=main.py`.

After all the steps mentioned above fulfilled, user can run this project via this command on the terminal<br>
`flask run`

**NOTES: Before running the app. It is advised to create `db` directory and then run the `userInit.py` script.**

## **GraphQL Playground**
Ariadne package by default ships with GraphQL Playground to access all and try all the available Queries and Mutations. The playground can be access on this endpoint `/graphql` via browser.