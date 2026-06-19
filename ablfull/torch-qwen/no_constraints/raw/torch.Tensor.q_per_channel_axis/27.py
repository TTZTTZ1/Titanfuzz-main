import torch

# Task 2: Generate input data
tensor = torch.tensor([[[0.5, -0.5], [1.0, -1.0]], [[0.25, -0.25], [0.75, -0.75]]])
q_scale = torch.tensor([0.1, 0.2])
q_zero_point = torch.tensor([0, 0])

# Task 3: Call the API
result = tensor.q_per_channel_axis(q_scale, q_zero_point)
print(result)