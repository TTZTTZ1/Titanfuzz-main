import torch

# Task 2: Generate input data
input_data = torch.randn(1, 3, 16, 16)

# Task 3: Call the API torch.nn.Dropout2d
dropout_layer = torch.nn.Dropout2d(p=0.5)
output_data = dropout_layer(input_data)