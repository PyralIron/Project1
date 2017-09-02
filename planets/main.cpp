#include <iostream>
#include <string>
#include <array>
#include <vector>
#include <initializer_list>
#include <SDL2/SDL.h>
#include "vector.h"
#include "point.h"
#include "planet.h"
using namespace std;

int main()
{
	if ( SDL_Init(SDL_INIT_EVERYTHING) != 0 )
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
	SDL_Window *window = SDL_CreateWindow("", 0, 0, 100, 100, 0);
        if (window == NULL)
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
	SDL_Surface* surface = SDL_GetWindowSurface(window);
	if (surface == NULL)
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
	SDL_Renderer *renderer = SDL_CreateSoftwareRenderer(surface);

	vector<Planet> planetlist = {
		Planet {"Earth", {0,0}, {0,0}, 100, 10, BLUE},
		Planet {"Sun", {100,100}, {0,0}, 1000, 20, YELLOW},
		Planet {"Mars", {200,50}, {5,0}, 100, 10, RED}
		};
	vector<Vector> forcearray(planetlist.size(),{0,0});
	while (true) {
		for (int i = 0; i < planetlist.size(); i++) {
			//cout << x.getname();
			forcearray[i] = {0,0};
			for (auto y : planetlist) {
				forcearray[i] += planetlist[i].gforce(y);
			}
		}
		for (int i = 0; i < planetlist.size(); i++) {
			auto F = forcearray[i];
			planetlist[i].setvelocity() = planetlist[i].getvelocity() + F/planetlist[i].getmass();
			planetlist[i].setposition() = planetlist[i].getposition() + planetlist[i].getvelocity();
		}
		SDL_FillRect(surface, NULL, BLACK);
		for (int i = 0; i < planetlist.size(); i++) {
			SDL_Rect rect = {planetlist[i].getposition()[0]-planetlist[i].getradius(),planetlist[i].getposition()[1]-planetlist[i].getradius(),planetlist[i].getradius()*2,planetlist[i].getradius()*2};
			SDL_FillRect(surface, &rect, planetlist[i].getcolor());
		}
		SDL_UpdateWindowSurface(window);
	}

	return 0;
}
