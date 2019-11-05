public class DoubleNumber implements Number<Double>{

    private double value;

    public DoubleNumber(String value) {
        this.value = Double.parseDouble(value);
    }

    @Override
    public Double add(Double aDouble) {
        return value + aDouble;
    }

    @Override
    public Double multiply(Double aDouble) {
        return value * aDouble;
    }
}
