package com.kym.a2020_androidtest_kimyumin_201610309;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    String password;
    EditText pwdEdit;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        pwdEdit = findViewById(R.id.pwdEdit);
        findViewById(R.id.LoginBtn).setOnClickListener(ClickMetd);
    }

    View.OnClickListener ClickMetd = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            switch (v.getId()) {
                case R.id.LoginBtn :{
                    Log.v("Debug","Hello");
                    password = pwdEdit.getText().toString();
                    LoginMethod(password);
                    break;
                }
                default:break;
            }
        }
    };

    private void LoginMethod(String inputData){
      switch (inputData.trim()){
            case "" :{
                Toast.makeText(this, "재입력", Toast.LENGTH_SHORT).show();
                pwdEdit.setText("");
                break;
            }
            case "1234":{
                Toast.makeText(this, "Success Login", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(this,SubActivity.class);
                startActivity(intent);
                overridePendingTransition(R.anim.anim_right_slide_in,R.anim.anim_left_slide_out);
                break;
            }
            default:{
                Toast.makeText(this, "1234 입력해주세요!!", Toast.LENGTH_SHORT).show();
                pwdEdit.setText("");
                break;
            }
        }
    }



}
