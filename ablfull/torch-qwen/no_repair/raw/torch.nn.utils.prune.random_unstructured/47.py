import torch
from torch.nn.utils import prune

# Create a simple model for demonstration
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(5, 2)

model = SimpleModel()

# Prepare valid input data
name = 'linear'
amount = 0.5

# Call the target API
pruned_model = prune.random_unstructured(model, name=name, amount=amount)