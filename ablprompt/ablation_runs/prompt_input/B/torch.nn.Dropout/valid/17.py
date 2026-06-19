import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.dropout = nn.Dropout(p=0.5)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# Create an instance of the network
net = SimpleNet()

# Define a loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Dummy input data
input_data = torch.randn(32, 784)
target_labels = torch.randint(0, 10, (32,))

# Forward pass
outputs = net(input_data)
loss = criterion(outputs, target_labels)

# Backward pass and optimization
optimizer.zero_grad()
loss.backward()
optimizer.step()