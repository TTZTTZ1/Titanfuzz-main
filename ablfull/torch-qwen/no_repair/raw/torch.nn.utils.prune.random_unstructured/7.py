import torch
from torch.nn.utils import prune

# Create a simple model for demonstration
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

model = SimpleModel()

# Prepare valid input data
name = 'fc'
amount = 0.5

# Call the API
prune.random_unstructured(model, name=name, amount=amount)