import torch
import torch.nn.functional as F

# Example usage of torch.nn.functional.one_hot
tensor = torch.tensor([0, 1, 2])
one_hot_tensor = F.one_hot(tensor)
print(one_hot_tensor)