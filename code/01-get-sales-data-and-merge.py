import urllib
from datetime import datetime
import pandas as pd
import glob
import os

#### THIS IS THE ONLY CODE YOU SHOULD NEED TO CHANGE, DEFINE YOUR WORKING DIRECTORY HERE
workDir = '/Users/danielmsheehan/GIS/projects/property_sales/' #change to nyc_property_sales
#### THIS IS THE ONLY CODE YOU SHOULD NEED TO CHANGE, DEFINE YOUR WORKING DIRECTORY HERE

d            = workDir + "data/"
years        = xrange(2003, 2015)
boroList     = ['Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'Staten Island']
boroNameList = [w.lower().replace(' ','') for w in boroList] 
boroAbbrev   = ['MN','BX','BK','QN','SI']

def makeDirectoryStructure(theDir):
	print 'adding subdir folders for ' + theDir
	dataDir = theDir+'/data' 
	if not os.path.exists(dataDir):
		os.makedirs(dataDir)
	inpDir = theDir+'/data/input' 
	if not os.path.exists(inpDir):
		os.makedirs(inpDir)
		os.makedirs(inpDir+'/rolling_sales')
		os.makedirs(inpDir+'/annual_sales')
	proDir = theDir+'/data/processing' 
	if not os.path.exists(proDir):
		os.makedirs(proDir)
		os.makedirs(proDir+'/rolling_sales')
		os.makedirs(proDir+'/annual_sales')
	outDir = theDir+'/data/output' 
	if not os.path.exists(outDir):
		os.makedirs(outDir)

makeDirectoryStructure(workDir)

#maybe get rid of this, since we're mostly looking at annual sales
print 'download rolling sales'
for i in boroNameList:
	ftime  = str(datetime.now()).replace(' ','-').replace(':','-').replace('.','-')
	inFile = "http://www1.nyc.gov/assets/finance/downloads/pdf/rolling_sales/rollingsales_"+i+".xls"
	ouFile = d+"input/rolling_sales/rollingsales_"+i+"_"+ftime+".xls"
	urllib.urlretrieve(inFile, ouFile)
	#print ouFile.split('/')[-1], 'is fully downloaded.' #resource: http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python

print 'download annual sales'
for i in boroNameList:
	for j in years:
		n = str(j)
		m = '0' + str(j - 2000) 
		if j < 2007:
			if i == 'statenisland': 
				k = 'si'	
				inFile = "http://www1.nyc.gov/assets/finance/downloads/sales_"+k+"_"+m+".xls"
			else:
				inFile = "http://www1.nyc.gov/assets/finance/downloads/sales_"+i+"_"+m+".xls"
		elif j == 2007:
			inFile = "http://www1.nyc.gov/assets/finance/downloads/excel/rolling_sales/sales_"+n+"_"+i+".xls"
		elif j == 2008:
			inFile = "http://www1.nyc.gov/assets/finance/downloads/pdf/09pdf/rolling_sales/sales_"+n+"_"+i+".xls"
		elif j == 2009:
			inFile = "http://www1.nyc.gov/assets/finance/downloads/pdf/rolling_sales/annualized-sales/"+n+"_"+i+".xls"
		elif j > 2009:
			j = str(j)
			inFile = "http://www1.nyc.gov/assets/finance/downloads/pdf/rolling_sales/annualized-sales/"+n+"/"+n+"_"+i+".xls" #http://www1.nyc.gov/assets/finance/downloads/pdf/rolling_sales/annualized-sales/2014/2014_manhattan.xls
		else:
			print 'THERE WAS A PROBLEM WITH THE DOWNLOAD'
		#print inFile
		ftime  = str(datetime.now()).replace(' ','-').replace(':','-').replace('.','-')
		ouFile = d+"input/annual_sales/"+n+'_'+i+"_"+ftime+".xls"
		urllib.urlretrieve(inFile, ouFile)
		#print ouFile.split('/')[-1], 'is fully downloaded.'

df_list  = []
allCount = 0

<<<<<<< HEAD
#maybe get rid of this b/c only looking at annual sales
for i, j in zip(boroNameList,boroList):
	boroFiles = glob.glob(d+"input/rolling_sales/rollingsales_"+i+"_*.xls") #http://stackoverflow.com/questions/23430395/glob-search-files-in-date-order
	boroFiles.sort(key=os.path.getmtime)
	#print("\n".join(boroFiles))
	mostRecent = boroFiles[-1]
	#print mostRecent

	inFile = mostRecent #d+"input/rolling_sales/rollingsales_"+i+"_"+ftime+".xls"
	ouFile = mostRecent.replace('input','processing').replace('.xls','.csv')

	df = pd.io.excel.read_excel(inFile, j, skiprows=4)
	df.to_csv(ouFile, index=False)
	print df.columns
	print i, len(df.index)
	allCount += len(df.index)
	df_list.append(df)

print allCount
df = pd.concat(df_list)
print len(df.index)
df = df.rename(columns=lambda x: x.replace(' ', '_').lower()) #rename cols, lower and replace ' ' with '_'

df['sale_date'] = pd.to_datetime(df['sale_date'])
df['sale_month'] = df['sale_date'].map(lambda x: x.strftime('%m')) #pull out month, set field as datetime first
df['sale_year']  = df['sale_date'].map(lambda x: x.strftime('%Y')) #pull out year, set field as datetime first
df['bbl_str'] = df.borough.map(str) + '-' + df.block.map(str) + '-' + df.lot.map(str)
df['sale_bbl'] = (df['borough']*1000000000) + (df['block']*10000) + df['lot']
df.to_csv(d+'processing/rolling_sales/all.csv', sep=',', index=False)

df_list  = []
allCount = 0

#years        = xrange(2012, 2015)

=======
>>>>>>> origin/master
for m in years:
	n = str(m)
	for i, j in zip(boroNameList,boroList):
		print i, j, n
		boroFiles = glob.glob(d+"input/annual_sales/"+n+"_"+i+"_*.xls") #http://stackoverflow.com/questions/23430395/glob-search-files-in-date-order
		print boroFiles
		boroFiles.sort(key=os.path.getmtime)
		print("\n".join(boroFiles))
		mostRecent = boroFiles[-1]
		#print mostRecent

		inFile = mostRecent #d+"input/rolling_sales/rollingsales_"+i+"_"+ftime+".xls"
		ouFile = mostRecent.replace('input','processing').replace('.xls','.csv')

		print i, n, 'up next...'
		if m < 2011:
			df = pd.io.excel.read_excel(inFile, j, skiprows=3)
		else: 
			df = pd.io.excel.read_excel(inFile, j, skiprows=4)
		df.to_csv(ouFile, index=False)
		df = df.rename(columns=lambda x: x.replace('\n', '')) #some excel files had carriage returns, getting rid of those here
		print df.columns
		print i, n, 'has', len(df.index), 'rows'
		allCount += len(df.index)
		df_list.append(df)

print allCount
df = pd.concat(df_list)
print len(df.index)

for i in df.columns:
	print  i
df = df.rename(columns=lambda x: x.replace(' ', '_').lower()) #rename cols, lower and replace ' ' with '_'

df['sale_date'] = pd.to_datetime(df['sale_date'])
df['sale_month'] = df['sale_date'].map(lambda x: x.strftime('%m')) #pull out month, set field as datetime first
df['sale_year']  = df['sale_date'].map(lambda x: x.strftime('%Y')) #pull out year, set field as datetime first
df['bbl_str'] = df.borough.map(str) + '-' + df.block.map(str) + '-' + df.lot.map(str)
df['sale_bbl'] = (df['borough']*1000000000) + (df['block']*10000) + df['lot']
df.to_csv(d+'processing/annual_sales/all.csv', sep=',', index=False)
