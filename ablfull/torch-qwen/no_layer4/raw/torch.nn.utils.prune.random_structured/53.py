import torch
from torch.nn.utils import prune

# Define a simple model for demonstration purposes
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

model = SimpleModel()

# Generate input data
name = 'linear.weight'
amount = 0.5
dim = 0

# Call the target API
prune.random_structured(model, name, amount, dim=dim)