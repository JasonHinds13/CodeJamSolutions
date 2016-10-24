#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define RADIUS 6378.137
#define PI 3.14159265359
#define MAX_SIZE 50000
#define ToRadians(point) (point * PI / 180.0)

typedef struct person{
    char date[10];
    char time[5];
    long double lat;
    long double lon;
    long int pnum;
    long int rad;
}subscriber;

subscriber subs[MAX_SIZE];

//selection sort
void sort_arr(long int arr[], int size){
    int pos;
    long int swap;
    
    for (int c=0 ; c <(size-1) ; c++){
      pos = c;
      for (int d=c+1; d < size; d++){
         if(arr[pos] > arr[d])
            pos = d;
      }
      if (pos != c){
         swap = arr[c];
         arr[c] = arr[pos];
         arr[pos] = swap;
      }
   }
}

//see if value is in array
int in_arr(long int arr[], int size, long int val){
    
    for(int i=0; i < size; i++){
        if(arr[i] == val){
            return 0;
        }
    }
    return 1;
}

int conv_time(char time[]){
    char new[5];
    
    new[0] = time[0];
    new[1] = time[1];
    new[2] = time[3];
    new[3] = time[4];
    
    return atoi(new);
}

char * get_elem_time(subscriber lis[], int size, long int num){
    for(int i=0; i < size; i++){
        if (lis[i].pnum == num){
            return lis[i].time;
        } 
    }
    return "00:00";
}

int main() {   
    //vars for food truck owner
    long double mylat, mylon;
    double range;
    char headers[39];
    
    long int phone_nums[MAX_SIZE]; //to hold phone numbers that are less than range
    long int ignore_nums[MAX_SIZE]; //phone_nums to ignore
    subscriber accepted[MAX_SIZE]; //similar purpose to phone_nums will help later
    int num_of_elems = 0; //to hold amount in phone_nums
    
    long double d; //If you laughed I know why :)
    
    char comma; //to read commas so I can ignore them
    int count = 0; //counter
    int count2 = 0;
    
    scanf("%Lf", &mylat);
    scanf("%c", &comma);
    scanf("%Lf %lf", &mylon, &range);
    
    mylat = ToRadians(mylat);
    mylon = ToRadians(mylon);
    
    scanf("%s", &headers);
    
    while (scanf("%s %5[^,], %Lf %c %Lf %c %ld", &subs[count].date, &subs[count].time, &subs[count].lat, &comma, &subs[count].lon, &comma, &subs[count].pnum) == 7){
        
        subs[count].lat = ToRadians(subs[count].lat);
        subs[count].lon = ToRadians(subs[count].lon);
        
        d = 2*RADIUS*asin(sqrt(pow(sin((subs[count].lat-mylat)/2),2)+cos(mylat)*cos(subs[count].lat)*pow(sin((subs[count].lon-mylon)/2),2)));
        
        subs[count].rad = d;
        
        if(d < range && in_arr(phone_nums, num_of_elems, subs[count].pnum) == 1){
            phone_nums[num_of_elems] = subs[count].pnum;
            accepted[num_of_elems] = subs[count];
            num_of_elems++;
        }
        
        else if(d >= range && in_arr(phone_nums, num_of_elems, subs[count].pnum) == 0){
            
            if(conv_time(subs[count].time) > conv_time(get_elem_time(accepted, num_of_elems,  subs[count].pnum))){
                ignore_nums[count2] = subs[count].pnum;
                count2++;
            }
        }
        count++;
    }
    
    sort_arr(phone_nums, num_of_elems);
    
    for(int i=0; i < num_of_elems; i++){
        
        if(in_arr(ignore_nums, count2, phone_nums[i]) == 1){
            printf("%ld", phone_nums[i]);
        
            if(i != num_of_elems-1)
                printf(",");
        }
    }
    
    return 0;
}

