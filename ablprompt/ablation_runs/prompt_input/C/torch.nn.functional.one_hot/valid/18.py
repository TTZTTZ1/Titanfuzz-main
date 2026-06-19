import torch
from torch.nn.functional import one_hot

# Example tensor of class indices
input_tensor = torch.tensor([0, 2, 3, 1])

# Convert to one-hot encoding
one_hot_encoded = one_hot(input_tensor, num_classes=4)

print(one_hot_encoded)