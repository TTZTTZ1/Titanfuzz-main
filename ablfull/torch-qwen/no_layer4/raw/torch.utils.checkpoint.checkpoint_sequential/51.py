import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(3, 5)

# Define sequential model
sequential_model = Sequential(
    Linear(5, 10),
    Linear(10, 15),
    Linear(15, 20)
)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(
    sequential_model,
    segments=2,
    input=input_tensor,
    use_reentrant=True
)