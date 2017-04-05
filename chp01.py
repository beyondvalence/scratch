# !/usr/bin/env python27
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:15:29 2016

@author: waynetliu
"""
#%%
from __future__ import division

users = [
         { "id": 0, "name": "Hero" },
         { "id": 1, "name": "Dunn" },
         { "id": 2, "name": "Sue" },
         { "id": 3, "name": "Chi" },
         { "id": 4, "name": "Thor" },
         { "id": 5, "name": "Clive" },
         { "id": 6, "name": "Hicks" },
         { "id": 7, "name": "Devin" },
         { "id": 8, "name": "Kate" },
         { "id": 9, "name": "Klein" }
]
print users
#%%
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
#%%               
for user in users:
    user["friends"]=[]
#%% appends together, not separately
for i, j in friendships:
    users[i]["friends"].append(users[j]) # adds j as a friend of i
    users[j]["friends"].append(users[i]) # adds i as a friend of j

print"\n", "users", "\n\n", users
#%%
# for first two friendship tuples
# hero - dunn, sue
# dunn - hero 
# sue  - hero (dunn)

def number_of_friends(user):
    """how many friends does user have?"""
    return len(users["friends"])    # length of friends_id list
    
total_connections = sum(number_of_friends(user) for user in users) # 24

print "total connections: ", total_connections

num_users = len(users)
avg_connections = num_users / total_connections

# create a list of (ids, number of friends)
num_friends_by_id = [(users["id"], number_of_friends(user))
                    for user in users]
                    
sorted(num_friends_by_id, 
       key=lambda (user_id, num_friends): num_friends, reverse=True)

print("/n", num_friends_by_id)
