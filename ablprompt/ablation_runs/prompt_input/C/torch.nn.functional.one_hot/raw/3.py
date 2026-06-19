import torch
from torch.nn import functional as F

# Example tensor of class indices
indices = torch.tensor([0, 2, 3, 1])

# Convert to one-hot encoding
one_hot_encoded = F.one_hot(indices)

print(one_hot_encoded)