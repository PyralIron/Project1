#include <iostream>
#include <SDL2/SDL.h>
using namespace std;
int main() {

	if ( SDL_Init(SDL_INIT_EVERYTHING) != 0 )
	{
		cerr << SDL_GetError() << '\n';
		return -1;
	}
	SDL_Window *window;

	window = SDL_CreateWindow("", 0, 0, 100, 100, 0);
	if (window == NULL)
	{
		cerr << SDL_GetError() << '\n';
		return -1;
	}
	SDL_Delay(3000);
	SDL_DestroyWindow(window);
	SDL_Quit();

	return 0;
}
