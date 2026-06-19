import torch
import torch.nn as nn

# Create a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 5)

net = SimpleNet()

# Define valid parameters
module = net.fc
name = 'weight'
amount = 0.5

# Call the API
torch.nn.utils.prune.random_unstructured(module, name, amount)