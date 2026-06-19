import torch
import torch.nn as nn

# Step 1: Create a simple neural network module
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

    def forward(self, x):
        return self.conv(x)

model = SimpleModel()

# Step 2: Prepare valid input data
name = "conv"
amount = 0.5

# Step 3: Call the target API
pruned_model = torch.nn.utils.prune.random_unstructured(model, name=name, amount=amount)