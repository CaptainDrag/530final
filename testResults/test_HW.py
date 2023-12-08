from scalesim.scale_sim import scalesim


def runSim(net, dataflow):
	content_path = "/home/ian/Desktop/530final/scale-sim-v2"

	topo = content_path + "/topologies/conv_nets/"+net+".csv"

	top = "/home/ian/Desktop/530final/testResults/"+net
	#vares = ["L","FS","IS","OS"]
	vares = ["L"]
	#vares = ["IS","OS"]
	for var in vares:
		for i in range(6):
			config = content_path + "/configs/"+dataflow+"/"+var+str(i)+".cfg"
			s = scalesim(save_disk_space=True, verbose=True,
						  config=config,
						  topology=topo
						  )
						  
			s.run_scale(top_path=top)

		
def runSim0(net, dataflow):
	content_path = "/home/ian/Desktop/530final/scale-sim-v2"

	topo = content_path + "/topologies/conv_nets/"+net+".csv"

	top = "/home/ian/Desktop/530final/testResults/"+net
	vares = ["L"]
	#vares = ["IS","OS"]
	config = content_path + "/configs/"+dataflow+"/"+"IS"+"4"+".cfg"
	s = scalesim(save_disk_space=False, verbose=True,
				  config=config,
				  topology=topo
				  )
				  
	s.run_scale(top_path=top)
	config = content_path + "/configs/"+dataflow+"/"+"IS"+"5"+".cfg"
	s = scalesim(save_disk_space=False, verbose=True,
				  config=config,
				  topology=topo
				  )
				  
	s.run_scale(top_path=top)
	for var in vares:
		for i in range(6):
			config = content_path + "/configs/"+dataflow+"/"+var+str(i)+".cfg"
			s = scalesim(save_disk_space=False, verbose=True,
						  config=config,
						  topology=topo
						  )
						  
			s.run_scale(top_path=top)
			
			
def main():
	print("Hello, this is the main function!")
if __name__ == "__main__":
	main()
	#runSim("mobilenet", "ws")
	#runSim("mobilenet", "os")
	#runSim("mobilenet", "is")
	#runSim("Resnet18", "ws")
	#runSim("Resnet18", "os")
	#runSim("Resnet18", "is")
	runSim("myNet", "ws")
	runSim("myNet", "os")
	runSim("myNet", "is")



