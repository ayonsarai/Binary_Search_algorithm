def binary_search(arr, target):
    # Set the initial low and high values to the first and last index of the array
    low = 0
    high = len(arr) - 1
    operations = 0

    # Keep searching until the low index is less than or equal to the high index
    while low <= high:
        # Find the middle index of the current range
        mid = (low + high) // 2
        # Get the value at the middle index
        guess = arr[mid]
        operations += 1

        # If the value at the middle index is equal to the target, we found it!
        if guess == target:
            return mid, operations
        # If the value at the middle index is less than the target, update the low index to search the right half
        elif guess < target:
            low = mid + 1
        # If the value at the middle index is greater than the target, update the high index to search the left half
        else:
            high = mid - 1

    # If we reach here, it means the target is not in the array
    return -1, operations


# The file path where the numbers are stored
numbers_file = "C:\\\\Users\\\\Sarai Ayon\\\\OneDrive - Whatcom Community College\\\\Spring 2024\\\\CS240 Database Structure & Algorithms\\\\numbers.txt"

# Open the file and read the numbers into a list
with open(numbers_file, 'r') as file:
    numbers = [int(line.strip()) for line in file]

# The number we want to search for
target = 196614208
# Call the binary_search function to find the position of the target in the array
position, num_operations = binary_search(numbers, target)
# Print the result
print(f"Position of {target} in the file: {position}")
print(f"Number of operations: {num_operations}")


# a. What is the position of 51216352 in the array? How many operations did it take to find?
# Position of 51216352 in the file: 499 
# Number of operations: 2 

# b. What is the position of 198313119 in the array? How many operations did it take to find?
#   Position of 198313119 in the file: 1980 
#   Number of operations: 11

# c. What is the position of 196614208 in the array? How many operations did it take to find?
#   Position of 196614208 in the file: -1
#   Number of operations: 11

# d. What is the worst case time complexity? Evaluate line by line, create a time complexity function and then define its Big O value.
#   The worst case time complexity is O(log n) because the algorithm divides the array in half with each iteration.
#   The time complexity function is f(n) = log n
#   The Big O value is O(log n)
#   The algorithm is efficient because it reduces the number of elements to search by half with each iteration.

# e. What would the worst case time complexity be if we have 4000 entries instead of 2000?
#   The worst case time complexity would still be O(log n) because the algorithm divides the array in half with each iteration.

#  f. What do you think the average case time complexity is for binary search? Explain your reasoning.
#   The average case time complexity for binary search is O(log n) because the algorithm divides the array in half with each iteration.

___________________________________________________________________________________________________________________________________________________

# Evaluate the time complexity of the following code snippets. Evaluate line by line, create a time complexity function and then define its Big O value.

#a.The time complexity of the first code snippet is O(n), where n is the length of the input array. 
# This is because the code iterates through each element of the array once.

function sum(arr){
  counter = 0

  for (i = 0; i < arr.length; i++) {
       counter += arr[i]
  }

     return counter
}
# The function is defined using the keyword "def" followed by the function name "sum" and parentheses "()". 
# This tells the computer that we are creating a new function called "sum".
# Inside the function, there is a variable called "counter" that is set to 0. This variable will keep track of the sum of the numbers.

# The code then enters a "for" loop. This loop will go through each number in the input array one by one.
# Inside the loop, the current number is added to the "counter" variable using the "+=" operator.
# This means that the current number is added to the existing value of "counter".

#After the loop finishes going through all the numbers in the array, the final value of "counter" is returned as the result of the function.



#b.The time complexity of the second code snippet is O(n^2), where n is the length of the longer input array. 
# This is because the code has nested loops, and for each element in the first array, it checks if it exists in the second array. 
# Therefore, the code has to iterate through each element of both arrays, resulting in a quadratic time complexity.

function getXOR(arr1, arr2){

  arr3 = []

  for (i = 0; i < arr1.length; i++){
      let unique = True
      for (j = 0; j < arr2.length; j++ }{
        if(arr1[i] == arr2[j]) {unique = False;}
      }
      if (unique) {arr3.append(arr1[i]);}
    }
  }  
  for (i = 0; i < arr2.length; i++){
    let unique = True
    for (j = 0; j < arr1.length; j++ }{
      if(arr2[i] == arr1[j]) {unique = False;}
    }
    if (unique) {arr3.append(arr2[i]);}
  }
  return arr[3]
}






