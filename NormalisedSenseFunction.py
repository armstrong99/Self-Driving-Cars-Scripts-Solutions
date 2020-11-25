#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
     q = []
     for i in range(len(world)):
         if Z == world[i]:
            p[i] = p[i] * pHit
         else:
              p[i] = p[i] * pMiss
      
     for i in range(len(p)):
         q.append((p[i] / sum(p))) 

     return (q)

print(sense(p,Z))