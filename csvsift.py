import csv
import numpy as np
import numbers
import re
import subprocess as sp
import csv
#reduced = filter(lambda w: for w !="" in A[i][9], re.split(r'\W+', sentence.lower()))

#The next function I need takes the UPB, the Co-op and Cafe sales data, and the minimum "upkeep" to then promt the user
#to pay certain bills, and also prompt the user about the deposit habits for the upcoming week (obviously including the day it is generated)
#then it should output the projection report based on the inputvdata
#I also need bank transaction data

def compare(A=[[]],B=[[]],Amount=0,Bmount=0,Afield=1,Bfield=1):
	# Code test: copy and paste into terminal: import csvsift as cs;reg = cs.mat();201707300703 0433Register;ban=cs.mat();201707300703 Transaction;Areg=7;Aban=3;Freg=4;Fban=2;cs.compare(reg,ban,Areg,Aban,Freg,Fban)
	K=[[]] #the best matrix ever
	C=[]
	D=[]
	E=[]
	for i in range(0,len(A)-1): #row amount == length of column... for some reason, the range overshoots. Even np.arange overshoots... why? Why is it showing up now?
		for j in range(0,len(B)-1): 
			if A[i][Amount] == B[j][Bmount]:
				C=np.append(C,[A[i][Amount]])
				D=np.append(D,[A[i][Afield]])
				E=np.append(E,[B[j][Bfield]]) 
	K=[[C[k],D[k],E[k]] for k in range(0,len(C))]
	print K 
	k=0
	for l in range(0,len(K)-1):
		while k < len(K)-1: #I don't get why it is missing when the range(0,len(K)) does not include the right endpoint
			k += 1
			if K[l] == K[k]:
				if k != l:
					K = K.pop(k)
		else:
			break
	return K #It works, but there are still duplicates
		
def contrast(A=[[]],B=[[]],Amount=0,Bmount=0,Afield=1,Bfield=1): #simply does the opposite of compare, it will tell me the things which don't match up
	# Code test: copy and paste into terminal: import csvsift as cs;reg = cs.mat();201707300703 0433Register;ban=cs.mat();201707300703 Transaction;Areg=7;Aban=3;Freg=4;Fban=2;cs.compare(reg,ban,Areg,Aban,Freg,Fban)
	K=[[]] #the best matrix ever
	C=[]
	D=[]
	E=[]
	F=[]
	for i in range(0,len(A)-1): #row amount == length of column... for some reason, the range overshoots. Even np.arange overshoots... why? Why is it showing up now?
		for j in range(0,len(B)-1): 
			if A[i][Amount] != B[j][Bmount]:
				for k in range(0,len(C)):
					if C[k] !=A[i][Amount]:
						C=np.append(C,[A[i][Amount]])
				for l in range(0,len(D)):
					if D[l] !=A[i][Afield]:		
						D=np.append(D,[A[i][Afield]])
				for m in range(0,len(E)):
					if E[m] !=B[j][Bmount]:
						E=np.append(E,[B[j][Bmount]])	
				for n in range(0,len(F)):
					if F[n] !=B[j][Bfield]:
						F=np.append(F,[B[j][Bfield]]) 
	K=[[C[k],D[k]] for k in range(0,len(C))]
	J=[[E[k],F[k]] for k in range(0,len(E))]
	L = [K,J]
	return L 

