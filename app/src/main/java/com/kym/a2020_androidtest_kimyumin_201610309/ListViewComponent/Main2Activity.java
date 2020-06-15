//package com.kym.myadaper;
//
//import androidx.appcompat.app.AppCompatActivity;
//
//import android.content.Intent;
//import android.os.Bundle;
//import android.util.Log;
//import android.view.View;
//import android.widget.AdapterView;
//import android.widget.ListView;
//
//import java.util.ArrayList;
//
//public class Main2Activity extends AppCompatActivity {
//    ListView simpleList;
//    ArrayList<Item> languageList = new ArrayList<Item>();
//
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState)q;
//        setContentView(R.layout.activity_main);
//
//
//        getSupportActionBar().setTitle("201610309 주제 : 프로그래밍 언어!!");
//        languageList.add(new Item("JavaScript", R.drawable.javascript, "1995/12", "넷스케이프, 모질라 재단", ".js"));
//        languageList.add(new Item("TypeScript", R.drawable.typescript, "2012/10", "마이크로소프트", ".ts"));
//        languageList.add(new Item("Go", R.drawable.go, "2009/11", "구글", ".go"));
//        languageList.add(new Item("php", R.drawable.php, "1995/06", "젠드 테크놀로지스", ".php"));
//        languageList.add(new Item("Java", R.drawable.java, "1996/01", "오라클", ".class , .java"));
//        languageList.add(new Item("Kotlin", R.drawable.kotlin, "2011", "젯브레인즈", ".kt,.kts"));
//        languageList.add(new Item("Python", R.drawable.phthon, "1991/02", "파이썬 소프트웨어 재단", ".py , .pyc ,.pyd"));
//        languageList.add(new Item("Ruby", R.drawable.ruby, "1995", "마츠모토 유키히로", ".rb"));
//        languageList.add(new Item("C++", R.drawable.cplus, "1983/..", "비야네 스트롭스트룹", ".cc , .cpp , .hh ........."));
//        languageList.add(new Item("C", R.drawable.cprogramming, "1972/..", "데니스 리치", ".c , .h"));
//
//
//        simpleList = findViewById(R.id.ListView);
//        CustomListAdapter arrayAdapter = new CustomListAdapter(this, languageList);
//        simpleList.setAdapter(arrayAdapter);
//
//        ListView simpleList = (ListView) findViewById(R.id.ListView);
//        simpleList.setOnItemClickListener(new AdapterView.OnItemClickListener() {
//            @Override
//            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
//                Item listItem = languageList.get(position);
//                Intent intent = new Intent(getApplicationContext(), MainActivity.class);
//                Intent intent11 = getIntent();
//                ArrayList<Item> addIntentArrayList = new ArrayList<Item>();
//                if (intent11.getExtras() != null) {
//                    ArrayList<Item> data = (ArrayList<Item>) intent11.getSerializableExtra("cache");
//                    addIntentArrayList = new ArrayList<Item>(data);
//                }
//                addIntentArrayList.add(listItem);
//                intent.putExtra("intentData", addIntentArrayList);
//                setResult(RESULT_OK, intent);
//                finish();
//            }
//        });
//    }
//}
//
//
//
//
