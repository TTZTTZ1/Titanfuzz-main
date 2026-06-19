import torch

# Generate a random tensor with shape (4, 4)
input_tensor = torch.randn(4, 4)

# Call the API with the generated input data
quantized_tensor = torch.Tensor.q_per_channel_axis(input_tensor, dtype=torch.qint8)