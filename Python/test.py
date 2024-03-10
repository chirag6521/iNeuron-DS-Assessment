# Answer 1 -

def construct_output(input_dict, prefix=[]):
    output = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            sub_output = construct_output(value, prefix + [key])
            for k, v in sub_output.items():
                output[k] = prefix + [key] + v
        else:
            output[key] = prefix + [key]
    return output

input_dict = {
    "hey": {
        "this": {
            "is": {
                "ass": {
                    "ess": {
                        "ment": {
                            "of": {
                                "ine": {
                                    "uron": "you are finally here !!!"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

output = construct_output(input_dict)
print(output)





print('************************************************************************************************************')





# Answer 2 

def min_distance_between_horses(stalls, k):
    stalls.sort() 
    low = 1  
    high = stalls[-1] - stalls[0]  

    while low <= high:
        mid = (low + high) // 2 
        if is_valid_configuration(stalls, k, mid):
            low = mid + 1
        else:
            high = mid - 1

    return high  

def is_valid_configuration(stalls, k, min_distance):
    count = 1
    last_position = stalls[0]  
    
    for stall in stalls[1:]:
        if stall - last_position >= min_distance:
            count += 1
            last_position = stall
        if count == k:
            return True
    return False  

stalls = [1, 2, 4, 8, 9]
k = 3
result = min_distance_between_horses(stalls, k)
print("Largest minimum distance is :", result)



print('************************************************************************************************************')



# Answer 3


def create_door_mat(n, m):
    if n % 2 == 0 or m != 3 * n:
        print("Invalid input! N must be an odd number and M must be 3 times N.")
        return

    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    welcome = 'WELCOME'.center(m, '-')
    door_mat = '\n'.join(pattern + [welcome] + pattern[::-1])
    
    print(door_mat)

n = 7  # Height 
m = 21  # Width 

print('Size in 7x21')
create_door_mat(7, 21) 
print('Size in 11x33')
create_door_mat(11, 33) 



print('************************************************************************************************************')



# Answer 4

def fourSum(nums, target):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            left = j + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    
    return result

nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)  



print('************************************************************************************************************')


