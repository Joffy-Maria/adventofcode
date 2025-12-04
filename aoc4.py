def count_accessible_rolls(grid):
 
    rows = len(grid)
    cols = len(grid[0])
    accessible = []
    
    # All 8 directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent_rolls = 0
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    accessible.append((r, c))
    
    return accessible


def part1(grid_input):
   
    grid = [list(line) for line in grid_input.strip().split('\n')]
    accessible = count_accessible_rolls(grid)
    return len(accessible)


def part2(grid_input):
    
    grid = [list(line) for line in grid_input.strip().split('\n')]
    total_removed = 0
    
    while True:
        accessible = count_accessible_rolls(grid)
        
        if not accessible:
            break
        
        # Remove accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'
        
        total_removed += len(accessible)
    
    return total_removed



with open('input.txt', 'r') as f:
    puzzle_input = f.read()


print(f"Part 1: {part1(puzzle_input)}")
print(f"Part 2: {part2(puzzle_input)}")