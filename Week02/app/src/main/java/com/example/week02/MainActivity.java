package com.example.week02;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.*;

public class MainActivity extends AppCompatActivity {

    private int count = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        final HashMap<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "치킨");
        map.put(2, "피자");
        map.put(3, "탕수육");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final Button btn = (Button) findViewById(R.id.button_1);
        final TextView tv = (TextView) findViewById(R.id.textView);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                count++;
                tv.setText(map.get(count)+"");
            }
        });
    }
}
