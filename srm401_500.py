import copy

cache = []

def compare_board(a,b):
  return a==b

def in_cache(a):
  global cache
  for x in cache:
    if compare_board(x, a):
      return True
  return False

def is_valid_sol(b, n):
  mallowed = n
  for row in range(len(b)):
    found = False
    for col in range(len(b[row])):
      if found == True and b[row][col] == 1:
        return False
      
  return False

def add_to_cache(b):
  global cache
  cache.append(copy.copy(b))

def generate_candidates(b,n):
def generate_candidate_board(b,candidate):
def revert_candidate_board(b,candidate):

def backtrack(b, n):
  if is_valid_sol(b, n) and not in_cache(b):
    add_to_cache(b)
  cand = generate_candidates(b,n)
  for candidate in cand:
    generate_candidate_board(b, candidate)
    backtrack(b, n)
    revert_candidate_board(b, candidate)



if __name__== "__main__":
  n = int(sys.argv[1])
  if n == 1:
    return 1
  else:
    board = [[0]*n for _ in range(n)]
    board[0][0] = 1
    backtrack(board, n)
    return len(cache)
