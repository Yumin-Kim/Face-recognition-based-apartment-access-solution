package com.kym.a2020_androidtest_kimyumin_201610309.ListViewComponent;

import java.io.Serializable;

public class Item  implements Serializable {
    public String title;
    public int srcImage;
    public String releaseDate;
    public String developer;
    public String fileExtension;

    public Item(String t , int s , String r , String d , String rel){
        this.title = t;
        this.srcImage = s;
        this.releaseDate = r;
        this.developer = d;
        this.fileExtension = rel;
    }

}

