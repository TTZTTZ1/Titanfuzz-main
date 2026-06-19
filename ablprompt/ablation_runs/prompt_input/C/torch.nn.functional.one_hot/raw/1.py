import torch
from torch.nn.functional import one_hot

# Example tensor
input_tensor = torch.tensor([1, 2, 3, 4])

# Convert to one-hot encoding
one_hot_encoded = one_hot(input_tensor, num_classes=5)

print(one_hot_encoded)