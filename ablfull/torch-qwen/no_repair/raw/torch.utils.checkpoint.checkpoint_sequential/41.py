import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 224, 224)

# Task 3: Call the API
functions = torch.nn.Sequential(
    torch.nn.Conv2d(3, 64, kernel_size=3),
    torch.nn.ReLU(),
    torch.nn.MaxPool2d(kernel_size=2)
)
segments = 2
preserve_rng_state = True
use_reentrant = False

output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor, preserve_rng_state=preserve_rng_state, use_reentrant=use_reentrant)