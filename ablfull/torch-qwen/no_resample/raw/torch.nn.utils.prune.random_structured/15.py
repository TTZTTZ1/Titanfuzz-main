import torch
import torch.nn as nn

# Create a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

model = SimpleModel()

# Prepare input parameters
name = 'conv'
amount = 0.5
dim = 0

# Call the API
torch.nn.utils.prune.random_structured(model, name, amount, dim)