import numpy as np

#f=2*x
X=np.array([1,2,3,4],dtype=np.float32)
Y=np.array([2,4,6,8],dtype=np.float32)

w = 0.0

#model prediction
def forward(x):
    return w * x
#loss
def loss(y,y_predicted):
    return ((y_predicted-y)**2).mean()

#gradinet
#MSE = 1/N * (w*x -y)**2
#dj/dw=1/N 2x (w*x -y)
def gradinet(x,y,y_predicted):
    return np.dot(2*x,y_predicted-y).mean()
print(f"predtion before training: f(5) = {forward(5):3f}")

#training
learning_rate=0.01
n_iters=1000
for epoch in range(n_iters):
    #prediction = forward pass
    y_pred = forward(X)

    #loss
    l = loss(Y,y_pred)

    #gradinet
    dw = gradinet(X,Y,y_pred)

    #update weights
    w -= learning_rate * dw

    if epoch % 1 == 0:
        print(f"epoch {epoch+1}: w = {w:.3f}, loss= {l:.8f} ")

print (f"predtion after training : f(5) = {forward(5):.3f}")
