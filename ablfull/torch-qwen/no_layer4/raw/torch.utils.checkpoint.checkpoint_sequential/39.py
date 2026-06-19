import torch

# Prepare input data
functions = torch.nn.Sequential(
    torch.nn.Linear(10, 20),
    torch.nn.ReLU(),
    torch.nn.Linear(20, 10)
)
segments = 2
input_tensor = torch.randn(5, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor)
print(output)