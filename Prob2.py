##################################################
# Name: Sonora
# Collaborators:
# Estimate of time spent (hr):
##################################################

def is_magic_square(square:list[list[int]]) -> bool:
    size = len(square)
    if any(len(row) != size for row in square):
        return False
    
    target_sum = sum(square[0])

    for row in square:
        if sum(row) != target_sum:
            return False
        
    for col in range(size):
        if sum(square[row][col] for row in range(size)) != target_sum:
            return False
        if sum(square[i][i] for i in range(size)) != target_sum:
            return False
        if sum(square[i][size - 1 - i] for i in range(size)) != target_sum:
            return False
        return True
    
    pass

magic_sqaure = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(magic_sqaure))

