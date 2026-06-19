import torch

# Prepare valid input data
input1 = torch.tensor([1.0, -1.0], dtype=torch.float32)
input2 = torch.tensor([-1.0, 1.0], dtype=torch.float32)
target = torch.tensor([1.0, -1.0], dtype=torch.float32)

# Create an instance of HingeEmbeddingLoss
criterion = torch.nn.HingeEmbeddingLoss()

# Call the API
output = criterion(input1, input2, target)

print(output)