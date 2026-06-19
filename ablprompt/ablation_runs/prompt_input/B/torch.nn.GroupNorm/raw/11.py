import torch
import torch.nn as nn

# Define a model using GroupNorm
class GroupNormModel(nn.Module):
    def __init__(self):
        super(GroupNormModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1)
        self.norm1 = nn.GroupNorm(num_groups=8, num_channels=128)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(in_features=128 * 7 * 7, out_features=10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.norm1(x)
        x = self.relu(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# Create an instance of the model and print its architecture
model = GroupNormModel()
print(model)