import torch
from torch.nn.functional import one_hot

# Example tensor of class indices
class_indices = torch.tensor([0, 1, 3, 4])

# Convert to one-hot encoding
one_hot_encoded = one_hot(class_indices, num_classes=5)

print(one_hot_encoded)