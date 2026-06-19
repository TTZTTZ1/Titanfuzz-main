import torch
from torch.nn.functional import one_hot

# Example usage of torch.nn.functional.one_hot
input_tensor = torch.tensor([0, 1, 2, 3], dtype=torch.int64)
one_hot_encoded = one_hot(input_tensor, num_classes=4)

print(one_hot_encoded)