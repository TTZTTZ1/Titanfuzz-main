import torch

# Task 2: Generate input data - creating a tensor of shape (3,) with values [1.0, 2.0, 3.0]
input_tensor = torch.tensor([1.0, 2.0, 3.0])

# Task 3: Call the API torch.Tensor.negative
result_tensor = input_tensor.negative()

print(result_tensor)