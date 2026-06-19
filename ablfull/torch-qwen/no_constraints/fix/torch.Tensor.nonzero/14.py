import torch
input_tensor = torch.tensor([[0, 1, 2], [3, 0, 5]], dtype=torch.float32)
result = input_tensor.nonzero()
print(result)