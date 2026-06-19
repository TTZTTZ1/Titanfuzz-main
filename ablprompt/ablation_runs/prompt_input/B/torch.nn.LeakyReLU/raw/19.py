import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network using LeakyReLU
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.leaky_relu = nn.LeakyReLU(negative_slope=0.1)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.leaky_relu(x)
        x = self.fc2(x)
        return x

# Initialize the model, loss function, and optimizer
model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy input data
input_data = torch.randn(32, 784)
target_labels = torch.randint(0, 10, (32,))

# Forward pass
output = model(input_data)
loss = criterion(output, target_labels)

# Backward pass and optimization
optimizer.zero_grad()
loss.backward()
optimizer.step()

print(f'Loss: {loss.item()}')