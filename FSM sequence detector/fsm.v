module fsm (
    input clk,
    input reset,
    input din,
    output reg out
);
    reg [2:0] state, next_state;

    // State encoding
    parameter S0 = 3'b000,
              S1 = 3'b001,
              S2 = 3'b010,
              S3 = 3'b011,
              S4 = 3'b100;

    // State register
    always @(posedge clk or posedge reset) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end

    // Next state logic
    always @(*) begin
        case (state)
            S0: next_state = (din == 1) ? S1 : S0;
            S1: next_state = (din == 0) ? S2 : S1;
            S2: next_state = (din == 1) ? S3 : S0;
            S3: next_state = (din == 1) ? S4 : S2;
            S4: next_state = S0; // Detected
            default: next_state = S0;
        endcase
    end

    // Output logic (Mealy)
    always @(*) begin
        out = 0;
        if (state == S3 && din == 1)
            out = 1;  // Detected 1011
    end
endmodule
