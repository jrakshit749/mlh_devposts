import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:percent_indicator/circular_percent_indicator.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: Pomodoro(),
  ));
}

class Pomodoro extends StatefulWidget {
  @override
  _PomodoroState createState() => _PomodoroState();
}

class _PomodoroState extends State<Pomodoro> {
  double percent = 0;
  // ignore: non_constant_identifier_names
  static int TimeInMinut = 25;
  // ignore: non_constant_identifier_names
  int TimeInSec = TimeInMinut * 60;

  Timer timer;
  _StartTimer(){
  TimeInMinut = 25;
  int Time = TimeInMinut*60;
  double SecPercent = (Time/100);
  timer = Timer.periodic(Duration(seconds: 1), (timer) {
    setState(() {
      if (Time > 0){
        Time--;
        if (Time % 60 == 0){
          TimeInMinut--;
        }
        if (Time % SecPercent == 0){
          if(percent < 1){percent += 0.01;}
          else{
            percent = 1;
          }
        }
      }
      else{
        percent = 0;
        timer.cancel();
      }
    });
  });
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: Container(
            decoration: BoxDecoration(
                gradient: LinearGradient(
                    colors: [Color(0xff1542bf), Color(0xff51a8ff)],
                    begin: FractionalOffset(0.5, 1))),
            width: double.infinity,
            child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: <Widget>[
                  Padding(
                    padding: EdgeInsets.only(top: 25.0),
                    child: Text(
                      "Pomodoro Clock",
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 35,
                      )
                    ),
                  ),
                  // expanded for the circular ring and text inside it
                  Expanded(
                    child: CircularPercentIndicator(

                      circularStrokeCap: CircularStrokeCap.round,
                      percent: percent,
                      animation: true,
                      animateFromLastPercent: true,
                      radius: 250.0,
                      lineWidth: 15,
                      progressColor: Colors.white,
                      center: Text(
                        "$TimeInMinut",
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 80.0,
                        ),
                      ),
                    )
                  ),
                  SizedBox(height: 30.0,),
                  Expanded(
                    child: Container(
                      width: double.infinity,
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.only(topRight: Radius.circular(30.0), topLeft: Radius.circular(30.0)),
                      ),
                      child: Padding(
                        padding: EdgeInsets.only(top: 30, left: 20, right: 20),
                        child: Column(
                          children: <Widget> [
                            Expanded(child: Row(
                              children: <Widget> [
                                Expanded(
                                    child: Column(
                                    children: <Widget> [
                                    Text(
                                      "Study Timer",
                                      style: TextStyle(
                                        fontSize: 25
                                      ),
                                    ),
                                    SizedBox(height: 10,),
                                    Text(
                                      "25",
                                      style: TextStyle(
                                        fontSize: 80
                                      ),
                                    ),

                                  ],
                                )),
                                Expanded(
                                    child: Column(
                                      children: <Widget> [
                                        Text(
                                          "Pause Time",
                                          style: TextStyle(
                                              fontSize: 25
                                          ),
                                        ),
                                        SizedBox(height: 10,),
                                        Text(
                                          "5",
                                          style: TextStyle(
                                              fontSize: 80
                                          ),
                                        ),

                                      ],
                                    )),
                              ],
                             ),
                            ),
                            Padding(
                                padding: EdgeInsets.symmetric(
                                    vertical: 20),
                                child: RaisedButton(

                                      onPressed: _StartTimer,
                                      color: Colors.blue,
                                      shape: RoundedRectangleBorder(
                                        borderRadius: BorderRadius.circular(100)
                                      ),
                                    child: Padding(
                                      padding: EdgeInsets.all(20.0),
                                      child: Text("Start Studying",
                                      style: TextStyle(
                                        color: Colors.white,
                                        fontSize: 22,

                                      )
                                      )
                                    ),
                                )
                                ),

                          ],
                        ),
                      )
                    )
                  )
                ])),
      ),
    );
  }
}
