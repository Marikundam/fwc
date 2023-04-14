module logicex(
    input clk,
    input Q0,
    input Q1,
    input Q2,
    output reg D0,
    output reg D1,
    output reg D2
    );

    always @(*) begin
	D2 = (Q2&&(!Q1)) || (Q0&&Q2);
	D1 = (Q2);
	D0 = (Q1);
end
endmodule




