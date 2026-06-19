import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Input sequence and initial hidden state
input_sequence = torch.randn(5, 3, input_size)  # Sequence length 5, batch size 3, input size 10
initial_hidden_state = torch.randn(3, hidden_size)  # Batch size 3, hidden size 20

# Process the input sequence
hidden_states = []
for i in range(input_sequence.size(0)):
    hidden_state = gru_cell(input_sequence[i], initial_hidden_state)
    hidden_states.append(hidden_state)
    initial_hidden_state = hidden_state

# Convert list to tensor
hidden_states = torch.stack(hidden_states)

print("Hidden states:", hidden_states)