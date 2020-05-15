#include<stdio.h>
void function(int a, int b, int c) {
	char buffer[5];
	buffer[0] = 'A';
	int *ret;
	ret = buffer + 21;
	*ret += 7;
}
int main() {
	int x;
	x = 0;
	function(1,2,3);
	x = 1;
	printf("%d\n",x);
	return 0;
}
