import torch
from torch.nn.functional import one_hot

# Example tensor of class indices
indices = torch.tensor([0, 2, 3, 1])

# Convert to one-hot encoding
one_hot_tensor = one_hot(indices, num_classes=4)

print(one_hot_tensor)