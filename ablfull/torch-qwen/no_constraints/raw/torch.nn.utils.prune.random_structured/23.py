import torch
from torch.nn.utils import prune

# Define a simple model for pruning
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 6, 5)
        self.pool = torch.nn.MaxPool2d(2, 2)
        self.conv2 = torch.nn.Conv2d(6, 16, 5)

model = SimpleModel()

# Prepare input data
input_data = torch.randn(1, 1, 32, 32)

# Apply random structured pruning to conv1
prune.random_structured(model.conv1, name='weight', amount=0.3)

# Call the API
pruned_model = prune.remove_pruning(model)