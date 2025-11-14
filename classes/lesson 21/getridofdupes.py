studentdata = {'id1':
    {'name' : ['Sarah'],
        'class':['V'],
        'subject':['History', 'Math', 'History', 'Math']},
}
{'id2':
    {'name' : ['David'],
        'class':['V'],
        'subject':['History', 'Math', 'History', 'Math']},
}
{'id3':
    {'name' : ['Chan'],
        'class':['VI'],
        'subject':['History', 'Math', 'History', 'Math']},
}
result = {}
for key, value in studentdata.items():
    if value not in result.values():
        result[key]=value
print(result)