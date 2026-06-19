import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1, 2], [0, 4]], dtype=torch.float32)

# Task 3: Call the API torch.Tensor.cummin
result = input_tensor.cummin(dim=1)
print(result)