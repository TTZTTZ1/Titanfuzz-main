import torch
from torch.nn.utils import prune

# Create a sample neural network module
class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)

net = SimpleNet()

# Prepare input data for the function call
name = 'conv'
amount = 0.3  # Example value within the valid range for float
dim = 1       # Example value greater than or equal to 0

# Call the target API
prune.random_structured(net, name, amount, dim)