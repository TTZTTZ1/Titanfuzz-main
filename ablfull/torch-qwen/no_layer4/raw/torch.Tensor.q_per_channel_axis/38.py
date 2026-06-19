import torch

# Generate input data
tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
q_params = [torch.quantization.QuantizerConfig(per_channel=True)]

# Call the API
result = tensor.q_per_channel_axis(q_params)

print(result)