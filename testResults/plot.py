import csv
import matplotlib.pyplot as plt

def getdata(nets,df,var):
	content_path = "/home/ian/Desktop/530final/testResults"

	net = content_path + "/"+nets
	if var == "HW":
		dataset = [12,16,32,64,128,256]
	else:
		dataset = [108,500,1000,2000,4000,6000]
	#dataset = [12]
	rt = []
	dataflow = df
	for i in dataset:
		if var == "HW":
			csv_file_path = net + "/"+dataflow+"_"+str(i)+"x"+str(i) + "/COMPUTE_REPORT.csv"
		else:
			csv_file_path = net + "/"+dataflow+"_"+var+str(i) + "/COMPUTE_REPORT.csv"

		# Open the CSV file in read mode
		with open(csv_file_path, mode='r') as file:
			csv_reader = csv.reader(file)
			temp = []
		# Read and print each row in the CSV file
			for row in csv_reader:
				temp.append(row)
			temp.pop(0)
			rt.append(temp)
			#print(rt)
	
	
	data = rt
	cycles = []
	for i in data:
		temp = []
		for j in i:
			temp.append(float(j[1]))
		cycles.append(temp)
		
	x_axis = [i for i in range(len(cycles[0]))]
	colors = ["blue","orange","green","red","purple","brown"]
	if var == "HW":
		labels = ["12x12","16x16","32x32","64x64","128x128","256x256"]
	else:
		labels = ["108","500","1000","2000","4000","6000"]
	tempNums = [12,16,32,64,128,256]
	for i in range(len(cycles)):
		
		tempNum = tempNums.pop(0)
		for j in range(len(cycles[i])):
			
			cycles[i][j] = cycles[i][j]*tempNum*tempNum
		plt.plot(x_axis, cycles[i], color=colors.pop(0), label=dataflow+"_"+var+labels.pop(0))
		
	plt.xlabel('Layers')
	plt.ylabel('area delay product')
	plt.title(nets+"\'s performance on dataflow "+dataflow+" while varing " + var)
	plt.legend()
	plt.show()
	
	util = []
	for i in data:
		temp = []
		for j in i:
			temp.append(float(j[3]))
		util.append(temp)
		
	x_axis = [i for i in range(len(util[0]))]
	colors = ["blue","orange","green","red","purple","brown"]
	if var == "HW":
		labels = ["12x12","16x16","32x32","64x64","128x128","256x256"]
	else:
		labels = ["108","500","1000","2000","4000","6000"]
	for i in util:
		plt.plot(x_axis, i, color=colors.pop(0), label=dataflow+"_"+var+labels.pop(0))
		
	plt.xlabel('Layer')
	plt.ylabel('Utilization')
	plt.title(nets+"\'s Utilization on dataflow "+dataflow+" while varing " + var)
	plt.legend()
	plt.show()
	
	
	
	
	
	for i in range(len(cycles)):
		cycles[i] = sum(cycles[i])
		
	labels = ["12x12","16x16","32x32","64x64","128x128","256x256"]
	plt.bar(labels, cycles, color='blue')
	plt.ylim(min(cycles)-1, max(cycles)+1)
	# Adding labels and title
	plt.xlabel('size of the array')
	plt.ylabel('total area delay product')
	plt.title(nets+"_"+df+"\'s total area delay product while varing size of the array")

	# Display the plot
	plt.show()
	
	
	
	
	

