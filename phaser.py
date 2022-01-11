
###################################################################
# Script to pharse .csv file from yoda to be used in ansible.
# Author: Andre Rocha
# Owner: Telus
# Date: Oct 2021
# Version: 1.0
#
# How to use:   Input file should be name as yoda_flow.csv
#               Output file will be ansible_input.csv
###################################################################

import os
import re
import csv

###################################################################
# Make sure no auxiliary files are present in OS

# file_path = "/home/t972990/firewall-testing-automation/"
file_path = "/var/tmp/reports/"

if os.path.exists(f'{file_path}aux_file1.csv'):
  os.remove(f'{file_path}aux_file1.csv')

if os.path.exists(f'{file_path}aux_file2.csv'):
  os.remove(f'{file_path}aux_file2.csv')

if os.path.exists(f'{file_path}aux_file3.csv'):
  os.remove(f'{file_path}aux_file3.csv')

if os.path.exists(f'{file_path}ansible_input.csv'):
  os.remove(f'{file_path}ansible_input.csv')


###################################################################
# Check if input file yoda_flow.csv exist

if os.path.exists(f'{file_path}yoda_flow.csv'):

    ###################################################################
    # Step1 - verify service and create multiple lines if field contains
    #  more than 1 value

    with open(f'{file_path}yoda_flow.csv') as file:
        reader = csv.DictReader(file)

        with open(f'{file_path}aux_file1.csv' , "w") as file:
            file.write("Source,Destination,Service,Action" + '\n')
        file.close()

        for l in reader:
            source = l["Source"]
            destination = l["Destination"]
            service = l["Service"]
            action = l["Action"]

            service = service.replace(" ", "").split(",")

            size_x = len(service)
            x = 0

            with open(f'{file_path}aux_file1.csv' , "a") as file:
                while x < size_x:
                    if size_x >= x:
                        field_1 = source
                        field_2 = destination
                        field_3 = service[x]
                        field_4 = action
                        file.write("\"" + field_1 + "\"" + "," + "\"" + field_2 + "\"" + "," + field_3 + "," + field_4 + '\n')
                        x = x + 1
            file.close()
        file.close()

    ###################################################################
    # Step2 - verify destination and create multiple lines if field contains
    #  more than 1 value

    with open(f'{file_path}aux_file1.csv') as file:
        reader = csv.DictReader(file)

        with open(f'{file_path}aux_file2.csv' , "w") as file:
            file.write("Source,Destination,Service,Action" + '\n')
        file.close()

        for l in reader:
            source = l["Source"]
            destination = l["Destination"]
            service = l["Service"]
            action = l["Action"]

            destination = destination.replace(" ", "").split(",")
            size_x = len(destination)
            x = 0

            with open(f'{file_path}aux_file2.csv' , "a") as file:
                while x < size_x:
                    if size_x >= x:
                        field_1 = source
                        field_2 = destination[x]
                        field_3 = service
                        field_4 = action

                        file.write("\"" + field_1 + "\"" + "," + field_2 + "," + field_3 + "," + field_4 + '\n')
                        x = x + 1
            file.close()
        file.close()



    ###################################################################
    # Step3 - verify source and create multiple lines if field contains
    #  more than 1 value

    with open(f'{file_path}aux_file2.csv') as file:
        reader = csv.DictReader(file)

        with open(f'{file_path}aux_file3.csv' , "w") as file:
            file.write("Source,Destination,Service,Action" + '\n')
        file.close()

        for l in reader:
            source = l["Source"]
            destination = l["Destination"]
            service = l["Service"]
            action = l["Action"]
        
            source = source.replace(" ", "").split(",")
            size_x = len(source)
            x = 0

            with open(f'{file_path}aux_file3.csv' , "a") as file:
                while x < size_x:
                    if size_x >= x:
                        field_1 = source[x]
                        field_2 = destination
                        field_3 = service
                        field_4 = action

                        file.write(field_1 + "," + field_2 + "," + field_3 + "," + field_4 + '\n')
                        x = x + 1
            file.close()

    ###################################################################
    # Step4 - Remove lines with text in source and destination, Split Service into protocol and port and formats final file

    with open(f'{file_path}aux_file3.csv') as file:
        reader = csv.DictReader(file)

        with open(f'{file_path}ansible_input.csv' , "w") as file:
            file.write("Source,Destination,Protocol,Port,Action" + '\n')
        file.close()

        for l in reader:
            source = l["Source"]
            destination = l["Destination"]
            service = l["Service"]
            action = l["Action"]
        

            with open(f'{file_path}ansible_input.csv' , "a") as file:

                pattern = re.compile("[A-Za-z]")
                
                if not pattern.search(source):
                    if not pattern.search(destination):

                        var = service.split("/")
                        field_1 = source
                        field_2 = destination
                        field_4 = action
                        
                        file.write(field_1 + "," + field_2 + "," + var[0] + "," + var[1] + "," + field_4 + '\n')

            file.close()



else:
    print ("The input file yoda_flow.csv does not exist!")

###################################################################
# Cleanup - Make sure no auxiliary files are present in OS

if os.path.exists(f'{file_path}aux_file1.csv'):
  os.remove(f'{file_path}aux_file1.csv')

if os.path.exists(f'{file_path}aux_file2.csv'):
  os.remove(f'{file_path}aux_file2.csv')

if os.path.exists(f'{file_path}aux_file3.csv'):
  os.remove(f'{file_path}aux_file3.csv')