This is a django project done with Django 2.1 to help my students from MBiB (UOC) with some examples:

HOW TO UPLOAD FILES USING ADMIN PANEL
=====================================
Check model.py in app "uploads" and admin.py.
In admin page, you will see the model called "UPLOAD" and just at the bottom "Event_files".
If you click on "Add", you will see a new menu with the option to upload the file.
That file is stored in the folder "events" inside the STATIC_URL defined in settings.py.

USE FILES UPLOADED TO DJANGO ADMIN
==================================
Check again "uploads". In models.py there is a Class with all needed tables.
Now we are going to fill all those tables: check the file 'insert_data.py' in
upload app. The only function takes the path and name of the excel file and creates
a DataFrame. Then this dataframe is iterated row by row and its data is stored into db.

HOW TO USE INDEX PAGE
============================
Select "Fecha Inicial", "Fecha Final", "Box" and "Dispositivo" and apply to "Enviar". If you want to insert new values, press "Borrar". You can also be redirect to "Intranet" (hospital web page).


