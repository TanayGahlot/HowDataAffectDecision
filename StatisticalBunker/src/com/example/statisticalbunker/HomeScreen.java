package com.example.statisticalbunker;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class HomeScreen extends Activity {
	
	static EditText ca;
	static EditText ta;
	static EditText el;
	static EditText coa;

	
	static int currentAttendance=0;
	static int totalAttendance=0;
	static int expectedLecture=0;
	static int cutoffAttendance=0;
	static TextView bunkAffordanceTextView;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_home_screen);
		ca=(EditText)findViewById(R.id.editText1);
		el=(EditText)findViewById(R.id.editText2);
		coa=(EditText)findViewById(R.id.editText3);
		ta=(EditText)findViewById(R.id.editText4);
		bunkAffordanceTextView=(TextView)findViewById(R.id.textView8);
		Button calcBunkAffordance = (Button) findViewById(R.id.button1); 
		calcBunkAffordance.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				currentAttendance=Integer.parseInt(ca.getText().toString());
				totalAttendance=Integer.parseInt(ta.getText().toString());
				expectedLecture=Integer.parseInt(el.getText().toString());
				cutoffAttendance=Integer.parseInt(coa.getText().toString());
				int bunkAffordanceVal=bunkAffordance(currentAttendance,totalAttendance,expectedLecture,cutoffAttendance);
				bunkAffordanceTextView.setText(String.valueOf(bunkAffordanceVal));
				

			
			}
		});
		
	}

	protected int bunkAffordance(int ca,int ta,int el,int cutoff){
			return (int) ((el*(100-cutoff)*.01)-(ta-ca));
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.home_screen, menu);
		return true;
	}
	
}
