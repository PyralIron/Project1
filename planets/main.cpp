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

#define WINDOW_HEIGHT 500
#define WINDOW_WIDTH 500

bool handleevents() {
	bool quit = false;
	SDL_Event event;
	while (SDL_PollEvent(&event)) {
		switch (event.type) {
		case SDL_QUIT:
			quit = true;
		}
	}
	return quit;
}

int main()
{
	if ( SDL_Init(SDL_INIT_EVERYTHING) != 0 )
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
	SDL_Window *window = SDL_CreateWindow("", 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, 0);
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
		Planet {"Earth", {0,0}, {0.1,0.1}, 100, 10, BLUE}
		//Planet {"Sun", {0,0}, {500,500}, 1000, 20, YELLOW},
		//Planet {"Mars", {200,50}, {5,0}, 100, 10, RED}
		};
	vector<Vector> forcearray(planetlist.size(),{0,0});
	bool quit = false;
	while (!quit) {
		quit = handleevents();
		for (int i = 0; i < planetlist.size(); i++) {
			//cout << x.getname();
			forcearray[i] = {0,0};
			for (int j = 0; j < planetlist.size(); j++) {
				if (i != j) {
					forcearray[i] += planetlist[i].gforce(planetlist[j]);
				}
			}
		}
		for (int i = 0; i < planetlist.size(); i++) {
			auto F = forcearray[i];
			planetlist[i].velocity() = planetlist[i].getvelocity() + F/planetlist[i].getmass();
			planetlist[i].position() = planetlist[i].getposition() + planetlist[i].getvelocity();
		}
		SDL_FillRect(surface, NULL, BLACK);
		for (int i = 0; i < planetlist.size(); i++) {
			auto p = planetlist[i];
			cout << p.getname() << ' ';
			cout << p.getposition()[0] << ' ';
			cout << p.getposition()[1] << '\n';
			cout << p.getvelocity()[0] << ' ' << p.getvelocity()[1] << '\n';
			Point rp = planetlist[i].getposition();
			int rr = planetlist[i].getradius();
			SDL_Rect rect = {rp[0]-rr,rp[1]-rr,rr*2,rr*2};
			SDL_FillRect(surface, &rect, planetlist[i].getcolor());
		}
		SDL_UpdateWindowSurface(window);
	}

	return 0;
}
