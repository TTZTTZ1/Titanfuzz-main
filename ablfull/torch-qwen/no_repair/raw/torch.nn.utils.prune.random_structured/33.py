import torch
from torch.nn import Module

# Create a simple model
class SimpleModel(Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

model = SimpleModel()

# Prepare valid input data
name = 'fc'
amount = 0.3
dim = 1

# Call the API
torch.nn.utils.prune.random_structured(model, name, amount=amount, dim=dim)