import torch
import torch.nn as nn

# Create a simple neural network module
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

    def forward(self, x):
        return self.conv(x)

# Initialize the model
model = SimpleNet()

# Prepare input data
input_data = torch.randn(1, 1, 4, 4)

# Call the API with valid parameters
torch.nn.utils.prune.random_unstructured(model, name='conv.weight', amount=0.5)