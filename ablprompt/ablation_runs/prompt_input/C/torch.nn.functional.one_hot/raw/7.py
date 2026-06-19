import torch
from torch.nn.functional import one_hot

# Example tensor of class indices
class_indices = torch.tensor([2, 0, 3, 1])

# Convert to one-hot encoding with inferred number of classes
one_hot_encoded = one_hot(class_indices)

print(one_hot_encoded)