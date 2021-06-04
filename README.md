##API Design  
When thinking about making APIs, there are a few perspectives we need to consider :  
1- The data the front end needs - something as simple as a data query - GET  
2- The processing tha needs to happen on server side and results rendered to front end - probably also GET?  
3- The data that needs to get saved into the backend - we need POST and PUT APIs   


##iam_farmer  
Description :   
We want to create an app that helps businesses sign up to farmers market, manage inventory, fulfill order, analyze performance data, advertise their goods  
Each Vendor has many Bins. Each Bin contains Many Products.  
  
Goal :   
design a db structure, and REST endpoints for data access  
  
  
##Sample User Stories/Wireframe Screens :  
Vendor Info :   
-- Update Vendor Info  
-- Login Existing Vendor  
-- Sign Up New Vendor  
  
  
  
Inventory Management :     
-- Find Route to Specific Product/Bin  
-- Show All Product Availability  
-- Show Specific Product Availability  
-- Add New Bins  
-- Add New Product  
-- Re-Assign Bins to Products  
-- Move Bins (new location)  
  
 
Order Management :   
-- Create New Order  
-- Update Existing Order (Mark as complete, update status, add notes, etc. )  
-- Show Order History  
-- Optimize Route for Order Fulfillment

  
Performance Data Center :   
-- Show Order Stats (averages and totals)  
-- Show Sales Info 

  
Advertisement :   
-- Social Media Integration  
-- Advertisement Cost Management (Screen) 
  
  
#Sample Endpoints  
  
  
#others  
Questions Asked in Interview Prompt :   
1- What tools and frameworks would you use?  
App needs a DB, a web server, open HTTPS ports, a json processing library(jsonify), a web application (that's what runs the APIs), 
a web service framework (Flask) - this is a collection of libraries that does repeated tasks required for running/creating a web application/web services,
need a hashing library for protecting passwords saved in database, need an authorization framework (OAuth Standard?), also need firewall (server protection)
some of these tools are bundled in when utilizing cloud based infrastructure  
  
2-How would you build a cost model for using these tools?  
I don't know what a cost model is. Is this in regards to buying infrastructure and cloud services? Because if so, I'm not really sure if cost modeling is relevant when it comes to cloud services. There are many pay-as-you-go models, which often offer the flexibility of utlizing services and allowing for a feedback loop to modify as needed. At the end of the day, it all comes down to understanding your API and server usage stats.. through puts, availability (up-time) requirements, load handling, ...
  
3- Software Documentation :  
Key concepts in software documentation :   
3.1- use software documentation tooling for web-based and navigatebale documentation..  
  
3.2- create as much automation as possible. webhooks that allow for automatic documentation update whenever you commit code are the most awesome thing, but this relies on devs and engs to use meaningful commit messages.  Use discovery tools like Atlassian's REST API Browser (included in JIRA server) It automatically scans for Javadoc notations and config files to auto-generate documentation, while also allowing for manual descriptions to be typed in.  
  
3.3- Crucial information that needs to go into documentation : the endpoint, the auth requirement, the request payload and what parameter is required vs. optional, the response paylod

 
