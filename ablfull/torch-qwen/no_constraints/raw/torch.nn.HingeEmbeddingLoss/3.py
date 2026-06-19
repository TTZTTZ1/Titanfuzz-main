import torch

# Prepare input data
input1 = torch.randn(3)
input2 = torch.randn(3)
target = torch.tensor([1.0, -1.0, 1.0])

# Call the API
criterion = torch.nn.HingeEmbeddingLoss()
loss = criterion(input1, input2, target)

print(loss)