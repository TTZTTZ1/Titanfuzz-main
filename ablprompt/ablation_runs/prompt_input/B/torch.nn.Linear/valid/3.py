import torch
import torch.nn as nn

class ComplexModel(nn.Module):
    def __init__(self):
        super(ComplexModel, self).__init__()
        self.fc1 = nn.Linear(784, 512)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(512, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = ComplexModel()
input_data = torch.randn(64, 784)
output = model(input_data)
print(output.shape)  # Should be (64, 10)