import torch
from torch.nn.utils import prune

# Create a sample neural network module
class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 6, 5)
    
    def forward(self, x):
        return self.conv1(x)

model = SimpleNet()

# Prepare valid input data
name = 'conv1.weight'
amount = 0.5
dim = 0

# Call the API
prune.random_structured(model, name, amount=amount, dim=dim)