#
# OBJECTIVE:
# for each department,
#       the number of times a product was requested,
#       number of times a product was requested for the first time
#       and a ratio of those two numbers.
#
# add_to_cart_order: sequence order in which each product was added to shopping cart
#   
# INPUTS
#   1. products.csv
#       product_id,product_name,aisle_id,department_id
#   2. order_products.csv
#       order_id,product_id,add_to_cart_order,reordered
#
# PRE-ANALYSIS checks
#
#   We performed an initial analysis to confirm that
#       the same product_id DID NOT exist in multiple departments.
#   Hence, the inputs are sufficient to summarize the results per department.
#
#   Just in case, the same product_id DID exist in multiple departments.
#       Our results would have been misleading, because the orders for a product
#       could erroneously be considered for multiple departments.
#
#       To overcome such a case,
#           we would have created a tuple (department_id, product_id) based lookup key
#           and proceeded accordingly for the summary at the Tuple level
#
# CAUTION
#
#   I had to use encoding="ascii", errors="surrogateescape" to overcome an encoding error
#       while reading the Input files. It may lead to missing some data unintentionally
#
#   I shall proceed jsut for the sake of the coding challenge
#       simply to demonstrate programming abilities
#
#
# APPROACH
#
# I have created 2 Dictionaries:
# 1. dictLookupDept: here I use Product_ID as KEY to lookUp Department_ID value
#                   using the products.csv
# 2. dictDeptMeasures: here I maintain Output results,
#           for each department_id (using it as the unique Key)
#               we shall update the corresponding statistics
#                   number_of_orders, number_of_first_orders
#               based on product_orders.csv data
#
#   RATIONALE: for choosing DICTIONARY as the data structure / data container
#               a. We need to be able to perform fast Key based search/ LookUp.
#                       Dictionaries provide Hash Key algorithms for fast search.
#               b. We can maintain a corresponding LIST of values.
#                       The value corresponding to each key, itself may be a list of items.
#           Thus a Dictionary functions similar to a relational database table.
#
# REPORT (OBJECTIVE)
# We need to generate a CSV file
#       (using dictDeptMeasures)
#       where each row is
#           department_id,number_of_orders,number_of_first_orders,percentage
#       Only for cases having number_of_orders > 0
#       Report must be Sorted by department_id 

# Libraries being used
import sys      # SYS library is part of standard Python 3.7 version
import csv      # CSV library is part of standard Python 3.7 version

# Identify Folder Paths
strPathInput  = "../input"
strPathOutput  = "../output"

# Identify Inputs: Filenames 
strCSV_Products      = "products.csv"

#strCSV_ProductOrders = "order_products__train.csv"      # Test_train
#strCSV_ProductOrders = "order_products__prior.csv"      # Test_prior
strCSV_ProductOrders = "order_products.csv"

# Identify Outputs: Filenames 
#strCSV_Report        = "report_train.csv"               # Test_train
#strCSV_Report        = "report_prior.csv"               # Test_prior
strCSV_Report        = "report.csv"

# Fully qualified Path & Filenames
strFileProducts         = strPathInput  + "/" + strCSV_Products
strFileProductOrders    = strPathInput  + "/" + strCSV_ProductOrders

strFileReport           = strPathOutput + "/" + strCSV_Report


##### Read the Inputs  #####
print("PARSE PRODUCTs FILE~~~~~~~~~~~~~Begin~~~~~~~~~~~~~~~~~~")
nRow           = 0
dictLookupDept = {}
with open(strFileProducts, 'r', newline='', encoding="ascii", errors="surrogateescape") as fileCSV_Products:
    # CSV library is part of standard Python 3.7 version
    CSV_Reader_Products = csv.reader(fileCSV_Products, delimiter=',')

    for (nRow, rowListCSVProducts) in enumerate(CSV_Reader_Products):
        # Skip the first Row (Its Field/ Column names)
        if nRow > 0:
            if (4 == len(rowListCSVProducts)):
                product_id, product_name, aisle_id, department_id = rowListCSVProducts

                # Data Type checks: to overcome unanticipated text values where numeric is expected
                if not isinstance(product_id, int):
                    product_id = int(product_id)
                if not isinstance(department_id, int):
                    department_id = int(department_id)

                # Input Data checking: Do programmatically, as its tough to visually browse huge text files
                if (department_id is None):
                    print("NoneType department_id ({}) encountered in Products file row '{}' ".format(department_id, rowListCSVProducts))
                    department_id = sys.maxsize     #Cant use None. NONETYPE is not iterable so cannot be a key        #"Undefined in products.csv"

                if (0 == len(dictLookupDept)) | (product_id not in dictLookupDept): 
                    dictLookupDept.update({product_id: department_id})
                    if nRow < 5:
                        print('Dictionary: added product_id {}: department_id {}'.format(product_id, department_id))
                else:
                    if (department_id != dictLookupDept.get(product_id)):
                        print('Warning: some product_id ({}) are assigned to multiple department_id ({}). Consider redesigning the solution'.format(product_id, department_id))
                        time.sleep(2)
                    #else:
                        # Valid value already exists: Do Nothing
                        # print('Dictionary: updated product_id ({}): department_id ({})'.format(product_id, department_id))
                        # dictLookupDept.update({product_id: department_id})
            else:
                print(" Row {} does not have expected 4 CSV items".format(nRow))
                print(type(rowListCSVProducts))
                print(rowListCSVProducts)

