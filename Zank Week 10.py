#Zank Week 10

import csv

with open('names.csv', 'w', newline ='')as csvfile:
    fieldnames = ['Name', 'Address', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    phone = input("Please enter your phone number: ")

    dir
    Phone = phone
    Address = address
    Phone = phone

    writer.writeheader()
    writer.writerow({'Name, Address, Phone'})

