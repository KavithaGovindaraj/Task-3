
#1)

#given List
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List to store even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# List to store all numbers
all_numbers = numbers.copy()

# Print the results
print("Even numbers:", even_numbers)
print("All numbers:", all_numbers)


#Output:
#Even numbers: [10, 22, 100]
#All numbers: [10, 501, 22, 37, 100, 999, 87, 351]



#2)


def is_prime(n):
    #Check if a number is a prime number.
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List to store prime numbers
prime_numbers = []

# Iterate through the given list and find prime numbers
for number in numbers:
    if is_prime(number):
        prime_numbers.append(number)

# Count of prime numbers
prime_count = len(prime_numbers)

# Print the results
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", prime_count)

#Output:
#Prime numbers: [37]
#Count of prime numbers: 1


#3)
def is_happy_number(n):
    #Determine if a number is a happy number.
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(char) ** 2 for char in str(n))
    return n == 1

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Count happy numbers
happy_count = sum(1 for number in numbers if is_happy_number(number))

# Print the count of happy numbers
print("Count of happy numbers:", happy_count)

#Output:
#Count of happy numbers: 2


#4)
def sum_first_and_last_digit(n):
   #Returns the sum of the first and last digit of an integer.
    # Convert the integer to a string to easily access the digits
    n_str = str(n)
    
    # Get the first and last digit
    first_digit = int(n_str[0])
    last_digit = int(n_str[-1])
    
    # Return the sum of the first and last digit
    return first_digit + last_digit

# Example usage
number = 12345
result = sum_first_and_last_digit(number)
print(f"The sum of the first and last digit of {number} is {result}")

#Output:
# The sum of the first and last digit of 12345 is 6   


#5)
def min_diff_mangoes(bags, students):
    #Find the minimum difference between the maximum and minimum number of mangoes in distributed bags.
    # Sort the list of bags
    bags.sort()
    
    # Initialize the minimum difference to a large number
    min_diff = float('inf')
    
    # Iterate over the list to find the minimum difference in any subarray of size 'students'
    for i in range(len(bags) - students + 1):
        current_diff = bags[i + students - 1] - bags[i]
        if current_diff < min_diff:
            min_diff = current_diff
    
    return min_diff

# Example usage
bags = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 33, 26, 1, 50, 29]
students = 7

result = min_diff_mangoes(bags, students)
print(f"The minimum difference between the maximum and minimum mangoes in distributed bags is: {result}")


#Output:
#The minimum difference between the maximum and minimum mangoes in distributed bags is: 7

#6)
def find_duplicates(list1, list2, list3):
    #Find duplicates across three lists.
    # Convert lists to sets
    set1, set2, set3 = set(list1), set(list2), set(list3)
    
    # Find common elements in all three sets
    common_elements = set1 & set2 & set3
    
    # Convert the result back to a list
    return list(common_elements)

# Example usage
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 7, 8, 9, 10]

duplicates = find_duplicates(list1, list2, list3)
print("Duplicates in the three lists are:", duplicates)

#Output:
#Duplicates in the three lists are: [5, 6]


#7)
def first_non_repeating_element(lst):
    #Find the first non-repeating element in a given list of integers.
    # Create a dictionary to store the count of each element
    count_dict = {}
    
    # Count the occurrences of each element in the list
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the first element with a count of 1
    for num in lst:
        if count_dict[num] == 1:
            return num
    
    return None  # Return None if there is no non-repeating element

# Example usage
lst = [4, 5, 1, 2, 1, 2, 4, 3]
result = first_non_repeating_element(lst)
print(f"The first non-repeating element is: {result}")

#Output:
#The first non-repeating element is: 5


#8)
def find_min_in_rotated_sorted_list(nums):
    #Find the minimum element in a rotated and sorted list.
    if not nums:
        return None  # Return None if the list is empty
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if the middle element is greater than the rightmost element
        if nums[mid] > nums[right]:
            # The minimum is in the right half
            left = mid + 1
        else:
            # The minimum is in the left half including mid
            right = mid
    
    # The left index will point to the minimum element
    return nums[left]

# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
result = find_min_in_rotated_sorted_list(nums)
print(f"The minimum element in the rotated and sorted list is: {result}")

#Output:
#The minimum element in the rotated and sorted list is: 0



#9)
def find_triplet(lst, target):
    #Find a triplet in the list whose sum is equal to the target value.
    lst.sort()
    n = len(lst)
    
    for i in range(n - 2):
        # Use two pointers to find the other two elements
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            if current_sum == target:
                return lst[i], lst[left], lst[right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return None  # Return None if no triplet is found

# Example usage
lst = [10, 20, 30, 9]
target = 59

result = find_triplet(lst, target)
if result:
    print(f"The triplet whose sum is equal to {target} is: {result}")
else:
    print(f"No triplet found with sum equal to {target}")


#Output:
#The triplet whose sum is equal to 59 is: (9, 20, 30)

#10)

def has_zero_sum_sublist(lst):
    #Check if there is a sublist with sum equal to zero.
    # Create a set to store the cumulative sums
    cum_sum_set = set()
    
    # Initialize the cumulative sum
    cum_sum = 0
    
    for num in lst:
        cum_sum += num
        
        # Check if cumulative sum is zero or already exists in the set
        if cum_sum == 0 or cum_sum in cum_sum_set:
            return True
        
        # Add the cumulative sum to the set
        cum_sum_set.add(cum_sum)
    
    return False

# Example usage
lst = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(lst)
if result:
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")

#Output:

#There is a sub-list with sum equal to zero.
