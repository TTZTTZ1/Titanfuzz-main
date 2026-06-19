import torch

# Prepare valid input data
input_tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
dtype_param = torch.quint8

# Call the API
output_tensor = input_tensor.q_per_channel_axis(dtype=dtype_param)