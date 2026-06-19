import torch
import torch.nn as nn

# Define a simple model
model = nn.Linear(4, 2)

# Generate random weights for the model
torch.manual_seed(0)
model.weight.data = torch.randn(model.weight.shape)
model.bias.data = torch.randn(model.bias.shape)

# Apply random unstructured pruning to the weight of the first layer
torch.nn.utils.prune.random_unstructured(model[0], name='weight', amount=0.5)