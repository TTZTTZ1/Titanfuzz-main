import torch
import torch.nn as nn

# Define a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 6, 5)

model = SimpleModel()

# Prepare valid input data
name = 'conv'
amount = 0.5

# Call the API
torch.nn.utils.prune.random_unstructured(model, name, amount)