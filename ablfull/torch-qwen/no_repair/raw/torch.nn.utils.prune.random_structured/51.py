import torch
import torch.nn as nn

# Define a simple convolutional neural network for testing
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv = nn.Conv2d(1, 6, 3)

model = SimpleCNN()

# Prepare input parameters
name = 'conv'
amount = 0.5
dim = 1

# Call the API
torch.nn.utils.prune.random_structured(model, name, amount=amount, dim=dim)