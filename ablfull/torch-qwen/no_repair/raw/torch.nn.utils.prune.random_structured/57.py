import torch
import torch.nn as nn

# Define a simple model to apply pruning
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()

# Prepare valid input data
name = 'fc.weight'
amount = 0.5
dim = 1

# Call the API
torch.nn.utils.prune.random_structured(model, name, amount=amount, dim=dim)