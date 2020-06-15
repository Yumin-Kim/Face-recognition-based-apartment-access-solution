package com.kym.a2020_androidtest_kimyumin_201610309;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ListView;

import com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent.CustomListAdapter;
import com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent.FragmentListView;
import com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent.Item;

import java.util.ArrayList;

public class SubActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sub);

        FragmentManager manager = getSupportFragmentManager();
        FragmentListView fragmeniListView= new FragmentListView();
        FragmentTransaction fragmentTransaction = manager.beginTransaction();
        fragmentTransaction.add(R.id.frameLayout, fragmeniListView);
        fragmentTransaction.commit();

    }
}
