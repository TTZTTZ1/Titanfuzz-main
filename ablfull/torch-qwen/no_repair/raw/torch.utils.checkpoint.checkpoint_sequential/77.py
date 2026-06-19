import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 224, 224)

# Task 3: Call the API
functions = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)
segments = 2
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, use_reentrant=False)