def look4(A=[[]], B=[[]]):  #this will search through the transaction summary by vendor and give the Vendor name, the total amount in COGS, 
							#and rank the resulting array by amount  since I ultimately need a list of vendors and contact info, pairing with 
							#the vendor list and possibly data matching should be included The first matrix will be the vendor list, the second 
							#will be the transaction information
	C=[] #vendor name, list
	D=[] #vendor number, list
	F=[] #vendor name, list 2
	G=[] #vendor amount, list
	I=[] #vendor sum, list
	K=[[]] #vendor name with sum, array of tuples
	Y=[[]] #vendor name with liability sum and phone number, array of triples
	for j in np.arange(0,len(A[0])): # row length, to search through the row for the word "vendor"
		a = re.search("Vendor",A[0][j]) #grabs vendor column number by searching through the first row (header)
		b = re.search("Main Phone",A[0][j]) #grabs the phone number
		if a:
			for i in np.arange(0,len(A)): #dive down the rows, in a column
				C = np.append(C,[A[i][j]]) #append vendor names
		if b:
			for i in np.arange(0,len(A)): #dive down the rows, in a column
				D = np.append(D,[A[i][j]]) #append vendor numbers
	E=[[C[j],D[j]] for j in np.arange(0,len(C))] # this attaches the vendor name with the contact numbers
	print E
	for j in np.arange(0,len(B[0])): # row length, to search through the row for the word ""
		c = re.search("",B[0][j]) #grabs vendor name, represented by "", column number by searching through the first row (header)
		if c:
			for i in np.arange(0,len(B)): #dive down the rows, in a column
				if B[i][j] != "":
					F = np.append(F,[B[i][j]]) #append vendor names
			print F
			break #I have no idea why it continues, but this stops it from doing so
	for j in np.arange(0,len(B[0])): # row length, to search through the row for the word "Amount"
		d = re.search("Amount",B[0][j]) #grabs the column for the amounts
		if d:
			for i in np.arange(2,len(B)): #dive down the rows, in a column, starts from 2 to skip the header and the first blank
				if B[i][j] !="":
					G = np.append(G,[B[i][j]]) #append vendor amounts, G will contain all vendor amounts by the end
				if B[i][j] =="":
					print G
					S = sum(float(G[l]) for l in range(0,len(G))) #find the sum of liabilities.
																	#Goes back by the length of the sum and the stopping point
																	#Should go back to the first amount of the list
					print str(i-len(G))+ "," + str(i) #range of the block, may be useful for other code
					print S
					I = np.append(I,S) #append them to a list to later be paired with the vendor name
					G=[] #clears the array to be reused
				if i == len(B)-1: #the final case, the end of file
					print G
					S = sum(float(G[l]) for l in range(0,len(G))) #find the sum of liabilities.
																	#Goes back by the length of the sum and the stopping point
																	#Should go back to the first amount of the list
					print str(i-len(G))+ "," + str(i) #range of the block, may be useful for other code
					print S
					I = np.append(I,S) #append them to a list to later be paired with the vendor name
					G=[] #clears the array to be reused
	print len(I)
	print len(F)
	for i in range(0,len(I)):
		K=[[F[i],I[i]] for i in range(0,len(I))] #this attaches the vendor name with the sum
	print K #It works. Yay!
			#Now to match K's entries with E to create a new array: Y with the vendor name, total liabilities, and phone number
	n = []
	for i in range(0,len(K)):
		for j in range(0,len(E)):
			if K[i][0] == E[j][0]: #matches the vendor name
				n = np.append(n,j) #indicies where I need info from E
	print n
	n = [int(n[i]) for i in range(0,len(n))]
	EE = [E[j][1] for j in n]
	Y = [[K[i][0],K[i][1],EE[i]] for i in range(0,len(K))]
	print Y # IT WORKS. YAY!
			# Now to rank by highest to lowest. Let's try Insertion Sort:
			# Get references for each value (Y[i][2])
			# Take the second value out, and compare it to everything before it.
			# If it is larger than something before it, shift everything after that thing by one and insert the compared value
			# Continue until list is exhausted
	invasive_IS(Y)
	print Y #Gives the sorted array in low to high
	Y = Y[::-1] #could have just reversed the invasive_IS internal comparison
	print Y #THIS SHIT FUCKING WORKS!
	return Y


def write4(A="",B=[[]]):
	if A == "":
		A= raw_input("What will you name the output csv file: ")
		
	with open(A, 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(B[i] for i in range(0,len(B)))
		
def pi_s(seq): #why reinvent the wheel?
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]: #goes back through the entire list down to 0 compared to 1
            seq[j - 1], seq[j] = seq[j], seq[j - 1] #short hand for multiple lines with equal signs
            j -= 1	#this back tracks in the list

			
def invasive_IS(Y): #why reinvent the wheel? Because the wheel can't be used in space
    for i in range(1, len(Y)):
        j = i
        while j > 0 and Y[j - 1][1] > Y[j][1]: #goes through the entire list up to j
            Y[j - 1], Y[j] = Y[j], Y[j - 1] #short hand for multiple lines with equal signs (seems more like a swapping technique)
            j -= 1	
	
def look3(A=[[]]):  #this currently makes a list of rank 1. Might be best to have a rank 2 array. I could also make it accept the pyplot data as initial arguments: 
					#(title, axes label)
	C=[]
	#for j in np.arange(0,len(A[0])): #There are as many columns as the lengths of the rows
	for i in np.arange(0,len(A)): #There are as many rows as the lengths of the columns (How do I find the row that comes right before the numbers start?)
		j = 9 #This makes the j for loop above redundant, but it may be more useful with added complexity
        while A[i][j] !="":
            C = np.append(C,[float(A[i][j])])
            return C
            if A[i][j] =="":
                a=re.search("\d*\.\d\d",A[i-1][j])
                if a:
                    print "Stopped at " + "row: " + str(i) + ", column: " + str(j)
                    print  "The start of the list is located at: " #After I solve my first question, I can put the answer here.
                    print  "The end of the list is located at: "+ str(i-2) + ", column: " + str(j)
                    choice = raw_input("Do you wish to continue? (y/n)")
                    if choice =="y":
                        checkpoint = i
                        print "Checkpoint...row: " + str(i) + ", column: " + str(j)  +"...Continuing Search"
                        continue
                    if choice =="n":
                        print "End of search.. row: " + str(i) + ", column: " + str(j) 
                        return C
                
        
    

