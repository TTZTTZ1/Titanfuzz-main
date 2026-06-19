import torch
import torch.nn as nn

# Prepare valid input data
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 5)

net = SimpleNet()
name = 'fc.weight'
amount = 0.5
dim = 1

# Call the API
pruned_model = torch.nn.utils.prune.random_structured(net, name, amount=amount, dim=dim)