import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 256, 256)
sequential_model = torch.nn.Sequential(torch.nn.Conv2d(3, 64, kernel_size=3), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2))
segments = 2

# Task 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential(sequential_model, segments, input_tensor, use_reentrant=True)