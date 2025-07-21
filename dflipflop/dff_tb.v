module dff_tb;
    reg clk, reset, enable, d;
    wire q;

    reg [3:0] input_mem [0:9]; // 4 bits: clk, reset, enable, d
    integer i;

    dff uut (.clk(clk), .reset(reset), .enable(enable), .d(d), .q(q));

    initial clk = 0;
    always #5 clk = ~clk; // Clock with period 10

    initial begin
        $readmemb("inputs.txt", input_mem);
        $display("Time\tclk\treset\tenable\td\tq");

        for (i = 0; i < 10; i = i + 1) begin
            reset  = input_mem[i][2];
            enable = input_mem[i][1];
            d      = input_mem[i][0];
            #10;
            $display("%0t\t%b\t%b\t%b\t%b\t%b", $time, clk, reset, enable, d, q);
        end
        $finish;
    end
endmodule
