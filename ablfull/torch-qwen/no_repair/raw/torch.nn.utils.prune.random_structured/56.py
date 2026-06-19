import torch
import torch.nn as nn
from torch.nn.utils import prune

# Step 2: Generate input data
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 5)

net = SimpleNet()
name = 'fc'
amount = 0.5
dim = 1

# Step 3: Call the API
prune.random_structured(net, name, amount, dim=dim)