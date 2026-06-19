import torch

# Task 2: Generate input data
input_data = torch.randn(1, 3, 4, 4, 4)

# Task 3: Call the API
padding_value = (1, 2, 3, 4, 5, 6)
output = torch.nn.functional.reflective_pad(input_data, padding=padding_value)