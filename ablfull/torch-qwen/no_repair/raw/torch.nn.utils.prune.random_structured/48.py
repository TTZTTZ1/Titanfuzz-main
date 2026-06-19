import torch
import torch.nn as nn
from torch.nn.utils import prune

# Create a sample neural network module
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 5)

net = SimpleNet()

# Prepare input data
name = 'fc'
amount = 0.2
dim = 0

# Call the API
prune.random_structured(net, name, amount=amount, dim=dim)