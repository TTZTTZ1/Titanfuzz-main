import torch
from torch.nn.functional import one_hot

# Example tensor with class indices
input_tensor = torch.tensor([1, 2, 3, 4])

# Convert to one-hot encoding with inferred number of classes
one_hot_encoded = one_hot(input_tensor)

print(one_hot_encoded)