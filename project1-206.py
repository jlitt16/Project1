import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
	inFile = open(file,'r')
	top_line = inFile.readline()
	info_lines = inFile.readlines()
	top_line_list = top_line.split(",")
	new_list = []
	inFile.close()
	for x in info_lines[0:]:
		diction = {}
		split = x.split(",")
		diction[top_line_list[0]]= split[0]
		diction[top_line_list[1]]= split[1]
		diction[top_line_list[2]]= split[2]
		diction[top_line_list[3]]= split[3]
		diction[top_line_list[4].strip()]= split[4].strip()
		if diction not in new_list:
			new_list.append(diction)
	return new_list
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	pass
def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
	x = sorted(data, key = lambda k: k[str(col)])
	organized_list = []
	for name in x:
		first = name["First"]
		second = name["Last"]
		organized_list.append(first + " " + second)
	return organized_list[0]
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	pass
def classSizes(data):
# Create a histogram
# Input: list of dictionaries
	list_tot = []
	fresh_total = 0
	soph_total = 0
	junior_total = 0
	senior_total = 0
	for info in data:
		if info["Class"] == "Freshman":
			fresh_total+= 1
		elif info["Class"] == "Sophomore":
			soph_total += 1
		elif info["Class"] == "Junior":
			junior_total += 1
		else:
			senior_total +=1
	list_tot.append(('Freshman', fresh_total))
	list_tot.append(('Sophomore', soph_total))
	list_tot.append(('Junior', junior_total))
	list_tot.append(('Senior', senior_total))
	return sorted(list_tot, key = lambda k: k[1], reverse = True)
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	pass
def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
	birth_list = []
	most_birthdays = 0
	birth_dict = {}
	for info in a:
		x = info["DOB"].split("/")
		birth_months = x[0]
		if birth_months not in birth_dict:
			birth_dict[birth_months] = 1
		else:
			birth_dict[birth_months]+=1
	sorted_guy = sorted(birth_dict.items(), key = lambda k: k[1], reverse = True)
	return(int(sorted_guy[0][0]))
			# 	x = most_birthdays
# Output: Return the month (1-12) that had the most births in the data

	pass
def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
	outFile = open(str(fileName),"w")
	x = sorted(a, key = lambda k: k[str(col)])
	for name in x:
		first = name["First"]
		second = name["Last"]
		email = name["Email"]
		outFile.write(first + "," + second + "," + email + "\n")
	outFile.close()
#Output: No return value, but the file is written
	pass
def findAge(a):
# def findAge(a):
# Input: list of dictionaries
	current_year = int(2018)
	total_ages = 0
	num_of_people = 0
	for x in a:
		num_of_people+=1
		dob = x["DOB"]
		dob_split = dob.split('/')
		dob_year= dob_split[2]
		age = int(current_year - int(dob_year))
		total_ages+= age
	return(int(total_ages/num_of_people))
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	pass

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