def cavg(A=[],t=1): #Takes averages in blocks of t + 1, shows a more refined set of data 
    k = 0
    z=[]
    while k + t <=len(A)-t:
        z = np.append(z,sum(float(A[i]) for i in np.arange(k,k+t+1))/len(np.arange(k,k+t+1)))
        k = k+t +1
    return z 
    
def ader(x=[],y=[],t=1):    #Calculates a derivative of market data based on a pre determined window, x is supposed to be days and y is supposed to be dollars. 
							#DOES NOT SHOW THE TRENDLINE I WANT. Probably best shown as an average derivative (use smallest step size, then use cavg)
	k = 0
	z=[]
	while (k + t)<=len(x)-t:
		z = np.append(z,[(float(y[k+t]) - float(y[k]))/(float(x[k+t]) - float(x[k]))])
		k = k + t
	return z
			

# def look(A=[[]]): #Designed to locate chunks of data with numbers and to give the range of this data for general use
	# for j in np.arange(0,len(A[0])): #There are as many columns as the lengths of the rows
		# for i in np.arange(0,len(A)): #There are as many rows as the lengths of the columns
			# r = re.search("(?<=Total) \w*",A[i][j])
			# if i == 0:
				# q = re.search("^(?!.*Total)
			# if r:
				# print "Stopped at " + A[i][j]
				# choice = raw_input("Do you wish to continue? (y/n)")
				# if choice =="y":
					# checkpoint = i
					# print "Checkpoint...row: " + str(i) + ", column: " + str(j)  "...Continuing Search"
					# continue
				# if choice =="n":
					# print "row: " + str(i) + ", column: " + str(j) 
					# return
                    
def look2(A=[[]]): #Designed to locate chunks of data with numbers and to give the range of this data for general use # 2!
	for j in np.arange(0,len(A[0])): #There are as many columns as the lengths of the rows
		for i in np.arange(0,len(A)): #There are as many rows as the lengths of the columns
			r = re.search("(?<=Total) \w*",A[i][j])
			if r:
				print "Stopped at " + A[i][j]
				choice = raw_input("Do you wish to continue? (y/n)")
				if choice =="y":
					checkpoint = i
					print "Checkpoint...row: " + str(i) + ", column: " + str(j) +  "...Continuing Search"
					continue
				if choice =="n":
					print "row: " + str(i) + ", column: " + str(j) 
					return	

def mat(A=""): #Designed to create a matrix out of a csv file for use in the terminal
	print "If you haven't, set the call of this function as a variable and you will have it for use in the terminal"
	if A == "":
		A = raw_input('What csv file would you like to open (give name without .csv at the end)? ')
	d = list(A)
	e = np.concatenate((d,['.','c','s','v']))
	f = "".join(e)
	with open(f, 'rb') as a:
		b = csv.reader(a)
		x=[row for row in b] #transforms csv file into a matrix of cells
	return x
	 
def goto(linenum): #Function to force code to go to a specific line number
    global line
    line = linenum
