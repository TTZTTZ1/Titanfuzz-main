import torch
from torch.nn import Sequential, Linear

# Step 1: Define a simple sequential model
model = Sequential(
    Linear(10, 20),
    Linear(20, 30),
    Linear(30, 40)
)

# Step 2: Prepare valid input data
input_data = torch.randn(5, 10)

# Step 3: Call the API with valid parameters
result = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_data, preserve_rng_state=True, use_reentrant=True)
print(result.shape)