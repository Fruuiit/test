import csv
import scipy
import numpy as np
from scipy.sparse import dok_matrix
# Reads csv file 
with open('testexample2.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		L = []
		for row in readCSV:
			#print(row)
			
			L.append(row[0]);


		#print(L)
		#M = list(set(L))
		
		Dforward = {}
		Dbackward = {}
		for i in range(len(L)):
			Dforward[L[i]] = i
			Dbackward[i] = L[i];
		#print(Dforward)
		#print(Dbackward);

with open('ad.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		Dtransfact = {}
		dtrfa_size = 0
		M = dok_matrix((265, 65070), dtype = np.int8)
		for row in readCSV:
			if row[0] not in Dtransfact.keys():
				Dtransfact[row[0]] = dtrfa_size
				dtrfa_size = dtrfa_size + 1;
			#M[Dtransfact.get(row[0]), Dforward.get(row[1])] = 1
			i = Dtransfact.get(row[0])
			j = Dforward.get(row[1])
			if j == None:
				j = 0;

			#print(row[0],row[1])
			#print(i,j)
			#print((Dtransfact.get(row[0]), Dforward.get(row[1])))
			M[i,j] = 1;

		#M[i,j] = 1
		#print(M[i,j])
		#print(Dtransfact.get('ENSG00000007372'))
		print(M.getcol(0).toarray());







