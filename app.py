from readExcel import *
from readJson import *
from py2neo import Graph, Node, Relationship

graph = Graph("bolt://localhost:7687", user="neo4j", password="Sharma@123")

def createNode(label, id, attributename, value):
	node = graph.merge_one(label, "id", id)
	node.properties[attributename] = value
	node.push()

if __name__ == '__main__':

	file_location = "/home/abhishek/Desktop/github/intern_project/data/Intern_Task_Graph_Schema.xlsx"
	json_file_location = "data/test_json.json"
	
	data = readExcelFile(file_location)
	json_file = readJson(json_file_location)
	#print(data)

	for row in data:
		if(row['Node/Relationship'] == 'Node'):
			for key,val in row.items():
				if(val=="NA" or key=="Label (Primary)"): continue
				else: createNode(row["Label (Primary)"], row["Seq_id"], key, val);
