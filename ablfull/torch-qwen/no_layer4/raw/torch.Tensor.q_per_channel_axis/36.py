import torch

# Prepare valid input data
tensor = torch.randint(0, 128, (4, 3, 224, 224), dtype=torch.uint8)
quint8_scale = torch.tensor([0.5] * 3, dtype=torch.float32)
quint8_zero_point = torch.tensor([64] * 3, dtype=torch.int32)

# Call the API
result = tensor.q_per_channel_axis(quint8_scale, quint8_zero_point)