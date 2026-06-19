import torch

# Task 2: Generate input data
input_tensor = torch.randn(2, 3, 4, 4)

# Task 3: Call the API torch.nn.Dropout2d
dropout_layer = torch.nn.Dropout2d(p=0.75)
output_tensor = dropout_layer(input_tensor)