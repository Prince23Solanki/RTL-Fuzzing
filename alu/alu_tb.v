module alu_tb;
    reg [3:0] A, B;
    reg [2:0] opcode;
    wire [3:0] result;

    integer i;
    reg [10:0] input_mem [0:9]; // 11-bit: A[3:0] B[3:0] opcode[2:0]

    alu uut (
        .A(A),
        .B(B),
        .opcode(opcode),
        .result(result)
    );

    initial begin
        $readmemb("inputs.txt", input_mem); // Read fuzzed inputs from file

        $display("Time\tA\tB\topcode\tResult");

        for (i = 0; i < 10; i = i + 1) begin
            A      = input_mem[i][10:7];
            B      = input_mem[i][6:3];
            opcode = input_mem[i][2:0];

            #10;
            $display("%0t\t%d\t%d\t%b\t%d", $time, A, B, opcode, result);
        end
        $finish;
    end
endmodule
