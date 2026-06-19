import torch

# Prepare valid input data
target = torch.tensor([1.0, -1.0])
input1 = torch.tensor([2.0, 0.5])
input2 = torch.tensor([-1.0, 1.0])

# Create an instance of HingeEmbeddingLoss with specified parameters
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')

# Call the API
loss = criterion(input1, input2, target)
print(loss)