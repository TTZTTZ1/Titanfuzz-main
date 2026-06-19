import torch

# Define the input size and hidden size
input_size = 10
hidden_size = 20

# Create a GRUCell instance
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_tensor = torch.randn(3, input_size)  # Batch size of 3, sequence length of 1, feature dimension of 10
hidden_state = torch.randn(3, hidden_size)  # Batch size of 3, feature dimension of 20

# Process the input through the GRUCell
new_hidden_state = gru_cell(input_tensor, hidden_state)

print(new_hidden_state)