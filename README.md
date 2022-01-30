# inSuRance
## smart inSuRance 


### To run Django Project

- Step 1:  To install all python's library run the below command

        pip install -r requirement.txt

- Step 2: To create a tables (collections)  with sqlite run the below migrations command

        python manage.py makemigrations
        
        python manage.py migrate
        

- Step 3: To run Django server (open new terminal)

        python manage.py runserver

- Step 4: To view Django API GUI type below url to your browser

       http://127.0.0.1:8000/api/v1/climate/
       
  - Note :
    - 


    List of endpoints. 
    API:
    admin/
    api/v1/policys/bulk_add/
    api/v1/policys/
    api/v1/policys/<int:id>/
    api/v1/policy/search/?cid=&pid=12350
    api/v1/policy/chart/

    UI : 
    ui/policy-detail
    ui/policy-chart 
    ui/policy-add 
    ui/policy-edit `

  Needs to be done:
  UI needs to be done with more attractive way, client side validation, logging, dynamic forms 