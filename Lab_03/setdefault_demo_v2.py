"""script to demonstrate dictionary where the values are lists,
   and use of .setdefault() to add to the dictionary
"""

study = [('Jane', 'CSN08114'),
         ('Jane', 'SET08101'),
         ('Tim', 'SET08101'),
         ('Sue', 'CSN08114')]

studies = {}

for name, module in study:
    studies.setdefault(name, []).append(module)

print(studies)
