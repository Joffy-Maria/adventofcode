def solve_part1(rotations):
    """Count how many times dial ends on 0 after a rotation"""
    position = 50
    count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:  # R
            position = (position + distance) % 100
        
        if position == 0:
            count += 1
    
    return count


def solve_part2(rotations):
    """Count how many times dial passes through 0 during rotations"""
    position = 50
    count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            # Count times we land on 0 going left
            for i in range(1, distance + 1):
                if (position - i) % 100 == 0:
                    count += 1
            position = (position - distance) % 100
        else:  # R
            # Count times we land on 0 going right
            for i in range(1, distance + 1):
                if (position + i) % 100 == 0:
                    count += 1
            position = (position + distance) % 100
    
    return count


# Read input
with open('input.txt', 'r') as f:
    rotations = [line.strip() for line in f if line.strip()]

# Solve both parts
part1_answer = solve_part1(rotations)
part2_answer = solve_part2(rotations)

print(f"Part 1 (ends on 0): {part1_answer}")
print(f"Part 2 (clicks through 0): {part2_answer}")