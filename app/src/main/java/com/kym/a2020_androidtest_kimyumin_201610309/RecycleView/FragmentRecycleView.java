package com.kym.a2020_androidtest_kimyumin_201610309.RecycleView;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.kym.a2020_androidtest_kimyumin_201610309.R;

import java.util.ArrayList;
import java.util.List;

public class FragmentRecycleView extends Fragment {
    final int ITEM_SIZE = 10;

    public FragmentRecycleView(){

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_2 , container ,false);
        ((AppCompatActivity)getActivity()).getSupportActionBar().setTitle("Fragment Second Content");
        ((AppCompatActivity)getActivity()).getSupportActionBar().setSubtitle("201610309 주제 : 전서계!!");

        RecyclerView recyclerView = v.findViewById(R.id.recyclerview);
        LinearLayoutManager layout = new LinearLayoutManager(getActivity().getApplicationContext());
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(layout);

        List<Item> items = new ArrayList<>();
        Item[] item = new Item[ITEM_SIZE];
        item[0] = new Item(R.drawable.a,"한국");
        item[1] = new Item(R.drawable.b,"이탈리아");
        item[2] = new Item(R.drawable.c,"브라질");
        item[3] = new Item(R.drawable.d,"독일");
        item[4] = new Item(R.drawable.e,"영국");
        item[5] = new Item(R.drawable.f,"일본");
        item[6] = new Item(R.drawable.g,"중국");
        item[7] = new Item(R.drawable.h,"미국");
        item[8] = new Item(R.drawable.i,"인도");
        item[9] = new Item(R.drawable.j,"싱가포르");

        for(int i = 0 ; i < ITEM_SIZE ; i ++) items.add(item[i]);

        recyclerView.setAdapter(new RecycleAdapter(getActivity(),items,123));
        return v;
    }
}
