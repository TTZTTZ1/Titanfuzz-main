import torch
from torch.nn import Conv2d

# Create a random convolutional layer as the module
module = Conv2d(in_channels=3, out_channels=64, kernel_size=3)

# Prepare valid input data satisfying every constraint
name = 'weight'
amount = 0.3
dim = 1

# Call the API
pruned_module = torch.nn.utils.prune.random_structured(module, name, amount, dim)