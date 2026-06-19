import torch
import torch.nn as nn

# Define a simple neural network module
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 1)

net = SimpleNet()

# Prepare input data
name = 'fc'
amount = 0.5

# Call the API
torch.nn.utils.prune.random_unstructured(net, name=name, amount=amount)