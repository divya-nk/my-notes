import os
def rename_files():
	# get file names from a folder
	file_list = os.listdir(r"C:\python_programs\prank") # r stands for raw path
	print(file_list)
	os.chdir(r"C:\python_programs\prank")
	
	# for each file, rename filename
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789")) 	# we're removing all numbers from the file_names
rename_files()
