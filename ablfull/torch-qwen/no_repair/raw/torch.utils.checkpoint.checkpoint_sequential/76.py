import torch
from torch.nn import Linear

# Task 2: Generate input data
sequential_model = torch.nn.Sequential(Linear(5, 5), Linear(5, 5))
input_data = torch.randn(1, 5)

# Task 3: Call the API
checkpointed_output = torch.utils.checkpoint.checkpoint_sequential(
    sequential_model, segments=2, input=input_data, preserve_rng_state=True, use_reentrant=False
)