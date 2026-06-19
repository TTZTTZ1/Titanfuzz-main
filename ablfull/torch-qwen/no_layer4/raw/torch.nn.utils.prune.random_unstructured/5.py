import torch
import torch.nn as nn

# Define a simple neural network module
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 5)

net = SimpleNet()

# Prepare input data for the API call
module = net.fc
name = 'weight'
amount = 0.5

# Call the API
pruned_module = torch.nn.utils.prune.random_unstructured(module, name, amount)