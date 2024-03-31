package HandelExaption;

public class First {

    public void Methodone() throws Exception {
        int x = 9;
        // Division by zero will throw ArithmeticException
        x /= 0;
        throw new Exception();
    }

    public void Methodtwo() throws Exception {
        String x = "kasem";
        // Parsing non-integer string will throw NumberFormatException
        int y = Integer.parseInt(x);
        throw new Exception();
    }
}
