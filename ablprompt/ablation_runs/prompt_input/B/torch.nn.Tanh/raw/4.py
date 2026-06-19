import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network with Tanh activation
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.tanh = nn.Tanh()
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.tanh(x)
        x = self.fc2(x)
        return x

# Create an instance of the network and move it to GPU if available
net = SimpleNet().cuda() if torch.cuda.is_available() else SimpleNet()

# Define a loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Dummy input data
input_data = torch.randn(32, 784).cuda() if torch.cuda.is_available() else torch.randn(32, 784)

# Forward pass
output = net(input_data)

# Compute the loss
target = torch.randint(0, 10, (32,)).cuda() if torch.cuda.is_available() else torch.randint(0, 10, (32,))
loss = criterion(output, target)

# Backward pass and optimization
optimizer.zero_grad()
loss.backward()
optimizer.step()

print(f"Loss: {loss.item()}")