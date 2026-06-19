import torch
import torch.nn as nn

# Define a simple model using Conv2d
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=(3, 3), stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=(2, 2), stride=2)
        self.fc = nn.Linear(in_features=16 * 14 * 14, out_features=10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, 16 * 14 * 14)
        x = self.fc(x)
        return x

# Create an instance of the model and print its architecture
model = SimpleCNN()
print(model)