# Take Home Exercise


## Prerequisition
- please install the following Python module if they're not installed  

```pip install requests```  

```pip install pytest```  

```pip install selenium```

- Make sure chromedriver is on the executable path

- Get access token from gorest.co.in, it's needed for create/update/delete operations  
1. Go to https://gorest.co.in/my-account/access-tokens
2. Generate a toke, save it locally

- Store the above access token as environment variable in the running environment
1. Assign the access token to environment variable with name: GOREST_ACCESS_TOKEN  


## To run these exercises:
1. For REST API exercise:  

```pytest user_test.py```

2. For Amazon Web Automation exercise  

```python amazon_order_automation.py```
