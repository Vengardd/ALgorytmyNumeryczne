public class FloatNumber implements Number<Float> {

    private float value;

    public FloatNumber(String value) {
        this.value = Float.parseFloat(value);
    }

    @Override
    public Float add(Float aFloat) {
        return value + aFloat;
    }

    @Override
    public Float multiply(Float aFloat) {
        return value * aFloat;
    }

}
