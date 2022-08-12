import torch
#x=torch.empty(2,3,3,8)
#x=torch.rand(3,3,dtype=torch.float16)
#x=torch.tensor([2.5,0.1])
x = torch.rand(3,3)
y = torch.rand(3,3)
y.add_(x) # add_ do a inplace operation in only pytorch
print(x)
print(y)
z = x-y
z=z.sub(y)
print(z)
print(z.size())
print(z.dtype)

