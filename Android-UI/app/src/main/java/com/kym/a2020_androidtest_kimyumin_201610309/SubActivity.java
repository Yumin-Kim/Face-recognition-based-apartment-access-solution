package com.kym.a2020_androidtest_kimyumin_201610309;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ListView;
import android.widget.Toast;

import com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent.CustomListAdapter;
import com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent.FragmentListView;
import com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent.Item;
import com.kym.a2020_androidtest_kimyumin_201610309.RecycleView.FragmentRecycleView;
import com.kym.a2020_androidtest_kimyumin_201610309.Util.UtilFragment;

import java.util.ArrayList;

public class SubActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sub);

        findViewById(R.id.btn_fragmentA).setOnClickListener(TabClickMethod);
        findViewById(R.id.btn_fragmentB).setOnClickListener(TabClickMethod);
        findViewById(R.id.btn_fragmentC).setOnClickListener(TabClickMethod);

        //Framgement Logic
        FragmentManager manager = getSupportFragmentManager();
        FragmentListView fragmeniListView = new FragmentListView();
        FragmentTransaction fragmentTransaction = manager.beginTransaction();
        fragmentTransaction.add(R.id.frameLayout, fragmeniListView);
        fragmentTransaction.commit();
    }

    View.OnClickListener TabClickMethod = new View.OnClickListener() {
        Fragment fragment = null;
        @Override
        public void onClick(View v) {
            FragmentTransaction fragmentTransaction = getSupportFragmentManager().beginTransaction();
            switch (v.getId()) {
                case R.id.btn_fragmentA: {
                    Log.v("Debug", "btn_fragmentA");
                    fragment = new FragmentListView();
                    break;
                }
                case R.id.btn_fragmentB: {
                    Log.v("Debug", "btn_fragmentB");
                    fragment = new FragmentRecycleView();
                    break;
                }
                case R.id.btn_fragmentC: {
                    Log.v("Debug", "btn_fragmentC");
                    fragment = new UtilFragment();
                    break;
                }
                default:
                    break;
            }
            fragmentTransaction.replace(R.id.frameLayout, fragment);
            fragmentTransaction.commit();
        }
    };

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.util,menu);
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        Intent intent = null;
        int selectMenu = item.getItemId();

        switch (selectMenu){
            case R.id.menu_call:{
                Log.v("DEBUG","SELECT CALL");
                intent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:(+82)12345789"));
                break;
            }
            case R.id.menu_check_list :{
                intent = new Intent(Intent.ACTION_VIEW, Uri.parse("content://contacts/people/"));
                break;
            }
            case R.id.menu_Tomap :{
                intent = new Intent(Intent.ACTION_VIEW, Uri.parse("geo:36.623334,127.48312?z=15"));
                break;
            }
        }
        if (intent != null) {
            startActivity(intent);
        }
        return super.onOptionsItemSelected(item);
    }
}
