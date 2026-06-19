import torch

# Prepare input data
input1 = torch.randn(5)
input2 = torch.randn(5)
target = torch.randint(0, 2, (5,))

# Create an instance of HingeEmbeddingLoss
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0)

# Call the API
loss = criterion(input1, input2, target)
print(loss.item())