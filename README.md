##API Design  
When thinking about making APIs, there are a few perspectives we need to consider :  
1- The data the front end needs - something as simple as a data query - GET  
2- The processing that needs to happen on server side and results rendered to front end - probably also GET? Depends on specific fxn  
3- The data that needs to get saved into the backend -  POST and PUT APIs   


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
  
  
#Endpoints
| HTTP Method | URI | Action | Why |
|-------------|:---:|------:|----:|
| GET | https://[hostname]/iam_farmer/api/v1.0/vendors | Retreive list of all vendors signed up | Can be helpful with marketing/community outreach |
| GET | https://[hostname]/iam_farmer/api/v1.0/vendors/[vendor_id] | Retrieve information associated with specific vendor | For Vendor Homescreen|
| GET | https://[hostname]/iam_farmer/api/v1.0/vendors/[vendor_id]/inventory | Retreive list of all bins and products and counts owned by vendor | For Inventory Management Screen|
| GET | https://[hostname]/iam_farmer/api/v1.0/orders/[vendor_id] | Retrieve information on all orders with speficic vendor w+- query params | For Order Management Screen|
| GET | https://[hostname]/iam_farmer/api/v1.0/orders/[order_id] | Retrieve details on specific order | For Order Details Screen |
| GET | https://[hostname]/iam_farmer/api/v1.0/locations | Retrieve all locations containing bins | For Building out map |
| POST | https://[hostname]/iam_farmer/api/v1.0/vendors | Create a new vendor | New Vendor Sign Up | 
| POST | https://[hostname]/iam_farmer/api/v1.0/orders | Create a new order | New Order Screen |
| POST | https://[hostname]/iam_farmer/api/v1.0/locations | Create a new location | For example if a new section was added to the building
| POST | https://[hostname]/iam_farmer/api/v1.0/bins | Create a new bin | Inventory Mgmt Functionality - "Add New Bin" | 
    
  
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

 
