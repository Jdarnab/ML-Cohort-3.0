# def name( **name):
#     print(name['fname'], name['lname'])
# name(fname='Jd', lname='arnab')
# def Name(fname, mname, lname):
#     print(fname,mname,lname)
# Name('Jd','arnab','hello')
# def avg (*number):
#      sum=0
#      for i in number:
#           sum +=i
#      print(sum / len(number))
# avg(1,2)
# def name( fname, dob, pa):
#      print(f'name :{fname}, Place: {dob}, Permanent address :{pa}')
# name('jd','bb', 'sobuzbag')
#video12 task
# def NID(fname,lname, gender,dob,pr):
#      print(f"Name : {fname} {lname}")
#      print(f'Gender: {gender}')
#      print(f'Date of Birth :{dob}')
#      print('Address :', pr)
# NID('Jd', 'Arnab', 'Male', '21/08/1999', 'sobuzbag, Medda')

def median(*numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle = length // 2
    if length % 2 == 0:
        print( (sorted_numbers[middle + 1] + sorted_numbers[middle]) / 2)
    else:
        print( sorted_numbers[middle])

# median(1, 10, 3)
# def median(numbers):
#     if not numbers:
#         return None
#     sorted_numbers = sorted(numbers)
#     length = len(sorted_numbers)
#     middle = length // 2
#     if length % 2 == 0:
#         return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
#     else:
#         return sorted_numbers[middle]

# # Example usage:
median(2, 5, 1, 3, 4)



