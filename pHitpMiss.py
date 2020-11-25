#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
firstRedCell = p[0] * pMiss
secondRedCell = p[1] * pHit
thirdRedCell = p[2] * pHit
fourthRedCell = p[3] * pMiss
fifthRedCell = p[4] * pMiss
p[0] = (firstRedCell)
p[1] = (secondRedCell)
p[2] = (thirdRedCell)
p[3] = (fourthRedCell)
p[4] = (fifthRedCell)

start = sum(p)

# for i in range((len(p))):
#     start = start + p[i]

for i in range((len(p))):
    p.append( ( p[i] / start) )

print(p)