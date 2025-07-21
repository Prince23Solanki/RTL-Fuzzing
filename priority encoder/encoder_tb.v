module encoder_tb;
    reg [7:0] in;
    wire [2:0] out;
    wire valid;

    reg [7:0] input_mem [0:9];
    integer i;

    encoder uut (.in(in), .out(out), .valid(valid));

    initial begin
        $readmemb("inputs.txt", input_mem);
        $display("Time\tin\tout\tvalid");

        for (i = 0; i < 10; i = i + 1) begin
            in = input_mem[i];
            #10;
            $display("%0t\t%b\t%b\t%b", $time, in, out, valid);
        end
        $finish;
    end
endmodule