def upb(name="",date=""): #Pay DEM BILLS Y'ALL
	h = [[]]
	v = [] #payment index
	vtemp =[] #temporary payment index
	vn = [] #vendor name vector
	cake=[] #cake for a cow
	cup=[] #cup for a cow
	if name =="":
		name = raw_input('What csv file would you like to open (give name without .csv at the end)? ') #asks for the Unpaid Bills Detail
	if date =="":
		date = raw_input('Give the date of the Sunday before the workweek (format: xx/xx/xxxx) ') #asks for date
	d = list(name) 
	o = list(date) #o[i], i in 0,9
	print o
	p = str(int(o[3] + o[4]) + 7) # adds 7 days to encompass next week
	list(p)
	o[3] = p[0]#changes the input date to the new date
	o[4] = p[1]
	print d
	print o
	g = int(o[6])*10**7 + int(o[7])*10**6 + int(o[8])*10**5 + int(o[9])*10**4 + int(o[0])*10**3 + int(o[1])*10**2 + int(o[3])*10 + int(o[4]) #turns date into a unique integer
	print g
	e = np.concatenate((d,['.','c','s','v'])) #puts the .csv at the end, so you don't have to!
	f = "".join(e)
	print f
	with open(f, 'rb') as a:
		b = csv.reader(a)
		x=[row for row in b] #transforms csv file into a matrix of cells
	print len(x) #number of rows
	print len(x[1])	#number of columns
	for i in np.arange(1,len(x),1):
		q = re.search("^(?!.*Total).*[a-zA-Z0-9_']+( [a-zA-Z0-9_'])*",x[i][0]) #Does not start with Total
		r = re.search("(?<=Total) \w*",x[i][0]) #Contains Total
		if q:
			print x[i][0]
			start = i
			vn = np.append(vn,start) #the vendor name row location (column 0)
			vn = np.array([int(yn) for yn in vn]) #converts to integer, now we know where the vendor name is (without "Total")
		if r:
			#This is where it stops to search in the chunk
			vtemp=[]
			v1 = len(v) #initial length (zero at begining, since v has not been added to)
			for j in np.arange(1,len(x[0]),1): #j is the Due Date column
				s = re.search("Due Date",x[0][j])
				if s:
					dd = j #saves the due date column
					print x[0][j] #shows that it works
					for k in np.arange(start,i,1):
						n = re.search("\d\d/\d\d/\d\d\d\d",x[k][j]) #searches for the actual due dates
						if n:
							z = list(str(x[k][j])) #turns due date into a list
							t = int(z[6])*10**7 + int(z[7])*10**6 + int(z[8])*10**5 + int(z[9])*10**4 + int(z[0])*10**3 + int(z[1])*10**2 + int(z[3])*10 + int(z[4]) 
							#rearranges due date into a unique integer
							if t <= g:
								print x[k][j] #due date location is k,j (dd), prints the due date
								x[k][j]=t #changes the date value into a numeric value
								print x[k][j] #prints the converted format of the due date
								for l in np.arange(1,len(x[0]),1): #l is the Open Balance column
									u = re.search("Open Balance",x[0][l]) 
									if u:
										print x[k][l] #k is the row for the relevant entry in dollars, dollar location k,l (balance)
										balance = l #saves the location of the open balance column
										vtemp = np.append(vtemp,k)
										vtemp = np.array([int(y) for y in vtemp])
										v = np.append(v,k) #gets the row number for the payments
										v = np.array([int(y) for y in v]) #converts entries into integers for use as indicies
			v2 = len(v) #final length
			index = np.arange(v1,v2) #chunk of due bills
			print v
			print "these below are the locations of the new entries from this query in the total list"
			print index
			print vtemp
			q = range(0,len(vtemp)) #the indicies of vtemp
			#the purpose of the selection below is to keep or remove entries. It never adds entries
			#I seem to have broken it, the list v, is never tentative. IT is the total list. I need a temporary list
			print "These below are the the locations of the entries of the current query"
			print q
			if len(index) == 0: #skip the vendors we dont need to pay
					continue		
			else:
				bubbles = raw_input('Will you pay '+ str(x[start][0]) + '? (y/n): ') # x[start][o] is the vendor name
				print "You said: " + bubbles
				if bubbles == "y":
					print q
					if len(index) > 1:
						bigbubbles = raw_input('Which bills will you pay? (give list of index numbers with spaces or give "all" to pay all of them): ')
						if bigbubbles == "all":
							print v
							continue
						if bigbubbles != "all":
							cow = list(bigbubbles)#captures the list input. The spaces divide the numbers, but now I need to concatenate the two digit numbers
							print cow
							for i in range(0,len(cow)):
								if cow[i] !=" ":
									cup=np.append(cup,cow[i])# this gets the numbers in line
								if cow[i] ==" " or i ==len(cow)-1:
									cupe = "".join(cup) #this makes the individual digits into the whole number by concatenation
									cake = np.append(cake,cupe) #this makes our changes permanent
									print cake
									cup=[]	#this allows us to search for different numbers
							cake = [int(ele) for ele in cake] #makes an integer
							print cake
							ind = np.delete(q,cake)#the index list for deleting, it's the available indicies with the chosen bills taken out so they don't get deleted
							print ind
							print v # the row index of bills to pay in relation to the whole file
							v[index[0]:] = np.delete(v[index[0]:],ind)
							continue
					if len(index) ==1:
						continue
				if bubbles == "n":
					v = np.delete(v,index)
					print v
					continue	
				if bubbles != "y" or bubbles != "n":
					print "You have failed your country."
					break
	v = [int(y) for y in v]
	print v
	tot = sum(float(x[a][balance]) for a in v)
	print tot
	z = [[x[i][balance],x[i][dd]] for i in v]#balance seems to equal dd, but the array iteration works
	return z
	