import torch
import torch.nn as nn
import torch.optim as optim

class ComplexModel(nn.Module):
    def __init__(self):
        super(ComplexModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=64)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc = nn.Linear(in_features=64 * 16 * 16, out_features=10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, 64 * 16 * 16)
        x = self.fc(x)
        return x

model = ComplexModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Dummy input
input_data = torch.randn(1, 3, 32, 32)
target = torch.randint(0, 10, (1,))

# Forward pass
output = model(input_data)
loss = criterion(output, target)

# Backward and optimize
optimizer.zero_grad()
loss.backward()
optimizer.step()

print(f'Loss: {loss.item()}')