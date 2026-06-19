import torch
from torch.nn.utils import prune

# Create a simple model to apply pruning
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = torch.nn.Conv2d(1, 6, 5)

model = SimpleModel()

# Prune the model's convolutional layer by randomly unstructuring it
prune.random_unstructured(model.conv, name='weight', amount=0.2)