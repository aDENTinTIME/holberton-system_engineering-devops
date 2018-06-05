#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{
	int i = 3;

	while (i--)
	{
		if (fork() == 0)
			printf("Zombie process created, PID: %d\n", getpid());
	}
	return (0);
}
