import torch
from torch.nn import Sequential, Linear

# Prepare input data
input_tensor = torch.randn(1, 3, 224, 224)
sequential_model = Sequential(
    Linear(3*224*224, 512),
    Linear(512, 256),
    Linear(256, 128)
)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(sequential_model, segments=2, input=input_tensor, use_reentrant=True)