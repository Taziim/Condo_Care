1...Download the file zip and extract somewhere 
2...install python on the machine 
3...downlaod the postgrel and pgadmin
4...download the vs code
5...after install the above software open the file in the vs code
6...Create a virtual environment by running the belwo command in the terminal:
  1.python -m venv venv(venv can be any name)
7...install djanog write (pip install django)
8...also install (pip install psycopg2-binary),pip install Pillow,pip install qrcode[pil] 
9...to view the package write pip list in the terminal 
10...connect the postgrel database to the project:
   1.installl postgrel and pgadmin
   2.to connect database and project write the command in the terminal write (pip install psycopg2)in the vs code
   3.make sure to give the password of the postgrel database is 1234 or you can change the password in the setting.py in 
   the database change section in the project  
   4.create a database name Condo_Care in the postgrel
11...after install everything activate the virtula env following the below codes writing in the terminal:
   1.cd venv
   2.cd scripts
   3.\activate
   3.after activating pathe will look like this (venv) PS C:\Users\abcd\OneDrive\Desktop\Condo_Care\venv\active 
   4.now write cd .. to go to (venv) PS C:\Users\abcd\OneDrive\Desktop\Condo_Care\
   5.enter the project by writing cd CONDO_CARE
   6.after entring the project the path will look like this (venv) PS 
   C:\Users\abcd\OneDrive\Desktop\Condo_Care\CONDO_CARE>
12...Now do the migrations of the database by writing this command (venv) PS C:\Users\abcd\OneDrive\Desktop\Condo_Care\CONDO_CARE> python manage.py makemigrations.actually we migrated the database now we have to create table for each app
13...to create each app table write wrtie the below command 
  1.(venv) PS C:\Users\tariq\OneDrive\Desktop\Condo_Care\CONDO_CARE> python manage.py sqlmigrate Main 0001
  2. python manage.py sqlmigrate Management 0001
  3.python manage.py sqlmigrate Owner 0001
  4.python manage.py sqlmigrate Security 0001
  5.python manage.py sqlmigrate Tenant 0001
14...now write python manage.py migrate to migrate the table to the database and check in the postgrel database in the schema and table section
15...Now ready to go run the command in the terminal (venv) PS C:\Users\tariq\OneDrive\Desktop\Condo_Care\CONDO_CARE> python manage.py runserver  
