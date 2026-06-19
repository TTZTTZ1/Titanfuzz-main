import torch
from torch.nn.functional import one_hot

# Example tensor of class indices
indices = torch.tensor([0, 2, 1, 3])

# Convert to one-hot encoding
one_hot_encoded = one_hot(indices)

print(one_hot_encoded)