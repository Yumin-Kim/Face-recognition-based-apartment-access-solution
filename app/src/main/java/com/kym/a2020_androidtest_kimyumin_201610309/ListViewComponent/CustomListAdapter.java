package com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.kym.a2020_androidtest_kimyumin_201610309.R;

import java.util.ArrayList;

public class CustomListAdapter extends BaseAdapter {
    Activity context;
    ArrayList<Item> arlist;
    public CustomListAdapter(Activity context, ArrayList<Item> list) {
        this.context = context;
        this.arlist = list;
    }
    @Override
    public int getCount() {
        return arlist.size();
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        //inflater는 xml파일을 View객체로 만들기 위해 LayoutInflator를 사용한다.
        LayoutInflater inflater = context.getLayoutInflater();

        if(convertView==null) convertView= inflater.inflate(R.layout.itemlistviewlayout, null, true);

        ImageView imageView = (ImageView) convertView.findViewById(R.id.image);
        TextView title = (TextView) convertView.findViewById(R.id.title);
        TextView rating = (TextView) convertView.findViewById(R.id.rating);
        TextView genre = (TextView) convertView.findViewById(R.id.genre);
        TextView year = (TextView) convertView.findViewById(R.id.releaseYear);


        Item item= (Item) arlist.get(position);


        title.setText( item.title);
        imageView.setImageResource(item.srcImage);
        rating.setText("출시일:"+item.releaseDate);
        genre.setText("개발자:"+item.developer);
        year.setText("파일 확장자:"+item.fileExtension);
        return convertView;
    }
}