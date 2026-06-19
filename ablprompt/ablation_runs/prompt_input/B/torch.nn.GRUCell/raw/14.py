import torch

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Create random input and hidden state
input_tensor = torch.randn(5, 10)  # Batch size of 5, sequence length of 5, input size of 10
hidden_state = torch.randn(5, 20)   # Batch size of 5, hidden size of 20

# Process each time step in the sequence
for i in range(input_tensor.size(1)):
    hidden_state = gru_cell(input_tensor[:, i], hidden_state)

print(hidden_state)