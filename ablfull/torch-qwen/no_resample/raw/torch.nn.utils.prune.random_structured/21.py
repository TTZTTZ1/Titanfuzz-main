import torch
import torch.nn as nn

# Create a sample neural network module
class SampleNet(nn.Module):
    def __init__(self):
        super(SampleNet, self).__init__()
        self.conv = nn.Conv2d(1, 6, 5)

model = SampleNet()

# Prepare valid input data
name = 'conv'
amount = 0.5
dim = 1

# Call the API
torch.nn.utils.prune.random_structured(model, name, amount, dim)