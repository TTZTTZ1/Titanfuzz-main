import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple CNN model with BatchNorm2d layers
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(128)
        self.fc = nn.Linear(128 * 7 * 7, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = torch.relu(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = torch.relu(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# Create an instance of the model
model = SimpleCNN()

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Dummy input data
input_data = torch.randn(32, 3, 32, 32)
target_labels = torch.randint(0, 10, (32,))

# Forward pass
outputs = model(input_data)
loss = criterion(outputs, target_labels)

# Backward and optimize
optimizer.zero_grad()
loss.backward()
optimizer.step()

print(f'Loss: {loss.item()}')