import torch
import torch.nn as nn

# Define a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 1, kernel_size=3)

model = SimpleModel()

# Prepare input parameters
name = 'conv'
amount = 0.5

# Call the API
pruned_model = nn.utils.prune.random_unstructured(model, name=name, amount=amount)