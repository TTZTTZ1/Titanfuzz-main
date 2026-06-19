import torch
from torch.nn.utils import prune

# Create a simple model for demonstration
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(4, 5)

model = SimpleModel()

# Prepare input data
name = "linear.weight"
amount = 0.5
dim = 1

# Call the API
prune.random_structured(model, name, amount=amount, dim=dim)