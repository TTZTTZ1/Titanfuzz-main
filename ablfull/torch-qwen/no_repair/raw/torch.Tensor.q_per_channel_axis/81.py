import torch

# Task 2: Generate input data
tensor = torch.rand(3, 4, dtype=torch.float32)
q_params = {'qscheme': torch.per_tensor_symmetric}

# Task 3: Call the API
result = tensor.quantize_per_channel(**q_params)