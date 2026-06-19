import torch
from torch import nn

# Example tensor of class indices
class_indices = torch.tensor([0, 2, 1])

# Convert to one-hot encoding
one_hot_encoded = nn.functional.one_hot(class_indices, num_classes=3)

print(one_hot_encoded)