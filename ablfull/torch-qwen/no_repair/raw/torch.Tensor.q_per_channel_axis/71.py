import torch

# Create a tensor satisfying the constraints for q_per_channel_axis
tensor = torch.tensor([[[[0.5, -0.5], [0.3, -0.3]]]], dtype=torch.float)

# Call the target API
quantized_tensor, scale, zero_point = tensor.q_per_channel_axis(ch_axis=3)