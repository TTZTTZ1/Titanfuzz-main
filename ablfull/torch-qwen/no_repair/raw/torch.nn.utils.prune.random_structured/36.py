import torch
import torch.nn as nn
import torch.nn.utils.prune as prune

# Define a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()

# Prepare valid input data
name = 'fc'
amount = 0.3
dim = 0

# Call the API
pruned_model = prune.random_structured(model, name, amount=amount, dim=dim)