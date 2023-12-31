val = [60,100,120]
wt = [1,2,3]
W = 5
n = len(val)

def knapsack(val,wt,W,n):
  k = [[0 for i in range(W+1)] for i in range(n+1) ]
  
  for i in range(n+1):
    for j in range(W+1):
      if i==0 or j==0:
        k[i][j]=0
      elif wt[i-1]<=j:
        k[i][j]= max(k[i-1][j], val[i-1] + k[i-1][j-wt[i-1]]) 
      else:
        k[i][j]=k[i-1][j]
  return k[n][W]

print("Maximum possible profit =", knapsack(val,wt,W,n))