#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{
	int i = 2;

	while (i--)
	{
		fork();
		printf("Zombie process created, PID: %d\n", getpid());
		sleep(1);
	}
	return (0);
}
