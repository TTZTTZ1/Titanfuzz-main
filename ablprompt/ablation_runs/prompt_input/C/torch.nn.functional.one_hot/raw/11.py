import torch
import torch.nn.functional as F

# Example tensor of class indices
indices = torch.tensor([2, 0, 1])

# Convert to one-hot encoding
one_hot_encoded = F.one_hot(indices)

print(one_hot_encoded)