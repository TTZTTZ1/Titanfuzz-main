import torch

# Define the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Initialize input and hidden state
input_tensor = torch.randn(5, 10)  # Batch size of 5, sequence length of 5, feature dimension of 10
hidden_state = torch.randn(5, 20)   # Batch size of 5, hidden state dimension of 20

# Process the input through the GRUCell
for t in range(input_tensor.size(0)):
    hidden_state = gru_cell(input_tensor[t], hidden_state)

print(hidden_state)