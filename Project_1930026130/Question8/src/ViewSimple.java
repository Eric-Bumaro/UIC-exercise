import java.awt.Dimension;
import java.awt.*;

import javax.swing.*;

public class ViewSimple extends View implements ModelListener{
    private JLabel label;
    public ViewSimple(Bank m,Controller c){
        super(m,c);
        label=new JLabel("total money: "+m.totalMoney(), label.CENTER);//center it
        this.add(label);
        m.addListener(this);
        this.setTitle("View imple");//the corresponding outlook
        this.setPreferredSize(new Dimension(800,100));//set the location
        Dimension dimension = Toolkit.getDefaultToolkit().getScreenSize();
        double width = dimension.getWidth() / 2;
        double height = dimension.getHeight() / 2;
        this.setLocation((int)width-400,(int)height-300);
        this.pack();
    }
    @Override
    public void update() {
        label.setText("total money: "+m.totalMoney());//update the text
    }
}