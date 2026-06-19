import torch
import torch.nn as nn

# Define a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 6, 5)

model = SimpleModel()

# Prepare input data satisfying the constraints
amount = 0.5  # Example value within the allowed range

# Call the API
pruned_model = torch.nn.utils.prune.random_unstructured(model, name='conv.weight', amount=amount)