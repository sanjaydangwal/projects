#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<iostream.h>
#include<string.h>
enum bool{False,True};
struct logInData
{
char userName[15];
char password[15];
};
struct Qustions
{
  char qus[100];
  char a[15];
  char b[15];
  char c[15];
  char d[15];
  char ans;
};
logInData enterLogInSignUp()
{
logInData enterData;
 int i=0;
  clrscr();
  cout<<"enter user name	:	";
  cin>>enterData.userName;
  cout<<"enter password		:	";
  while(1)
  {
   enterData.password[i] = getch();
   enterData.password[i+1] = NULL;
   if(enterData.password[i] == 13)
   break;
   printf("*");
   i++;
  }
  return (enterData);
}
class Admin
{
logInData existData,enterData;
 public:
 bool adminSignUp()
 {
 enterData = enterLogInSignUp();
  FILE *fp;
  fp = fopen("adminData.dat","rb");
  while(fread(&existData,sizeof(existData),1,fp))
  {
   if(!strcmp(existData.userName,enterData.userName))
    return False;
  }
  fclose(fp);
  fp = fopen("adminData.dat","ab");
  fwrite(&enterData,sizeof(enterData),1,fp);
  fclose(fp);
  return True;
 }
 bool adminLogIn()
 {
 enterData = enterLogInSignUp();
  FILE *fp;
  fp=fopen("adminData.dat","rb");
  while(fread(&existData,sizeof(existData),1,fp))
  {
  if(!strcmp(enterData.userName,existData.userName)&&!strcmp(enterData.password,existData.password))
  {
  return True;
  }
  }
  return False;
 }
 void addQustion(char exam[])
 {
 clrscr();
   Qustions enterQustion;
  cout<<"Qustion -: ";
  fflush(stdin);
  gets(enterQustion.qus);
   fflush(stdin);
  cout<<"option A :- ";
   fflush(stdin);
  gets(enterQustion.a);
   cout<<"option B :- ";
    fflush(stdin);
  gets(enterQustion.b);
   cout<<"option C :- ";
    fflush(stdin);
  gets(enterQustion.c);
   cout<<"option D :- ";
    fflush(stdin);
  gets(enterQustion.d);
  cout<<"right option  -:   ";
  enterQustion.ans = getchar();
  if((enterQustion.ans>=97&&enterQustion.ans<=100)||(enterQustion.ans>=65&&enterQustion.ans<=68))
  {
  clrscr();
  FILE *fp;
  fp = fopen(exam,"ab");
  fwrite(&enterQustion,sizeof(Qustions),1,fp);
  fclose(fp);
  }
  else
  {
  cout<<"enter valid option";
  getch();
  }
 }
};

class User
{
 logInData enterData,existData;
 public:
  bool userSignUp()
 {
  enterData = enterLogInSignUp();
  FILE *fp;
  fp = fopen("userData.dat","rb");
  while(fread(&existData,sizeof(existData),1,fp))
  {
   if(!strcmp(existData.userName,enterData.userName))
    return False;
  }
  fclose(fp);
  fp = fopen("userData.dat","ab");
  fwrite(&enterData,sizeof(enterData),1,fp);
  fclose(fp);
  return True;
 }

  bool userLogIn()
 {
  enterData = enterLogInSignUp();
  FILE *fp;
  fp=fopen("userData.dat","rb");
  while(fread(&existData,sizeof(existData),1,fp))
  {
  if(!strcmp(enterData.userName,existData.userName)&&!strcmp(enterData.password,existData.password))
  return True;
  }
  return False;
  }
  void giveExam(char exam[])
  {
   int marks = 0;
   FILE *fp;
   char ans;
   Qustions existQustion;
   fp = fopen(exam,"rb");
   while(fread(&existQustion,sizeof(Qustions),1,fp))
   {
    clrscr();
    cout<<"Qus :- "<<existQustion.qus<<endl;
    cout<<"a : "<<existQustion.a<<"		b : "<<existQustion.b<<endl<<"c : "<<existQustion.c<<"		d : "<<existQustion.d;
    while(1)
    {
     cout<<endl<<"your option : ";
     fflush(stdin);
     ans = getchar();
     if(ans=='a'||ans=='A'||ans=='b'||ans=='B'||ans=='c'||ans=='C'||ans=='d'||ans=='D')
     {
      if(ans == existQustion.ans)
       marks++;
      break;
     }
     else
     {
      cout<<endl<<"invalid input";
      getch();
     }
    }
   }
   cout<<endl<<"your marks  :  "<<marks;
  }
};
void main()
{
void adminDilog();
void userDilog();
char ch;
clrscr();
do
{
clrscr();
cout<<"1 Admin\n2 User\nx exit";
ch = getch();
switch(ch)
{
 case '1':
 adminDilog();
 break;
 case '2':
 userDilog();
 break;
 case 'x':
 break;
 default:
 clrscr();
 cout<<"\ninvalid input";
 getch();
}
}while(ch!='x');
}
void adminDilog()
{
char ch;
Admin a;
do
{
clrscr();
cout<<"1 Sign up"<<endl<<"2 Log in"<<endl<<"x exit";
ch = getch();
switch(ch)
{
 case '1':
 if(a.adminSignUp())
 cout<<endl<<"your account has created";
 else
 cout<<endl<<"user allready exist";
 getch();
 break;
 case '2':
 if(a.adminLogIn())
 {
 char ch2;
 do
 {
 clrscr();
 cout<<"1 add qustion"<<endl<<"2 back";
 ch2 = getch();
 switch(ch2)
 {
 case '1':
 a.addQustion("apt.txt");
 break;
 case '2':
 break;
 default:
 cout<<endl<<"invalid input";
 getch();
 }
 }while(ch2!='2');
 }
 else
 {
 cout<<endl<<"worng user name or password";
 getch();
 }
 break;
 case 'x':
 break;
 default :
 clrscr();
 cout<<"invalid input";
 getch();
 }
}while(ch!='x');
}
void userDilog()
{
char ch;
User u;
do
{
 clrscr();
 cout<<"1 Sign Up"<<endl<<"2 Log in"<<endl<<"x exit";
 ch = getch();
 switch(ch)
 {
  case '1':
  if(u.userSignUp())
  cout<<endl<<"your account created";
  else
  cout<<endl<<"user allready exist";
  getch();
  break;
  case '2':
  if(u.userLogIn())
  {
  char ch2;
  do{
  clrscr();
  cout<<"welcome"<<endl<<"1 give text\n2 back";
  ch2 = getch();
  switch(ch2)
  {
  case '1':
  clrscr();
  u.giveExam("apt.txt"); // give exam function
  getch();
  break;
  case '2':
  break;
  default :
  clrscr();
  cout<<"invalid input";
  getch();
  }
  }while(ch2!='2');
  }
  else
  {
  cout<<endl<<"wrong user name or password";
  getch();
  }
  break;
  case 'x':
  break;
  default:
  clrscr();
  cout<<"invalid input";
  getch();
 }
}while(ch!='x');
}