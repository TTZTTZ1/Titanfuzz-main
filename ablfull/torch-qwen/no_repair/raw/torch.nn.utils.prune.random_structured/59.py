import torch
import torch.nn as nn
from torch.nn.utils import prune

# Step 2: Generate input data
class SimpleModule(nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.linear = nn.Linear(10, 5)

model = SimpleModule()
name = 'linear.weight'
amount = 0.3
dim = 0

# Step 3: Call the API
prune.random_structured(model, name, amount=amount, dim=dim)