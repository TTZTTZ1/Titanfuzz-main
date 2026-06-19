import torch
import torch.nn as nn

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

    def forward(self, x):
        return self.conv(x)

# Create a sequential model with multiple layers
model = SimpleModel()
sequential_model = nn.Sequential(model, model)

# Prepare input data
input_data = torch.randn(1, 1, 3, 3)

# Call the checkpoint_sequential function
output = torch.utils.checkpoint.checkpoint_sequential(sequential_model, segments=2, input=input_data, use_reentrant=True)