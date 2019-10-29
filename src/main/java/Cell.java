public class Cell<T> {

    private T value;
    private Position position;

    public Cell(T value, Position position) {
        this.value = value;
        this.position = position;
    }

    public Cell(T value, int x, int y) {
        this.value = value;
        this.position = new Position(x, y);
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }

    public Position getPosition() {
        return position;
    }

    public void setPosition(Position position) {
        this.position = position;
    }
}