import torch
from torch import nn, optim

# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))

# Initialize the model, loss function, and optimizer
model = SimpleNet()
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Generate random input and target data
input_data = torch.randn(5, 10)
target_data = torch.randint(0, 2, (5, 1)).float()

# Forward pass
output = model(input_data)
loss = criterion(output, target_data)

# Backward pass and optimization
optimizer.zero_grad()
loss.backward()
optimizer.step()

print(f"Loss: {loss.item()}")