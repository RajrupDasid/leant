import torch
#x =  torch.rand(5,3)
#print(x[:,0])
#print(x[1:])
#print(x[1,1].item())


# reshapng a tensor using pytorch

x=torch.rand(4,4)
print(x)
y=x.view(-1,16)
print(y)
print(y.size())
