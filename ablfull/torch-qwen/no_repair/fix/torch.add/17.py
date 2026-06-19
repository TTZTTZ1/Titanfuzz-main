
import torch
input_tensor = torch.tensor([1, 2, 3], dtype=torch.float)
other_tensor = torch.tensor([4, 5, 6], dtype=torch.float)
result = torch.add(input_tensor, other_tensor, alpha=2)
print(result)
