# LoginSystem
This application is a modular basic login system to a database.
The goal is to implement such system that the users could sign in on database with username 
and password and store private data to future using. 
The users could connect to the database, and if the database recognize them as 
registered users, they can access to their data, and of course adding more data.
The events that occur on our system are being recorded as logs to special log file.
There is one special admin user who can access to those logs.

Few thechnical information about the coding design:
The backend logic is as follows:
  There is Database class which implements the abstract IDB class - by implemeting the
   the basic operations of database.
   This concrete Database is implemented with file text (as container to te data).
   When the database will be create, it'll create his data files locally.
  
  There is Logger class which take care about the events logging - saves the data on file.
  
  There is User class which encapsulate all the operations that registered user can make
   in the system. The user can pull his saved data from the server.In order to append new data
   to the database he has to modify his LOCALDATA and then PUSH it to the database.
  
  There is a Validator bewtween the user and the database. This object is like a proxy bewtween
  the User and the Database. The validator expects to get an abstract Database without caring
   how the database is implemeted (excel, file, or any else...) - this give us a flexible system.
   
The front App is:
  The user has a CMD style interface application.
  The admin has his own CMD style interface application.
