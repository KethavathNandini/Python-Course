# comma separated key-value pairs enclosed within ()
# {key1 :value1, key2:value2,.......}
# dictionaries are mutable

student_det = {
    'name' : 'sinpie',
    'age' : 20,
    'phone-no': 12387869
}
student_det['personalaity'] = 'introvert' # adds new pair to the dict
print(student_det)
# get()
print(student_det.get('name'))
