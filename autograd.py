#gradient for model optimization later
import torch

#x = torch.randn(3,requires_grad=True)
#print(x)

#y=x+2

#print(y)
#z=y*y*2
#z=z.mean() #this is a menian  this will produce a scalar result for backward tensor generation
#print(z)
#v=torch.tensor([0.1,1.0,0.001],dtype=torch.float32) #vector chekovian product
#z.backward(v)# scalar value
#print(x.grad)

#how to prevent tracking the hostory

#x.requires_grad(Flase)
#x.detach()
#with torch.no_grad
#x.requires_grad(False)
#print(x)
#y=x.deatch() #it doesnot require the gradient
#with toch.no_grad():
 #   y=x+2
  #  print(y)


#DUMMY TRAINING EXAMPLE

weights=torch.ones(4,requires_grad=True)

#optimization inside model creation
optimizer=torch.optim.SGD(weights,lr=0.01)
optimizer.zero_grad()


#for epoch in range(2):
 #   model_output =  (weights*3).sum()
  #  model_output.backward()
   # print(weights.grad)
    #print ( weights.grad.zero_())


