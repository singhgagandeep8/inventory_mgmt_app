# inventory_mgmt_app

Prerequisites: Python, Djano 1.9. MySQL installed on local machine.

Unzip the 'itake' folder to any location on your local machine. 

Open up terminal or PowerShell, and change directory into the folder containing "manage.py". 
We can access the database (hosted in AWS) through the command line. 
Copy this on the terminal: mysql -h ecommerce3.cia2arykzkpz.us-west-2.rds.amazonaws.com -P 3306 -u admin -p
Now you’re inside the database in mysql shell. 
Type ‘use Ecommerce3;’ We are connected to our database on AWS. Type this command: python manage.py runserver

Url to the admin page: http://127.0.0.1:8000/admin/ 
username: admin1 
password: pass1234 
On logging in, we can view itake – which contains our tables Order items, Orders, Products, Vendors, Warehouses.

Next, navigate to our itake page, the url for which is: http://127.0.0.1:8000/itake/ This is our home page. CRUD Functionality: 
On clicking the Product Button (http://127.0.0.1:8000/itake/product/) we can view the List of Products. 	
On clicking the product in the list, you can view the detail information of each product. 
On clicking the ‘Add Product’ button in the product list page (http://127.0.0.1:8000/itake/product/), you can add new product to the table. 	
On clicking the ‘Edit’ button in the product list (http://127.0.0.1:8000/itake/product/), you are directed to the update page of the specific product. 
On clicking the ‘Delete’ button in the product list (http://127.0.0.1:8000/itake/product/), you are directed to a confirmation page. By clicking on the ‘submit’ button, you can delete the product from the table.

URL of the homepage:http://itakev10.efh2tfmqw8.us-west-2.elasticbeanstalk.com/itake/
