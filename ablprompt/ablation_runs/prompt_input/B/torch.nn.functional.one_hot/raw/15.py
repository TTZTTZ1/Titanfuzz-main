import torch
from torch.nn.functional import one_hot

# Example usage of torch.nn.functional.one_hot
input_tensor = torch.tensor([0, 1, 2, 3])
one_hot_encoded = one_hot(input_tensor)
print(one_hot_encoded)