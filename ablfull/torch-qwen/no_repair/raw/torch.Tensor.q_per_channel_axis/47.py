import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[[0.5, 1.5], [2.5, 3.5]], [[4.5, 5.5], [6.5, 7.5]]])
q_per_channel_axis = torch.quantize_per_channel(input_tensor, scales=torch.tensor([0.1, 0.2]), zero_points=torch.tensor([0, 0]), dtype=torch.quint8)

# Task 3: Call the API
result = q_per_channel_axis.q_per_channel_axis()
print(result)