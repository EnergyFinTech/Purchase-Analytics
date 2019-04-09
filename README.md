## InsightDataEngineeringCodingChallenge
Coding challenge private repository for Inghts Data Engineering program application
Purchase-Analytics

### Problem & Objective
We are using the Instacart published dataset containing purchase orders.

For this challenge, we want to calculate a report summary 
(a.) per department, 
(b.) the count of times 'a product was requested', 
(c.) the count of times 'a product was requested for the first time' and 
(d.) a ratio of those two numbers ( c / b)

So we created the necessary program code in a file named rptDeptOrder.py and have made it avalable in the src directory. Our code has been developed and tested using Python version 3.6 

### Input Datasets
For this challenge, assume that we have two separate input data sources, order_products.csv and products.csv.
These two input files shall reside in the input directory.

#### PRODUCTS.CSV
It has been described to hold data on every product.
We assume that its the master table (as in Master-Detail relationship).
The file format is:
    product_id,product_name,aisle_id,department_id
where
    product_id: unique identifier of the product (Data type: Integer)
    product_name: name of the product (Data type: String)
    aisle_id: identifier of aisle in which product is located (Data type: Integer)
    department_id: identifier of department (Data type: Integer)

#### ORDER_PRODUCTS.CSV
We assumed each line of the file order_products.csv holds data for one request. The file format is:
    order_id,product_id,add_to_cart_order,reordered
where
    order_id: unique identifier of order (Data type: Integer)
    product_id: unique identifier of product (Data type: Integer)
    add_to_cart_order: sequence order in which each product was added to shopping cart (Data type: Integer)
    reordered: flag indicating if the product has been ordered by this user at some point in the past. The field is 1 if the user has ordered it in the past and 0 if the user has not. Here, we presume that the reordered flag accurately reflects whether the product has been ordered by the user before. (Data type: Integer)

### Output
The program reads the two input files from the input directory, and creates an output file, report.csv, in the output directory. 
For each department, the program computes the following statistics:
    number_of_orders: count of times a product was requested for its department. (If the same product was ordered multiple times, we counted it as multiple requests. We did not check whether a product appeared multiple times on an order, and counted each instance here.)
    number_of_first_orders: How many of those requests contain products ordered for the first time? (We presumed a 'reordered' flag value 0 to indicate a first order.)
    percentage: It is the percentage of requests containing products ordered for the first time compared with the total number of requests for products from that department. (e.g., number_of_first_orders divided by number_of_orders)

#### REPORT.CSV
The output file format is:
    department_id,number_of_orders,number_of_first_orders,percentage
The data type for percentage is float (2 decimal values). The other fields have an integer data type.

The output file adheres to the following pre-specified rules:
    (a.) Output is listed in a ascending sorted order by department_id, 
    (b.) department_id is listed only where number_of_orders is greater than 0, and 
    (c.) percentage has been rounded to the second decimal
    
### Repository directory structure
The directory structure for our repo looks like below:

    ├── README.md
    ├── run.bat                               (used to test in Windows environment)
    ├── run.sh
    ├── src
    │   └── rptDeptOrder.py
    ├── input
    │   └── products.csv
    |   └── order_products.csv
    ├── output
    |   └── report.csv
    └── insight_testsuite
        └── run_tests.bat                    (used to test in Windows environment)
        └── run_tests.sh
        └── tests
            ├── test_1
            |   ├── run.bat                  (used to test in Windows environment)
            |   ├── run.sh
            |   ├── src
            |   │   └── rptDeptOrder.py      (Its a link to or copy of main src/rptDeptOrder.py code)
            |   ├── input
            |   │   └── products.csv
            |   │   └── order_products.csv
            |   |__ output
            |       └── report.csv
            ├── test_train
            |   ├── run.bat                  (used to test in Windows environment)
            |   ├── run.sh
            |   ├── src
            |   │   └── rptDeptOrder.py      (Its a link to or copy of main src/rptDeptOrder.py code)
            |   ├── input
            |   │   └── products.csv
            |   │   └── order_products.csv   (Its a copy of order_products__train.csv)
            |   |__ output
            |       └── report.csv
            └── test_prior
                ├── run.bat                  (used to test in Windows environment)
                ├── run.sh
                ├── src
                │   └── rptDeptOrder.py      (Its a link to or copy of main src/rptDeptOrder.py code)
                ├── input
                │   └── products.csv
                |   └── order_products.csv   (Its a copy of order_products__prior.csv)
                └── output
                    └── report.csv
 
### Code
#### Development Environment
I created a single code script rptDeptOrder.py using Python version 3.6 (64-bit) using standard IDLE development environment on a Windows 10 PC. It references two standard python libraries sys and csv.

#### Data Structures
I created 2 Dictionary objects as data containers to facilitate processing:
1. dictLookupDept: here I use Product_ID as KEY to lookUp Department_ID value using the products.csv
2. dictDeptMeasures: here I maintain Output results,
           for each department_id (using it as the unique Key)
               we shall update the corresponding statistics
                   number_of_orders, number_of_first_orders
               based on product_orders.csv data

##### RATIONALE: for choosing DICTIONARY as the data structure / data container
               a. We need ability to perform a fast KEY based search/ LookUp.
                       Dictionaries provide Hash Key algorithms for fast search and sort.
               b. We can maintain a corresponding LIST of values, for each KEY.
                       The value corresponding to each key, itself may be a list of items (or other data containers).
           A Dictionary could be considered functionally similar to a relational database table with a unique key field based index.

#### Development Practice and Considerations
* The code follows a descriptive self-documented type coding style. General descriptive variable naming convention has been observed.
* Simplicity and readability has been preferred at some instances without sacrificing much efficiency. 
* Some extra checks have been incorporated to overcome often encountered issues dealing with data from unknown external sources. For example 
    - specified encoding="ascii" amd errors="surrogateescape" to overcome encoding errors while reading input files,
    - checking count of encountered values on each line to the expected format,
    - data type checking and conversion,
    - checking for missing or none,
    - warning when orders reference a product that is not listed in the master file,
    - generating descriptive diagnostic messages, etc.

### Testing
The code was tested using Python 3.6 version.
The execution timing seems satisfactory for this exercise.
 
The code was tested locally using various instances of order_products.csv created from order_products__prior.csv and order_products__train.csv files. The products.csv file was a common input for the various tests.
The test input data and generated results for the two scenarios have been uploaded to this repository in the respective folders test_prior and test_train.
 
Unit tests for specific instances of product_id were used for validation.
 
### Instructions
I developed and tested my code on a Windows Environment. I used Python version 3.6 64-bit version. 
The python code assumes that the the src folder is the current working directory for the python program code (rptDeptOrder.py).

I used run.bat and run_tests.bat files, besides the Python version 3.6 64-bit edition IDLE to successfully run my code for the various test scenarios (test_1, test_prior and test_train). The respective input and outputs are also uploaded in the repository.

I believe this code would work fine on a Unix/Linux environment too. I have named the command as python3 in the respective run.sh scripts.
