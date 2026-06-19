import torch
from torch.nn.functional import one_hot

# Example usage of one_hot function
input_tensor = torch.tensor([0, 2, 3, 1])
one_hot_encoded = one_hot(input_tensor, num_classes=4)
print(one_hot_encoded)