def plotDiff(nets):
	content_path = "/home/ian/Desktop/530final/testResults"

	net = content_path + "/"+nets
	var = "HW"
	if nets == "Resnet18":
		dataset = [12,16,12]
	else:
		dataset = [12,12,12]
	
	rt = []
	dataflows = ["is","os","ws"]
	
	for dataflow in dataflows:
		i = dataset.pop(0)
		csv_file_path = net + "/"+dataflow+"_"+str(i)+"x"+str(i) + "/COMPUTE_REPORT.csv"
		
		
		# Open the CSV file in read mode
		with open(csv_file_path, mode='r') as file:
			csv_reader = csv.reader(file)
			temp = []
		# Read and print each row in the CSV file
			for row in csv_reader:
				temp.append(row)
			temp.pop(0)
			rt.append(temp)
		#print(rt)
	
	
	data = rt
	cycles = []
	for i in data:
		temp = []
		for j in i:
			temp.append(float(j[1]))
		cycles.append(temp)
		
	x_axis = [i for i in range(len(cycles[0]))]
	colors = ["blue","orange","green","red","purple","brown"]
	if nets == "Resnet18":
		labels = ["is_12x12","os_16x16","ws_12x12"]
	else:
		labels = ["is_12x12","os_12x12","ws_12x12"]
	
	
	
	if nets == "Resnet18":
		tempNums = [12,16,12]
	else:
		tempNums = [12,12,12]
	for i in range(len(cycles)):
		
		tempNum = tempNums.pop(0)
		for j in range(len(cycles[i])):
			
			cycles[i][j] = cycles[i][j]*tempNum*tempNum
			
			
	for i in cycles:
		plt.plot(x_axis, i, color=colors.pop(0), label=labels.pop(0))
		
	plt.xlabel('Layers')
	plt.ylabel('area delay product')
	plt.title(nets+"\'s performance while varing dataflow")
	plt.legend()
	plt.show()
	
	util = []
	for i in data:
		temp = []
		for j in i:
			temp.append(float(j[3]))
		util.append(temp)
		
	x_axis = [i for i in range(len(util[0]))]
	colors = ["blue","orange","green","red","purple","brown"]
	if nets == "Resnet18":
		labels = ["is_12x12","os_16x16","ws_12x12"]
	else:
		labels = ["is_12x12","os_12x12","ws_12x12"]
	for i in util:
		plt.plot(x_axis, i, color=colors.pop(0), label=labels.pop(0))
		
	plt.xlabel('Layer')
	plt.ylabel('Utilization')
	plt.title(nets+"\'s Utilization while varing dataflow")
	plt.legend()
	plt.show()
	
	for i in range(3):
		cycles[i] = sum(cycles[i])/len(cycles[i])
		util[i] = sum(util[i])/len(util[i])
	dataflows = ["is","os","ws"]
	plt.bar(dataflows, cycles, color='blue')
	plt.ylim(min(cycles)-1, max(cycles)+1)
	# Adding labels and title
	plt.xlabel('Dataflow')
	plt.ylabel('Average area delay product')
	plt.title(nets+"\'s average performance while varing dataflow")

	# Display the plot
	plt.show()
	
	plt.bar(dataflows, util, color='blue')
	plt.ylim(min(util)-1, max(util)+1)
	# Adding labels and title
	plt.xlabel('Dataflow')
	plt.ylabel('Average Utilization')
	plt.title(nets+"\'s average utilization while varing dataflow")

	# Display the plot
	plt.show()


def compare(nets):
	content_path = "/home/ian/Desktop/530final/testResults"

	net1 = content_path + "/"+nets[0]
	net2 = content_path + "/"+nets[1]
	rt = []
	csv_file_path = net1 + "/"+"os"+"_"+str(12)+"x"+str(12) + "/COMPUTE_REPORT.csv"
	
	
	# Open the CSV file in read mode
	with open(csv_file_path, mode='r') as file:
		csv_reader = csv.reader(file)
		temp = []
	# Read and print each row in the CSV file
		for row in csv_reader:
			temp.append(row)
		temp.pop(0)
		rt.append(temp)
	#print(rt)
	csv_file_path = net2 + "/"+"os"+"_"+str(12)+"x"+str(12) + "/COMPUTE_REPORT.csv"
	
	
	# Open the CSV file in read mode
	with open(csv_file_path, mode='r') as file:
		csv_reader = csv.reader(file)
		temp = []
	# Read and print each row in the CSV file
		for row in csv_reader:
			temp.append(row)
		temp.pop(0)
		rt.append(temp)
	
	data = rt
	cycles = []
	for i in data:
		temp = []
		for j in i:
			temp.append(float(j[1]))
		cycles.append(temp)
		
	x_axis = [i for i in range(len(cycles[0]))]
	colors = ["blue","orange","green","red","purple","brown"]
	labels = ["mobilenet_os_12x12","myNet_os_12x12"]
	
	
	

	for i in range(len(cycles)):

		for j in range(len(cycles[i])):
			
			cycles[i][j] = cycles[i][j]*12*12
			
			
	for i in cycles:
		plt.plot(x_axis, i, color=colors.pop(0), label=labels.pop(0))
		
	plt.xlabel('Layers')
	plt.ylabel('area delay product')
	plt.title("Comparing "+nets[0]+" and "+nets[1]+"\'s performance")
	plt.legend()
	plt.show()
	
	util = []
	for i in data:
		temp = []
		for j in i:
			temp.append(float(j[3]))
		util.append(temp)
		
	x_axis = [i for i in range(len(util[0]))]
	colors = ["blue","orange","green","red","purple","brown"]
	labels = ["mobilenet_os_12x12","myNet_os_12x12"]
	for i in util:
		plt.plot(x_axis, i, color=colors.pop(0), label=labels.pop(0))
		
	plt.xlabel('Layer')
	plt.ylabel('Utilization')
	plt.title("Comparing "+nets[0]+" and "+nets[1]+"\'s utilization")
	plt.legend()
	plt.show()
	
	for i in range(2):
		cycles[i] = sum(cycles[i])/len(cycles[i])
		util[i] = sum(util[i])/len(util[i])
	dataflows = ["mobilenet_os_12x12","myNet_os_12x12"]
	plt.bar(dataflows, cycles, color='blue')

	# Adding labels and title
	plt.xlabel('Architecture')
	plt.ylabel('Average area delay product')
	plt.title("Comparing "+nets[0]+" and "+nets[1]+"\'s performance")

	# Display the plot
	plt.show()
	
	plt.bar(dataflows, util, color='blue')

	# Adding labels and title
	plt.xlabel('Architecture')
	plt.ylabel('Average Utilization')
	plt.title("Comparing "+nets[0]+" and "+nets[1]+"\'s utilization")

	# Display the plot
	plt.show()


