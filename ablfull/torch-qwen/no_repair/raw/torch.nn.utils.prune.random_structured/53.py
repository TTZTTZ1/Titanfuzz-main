import torch
from torch.nn.utils import prune

# Prepare a simple neural network module as input for pruning
class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 16, kernel_size=5)
        
net = SimpleNet()

# Prepare input parameters
name = 'conv1'
amount = 0.3
dim = 1

# Call the target API
prune.random_structured(net, name, amount, dim=dim)