#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define RED 	"\033[31m"
#define GREEN	"\033[32m"
#define YELLOW	"\033[33m"
#define RESET	"\033[0m"

int main (int argc, char *argv[]) {
	if (argc != 3) {
		printf(RED);
		printf("Usage: %s <image_file> <wordlist>", argv[0]);
		printf(RESET);

		return 1;
	}
	
	char *wordlist = argv[2];
	char *image = argv[1];
	char password[300];
	char command[500];
	int result;
	int count;

	FILE *file;

	file = fopen(wordlist, "r");
	if (!file) {
		printf(RED "Error opening wordlist file\n" RESET);
		return 1;
	}

	while(fgets(password, sizeof(password), file)) {
		password[strcspn(password, "\n")] = 0;
		
		count++;
		printf(YELLOW);
		printf("[*] Trying (%d): %s\n", count, password);
		printf(RESET);

		snprintf(command, sizeof(command), "steghide extract -sf \"%s\" -p  \"%s\" -f > /dev/null 2>&1", image, password);

		result = system(command);

		if (result == 0) {
			printf(GREEN);
			printf("[+] PASSWORD FOUND: %s\n", password);
			printf(RESET);
			
			fclose(file);
			return 0;
		}
	}
	
	fclose(file);
	printf(RED "[-] Password not found in wordlist/n");

	return 0;
}
