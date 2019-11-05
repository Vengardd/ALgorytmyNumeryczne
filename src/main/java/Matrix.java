import enums.ValueType;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Matrix<T> {

    private List<List<Number<T>>> cells;

    @SuppressWarnings("unchecked")
    public void setCellsFromFile(File file, ValueType type)  {
        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader("example.txt"));
            String line = bufferedReader.readLine();
            NumberFactory factory = new NumberFactory();
            int y = 0;
            while (line != null) {
                String[] values = line.split(",");
                List<Number<T>> list = new ArrayList<Number<T>>();
                for (int x = 0; x < values.length; x++) {
                    list.add(factory.createNumberFromValue("123", type));
                }
                cells.add(list);
                line = bufferedReader.readLine();
                y++;
            }
        } catch (IOException ex){

        }
    }

}