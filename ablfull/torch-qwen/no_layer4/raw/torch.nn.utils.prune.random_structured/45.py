import torch
from torch.nn.utils import prune

# Define a simple model for demonstration
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 1)

model = SimpleModel()

# Prepare valid input data
name = 'fc.weight'
amount = 0.5
dim = 0

# Call the API
pruned_module = prune.random_structured(model, name, amount, dim)