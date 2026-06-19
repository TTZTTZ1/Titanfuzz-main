import torch
import torch.nn as nn

# Define a simple model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()

# Prepare valid input data
name = 'fc'
amount = 0.5

# Call the API
torch.nn.utils.prune.random_unstructured(model, name, amount)