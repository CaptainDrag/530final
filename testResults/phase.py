import os


content_path = "/home/ian/Desktop/530final/scale-sim-v2"
folder_path = content_path + "/configs/mobilenet"



# List all files in the folder
files = os.listdir(folder_path)

# Loop through each file and open it
for file_name in files:
	file_path = os.path.join(folder_path, file_name)

	with open(file_path, 'r') as input_file:
		lines = input_file.readlines()

	
	lines[1] = lines[1].replace("ws","is")
	lines[12] = lines[12].replace("ws","is")
		
	
	
	new_folder_path=content_path + "/configs/is"
	output_file_path = os.path.join(new_folder_path, file_name)
	# Write the modified content to the output file
	with open(output_file_path, 'w') as output_file:
		output_file.writelines(lines)
			

