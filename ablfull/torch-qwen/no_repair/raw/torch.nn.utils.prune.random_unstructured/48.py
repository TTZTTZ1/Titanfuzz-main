import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(10, 5)

net = SimpleNet()
torch.nn.utils.prune.random_unstructured(net.fc, name='weight', amount=0.5)