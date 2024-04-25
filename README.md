Step 1 : git clone https://github.com/coderrohanpahwa/krakend.git  
Step 2 : cd krakend/  
Step 3 : python -m venv venv  
Step 4 : source venv/bin/activate  
Step 5 : pip install -r requirements.txt   
Step 6 : python user_service/user_service.py ## This will run flask server on port 5000  
Step 7 : Now open a new terminal and activate virtual environment (cd krakend/ && source venv/bin/activate )  
Step 8 : python payment_service/payment.py ## This will run flask server on port 5001  
Step 9 : Now open a new terminal and run cd krakend  
Step 10 : krakend run -c krakend.json  
