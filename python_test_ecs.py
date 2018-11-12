#!/usr/bin/python
import os

def main():
    # Define an array to hold the nation.tbl regionkey values    
    hold_nation = []
    hold_nation_wodup = []

    # Lets read in the variable file so we can get the join files we want to process
    with open('/share_data/dockertest/python_test/script_env.run') as f:
        for line in f:
            if 'export' not in line:
                continue
            if line.startswith('#'):
                continue
            # Remove leading `export `
            # then, split name / value pair
            key, value = line.replace('export ', '', 1).strip().split('=', 1)
            os.environ[key] = value
    
    # Set the variables for usage in the script
    DATA_PATH=(os.environ['DATA_PATH'])
    FILE1=(os.environ['FILE1'])
    FILE2=(os.environ['FILE2'])
    FILE1_FILTER=(os.environ['FILE1_FILTER_NUM'])
    FILE2_FILTER=(os.environ['FILE2_FILTER_NUM'])
    
    # Test if the file exists and if it does.. remove it.
    # This is the file we are writing the data set to after the join
    if os.path.exists(DATA_PATH + "/dockertest/python_test/test_output_from_python_test_code.out"):
       os.remove(DATA_PATH + "/dockertest/python_test/test_output_from_python_test_code.out")

    os.chdir(DATA_PATH)
    fd = os.getcwd()
    #print(fd)

    # List the files in the directory to make sure we are here
    #ld = os.listdir(DATA_PATH)
    #for a in ld:
    #    print(a)

    # open the list to search from
    list_file = open(DATA_PATH + "/" + FILE1,"r")
    
    # loop through the list
    for nation in list_file:
        # Strip the line to remove whitespace.
        line = nation.strip()
        #print(nation)

        # Split the line.
        parts = line.split("|")

        # Display each part of the line to make sure we are splitting right
        # We have to convert the environment variable to an integer (int)
        #for part in parts:
            #print(parts[int(FILE1_FILTER)])

        # Pull the value from the split array 'parts' - 0 based counter - array value 1 = 0 [0,1,2,3,etc]
        # and append it to the array. We have to convert the environment variable to an integer (int)
        hold_nation.append(parts[int(FILE1_FILTER)])

    # Close the nation.tbl file from reading
    list_file.close()

    # This removes the duplicate values from the hold_nation array
    hold_nation_wodup = set(hold_nation)

    # Lets make sure we have the values in the array so we are good
    #for ra in hold_nation_wodup:
    #    print("Region Code from Nation.tbl",ra)

    # open the region file
    region = open(DATA_PATH + "/" + FILE2,"r")
    new_file = open(DATA_PATH + "/dockertest/python_test/test_output_from_python_test_code.out","w")

    # loop through the list
    for region_line in region:
        # Strip the line to remove whitespace.
        line = region_line.strip()
        #print(region_line)

        # Display the line for the sanity.
        #print(line)

        # Split the line.
        parts = line.split("|")

        # Display each part of the line to make sure we are splitting right
        #for part in parts:
        #    print(part)

        for nation in hold_nation_wodup:
            #print("NATION VALUE",nation)
            if parts[0] == nation:
               #print("Region for data is:", parts[1]) 
               new_file.write(parts[1] + "\n")
 
    # Close the region file
    region.close()

    new_file.close()

    # Now lets read out the new_file and see if we have data
    testout = open(DATA_PATH + "/dockertest/python_test/test_output_from_python_test_code.out","r")

    for x in testout:
        line = x.strip()
        print(line)

    testout.close()

if __name__== "__main__":
  main()

