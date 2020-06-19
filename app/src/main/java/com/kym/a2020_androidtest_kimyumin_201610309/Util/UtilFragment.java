package com.kym.a2020_androidtest_kimyumin_201610309.Util;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CalendarView;
import android.widget.TimePicker;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;

import com.kym.a2020_androidtest_kimyumin_201610309.R;

public class UtilFragment extends Fragment {
    private String dateInfo;
    private String timeInfo;
    private Activity activity;
    private TimePicker picker;
    private CalendarView calendarView;
    private CalendarView.OnDateChangeListener calenderLisener;
    private TimePicker.OnTimeChangedListener timeChangeLisener;




    public UtilFragment() {

        calenderLisener = new CalendarView.OnDateChangeListener() {
            @Override
            public void onSelectedDayChange(@NonNull CalendarView view, int year, int month, int dayOfMonth) {
                month = month + 1;
                dateInfo =  year + "년" + month + " 월"  + dayOfMonth + " 일 입니다!!" +"\n\n";
            }
        };

        timeChangeLisener = new TimePicker.OnTimeChangedListener() {
            @Override
            public void onTimeChanged(TimePicker view, int hourOfDay, int minute) {
                int hour = picker.getCurrentHour();
                int min = picker.getCurrentMinute();
                String hourConfirm = null;
                if(hour > 12){
                    hour-=12;
                    hourConfirm = "오후 ";
                }else{
                    hourConfirm = "오전 ";
                }

                timeInfo = hourConfirm + hour + "시" + min + "분 입니다 \n\n";
            }
        };

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_3, container, false);
        activity = getActivity();
        v.findViewById(R.id.collectBtn).setOnClickListener(getDateInfo);

        ((AppCompatActivity)getActivity()).getSupportActionBar().setTitle("Fragment Third Content");
        ((AppCompatActivity)getActivity()).getSupportActionBar().setSubtitle("201610309 주제 : 원하는 날짜,시간 보여줘요!!");

        calendarView = v.findViewById(R.id.calender);
        calendarView.setOnDateChangeListener(calenderLisener);

        picker = v.findViewById(R.id.timePicker);
        picker.setIs24HourView(true);
        picker.setOnTimeChangedListener(timeChangeLisener);

        return v;
    }

    View.OnClickListener getDateInfo = new View.OnClickListener() {

        @Override
        public void onClick(View v) {
            AlertDialog.Builder builder = new AlertDialog.Builder(activity);
            if(dateInfo==null || timeInfo == null){
                builder.setTitle("선택한 날짜 혹은 시간을 선택하지 않으셧습니다!!\n\n\n\n").setMessage("다시 선택해주세요!!\n\n");
            }else{
                builder.setTitle("선택한 날짜 시간입니다!!\n").setMessage(dateInfo+timeInfo);
            }
            AlertDialog alertDialog = builder.create();
            alertDialog.show();
        }
    };

}
