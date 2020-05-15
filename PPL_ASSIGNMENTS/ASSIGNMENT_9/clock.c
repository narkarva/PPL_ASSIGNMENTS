#include<stdio.h>
#include<unistd.h>
#include<pthread.h>
int sec, min, hrs;
void *fun3(void *args) {	
	if(min == 60) {
		hrs++;
		min = 0;
	}
}
void *fun2(void *args) {
	pthread_t id3;
	if(sec == 60) {
		sec = 0;        	
		min++;
	}
	pthread_create(&id3, NULL, fun3, NULL);
	pthread_join(id3, NULL);	
}

void *fun1(void *args) {
	pthread_t id2;
	while(1) {
		sleep(1);		
		sec++;
		pthread_create(&id2, NULL, fun2, NULL);		
		pthread_join(id2, NULL);		
		printf("%d:%d:%d\n", hrs, min, sec);			
	}
}
int main() {
	pthread_t id1, id2, id3;	
	int err = pthread_create(&id1, NULL, fun1, NULL);
	err = pthread_join(id1, NULL);
	return 0;
}
