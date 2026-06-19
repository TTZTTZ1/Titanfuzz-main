import torch

# Task 2: Generate input data
tensor = torch.randn(4, 3, 224, 224)
q_params = torch.quantization.get_default_qparams("per_tensor_affine", dtype=torch.float)

# Task 3: Call the API
result = tensor.q_per_channel_axis(q_params, axis=0)