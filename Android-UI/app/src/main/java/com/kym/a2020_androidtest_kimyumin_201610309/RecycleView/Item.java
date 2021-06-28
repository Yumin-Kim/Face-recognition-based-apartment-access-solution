package com.kym.a2020_androidtest_kimyumin_201610309.RecycleView;

public class Item {
    private int image;
    private String title;

    int getImage(){
        return this.image;
    }

    String getTitle(){
        return this.title;
    }

    public Item(int image , String title){
        this.image = image;
        this.title = title;
    }
}
