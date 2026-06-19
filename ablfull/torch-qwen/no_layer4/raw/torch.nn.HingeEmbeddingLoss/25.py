import torch

# Prepare input data
input1 = torch.tensor([1.0, -1.0])
input2 = torch.tensor([-1.0, 1.0])
target = torch.tensor([1.0, -1.0])

# Create an instance of HingeEmbeddingLoss
criterion = torch.nn.HingeEmbeddingLoss(reduction='mean')

# Call the API
loss = criterion(input1, input2, target)
print(loss)