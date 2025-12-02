def is_invalid_id(num):
    """Check if a number is invalid (digits repeated at least twice)."""
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to length//2
    # (pattern must repeat at least twice, so max pattern length is length//2)
    for pattern_len in range(1, length // 2 + 1):
        # Check if the length is divisible by pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            # Check if repeating the pattern gives us the original string
            if pattern * (length // pattern_len) == s:
                return True
    
    return False

def find_invalid_ids(ranges_str):
    """Find all invalid IDs in the given ranges and return their sum."""
    # Parse the ranges
    ranges = []
    for range_str in ranges_str.strip().split(','):
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    
    total = 0
    invalid_ids = []
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                invalid_ids.append(num)
                total += num
    
    return total, invalid_ids



puzzle_input = """4487-9581,755745207-755766099,954895848-955063124,4358832-4497315,15-47,1-12,9198808-9258771,657981-762275,6256098346-6256303872,142-282,13092529-13179528,96201296-96341879,19767340-19916378,2809036-2830862,335850-499986,172437-315144,764434-793133,910543-1082670,2142179-2279203,6649545-6713098,6464587849-6464677024,858399-904491,1328-4021,72798-159206,89777719-90005812,91891792-91938279,314-963,48-130,527903-594370,24240-60212"""

result, ids = find_invalid_ids(puzzle_input)
print(f"Total sum of invalid IDs: {result}")