def getdata0(nets,df,var):
	content_path = "/home/ian/Desktop/530final/testResults"

	net = content_path + "/"+nets
	if var == "HW":
		dataset = [12,16,32,64,128,256]
	else:
		dataset = [108,500,1000,2000,4000,6000]
	#dataset = [12]
	rt = []
	dataflow = df
	for i in dataset:
		if var == "HW":
			csv_file_path = net + "/"+dataflow+"_"+str(i)+"x"+str(i) + "/COMPUTE_REPORT.csv"
		else:
			csv_file_path = net + "/"+dataflow+"_"+var+str(i) + "/COMPUTE_REPORT.csv"

		# Open the CSV file in read mode
		with open(csv_file_path, mode='r') as file:
			csv_reader = csv.reader(file)
			temp = []
		# Read and print each row in the CSV file
			for row in csv_reader:
				temp.append(row)
			temp.pop(0)
			rt.append(temp)
			#print(rt)
	
	
	data = rt
	cycles = []
	for i in data:
		temp = []
		for j in i:
			temp.append(float(j[1]))
		cycles.append(temp)
		
	x_axis = [i for i in range(len(cycles[0]))]
	colors = ["blue","orange","green","red","purple","brown"]
	if var == "HW":
		labels = ["12x12","16x16","32x32","64x64","128x128","256x256"]
	else:
		labels = ["108","500","1000","2000","4000","6000"]
	
	for i in range(len(cycles)):
		
		
		plt.plot(x_axis, cycles[i], color=colors.pop(0), label=dataflow+"_"+var+labels.pop(0))
		
	plt.xlabel('Layers')
	plt.ylabel('area delay product')
	plt.title(nets+"\'s performance on dataflow "+dataflow+" while varing " + var)
	plt.legend()
	plt.show()
	
	util = []
	for i in data:
		temp = []
		for j in i:
			temp.append(float(j[3]))
		util.append(temp)
		
	x_axis = [i for i in range(len(util[0]))]
	colors = ["blue","orange","green","red","purple","brown"]
	if var == "HW":
		labels = ["12x12","16x16","32x32","64x64","128x128","256x256"]
	else:
		labels = ["108","500","1000","2000","4000","6000"]
	for i in util:
		plt.plot(x_axis, i, color=colors.pop(0), label=dataflow+"_"+var+labels.pop(0))
		
	plt.xlabel('Layer')
	plt.ylabel('Utilization')
	plt.title(nets+"\'s Utilization on dataflow "+dataflow+" while varing " + var)
	plt.legend()
	plt.show()
	
	
	
	
	
	

def main():
	print("Hello, this is the main function!")
if __name__ == "__main__":
	main()
	# This code will only be executed if the script is run directly
	#getdata("mobilenet","ws","HW")
	"""
	nets = ["mobilenet"]
	dataflows = ["ws", "is","os"]
	vares = ["HW"]
	for net in nets:
		for dataflow in dataflows:
			for var in vares:
				getdata(net,dataflow,var)
	nets = ["Resnet18"]
	dataflows = ["ws", "is","os"]
	vares = ["HW"]
	for net in nets:
		for dataflow in dataflows:
			for var in vares:
				getdata(net,dataflow,var)
	
	nets = ["myNet"]
	dataflows = ["ws", "is","os"]
	vares = ["HW"]
	for net in nets:
		for dataflow in dataflows:
			for var in vares:
				getdata(net,dataflow,var)
	
	
	plotDiff("mobilenet")
	plotDiff("Resnet18")
	plotDiff("myNet")
	
	nets = ["mobilenet"]
	dataflows = ["ws", "is","os"]
	vares = ["FS","IS","OS"]
	for net in nets:
		for dataflow in dataflows:
			for var in vares:
				getdata0(net,dataflow,var)
	"""
	compare(["mobilenet","myNet"])


