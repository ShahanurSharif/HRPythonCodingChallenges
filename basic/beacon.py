import math

def beacon_signal(x1, y1, x2, y2, xl, yl, R):
    count = 0
    
    # Iterate through each node in the rectangular grid
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            # Calculate the Euclidean distance from the beacon's center
            distance = math.sqrt((x - xl) ** 2 + (y - yl) ** 2)
            
            # Check if the node is completely illuminated
            if distance <= R:
                count += 1
                
    return count

# Test Case
x1, y1, x2, y2, xl, yl, R = -1, 1, 3, 2, 0, 0, 2
expected_output = 4

# Running the function
result = beacon_signal(x1, y1, x2, y2, xl, yl, R)
print(f"Output: {result}, Expected: {expected_output}")