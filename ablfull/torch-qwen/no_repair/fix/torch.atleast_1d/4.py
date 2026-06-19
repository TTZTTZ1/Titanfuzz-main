
import torch
input_data = [torch.tensor([1, 2, 3]), torch.tensor(4)]
result = torch.atleast_1d(*input_data)
print(result)
