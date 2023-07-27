
 **- Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.**   
To programmatically request data from the microservice, you must make a POST request to the /get_ratios endpoint of the host that the service is running on. The default port that this service uses is 5000 so the program calling this service must be using the URL "http://localhost:5000/get_ratios" to send and receive data.

I wrote a quick Python program "testing.py" to test if it is working. This can be found in testing.py. If working, this will print:   

"""   
Sharpe Ratio:  0.24112141108520604   
Treynor Ratio:  0.004166666666666667   
Calmar Ratio:  0.03   
"""   

You can also use this curl request to test if the get_ratio.py file is properly working:   
"""     
curl --location --request POST 'http://localhost:5000/get_ratios' \
--header 'Content-Type: application/json' \
--data-raw '{
   "returns": [0.01, 0.02, -0.01, 0.03, -0.02],
   "risk_free_rate": 0.001,
   "beta": 1.2,
   "max_drawdown": 0.2
}'   
"""    
   
Which prints in the JSON format:   
"""   
{"calmar_ratio":0.03,"sharpe_ratio":0.24112141108520604,"treynor_ratio":0.004166666666666667}   
"""   

**- Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.**   
To programmatically receive data from the microservice, you must first ensure that the get_ratios.py file is running. Run the file with "python3 get_ratios.py". Once it is running, it will be listening for all incoming requests on "http://localhost:5000/get_ratios". You can now send requests to the service as shown above, and it will return the 3 ratios.      

 **- UML sequence diagram showing how requesting and receiving data works.**   
 Sequence Diagram -    
![Screen Shot 2023-07-26 at 11 10 36 PM](https://github.com/ryanmaki18/CS-361-Project/assets/130192949/02b92869-747e-43e4-8c7d-14d9ecfdebf2)



 Class Diagram -    
![Screen Shot 2023-07-26 at 11 06 54 PM](https://github.com/ryanmaki18/CS-361-Project/assets/130192949/7432b485-5055-4532-bef5-46318e7d5e8e)   
