import enums.ValueType;

public class NumberFactory {

    public Number createNumberFromValue(String x, ValueType type) {
        switch (type) {
            case FLOAT:
                return new FloatNumber(x);
            case DOUBLE:
                return new DoubleNumber(x);
            default:
                throw new UnsupportedOperationException("Nie obslugiwany typ liczby: " + type);
        }
    }
}
