import torch

# Task 2: Generate input data
model = torch.nn.Sequential(torch.nn.Linear(5, 5), torch.nn.ReLU(), torch.nn.Linear(5, 5))
segments = 2
input_data = torch.randn(1, 5)

# Task 3: Call the API
result = torch.utils.checkpoint.checkpoint_sequential(model, segments, input_data, use_reentrant=True)