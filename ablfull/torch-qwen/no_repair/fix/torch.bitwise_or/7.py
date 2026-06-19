
import torch
input_tensor = torch.tensor([1, 0, (- 1)], dtype=torch.int32)
other_tensor = torch.tensor([(- 1), 0, 1], dtype=torch.int32)
result = torch.bitwise_or(input_tensor, other_tensor)
print(result)
