#include <iostream> 
#include <string> 
#include <array> 
#include <vector>
#include <initializer_list> 
#include <SDL2/SDL.h> 
#include <SDL2/SDL_opengles2.h> 
#include <fstream> 
#include <stdlib.h> 
#include "vector.h" 
#include "point.h" 
#include "planet.h"
using namespace std;

#define WINDOW_HEIGHT 1000
#define WINDOW_WIDTH 500

bool handleevents() {
	bool quit = false;
	SDL_Event event;
	while (SDL_PollEvent(&event)) {
		switch (event.type) {
		case SDL_QUIT:
			quit = true;
			break;
		case SDL_KEYDOWN:
			switch (event.key.keysym.sym) {
			case SDLK_ESCAPE:
				quit = true;
				break;
			}
			break;
		}
	}
	return quit;
}

GLuint compileShader(GLenum shadertype, char* filename) {
	GLuint shader = glCreateShader(shadertype);

	fstream fin(filename, fstream::in);
	string s((istreambuf_iterator<char>(fin)), (istreambuf_iterator<char>()));
	const char * vchar = s.c_str();
	glShaderSource(shader, 1, &vchar, NULL);
	fin.close();

	glCompileShader(shader);

	GLint success = 0;
	glGetShaderiv(shader, GL_COMPILE_STATUS, &success);

	if (!success) {
		GLint logSize = 0;
		glGetShaderiv(shader, GL_INFO_LOG_LENGTH, &logSize);
		char* log = (char*)malloc(logSize);
		glGetShaderInfoLog(shader, logSize, NULL, log);
		cerr << log;
		free(log);
	}

	return shader;
}

int init(SDL_Window **window, SDL_GLContext *glcontext, GLuint *program) {
	if ( SDL_Init(SDL_INIT_EVERYTHING) != 0 )
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
        *window = SDL_CreateWindow("", 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_OPENGL | SDL_WINDOW_FULLSCREEN);
        if (*window == NULL)
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
	*glcontext = SDL_GL_CreateContext(*window);
        if (*glcontext == NULL)
        {
                cerr << SDL_GetError() << '\n';
                return -1;
        }
	int version = 0;
	int version2 = 0;
	SDL_GL_GetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, &version);
	SDL_GL_GetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, &version2);
	cout << version << " " << version2 << '\n';
	glClearColor(0.0,0.0,0.0,1.0);

	GLuint vbo;
	glGenBuffers(1, &vbo);

	float vertices[] = {-1,1,
			    1,1,
 			     -1,-1,
			     1,-1};
	glEnableVertexAttribArray(0);

	glBindBuffer(GL_ARRAY_BUFFER, vbo);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
	glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, 0);

	auto vshader = compileShader(GL_VERTEX_SHADER, "shader.vert");
	auto fshader = compileShader(GL_FRAGMENT_SHADER, "shader.frag");
	*program = glCreateProgram();

	glAttachShader(*program, vshader);
        glAttachShader(*program, fshader);
	glBindAttribLocation(*program, 0, "quad");
        glLinkProgram(*program);
        glDetachShader(*program, vshader);
        glDetachShader(*program, fshader);

	GLint success = 0;
        glGetProgramiv(*program, GL_LINK_STATUS, &success);

        if (!success) {
                GLint logSize = 0;
                glGetProgramiv(*program, GL_INFO_LOG_LENGTH, &logSize);
                char* log = (char*)malloc(logSize);
                glGetProgramInfoLog(*program, logSize, NULL, log);
                cerr << log;
                free(log);
        }
        glUseProgram (*program);

	//GLint apos = glGetAttribLocation(*program, "quad");
	//glBindAttribLocation(*program, 0, "quad");

	glDisable(GL_CULL_FACE);
	return 0;

}

int main()
{
	SDL_Window *window = NULL;
	SDL_GLContext glcontext;
	GLuint program;
	if (init(&window, &glcontext, &program)) {
		exit(-1);
	}

	GLint upos = glGetUniformLocation(program, "pos");
        GLint ucolor = glGetUniformLocation(program, "color");
	GLint uscale = glGetUniformLocation(program, "scale");
	GLint udimensions = glGetUniformLocation(program, "dimensions");

	vector<Planet> planetlist = {
		Planet {"Earth", {0,-0.4}, {0.00075,-0.0015}, 0.0000001, 0.1, BLUE},
		//Planet {"Sun", {0,0}, {500,500}, 1000, 20, YELLOW},
		Planet {"Mars", {0.0,0.4}, {-0.00075,0.0015}, 0.0000001, 0.1, RED}
		};
	vector<Vector> forcearray(planetlist.size(),{0,0});

	int win_width = 0;
	int win_height = 0;
	SDL_GetWindowSize(window, &win_width, &win_height);
	cerr << "resolution: " << win_width << " x " << win_height << '\n';
	glUniform2f(udimensions, win_width, win_height);
	glViewport(0, 0, win_width, win_height);

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

		//SDL_FillRect(surface, NULL, BLACK);
		glClear(GL_COLOR_BUFFER_BIT);
		glEnableVertexAttribArray(0);
		//glDisableVertexAttribArray(0);
		glVertexAttrib2f(0, 0.0, 0.0);
		for (int i = 0; i < planetlist.size(); i++) {
			auto p = planetlist[i];
/*
			cout << p.getname() << ' ';
			cout << p.getposition()[0] << ' ';
			cout << p.getposition()[1] << '\n';
			cout << p.getvelocity()[0] << ' ' << p.getvelocity()[1] << '\n';

*/			Point rp = planetlist[i].getposition();
			Color color = planetlist[i].getcolor();
			long double rr = planetlist[i].getradius();
			glUniform2f(upos,rp[0],rp[1]);
			glUniform1f(uscale,rr);
			glUniform3f(ucolor,colors[color][0],colors[color][1],colors[color][2]);
			glDrawArrays(GL_TRIANGLE_STRIP, 0, 4);
		}

		SDL_GL_SwapWindow(window);
		//SDL_UpdateWindowSurface(window);
	}

	return 0;
}
