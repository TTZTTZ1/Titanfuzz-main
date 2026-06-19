import torch
import torch.nn as nn

# Step 1: Create a sample neural network module
class SampleModel(nn.Module):
    def __init__(self):
        super(SampleModel, self).__init__()
        self.conv = nn.Conv2d(1, 64, kernel_size=3)
        
model = SampleModel()

# Step 2: Prepare valid input data
name = 'conv'
amount = 0.5  # A float between 0.0 and 1.0
dim = 1       # An integer greater than or equal to 0

# Step 3: Call the API
torch.nn.utils.prune.random_structured(model, name, amount, dim=dim)