print('dictLookupDept has {} unique product_id (s) '.format(len(dictLookupDept.items())))
print(type(dictLookupDept))
#print(dictLookupDept)
print("PARSE PRODUCTs FILE~~~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~")

print("PARSE ORDER DETAILs FILE~~~~~~~~~~~Begin~~~~~~~~~~~~~~~~~~~~")
nRow                    = 0
dictLookupOrderSummary  = {}
with open(strFileProductOrders, 'r', newline='', encoding="ascii", errors="surrogateescape") as fileCSV_Orders:
    # CSV library is part of standard Python 3.7 version
    CSV_Reader_Orders = csv.reader(fileCSV_Orders, delimiter=',')

    for (nRow, rowListCSVOrders) in enumerate(CSV_Reader_Orders):
        # Skip the first Row (Its Field/ Column names)
        if nRow > 0:
            if 4 == len(rowListCSVOrders):
                order_id, product_id, add_to_cart_order, reordered = rowListCSVOrders

                # Data Type checks: to overcome unanticipated text values where numeric is expected
                if not isinstance(product_id, int):
                    product_id = int(product_id)
                if not isinstance(add_to_cart_order, int):
                    add_to_cart_order = int(add_to_cart_order)
                if not isinstance(reordered, int):
                    reordered = int(reordered)

                # Find Corresponding department_id
                if product_id in dictLookupDept:
                    # If Product is known, fetch its Department
                    department_id = dictLookupDept.get(product_id)
                    # Input Data checking: Do programmatically, as its tough to visually browse huge text files
                    if department_id is None:
                        print("Warning: None value department_id encountered for product_id ({}) in Orders file row '{}' ".format(product_id, rowListCSVOrders))
                else:
                    print("Warning: Unknown product_id ({}) encountered in Orders file row '{}'. \n Products.csv file may not be complete. Please check more ".format(product_id, rowListCSVOrders))
                    # If Product is unknown, Assign it to a Dummy Department
                    department_id = sys.maxsize     #Cant use None. NONETYPE is not iterable so cannot be a key        #"Undefined in products.csv"
                    # Update Product-Department Lookup Dictionary
                    dictLookupDept.update({product_id: department_id})
                    print("Warning: Unknown product_id ({}) was assigned to a Dummy department_id ({}) \n to ensure that it gets accounted for in the results \n Check with Business for appropriateness ".format(product_id, department_id))
                    
                # Create Summary row for Department, if it doesnt already exist
                if (0 == len(dictLookupOrderSummary)) | (department_id not in dictLookupOrderSummary):
                    # Output fields: department_id,number_of_orders,number_of_first_orders,percentage
                    number_of_orders, number_of_first_orders = [0, 0]
                    dictLookupOrderSummary.update({department_id: [number_of_orders, number_of_first_orders]})
                    if nRow < 5:
                        print('Dictionary: Introduced department_id {}'.format(department_id))
                else:
                    # Find Department Summary status to Update
                    [number_of_orders, number_of_first_orders] = dictLookupOrderSummary.get(department_id)

                # Increment Count of Total products ordered, for the Department
                number_of_orders = number_of_orders + 1
                # Check if its a Reorder
                if (0 == reordered):
                    # Increment Count of Total First orders, for the Department
                    number_of_first_orders = number_of_first_orders + 1
                    dictLookupOrderSummary.update({department_id: [number_of_orders, number_of_first_orders]})
                # Update Department Summary
                dictLookupOrderSummary.update({department_id: [number_of_orders, number_of_first_orders]})
                if nRow < 5:
                    print('Dictionary: Updated measures for department_id {}'.format(department_id))
            else:
                print(" Row {} does not have expected 4 CSV items".format(nRow))
                print(type(rowListCSVOrders))
                print(rowListCSVOrders)

print('dictLookupOrderSummary has {} unique department_id (s) '.format(len(dictLookupOrderSummary.items())))
print(type(dictLookupOrderSummary))
#print(dictLookupOrderSummary)
print("PARSE ORDER DETAILs FILE~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~~~")

# OUTPUT REPORT
# Report
# We need to generate a CSV file
#       where each row is
#           department_id,number_of_orders,number_of_first_orders,percentage
#       Only for cases having number_of_orders > 0
#
#       Sorted by Department_ID
#
# The output file should adhere to the following rules
#   1. It is listed in ascending order by department_id
#   2. A department_id should be listed only if number_of_orders is greater than 0
#   3. percentage should be rounded to the second decimal

print("OUTPUT GENERATION ~~~~~~~~~~~Begin~~~~~~~~~~~~~~~~~~~~")
with open(strFileReport, 'w', newline='', encoding="ascii", errors="surrogateescape") as fileCSV_Report:
    fileCSV_Report.write("department_id,number_of_orders,number_of_first_orders,percentage\n")
    # Output requirement 1. It is listed in ascending order by department_id
    for (nRow, department_id) in enumerate(sorted(dictLookupOrderSummary.keys())):
        [number_of_orders, number_of_first_orders] = dictLookupOrderSummary.get(department_id)
        # Output requirement 2. A department_id should be listed only if number_of_orders is greater than 0
        # Check if there were any orders
        if 0 < number_of_orders:
            percentage = number_of_first_orders / number_of_orders
            #  Output requirement 3. percentage should be rounded to the second decimal
            fileCSV_Report.write("{},{},{},{:.2f}\n".format(department_id,number_of_orders,number_of_first_orders,percentage))
print("OUTPUT GENERATION ~~~~~~~~~~~End~~~~~~~~~~~~~~~~~~~~")
            
    
