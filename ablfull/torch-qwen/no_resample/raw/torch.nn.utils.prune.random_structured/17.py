import torch
import torch.nn as nn

# Define a simple model for demonstration
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()
name = 'fc'
amount = 0.5
dim = 0

torch.nn.utils.prune.random_structured(model, name, amount, dim)