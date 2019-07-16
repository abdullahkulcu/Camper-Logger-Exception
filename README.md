# Camper-Logger-Exception  
**Simple, pretty and powerful logger and exception Catcher for python**  
  
This library has been developed to make it easier to detect errors in the application,   
and to make the process easier.  
  Also , More regular display of logs used in the application, allows saving to local file
  
## **Install** 
*(For use 3.4+)*

    pip install Camper-Logger-Exception


##### Using Logger
	from Camper.Log import CamperLogger
	logger = CamperLogger(logger_name=__name__, debug=True, record=True, log_path="/usr/log")


**logger_name :** Logger name for application or class - Required 
 
**debug :** Debug Mode True or False (default False) - Optional

 **log_path :**  The path of the saved log file (default project folder ) - Optional
 
**record :** If it is called True, it saves the records to the file. (default False ) - Optional

 ##### Usage : 
		 

    logger.error(message="test")
    logger.warning(message="test")
    logger.info(message="test")
    
 
 ##### Using Exception Catcher
	from Camper.ExceptionCatcher import CamperException
	@CamperException.exception_catcher(default=5,record=True)  
	def example(value):
		#do something here


**default :**  if If the function receives an error, the value to return. (default None) - Optional  

**default_callback :** Sends the default value to the specified function. - Optional 

 **error_callback :**  Sends the error message to the specified function. - Optional  

**log_path :** The path of the saved log file (default project folder ) - Optional

**record :** If it is called True, it saves the records to the file. - Optional

**post_endpoint :** If post_endpoint is added, it will post the message text to the url. (Post Payload {"error":" Error message"}) - Optional

**extra_data :** Extra data added to post_endpoint (key extra) - Optional
  
 ###### Contribute:
Send me more features if you want it

We need your Help to become it to better.

 ###### EDIT:
 07-16-2019 : Add Sentry Capture Exception Feature
 for using - CamperException(sentry_dns="http://xxxxx.sentry.io/xxxxx") 

###### Contact:

>abdullahkulcu@outlook.com 
