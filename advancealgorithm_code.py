# This program will allow the user to pair up socks such that she/he keeps the 
# as organized pairs of similar socks. Pairing up the socks will be based on the 
# color (two socks of the same color will be paired up).

def matchingSocks(pairs):
    # To store the frequency of every unique sock initializing a dictionary 
    dictionary = {}
    
    # Use a for loop to find the occurance of the sock 
    for pair in range(len(pairs)):
        # Use an if statement to check that the pair is not in the array 
        if pairs[pair] not in dictionary:
            dictionary[pairs[pair]] = 1
        # Us an else statement to check that the pair is in the array 
        else:
            dictionary[pairs[pair]] += 1
            
    # Create a variable to be incremented each time the occurance of the unique pairs is divided by 2 
    pairsSum = 0
    # Use a for loop to check through the dictionary
    for x in dictionary:
        # This is where the increment is taking place 
        pairsSum += dictionary[x] // 2
    
    # the function returns the result 
    return pairsSum

# Testing on the 2 arrays as instructed in the rubric 
pairsSum_test1 = [100,1,20,20,2,3,4,5,6,1,2,4,5,6,7,1,3,4,5,6,7,1,2,2,2,500,67,87,27,88]
pairsSum_test2 = [100,1,20,20,2,3,4,5,6,1,2,4,5,6,7,1,3,4,5,6,7,1,2,2,2,500,67,87,27,88,100,1,20,20,2,3,4,5,6,1,2,4,5,6,7,1,3,4,5,6,7,1,2,2,2,500,67,87,27,88,100,1,20,94,2,3,4,5,6,1,2,4,5,6,7,1,3,4,5,6]

# Print the result of the tests done 
print("The total elements in the array 1 are " + str(len(pairsSum_test1)), "and it returns " + str(matchingSocks(pairsSum_test1)) + " pairs")
print("The total elements in the array 2 are " + str(len(pairsSum_test2)), "and it returns " + str(matchingSocks(pairsSum_test2)) + " pairs")


