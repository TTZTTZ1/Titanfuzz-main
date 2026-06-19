import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, -1.0], [2.0, -2.0]], dtype=torch.float32)
scale_tensor = torch.tensor([0.5, 0.5], dtype=torch.float32)

# Task 3: Call the API
result = torch.Tensor.q_per_channel_axis(tensor, scale_tensor)
print(result)