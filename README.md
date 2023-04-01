# TO-DO-List
  #### To Do list app with Multiple User Registration, Login, and full Create Read Update and DELETE functionality.

# Setting up the project:
> Project Setup 
### Let’s initialize our project by creating a new folder :

1. Clone this repository :

		git clone git@github.com:JammulaVarun/TO-DO-List.git

2. Now Create & Activate the Virtual environment by typing this below line's in Commmand Line :

		python -m venv venv
		venv\Scripts\activate
		
3. Intall the Project Requirements :

		pip install -r requirements.txt
	
4. After installation, Create a migration file containing instructions for altering the database table :

		python manage.py makemigrations
		
5. Migrate the database table by running the below code:

		python manage.py migrate
		
6. Run the Server :

		python3 manage.py runserver
		
#### For creating superuser, first reach the same directory as that of manage.py and run the following command:

> To create a Django Superuser

	python manage.py createsuperuser
	
  - Then enter the Username of your choice and press enter.
  - Then enter the Email address and press enter.(It can be left blank)
  - Next, enter the Password in-front of the Password field and press enter.Enter a strong password so as to keep it secure.
  - Then again enter the same Password for confirmation.
  
> To Deactivate the virtual environment:

		deactivate
