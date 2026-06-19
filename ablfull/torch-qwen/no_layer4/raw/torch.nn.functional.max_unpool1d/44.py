import torch

input_data = torch.randn(1, 64, 7)
indices = torch.argmax(input_data, dim=-1).unsqueeze(-1).expand(-1, -1, 7)
kernel_size = 3
output = torch.nn.functional.max_unpool1d(input_data, indices, kernel_size, stride=kernel_size, padding=0)
print(output.shape)  # Should be torch.Size([1, 64, 21])