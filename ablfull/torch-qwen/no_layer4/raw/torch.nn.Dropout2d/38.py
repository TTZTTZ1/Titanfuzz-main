import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 4, 4)

# Task 3: Call the API
dropout_layer = torch.nn.Dropout2d(p=0.7, inplace=False)
output_tensor = dropout_layer(input_tensor)