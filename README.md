# interview


Prerequisition
- please install the following Python module if they're not installed
```pip install requests```
```pip install pytest```
```pip install selenium```

- Get access token from gorest.co.in, it's needed for create/update/delete operations
Go to https://gorest.co.in/my-account/access-tokens
Generate a toke, save it locally

- Save the above access token as environment variable in the running environment
Assign the access token to environment variable with name: GOREST_ACCESS_TOKEN

To run assignments:
- For REST API assignment: 
```pytest user_test.py```
- For Amazon Web Automation assignment: 
```python amazon_order_automation.py```
