import torch

# Prepare valid input data
input_data = torch.tensor([-0.5, 0.0, 0.5])

# Call the API
result = input_data.asin_()

print(result)