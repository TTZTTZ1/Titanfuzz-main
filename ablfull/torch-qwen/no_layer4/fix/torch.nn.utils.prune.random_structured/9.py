import torch
from torch.nn.utils import prune

class SimpleNet(torch.nn.Module):

    def __init__(self):
        super(SimpleNet, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 6, 5)

    def forward(self, x):
        return x
net = SimpleNet()
module = net.conv1
name = 'weight'
amount = 0.3
dim = 1
prune.random_structured(module, name, amount, dim=dim)