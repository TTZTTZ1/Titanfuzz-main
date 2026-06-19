import torch

# Prepare valid input data
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)

# Call the API
result = tensor.q_per_channel_axis()

print(result)