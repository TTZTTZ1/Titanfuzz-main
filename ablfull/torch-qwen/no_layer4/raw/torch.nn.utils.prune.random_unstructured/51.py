import torch
import torch.nn as nn

# Create a simple neural network
model = nn.Sequential(nn.Linear(10, 5), nn.ReLU(), nn.Linear(5, 2))

# Define valid input parameters
module = model[0]  # Using the first layer as the example module
name = 'weight'
amount = 0.5  # Example amount within the specified range

# Call the API
torch.nn.utils.prune.random_unstructured(module, name, amount)