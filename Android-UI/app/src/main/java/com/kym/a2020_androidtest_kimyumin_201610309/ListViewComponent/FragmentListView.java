package com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent;

import android.app.Activity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import com.kym.a2020_androidtest_kimyumin_201610309.R;
import java.util.ArrayList;

public class FragmentListView extends Fragment {
    ListView simpleList;
    ArrayList<Item> languageList = new ArrayList<Item>();

    public FragmentListView() {
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.activity_listview,container,false);
        ((AppCompatActivity)getActivity()).getSupportActionBar().setTitle("Fragment First Content");
        ((AppCompatActivity)getActivity()).getSupportActionBar().setSubtitle("201610309 주제 : 프로그래밍 언어!!");
        languageList.add(new Item("JavaScript", R.drawable.javascript, "1995/12", "넷스케이프, 모질라 재단", ".js"));
        languageList.add(new Item("TypeScript", R.drawable.typescript, "2012/10", "마이크로소프트", ".ts"));
        languageList.add(new Item("Go", R.drawable.go, "2009/11", "구글", ".go"));
        languageList.add(new Item("php", R.drawable.php, "1995/06", "젠드 테크놀로지스", ".php"));
        languageList.add(new Item("Java", R.drawable.java, "1996/01", "오라클", ".class , .java"));
        languageList.add(new Item("Kotlin", R.drawable.kotlin, "2011", "젯브레인즈", ".kt,.kts"));
        languageList.add(new Item("Python", R.drawable.phthon, "1991/02", "파이썬 소프트웨어 재단", ".py , .pyc ,.pyd"));
        languageList.add(new Item("Ruby", R.drawable.ruby, "1995", "마츠모토 유키히로", ".rb"));
        languageList.add(new Item("C++", R.drawable.cplus, "1983/..", "비야네 스트롭스트룹", ".cc , .cpp , .hh ........."));
        languageList.add(new Item("C", R.drawable.cprogramming, "1972/..", "데니스 리치", ".c , .h"));
        simpleList = v.findViewById(android.R.id.list);
        CustomListAdapter arrayAdapter = new CustomListAdapter(getActivity(), languageList);
        simpleList.setAdapter(arrayAdapter);
        return v;
    }
}
