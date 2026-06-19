import torch
import torch.nn as nn

# Create a simple neural network module
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 5)

net = SimpleNet()

# Prepare input data
name = 'fc'
amount = 0.5
dim = 0

# Call the API
torch.nn.utils.prune.random_structured(net, name, amount, dim)