import torch
import torch.nn.functional as F

# Example usage of torch.nn.functional.one_hot
input_tensor = torch.tensor([1, 2, 3])
one_hot_output = F.one_hot(input_tensor)
print(one_hot_output)