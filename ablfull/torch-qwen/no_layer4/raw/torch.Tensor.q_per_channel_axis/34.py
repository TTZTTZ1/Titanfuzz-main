import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
scale_tensor = torch.tensor([1.0, 1.0])
zero_point_tensor = torch.tensor([0, 0])

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale=scale_tensor, zero_point=zero_point_tensor, axis=0)

print(result)