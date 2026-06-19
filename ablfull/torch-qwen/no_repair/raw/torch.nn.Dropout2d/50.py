import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 64, 64)

# Task 3: Call the API
dropout_layer = torch.nn.Dropout2d(p=0.7)
output_tensor = dropout_layer(input_tensor)