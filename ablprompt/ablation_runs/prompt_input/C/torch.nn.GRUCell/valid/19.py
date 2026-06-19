import torch

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Input sequence and initial hidden state
input_sequence = torch.randn(5, 3, 10)  # 5 time steps, 3 samples, each sample has 10 features
initial_hidden_state = torch.randn(3, 20)  # 3 samples, each sample has a hidden state of size 20

# Process the input sequence through the GRUCell
output_states = []
hidden_state = initial_hidden_state
for input_step in input_sequence:
    hidden_state = gru_cell(input_step, hidden_state)
    output_states.append(hidden_state)

# Convert list to tensor for further processing if needed
output_states = torch.stack(output_states)

print(output_states.shape)  # Should print: torch.Size([5, 3, 20])