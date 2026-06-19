import torch
import torch.nn as nn

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 6, 5)

model = SimpleModel()

# Prepare input data for pruning
amount = 0.3  # Valid float value between 0.0 and 1.0

# Call the API
torch.nn.utils.prune.random_unstructured(model.conv, name='weight', amount=amount)