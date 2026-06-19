import torch

# Task 2: Generate input data
sequential_model = torch.nn.Sequential(
    torch.nn.Linear(10, 5),
    torch.nn.ReLU(),
    torch.nn.Linear(5, 2)
)

input_data = torch.randn(3, 10)

# Task 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential([sequential_model], 1, input_data, use_reentrant=True)