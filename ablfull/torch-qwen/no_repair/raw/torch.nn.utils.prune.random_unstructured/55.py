import torch
import torch.nn as nn

# Create a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()

# Prepare input data
amount = 0.5

# Call the API
pruned_model = torch.nn.utils.prune.random_unstructured(model, name='fc', amount=amount)