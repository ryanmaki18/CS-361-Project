
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
Which prints the JSON format:
"""
{"calmar_ratio":0.03,"sharpe_ratio":0.24112141108520604,"treynor_ratio":0.004166666666666667}
"""


**- Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.**
To programmatically receive data from the microservice, you must first ensure that the get_ratios.py file is running.




 **- UML sequence diagram showing how requesting and receiving data works.**
    
