# SaveMyClick

Register and Login to Upload your photos. Categorize them and if the photos become too many, filter them by categories you created.

# Navigation Guide

1. photoalbum -> photoalbum folder contains project settings and urls.py of the entire project ( Individual App URLs are specified later )

2. photoalbum -> photos folder is the most important folder of project.
   It contains Templates, admin.py, Migrations data, Forms, Models, Urls of the app and the Views.
   2(a) Templates have the html files of login, register, gallery, view photo and add photos. 
   
3. The photoalbum -> staticfiles folder contains admin panel (HTML, CSS, JS) files.

4. photoalbum -> static/images contains all the images of users stored locally. 


# Update
1. Will be adding updation, deletion functionalities soon.
2. Will use S3 Buckets for storing the photos.
