import torch
from torch.nn.utils import prune

# Create a simple neural network module
class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 16, kernel_size=3)

net = SimpleNet()

# Prune 50% of the weights in the first convolutional layer randomly
prune.random_unstructured(net.conv1.weight, name='weight', amount=0.5)