from collections import Counter
from heapq import heappush, heappop


def rearrange(strs):
  s=[]
  s[:0]=strs
  count = Counter(s)

  pq = []
  for k, v in count.items():
    heappush(pq, (-v, k))  
 
  result = [0]*len(s)

  prev = (1, '#')


  ind = 0
  while pq:
    if ind >= len(s):
      break

    k = heappop(pq)
    result[ind] = k[1]

    if prev[0] < 0:
      heappush(pq, prev)

    prev = (k[0]+1, k[1])

    ind += 1

  if ind != len(s):
    return None
  elif isinstance(s, list):
    return result
  else:
    return ''.join(result)
print(rearrange("aaabc"))