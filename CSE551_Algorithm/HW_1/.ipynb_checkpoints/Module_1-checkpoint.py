#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Heng Yu Hsu

# Input values
M = [ [2, 1, 4, 5, 3],              # Department preference list
     [4, 2, 1, 3, 5], 
     [2, 5, 3, 4, 1], 
     [1, 4, 3, 2, 5], 
     [2, 4, 1, 5, 3] ]
W = [ [5, 1, 2, 4, 3],              # Employee preference list
     [3, 2, 4, 1, 5], 
     [2, 3, 4, 5, 1], 
     [1, 5, 4, 3, 2], 
     [4, 2, 5, 3, 1] ]
N = 5                               # Number of departments & employees





# Initialize arrays using None
department_employee = [None] * N
employee_department = [None] * N
free_departments = list(range(N))


while free_departments:
    
    d = free_departments.pop(0)
    
    for e in M[d]:
        e -= 1

        if employee_department[e] is None: 
            
            department_employee[d] = e
            employee_department[e] = d
            break
        else:
            current_d = employee_department[e]
            
            if W[e].index(d + 1) < W[e].index(current_d + 1):
                
                department_employee[d] = e
                employee_department[e] = d

                free_departments.append(current_d)
                break




# Visualizing the result, Printing the output
Names = [ ['HR', 'CRM', 'Admin', 'Research', 'Development'],      # Initialize the mapping of names
         ['Adam', 'Bob', 'Clare', 'Diane', 'Emily'] ]
print('Result is:-')
for i in range(N):
    print(Names[0][i], ":", Names[1][department_employee[i]])                # Map the result to the names