import torch

# Generate input data
tensor = torch.randint(0, 16, size=(4, 3), dtype=torch.uint8)
quantization_param = torch.tensor([0.5] * 4, dtype=torch.float32)

# Call the API
result = torch.quantization.q_per_channel_axis(tensor, quantization_param, 0, 'symmetric')
print(result)