import torch
import numpy as np
#torch tensors
#a = torch.rand(5,5) #creating tensors
#print(a)
#converted to numpy array
#b = a.numpy()
#print(b)

#print (a.add_(1))
#print

#a= np.ones(7)
#print(a)
#b= torch.from_numpy(a)
#print(b)
#a+=1
#print(a)
#print(b)

# how to replicate on gpu

#if torch.cuda.is_available():
 #   device=torch.device("cuda")
  #  x=torch.ones(5,device=device)
   # y=torch.ones(5)
   # y=y.to(device)
    #z=x+y
    #z=z.to("cpu")
    #print(z)


# gradiant calculations for later optimization
x=torch.ones(5,requires_grad=True)
print(x)
