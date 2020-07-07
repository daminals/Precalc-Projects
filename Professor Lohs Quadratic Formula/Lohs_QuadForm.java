/*
 * Daniel Kogan
 * Professor Loh of Carnegie Mellon's NEW Quadratic Formula Method
 * 7/7/2020
 */

import java.io.*;
import static java.lang.System.*;

import java.util.Arrays;
import java.util.Scanner;

class QuadForm{

     static float[] LohForm(float a_, float b_,float c_){
          float Z_,b2_;
          float[] solutions_ = new float[2];
          Z_= solveZ(a_,b_,c_);
          b2_ = (-b_/2);
          Z_ = (float) Math.sqrt(Z_);
          solutions_ = solveRoots(b2_,Z_);
          return solutions_;
     }

     static float[] QuadForm(float a_, float b_,float c_){
          float[] sol = new float[2];
          float b2,FourAC,TwoA,NegB,Discrim;
          b2 = (float )Math.pow(b_,2);
          FourAC = 4*a_*c_;
          TwoA = 2*a_;
          Discrim = b2 - FourAC;
          Discrim = (float) Math.sqrt(Discrim);
          Discrim /= TwoA;
          NegB = ((-b_)/TwoA);
          sol[0] = NegB + Discrim;
          sol[1] = NegB - Discrim;
          return sol;
     }

     static float solveZ(float a_, float b_,float c_) {
          float Z_,avg;
          avg = ((-b_/a_)/2);
          avg = (float) Math.pow(avg,2);
          Z_ = (c_/a_) - avg;
          Z_*=-1;
          //Z_ = (float) Math.sqrt(Z_);
          return Z_;
     }

     static float[] solveRoots(float b2_, float Z_) {
          float[] solutions_ = new float[2];
          solutions_[0] = b2_ + Z_;
          solutions_[1] = b2_ - Z_;
          return solutions_;
     }

     static Boolean compare(float[] a, float[] b){
          return Arrays.equals(a,b);
     }

     static void CompTest(int amount){
          float a,b,c;
          //This tests for a specified amount:
          for (int i=1; i<= amount; i++) {
               a = 1; b = i; c=2*i;
               //System.out.println(Arrays.toString(QuadForm(a, b, c)));
               //System.out.println(Arrays.toString(LohForm(a, b, c)));
               System.out.println(compare(QuadForm(a,b,c),LohForm(a,b,c)));
          }

     }

     static void solveIndiv(){
          float a,b,c,Z,b2;

          // This uses the method to actually solve Quadratic Equations

          Scanner scan = new Scanner (System.in);
          float[] solutions = new float[2];
          System.out.println("Type in the Coefficients:");

          System.out.print("a: ");
          a = scan.nextFloat();
          System.out.print("b: ");
          b = scan.nextFloat();
          System.out.print("c: ");
          c = scan.nextFloat();

          Z = solveZ(a,b,c);

          float sqr;
          String sqrtt,b2Str;
          String[] strSol = new String[2];

          b2 = (-b/2);
          sqr = (float) Math.sqrt(Z);
          // This solves using the new method

          if (Math.round(sqr)==Z){
               Z = sqr;
               solutions = solveRoots(b2,Z);
               System.out.println(solutions[0]);
               System.out.println(solutions[1]);
          }else{
               sqrtt = "√"+ String.valueOf((int)Z);
               b2Str = String.valueOf((int)b2);
               strSol[0] = b2Str + " + " + sqrtt;
               strSol[1] = b2Str + " - " + sqrtt;
               System.out.println(strSol[0]);
               System.out.println(strSol[1]);
          }
     }

     public static void main (String str[]) throws IOException {
          float a,b,c,Z,b2;

          //solveIndiv();

          //CompTest(1000);



          int i = 1;
          while (true){
               a = 1; b = i; c=2*i;
               System.out.println(compare(QuadForm(a,b,c),LohForm(a,b,c)));
               i++;
          }

     }

}


