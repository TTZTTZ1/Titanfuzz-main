import torch
import torch.nn as nn
import torch.nn.functional as F

class ComplexModel(nn.Module):
    def __init__(self):
        super(ComplexModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=64)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(num_features=128)
        self.fc = nn.Linear(in_features=128 * 7 * 7, out_features=10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = F.relu(x)
        x = F.avg_pool2d(x, 2)
        x = x.view(-1, 128 * 7 * 7)
        x = self.fc(x)
        return x

model = ComplexModel()
input_tensor = torch.randn(1, 3, 32, 32)
output = model(input_tensor)
print(output.shape)