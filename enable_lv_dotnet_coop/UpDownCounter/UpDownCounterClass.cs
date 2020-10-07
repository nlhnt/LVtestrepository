using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading; //Include to be able to sleep

namespace UpDownCounterClass
{
    public delegate void CountStatus(int countValue);
    public class UpDownCounter
    {
        //Constructor
        public UpDownCounter(){

        }

        //Destructor
        ~UpDownCounter(){

        }

        public event CountStatus OnCallBack;

        public bool countUp(int upper, int lower, int sleep){
            for(int i = lower; i <= upper; i++){
                //Generate the event
                OnCallBack(i);
                Thread.Sleep(sleep);
            }
            return true;
        }

        public bool countDown(int upper, int lower, int sleep){
            for(int i = upper; i >= lower; i--){
                //Generate the event
                OnCallBack(i);
                Thread.Sleep(sleep);
            }
            return true;
        }

        public double adder(double x, double y){
            return (x+y);
        }

        public string concatenateStrings(string x, string y){
            return String.Concat(x,y);
        }
    }
}
