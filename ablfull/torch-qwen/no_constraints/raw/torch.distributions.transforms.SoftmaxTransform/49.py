import torch

# Task 2: Generate input data
input_data = torch.tensor([1.0, 2.0, 3.0])

# Task 3: Call the API
transform = torch.distributions.transforms.SoftmaxTransform()
output = transform(input_data)
print(output)