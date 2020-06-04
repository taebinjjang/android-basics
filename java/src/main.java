import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class main extends JFrame {
    private int count;
    main() {
        Dimension dek = Toolkit.getDefaultToolkit().getScreenSize();
        setTitle("Clicker");
        setLayout(new FlowLayout());
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocation(dek.width/2-150, dek.height/2-75);
        JButton btn = new JButton("Click한 횟수");
        JButton btn_1 = new JButton("Reset");
        JLabel leb = new JLabel(Integer.toString(count));

        btn_1.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                count = 0;
                leb.setText("         "+Integer.toString(count)+"        ");
            }
        });

        btn.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                btn.setText("         "+Integer.toString(count)+"        ");
                leb.setText("         "+Integer.toString(count)+"        ");
            }

            @Override
            public void mouseExited(MouseEvent e) {
                btn.setText("Click한 횟수");
            }

            @Override
            public void mouseClicked(MouseEvent e) {
                count++;
                btn.setText("         "+Integer.toString(count)+"        ");
                leb.setText("         "+Integer.toString(count)+"        ");
            }
        });

        add(btn);
        add(btn_1);
        add(leb);
        setSize(300, 150);
        setVisible(true);
    }

    public static void main(String arg[]) {
        new main();
    }
}
