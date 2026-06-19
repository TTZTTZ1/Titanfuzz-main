import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 16)
indices = torch.argmax(input_tensor, dim=1).unsqueeze(0).expand(-1, -1, input_tensor.size(2))
kernel_size = 2
stride = 2

# Task 3: Call the API
output = torch.nn.functional.max_unpool1d(input_tensor, indices, kernel_size, stride)

print(output)