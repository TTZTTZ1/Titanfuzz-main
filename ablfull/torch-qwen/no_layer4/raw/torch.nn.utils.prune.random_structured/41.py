import torch
from torch.nn.utils import prune

# Define a simple neural network module
class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 6, 5)
    
    def forward(self, x):
        return x

# Create an instance of the network
net = SimpleNet()

# Prepare valid input data
module = net.conv1
name = 'weight'
amount = 0.3
dim = 1

# Call the API
prune.random_structured(module, name, amount, dim=dim)