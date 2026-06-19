import torch

# Generate input data
input_tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
q_params = {'qscheme': torch.per_channel_affine, 'dtype': torch.qint8}

# Call the API
result = torch.ops.torchvision.quantization.q_per_channel_axis(input_tensor, q_params['qscheme'], q_params['dtype'])