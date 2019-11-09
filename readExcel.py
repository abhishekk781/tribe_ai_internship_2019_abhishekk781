import xlrd

'''
	This function is responsible for fetching data form excel file based on file location
	@param fileLocation 	location of path where excel file is located

'''
def readExcelFile(fileLocation):
	workbook = xlrd.open_workbook(fileLocation)
	sheet = workbook.sheet_by_index(0)

	numberOfRows = sheet.nrows
	numberOfCols = sheet.ncols


	data = [[sheet.cell_value(r,c) for c in range(numberOfCols)] for r in range(numberOfRows)]
	mapped_data = []	#list of dictionary contained mapped data 
	
	for i in range(1,len(data)):
		dic = {}
		for j in range(len(data[0])):
			dic[data[0][j]] = data[i][j]
		mapped_data.append(dic)
	
	return mapped_data

