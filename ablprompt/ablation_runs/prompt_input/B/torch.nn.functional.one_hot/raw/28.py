import torch
from torch.nn.functional import one_hot

# Example tensor of class indices
input_tensor = torch.tensor([0, 2, 3, 1])

# Convert to one-hot encoding with inferred number of classes
one_hot_encoded = one_hot(input_tensor)

print(one_hot_encoded)