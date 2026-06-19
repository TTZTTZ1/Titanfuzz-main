import torch

# Task 2: Generate input data
tensor = torch.tensor([[[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]])
q_scale = torch.tensor([[0.1, 0.2]])
q_zero_point = torch.tensor([[0, 0]])

# Task 3: Call the API
result = tensor.q_per_channel_axis(q_scale, q_zero_point)
print(result)