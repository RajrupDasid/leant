#back propagation and how to clculate stuffs
import torch


# the gradient calculation
x =  torch.tensor(1.0)
y = torch.tensor(2.0)
w=torch.tensor(1.0,requires_grad=True)

#forward pass and compute the loss
y_hat =  w * x
loss = (y_hat - y)**2

print(2)

#backward pass
loss.backward()
print(w.grad)

##update weight
